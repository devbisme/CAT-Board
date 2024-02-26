from myhdl import *
from sd_intf import SdramIntf
from math import ceil

commands = enum("COM_INHIBIT", "NOP", "ACTIVE", "READ", "WRITE", "BURST_TERM",
                "PRECHARGE", "AUTO_REFRESH", "LOAD_MODE", "OUTPUT_EN", "OUTPUT_Z", "INVALID")

states = enum("Uninitialized", "Initialized", "Idle", "Activating", "Active",
              "Read", "Reading", "Read_rdy", "Write", "Writing")

# generic parameters
FREQ_GHZ_G = SdramIntf.SDRAM_FREQ_C / 1000
ENABLE_REFRESH_G = True
NROWS_G = SdramIntf.SDRAM_NROWS_C
T_INIT_G = SdramIntf.SDRAM_T_INIT_C  # min initialization interval (ns).
T_RAS_G = SdramIntf.SDRAM_T_RAS_C    # min interval between active to precharge commands (ns).
T_RCD_G = SdramIntf.SDRAM_T_RCD_C    # min interval between active and R/W commands (ns).
T_REF_G = SdramIntf.SDRAM_T_REF_C    # maximum refresh interval (ns).
T_RFC_G = SdramIntf.SDRAM_T_RFC_C    # duration of refresh operation (ns).
T_RP_G = SdramIntf.SDRAM_T_RP_C      # min precharge command duration (ns).
T_XSR_G = SdramIntf.SDRAM_T_XSR_C    # exit self-refresh time (ns).

# delay constants
INIT_CYCLES_C = int(ceil(T_INIT_G * FREQ_GHZ_G))
RP_CYCLES_C = int(ceil(T_RP_G * FREQ_GHZ_G))
RFC_CYCLES_C = int(ceil(T_RFC_G * FREQ_GHZ_G))
REF_CYCLES_C = int(ceil(T_REF_G * FREQ_GHZ_G / NROWS_G))
RCD_CYCLES_C = int(ceil(T_RCD_G * FREQ_GHZ_G/10))
RAS_CYCLES_C = int(ceil(T_RAS_G * FREQ_GHZ_G))
MODE_CYCLES_C = 2
CAS_CYCLES_C = 3
WR_CYCLES_C = 2
RFSH_OPS_C = 8                            # number of refresh operations needed to init SDRAM.


# show_state and show_command are variables to show/hide log messages
def sdram(clk, sd_intf, show_command=False):

    curr_command = Signal(commands.INVALID)
    control_logic_inst = control_logic(curr_command, sd_intf)

    curr_state = [State(0, sd_intf), State(1, sd_intf), State(2, sd_intf), State(3, sd_intf)]  # state of eah bank

    # refresh variables
    ref_cycles_c = int(sd_intf.timing['ref'] / sd_intf.SDRAM_FREQ_C)
    rfsh_count_c = sd_intf.SDRAM_NROWS_C
    rfsh_timer = Signal(modbv(1, min=0, max=ref_cycles_c))
    rfsh_count = Signal(intbv(0, min=0, max=rfsh_count_c))

    @always(clk.posedge)
    def main_function():
        if sd_intf.cke == 1:
            if show_command:
                print(" SDRAM : [COMMAND] ", curr_command)

            for bank_state in curr_state:
                bank_state.next_state(curr_command)

            if curr_command == commands.INVALID:
                print(" SDRAM : [ERROR] Invalid command is given")
            elif curr_command == commands.LOAD_MODE:
                load_mode(sd_intf.bs, sd_intf.addr)
            elif curr_command == commands.ACTIVE:
                activate(sd_intf.bs, sd_intf.addr)
            elif curr_command == commands.READ:
                read(sd_intf.bs, sd_intf.addr)
            elif curr_command == commands.WRITE:
                write(sd_intf.bs, sd_intf.addr)
            elif curr_command == commands.PRECHARGE:
                precharge(sd_intf.bs, sd_intf.addr)
            elif curr_command == commands.AUTO_REFRESH:
                rfsh_count.next = rfsh_count + 1 if rfsh_timer != 0 else 0

            rfsh_timer.next = (rfsh_timer + 1)
            if rfsh_timer == 0:
                if rfsh_count < rfsh_count_c:
                    print(" SDRAM : [ERROR] Refresh requirement is not met")

    @always(clk.negedge)
    def read_function():
        bank_state = curr_state[sd_intf.bs.val]
        if bank_state.state == states.Read_rdy or bank_state.state == states.Reading:
            bank_state.driver.next = bank_state.data
        else:
            bank_state.driver.next = None

    def load_mode(bs, addr):

        cas = int(addr[7:4])
        burst = 2**int(addr[3:0])
        if addr[9] == 1:
            mode = "Single "
        else:
            mode = "Burst  "
        print("Bank :", bs)
        print("--------------------------")
        print(" Mode   | CAS   |   Burst ")
        print("--------|-------|---------")
        print(" %s| %i     |   %i " % (mode, cas, burst))
        print("--------------------------")

    def activate(bs, addr):
        if curr_state[bs.val].active_row:
            print(" SDRAM : [ERROR] A row is already activated. Bank should be precharged first")
            return None
        if curr_state[bs.val].get_state() == states.Uninitialized:
            print(" SDRAM : [ERROR] Bank is not in a good state. Too bad for you")
            return None
        curr_state[bs.val].active_row = addr.val

    def read(bs, addr):
        if not curr_state[bs.val].active_row:
            print(" SDRAM : [ERROR] A row should be activated before trying to read")
        else:
            print(" SDRAM : [READ]", addr, " Commnad registered ")

    def write(bs, addr):
        if not curr_state[bs.val].active_row:
            print(" SDRAM : [ERROR] A row should be activated before trying to write", addr)

    def precharge(bs, addr):
        if addr.val[10] == 1:           # Precharge all banks command
            for bank in curr_state:
                bank.active_row = None
        else:                            # Precharge selected bank
            curr_state[bs.val].active_row = None

    return instances()


def control_logic(curr_command, sd_intf):

    @always_comb
    def decode():
        # detect the registered command
        if sd_intf.cs == 1:
            # cs ras cas we dqm : H X X X X
            curr_command.next = commands.COM_INHIBIT
        else:
            if sd_intf.ras == 1:
                if sd_intf.cas == 1:
                    if sd_intf.we == 1:
                        # cs ras cas we dqm : L H H H X
                        curr_command.next = commands.NOP
                    else:
                        # cs ras cas we dqm : L H H L X
                        curr_command.next = commands.BURST_TERM
                else:
                    if sd_intf.we == 1:
                        # cs ras cas we dqm : L H L H X
                        curr_command.next = commands.READ
                    else:
                        # cs ras cas we dqm : L H L L X
                        curr_command.next = commands.WRITE
            else:
                if sd_intf.cas == 1:
                    if sd_intf.we == 1:
                        # cs ras cas we dqm : L L H H X
                        curr_command.next = commands.ACTIVE
                    else:
                        # cs ras cas we dqm : L L H L X
                        curr_command.next = commands.PRECHARGE
                else:
                    if sd_intf.we == 1:
                        # cs ras cas we dqm : L L L H X
                        curr_command.next = commands.AUTO_REFRESH
                    else:
                        # cs ras cas we dqm : L L L L X
                        curr_command.next = commands.LOAD_MODE

    return decode


class State:

    def __init__(self, bank_id, sd_intf):
        self.state = states.Uninitialized
        self.init_time = now()
        self.wait = 0
        self.bank_id = bank_id
        self.memory = {}
        self.sd_intf = sd_intf
        self.driver = sd_intf.dq.driver()
        self.active_row = None
        self.addr = None
        self.data = None
        self.tick = 0

    def next_state(self, curr_command):
        self.wait += 1
        if self.state == states.Uninitialized:
            if self.wait >= INIT_CYCLES_C:
                print(" BANK", self.bank_id, "STATE : [CHANGE] Uninitialized -> Initialized @ ", now())
                self.state = states.Initialized
                self.wait = 0

        elif self.state == states.Idle or self.state == states.Initialized:
            self.data = 0
            # Reading command
            if curr_command == commands.READ and self.bank_id == self.sd_intf.bs.val:
                self.state = states.Reading
                self.wait = 0
                if self.sd_intf:
                    self.addr = self.sd_intf.addr.val
            # Writing command
            elif curr_command == commands.WRITE and self.bank_id == self.sd_intf.bs.val:
                self.state = states.Writing
                self.wait = 0
                if self.sd_intf:
                    self.addr = self.sd_intf.addr.val
                    self.data = self.sd_intf.dq.val

        elif self.state == states.Reading:
            if self.wait >= CAS_CYCLES_C - 1:
                self.state = states.Read_rdy
                self.wait = 0
                if self.active_row:
                    self.data = self.memory[self.active_row * 10000 + self.addr]
                print(" STATE : [READ] Data Ready @ ", now(), " value : ", self.data)

        elif self.state == states.Read_rdy:
                self.state = states.Idle
                self.wait = 0
                self.driver.next = None

        elif self.state == states.Writing:
            if self.wait >= RCD_CYCLES_C:
                self.state = states.Idle
                self.wait = 0
                if self.active_row:
                    print(" DATA : [WRITE] Addr:", self.addr, " Data:", self.data)
                    self.memory[self.active_row * 10000 + self.addr] = self.data

    def get_state(self):
        return self.state

    def get_data(self):
        return self.data
