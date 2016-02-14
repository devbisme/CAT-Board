# MIT license
# 
# Copyright (C) 2016 by XESS Corp.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import rhea.build as build
from rhea.build.boards import get_board
from sdram_test import sdram_test
from SDRAM_Controller.sd_intf import *


def run_catboard():
    # Get the CAT Board object.
    brd = get_board('catboard')
    # Add the ports and pin assignments for PMOD socket PM3.
    brd.add_port('d0_o', 'A11')
    brd.add_port('d1_o', 'B10')
    brd.add_port('d2_o', 'B12')
    brd.add_port('d3_o', 'B11')
    brd.add_port('d4_o', 'B14')
    brd.add_port('d5_o', 'B13')
    brd.add_port('d6_o', 'B15')
    brd.add_port('d7_o', 'A15')
    # Add the clock port to the 100 MHz on-board oscillator.
    brd.add_clock('master_clk_i', 1e8, 'C8')
    # Route clocks to/from the SDRAM.
    brd.add_port('sdram_clk_o', 'G16')
    brd.add_clock('sdram_clk_i', 1e8, 'H16')
    # Add the ports to the pushbuttons.
    brd.add_port('pb_i', 'A16', PULLUP='PULLUP')
    # Add the connections to the SDRAM.
    brd.add_port('sdintf.cke', 'G15')
    brd.add_port('sdintf.cs', 'H13')
    brd.add_port('sdintf.cas', 'K15')
    brd.add_port('sdintf.ras', 'K16')
    brd.add_port('sdintf.we', 'J14')
    brd.add_port('sdintf.bs', ('H14','G13'))
    brd.add_port('sdintf.addr', ('F13','E14','E13','D14','B16','C16','D15','D16','E16','F15','F14','F16','G14'))
    brd.add_port('sdintf.dqml', 'J13')
    brd.add_port('sdintf.dqmh', 'J15')
    brd.add_port('sdintf.dq', ('R14','P14','M13','M14','L13','L14','K13','K14','J16','L16','M16','M15','N16','P16','P15','R15'))
    # Run the MyHDL+yosys+arachne-pnr design tools on the top-level module.
    flow = brd.get_flow(top=sdram_test)
    flow.run()


if __name__ == '__main__':
    run_catboard()
