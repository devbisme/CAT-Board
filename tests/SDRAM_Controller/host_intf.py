from myhdl import *

class host_intf(object):

    def __init__(self):
        # Host side signals
        self.rst_i      = ResetSignal(0, active=1, async=True)
        self.rd_i       = Signal(bool(0))
        self.wr_i       = Signal(bool(0))
        self.addr_i     = Signal(intbv(0)[24:]) # host side address = sdram side row + col + bank
        self.data_i     = Signal(intbv(0)[16:])
        self.data_o     = Signal(intbv(0)[16:])
        self.done_o     = Signal(bool(0))
        self.rdPending_o= Signal(bool(0))
    #    self.status_o   = Signal(bool(0))

    def read(self,addr):
        self.addr_i.next = addr
        self.rd_i.next   = 1
        yield delay(2)
        self.rd_i.next   = 0

    def write(self,addr,data):
        self.addr_i.next = addr
        self.data_i.next = data
        yield delay(5)
        self.wr_i.next   = 1

    def nop(self):
        self.rd_i.next = 0
        self.wr_i.next = 0

    def waitUntilDone(self):
        yield self.done_o.posedge

    def readData(self):
        return self.data_o.val
