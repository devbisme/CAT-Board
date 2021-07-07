from myhdl import *
from SdramCntl import *
from Clk import *
from sdram import *
from host_intf import *
from sd_intf import *

clk_i = Signal(bool(0))
rst_i = ResetSignal(0,active=1,async=True)

clkDriver_Inst      = clkDriver(clk_i)
sd_intf_Inst        = sd_intf()
host_intf_Inst      = host_intf()

sdramCntl_Inst = MySdramCntl(clk_i,host_intf_Inst,sd_intf_Inst)

toVerilog(MySdramCntl,clk_i,host_intf_Inst,sd_intf_Inst)
toVHDL(MySdramCntl,clk_i,host_intf_Inst,sd_intf_Inst)
