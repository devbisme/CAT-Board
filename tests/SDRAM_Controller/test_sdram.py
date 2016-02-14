from myhdl import *
from Clk import clkDriver
from sd_intf import sd_intf
from sdram import sdram

def test_readWrite(clk,sd_intf):

    driver = sd_intf.getDriver()
    
    @instance
    def test():
        
        sd_intf.cke.next = 1
	
        yield sd_intf.nop(clk)
	yield delay(10000)
	yield sd_intf.loadMode(clk)
	yield sd_intf.nop(clk)
        yield sd_intf.activate(clk,17)
        yield sd_intf.nop(clk)
        yield delay(10000)

        yield sd_intf.write(clk,driver,20,31)
	
        #yield delay(5)
        yield sd_intf.nop(clk)
        yield delay(100)
        yield sd_intf.read(clk,20)
        #yield delay(10)
        yield sd_intf.nop(clk)
        yield delay(4)
	print "sd_intf dq = ",sd_intf.dq.val," @ ",now()
        
    return test

clk = Signal(bool(0))

clkDriver_Inst      = clkDriver(clk)
sd_intf_Inst        = sd_intf()
sdram_Inst          = sdram(clk,sd_intf_Inst)
test_readWrite_Inst = test_readWrite(clk,sd_intf_Inst)

sim = Simulation(clkDriver_Inst,sdram_Inst,test_readWrite_Inst)
sim.run(25000)
