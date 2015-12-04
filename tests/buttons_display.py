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
from led_digits_display import *
from ice40_primitives import *


def buttons_display(d0_o, d1_o, d2_o, d3_o, d4_o, d5_o, d6_o, d7_o, clk_i,
                    sw1_i, sw2_i, sw3_i):
    '''Module for testing buttons and DIP switches.
    d0_o, ... d7_o: 3-state outputs to drive the StickIt! LEDDigits board.
    clk_i: Input clock.
    sw1_i, sw2_i: Pushbutton inputs.
    sw3_i: DIP switch input (4 bits).
    '''

    # Internal versions of the switch inputs.
    sw1, sw2 = [Signal(bool(0)) for _ in range(2)]
    sw3 = Signal(intbv(0)[len(sw3_i):])

    # Use input pins with pullups enabled to get the switch inputs to their internal versions.
    sw1_inst = input_pin(sw1_i, sw1, pullup=True)
    sw2_inst = input_pin(sw2_i, sw2, pullup=True)
    sw3_inst = input_pin(sw3_i, sw3, pullup=True)

    # Signals for holding 7-segment LED digit values.
    sw1_digit, sw2_digit = [Signal(intbv(0)[7:]) for _ in range(2)]
    space = 0x20  # ASCII code for a blank space. (LED digit will be OFF.)

    # Unpressed pushbuttons will be read as high inputs because of the pullups.
    # When high, the hex value of the four DIP switch inputs will be displayed.
    # When the pushbutton is pressed, its input pin is pulled low and the
    # digit will display a space.
    @always_comb
    def sw_logic():
        if sw1 == 1:
            sw1_digit.next[4:0] = sw3
            sw1_digit.next[7:4] = 0
        else:
            sw1_digit.next[7:0] = space
        if sw2 == 1:
            sw2_digit.next[4:0] = sw3
            sw2_digit.next[7:4] = 0
        else:
            sw2_digit.next[7:0] = space

    # Attach the hex digit code for SW1 to the first LED digit, and the
    # code for SW2 to the last digit of the LED display.
    drvrs = [TristateSignal(bool(0)) for _ in range(8)]
    display = led_digits_display(drvrs[0], drvrs[1], drvrs[2], drvrs[3],
                                 drvrs[4], drvrs[5], drvrs[6], drvrs[7], clk_i,
                                 sw1_digit, space, space, space, space, space,
                                 space, sw2_digit)

    # Attach the LEDDigits drivers to the output pins of this module.
    @always_comb
    def io_logic():
        d0_o.next = drvrs[0]
        d1_o.next = drvrs[1]
        d2_o.next = drvrs[2]
        d3_o.next = drvrs[3]
        d4_o.next = drvrs[4]
        d5_o.next = drvrs[5]
        d6_o.next = drvrs[6]
        d7_o.next = drvrs[7]

    return instances()


def buttons_display_tb():
    '''Testbench for the switch tester.'''
    d0, d1, d2, d3, d4, d5, d6, d7 = [TristateSignal(bool(0))
                                      for _ in range(8)]
    clk, sw1, sw2 = [Signal(bool(0)) for _ in range(3)]
    sw3 = Signal(intbv(0)[4:])

    dut = buttons_display(d0.driver(), d1.driver(), d2.driver(), d3.driver(),
                          d4.driver(), d5.driver(), d6.driver(), d7.driver(),
                          clk, sw1, sw2, sw3)

    @always(delay(10))
    def clk_gen():
        clk.next = not clk

    @instance
    def stimulus():
        sw3.next = 0xA
        sw1.next = 0
        sw2.next = 1
        yield delay(1000000)
        raise StopSimulation

    return instances()

# Main routine that does simulation and Verilog conversion.
if __name__ == '__main__':

    Simulation(traceSignals(buttons_display_tb)).run()

    d0, d1, d2, d3, d4, d5, d6, d7 = [TristateSignal(bool(0))
                                      for _ in range(8)]
    clk, sw1, sw2 = [Signal(bool(0)) for _ in range(3)]
    sw3 = Signal(intbv(0)[4:])
    toVerilog(buttons_display, d0.driver(), d1.driver(), d2.driver(),
              d3.driver(), d4.driver(), d5.driver(), d6.driver(), d7.driver(),
              clk, sw1, sw2, sw3)
