from myhdl import *
from math import log


class SdramIntf(object):

    addr_width = 13
    data_width = 16
    # constant for sdram
    SDRAM_NROWS_C = 8192            # Number of rows in SDRAM array.
    SDRAM_NCOLS_C = 512             # Number of columns in SDRAM array.
    SDRAM_DATA_WIDTH_C = 16         # Host & SDRAM data width.
    SDRAM_HADDR_WIDTH_C = 24        # Host-side address width.
    SDRAM_SADDR_WIDTH_C = 13        # SDRAM-side address width.
    SDRAM_T_INIT_C = 20000.0        # 200000.0   # Min initialization interval (ns).
    SDRAM_T_RAS_C = 45.0            # Min interval between active to precharge commands (ns).
    SDRAM_T_RCD_C = 20.0            # Min interval between active and R/W commands (ns).
    SDRAM_T_REF_C = 64000000.0      # Maximum refresh interval (ns).
    SDRAM_T_RFC_C = 65.0            # Duration of refresh operation (ns).
    SDRAM_T_RP_C = 20.0             # Min precharge command duration (ns).
    SDRAM_T_XSR_C = 75.0            # Exit self-refresh time (ns).

    SDRAM_FREQ_C = 100.0            # Operating frequency in MHz.
    SDRAM_IN_PHASE_C = True         # SDRAM and controller XESS on same or opposite clock edge.
    SDRAM_PIPE_EN_C = False         # If true, enable pipelined read operations.
    SDRAM_ENABLE_REFRESH_C = True   # If true, row refreshes are automatically inserted.
    SDRAM_MULTIPLE_ACTIVE_ROWS_C = False      # If true, allow an active row in each bank.
    SDRAM_MAX_NOP_C = 10000         # Number of NOPs before entering self-refresh.
    SDRAM_BEG_ADDR_C = 16           # 00_0000#;  -- Beginning SDRAM address.
    SDRAM_END_ADDR_C = 16           # FF_FFFF#;  -- Ending SDRAM address.

    SDRAM_NOP_CMD_C = intbv("0111")[4:]     # 0,1,1,1,0,0
    SDRAM_ACTIVE_CMD_C = intbv("0011")[4:]  # 0,0,1,1,0,0
    SDRAM_READ_CMD_C = intbv("0101")[4:]    # 0,1,0,1,0,0
    SDRAM_WRITE_CMD_C = intbv("0100")[4:]   # 0,1,0,0,0,0
    SDRAM_PCHG_CMD_C = intbv("0010")[4:]    # 0,0,1,0,0,0
    SDRAM_MODE_CMD_C = intbv("0000")[4:]    # 0,0,0,0,0,0
    SDRAM_RFSH_CMD_C = intbv("0001")[4:]    # 0,0,0,1,0,0
    SDRAM_MODE_C = intbv("00_0_00_011_0_000")[12:]  # mode command for set_mode command

    SDRAM_ALL_BANKS_C = intbv("001000000000")[12:]       # value of CMDBIT to select all banks
    SDRAM_ONE_BANK_C = intbv("000000000000")[12:]

    timing = {  # timing details refer data sheet
        'init': 100,       # min init interval
        'ras':  10,        # min interval between active prechargs
        'rcd':  10,        # min interval between active R/W
        'cas':  20,
        'ref':  64000000,  # max refresh interval
        'rfc':  65,        # refresh opertaion
        'rp':   20,        # min precharge
        'xsr':  75,        # exit self-refresh time
        'wr':   55,        # @todo ...
    }

    def __init__(self):

        self.cke = Signal(bool(0))
        self.cs = Signal(bool(0))
        self.cas = Signal(bool(0))
        self.ras = Signal(bool(0))
        self.we = Signal(bool(0))
        self.bs = Signal(intbv(0)[2:])
        self.addr = Signal(intbv(0)[self.addr_width:])
        self.dqml = Signal(bool(0))
        self.dqmh = Signal(bool(0))
        self.dq = TristateSignal(intbv(0)[self.data_width:])

    # Written below are transactors for passing commands to sdram

    def nop(self, clk):
        # [NOP] cs ras cas we : L H H H
        self.cs.next, self.ras.next, self.cas.next, self.we.next = 0, 1, 1, 1
        yield clk.posedge

    def activate(self, clk, row_addr, bank_id=0):
        self.bs.next = bank_id
        self.addr.next = row_addr
        # [ACTIVE] cs ras cas we : L L H H
        self.cs.next, self.ras.next, self.cas.next, self.we.next = 0, 0, 1, 1
        yield clk.posedge

    def load_mode(self, clk, mode='burst', cas=3, burst=1):
        addr = 0
        if mode.lower() == 'single':
            addr += 2**9
        addr += cas*(2**4)
        addr += int(log(burst, 2))
        self.addr.next = addr
        # [LOAD_MODE] cs ras cas we dqm : L L L L X
        self.cs.next, self.ras.next, self.cas.next, self.we.next = 0, 0, 0, 0
        yield clk.posedge
        yield clk.posedge

    def precharge(self, clk, bank_id=None):
        if not bank_id:    # precharge all banks
            self.addr.next = 2**10  # A10 is high
        else:
            self.addr.next = 0
            self.bs.next = bank_id
        # [PRECHARGE] cs ras cas we : L L H L
        self.cs.next, self.ras.next, self.cas.next, self.we.next = 0, 0, 1, 0
        yield clk.posedge

    def read(self, clk, addr, bank_id=0):
        self.bs.next = bank_id
        self.addr.next = addr
        # [READ] # cs ras cas we dqm : L H L H X
        self.cs.next, self.ras.next, self.cas.next, self.we.next = 0, 1, 0, 1
        yield clk.posedge
        yield clk.posedge

    def write(self, clk, driver, addr, value, bank_id=0):
        self.bs.next = bank_id
        self.addr.next = addr
        driver.next = value
        # [WRITE] # cs ras cas we dqm : L H L L X
        self.cs.next, self.ras.next, self.cas.next, self.we.next = 0, 1, 0, 0
        yield clk.posedge
        yield clk.posedge
        driver.next = None

    def get_driver(self):
        return self.dq.driver()
