# MIT license
# 
# Copyright (C) 2015-2021 by Dave Vandenbout.
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
from led_digits_display import led_digits_cnt, led_digits_scroll


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
    brd.add_clock('clk_i', 1e8, 'C8')
    # Run the MyHDL+yosys+arachne-pnr design tools on the top-level module.
    # Use 'top = led_digits_cnt' to display a counter.
    # Use 'top = led_digits_scroll' to display a scrolling string of digits.
    flow = brd.get_flow(top=led_digits_cnt)
    flow.run()


if __name__ == '__main__':
    run_catboard()
