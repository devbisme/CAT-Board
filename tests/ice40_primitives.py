# MIT license
# 
# Copyright (C) 2015 by XESS Corporation
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

from myhdl import *

inst_num = 0  # Incrementing index for making unique Verilog instantiation names.


def input_pin(i, o, pullup=False):
    '''Input pin module with integrated pullup enable.
        i: Input signal (either scalar or vector) from pin.
        o: Input signal passed to the internal LUTs of the FPGA.
        pullup: Set to True to turn on integrated pullups for this input
    '''

    # Code for simulating the input pin.
    @always_comb
    def in_to_out():
        o.next = i  # Just pass the value on the input pin to the output.

    # The rest is for instantiating the synthesizable Verilog block for the input pin.

    # Create the Verilog vector index if a vector input is used.
    vector = ''
    if len(i) > 1:
        vector = '[{}:{}]'.format(len(i) - 1, 0)

    # Set the pullup bit.
    pup = 0
    if pullup != False:
        pup = 1

    # Tell MyHDL that the I/O pins of this module are connected since it can't interpret the verilog_code string.
    i.driven = True
    o.driven = True

    # Increment the Verilog instantiation index.
    global inst_num
    inst_num += 1

    return instances()

# This is the Verilog code that gets inserted for the input pin when the MyHDL is converted to Verilog.
# The values of vector, pup, inst_num, i and o are inserted into the string.
input_pin.verilog_code = \
"""
SB_IO #(
  .PIN_TYPE(6'b000001),
  .PULLUP(1'b$pup)
) input_pin_$inst_num $vector (
  .PACKAGE_PIN($i),
  .D_IN_0($o)
);
"""
