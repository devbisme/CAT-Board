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
from math import ceil


def ascii_to_7seg(segments_o, ascii_char_i):
    '''Return the segment activations to display the given ASCII character.

        ascii_char_i: ASCII character code.
        segments_o: Activation code for 7-segment LED digit.
    '''

    @always_comb
    def logic():
        if ascii_char_i == 0x20:
            segments_o.next = intbv('0000000')  # Space.
        elif ascii_char_i == 0x2d:
            segments_o.next = intbv('1000000')  # Minus sign (-).
        elif ascii_char_i == 0x00 or ascii_char_i == 0x30:
            segments_o.next = intbv('0111111')  # Zero.
        elif ascii_char_i == 0x01 or ascii_char_i == 0x31:
            segments_o.next = intbv('0000110')  # One.
        elif ascii_char_i == 0x02 or ascii_char_i == 0x32:
            segments_o.next = intbv('1011011')  # Two.
        elif ascii_char_i == 0x03 or ascii_char_i == 0x33:
            segments_o.next = intbv('1001111')  # Three.
        elif ascii_char_i == 0x04 or ascii_char_i == 0x34:
            segments_o.next = intbv('1100110')  # Four.
        elif ascii_char_i == 0x05 or ascii_char_i == 0x35:
            segments_o.next = intbv('1101101')  # Five.
        elif ascii_char_i == 0x06 or ascii_char_i == 0x36:
            segments_o.next = intbv('1111101')  # Six.
        elif ascii_char_i == 0x07 or ascii_char_i == 0x37:
            segments_o.next = intbv('0000111')  # Seven.
        elif ascii_char_i == 0x08 or ascii_char_i == 0x38:
            segments_o.next = intbv('1111111')  # Eight.
        elif ascii_char_i == 0x09 or ascii_char_i == 0x39:
            segments_o.next = intbv('1101111')  # Nine.
        elif ascii_char_i == 0x0a or ascii_char_i == 0x41 or ascii_char_i == 0x61:
            segments_o.next = intbv('1110111')  # A.
        elif ascii_char_i == 0x0b or ascii_char_i == 0x42 or ascii_char_i == 0x62:
            segments_o.next = intbv('1111100')  # b.
        elif ascii_char_i == 0x0c or ascii_char_i == 0x43 or ascii_char_i == 0x63:
            segments_o.next = intbv('0111001')  # C.
        elif ascii_char_i == 0x0d or ascii_char_i == 0x44 or ascii_char_i == 0x64:
            segments_o.next = intbv('1011110')  # d.
        elif ascii_char_i == 0x0e or ascii_char_i == 0x45 or ascii_char_i == 0x65:
            segments_o.next = intbv('1111001')  # E.
        elif ascii_char_i == 0x0f or ascii_char_i == 0x46 or ascii_char_i == 0x66:
            segments_o.next = intbv('1110001')  # F.
        elif ascii_char_i == 0x47 or ascii_char_i == 0x67:
            segments_o.next = intbv('0111101')  # G.
        elif ascii_char_i == 0x48 or ascii_char_i == 0x68:
            segments_o.next = intbv('1110100')  # h.
        elif ascii_char_i == 0x49 or ascii_char_i == 0x69:
            segments_o.next = intbv('0110000')  # I.
        elif ascii_char_i == 0x4a or ascii_char_i == 0x6a:
            segments_o.next = intbv('0011110')  # J.
        elif ascii_char_i == 0x4b or ascii_char_i == 0x6b:
            segments_o.next = intbv('0001000')  # Blank.
        elif ascii_char_i == 0x4c or ascii_char_i == 0x6c:
            segments_o.next = intbv('0111000')  # L.
        elif ascii_char_i == 0x4d or ascii_char_i == 0x6d:
            segments_o.next = intbv('0001000')  # Blank.
        elif ascii_char_i == 0x4e or ascii_char_i == 0x6e:
            segments_o.next = intbv('1010100')  # n.
        elif ascii_char_i == 0x4f or ascii_char_i == 0x6f:
            segments_o.next = intbv('1011100')  # o.
        elif ascii_char_i == 0x50 or ascii_char_i == 0x70:
            segments_o.next = intbv('1110011')  # P.
        elif ascii_char_i == 0x51 or ascii_char_i == 0x71:
            segments_o.next = intbv('0001000')  # Blank.
        elif ascii_char_i == 0x52 or ascii_char_i == 0x72:
            segments_o.next = intbv('1010000')  # r.
        elif ascii_char_i == 0x53 or ascii_char_i == 0x73:
            segments_o.next = intbv('1101101')  # S.
        elif ascii_char_i == 0x54 or ascii_char_i == 0x74:
            segments_o.next = intbv('1111000')  # t.
        elif ascii_char_i == 0x55 or ascii_char_i == 0x75:
            segments_o.next = intbv('0011100')  # u.
        elif ascii_char_i == 0x56 or ascii_char_i == 0x76:
            segments_o.next = intbv('0001000')  # Blank.
        elif ascii_char_i == 0x57 or ascii_char_i == 0x77:
            segments_o.next = intbv('0001000')  # Blank.
        elif ascii_char_i == 0x58 or ascii_char_i == 0x78:
            segments_o.next = intbv('0001000')  # Blank.
        elif ascii_char_i == 0x59 or ascii_char_i == 0x79:
            segments_o.next = intbv('1101110')  # y.
        elif ascii_char_i == 0x5a or ascii_char_i == 0x7a:
            segments_o.next = intbv('0001000')  # Blank.
        elif ascii_char_i == 0x5f:
            segments_o.next = intbv('0001000')  # Underscore (_).
        else:
            segments_o.next = intbv('0001000')  # Blank.

    return instances()


def led_digits_display(d0_o,
                       d1_o,
                       d2_o,
                       d3_o,
                       d4_o,
                       d5_o,
                       d6_o,
                       d7_o,
                       clk_i,
                       digit1_i=Signal(intbv(0)[7:]),
                       digit2_i=Signal(intbv(0)[7:]),
                       digit3_i=Signal(intbv(0)[7:]),
                       digit4_i=Signal(intbv(0)[7:]),
                       digit5_i=Signal(intbv(0)[7:]),
                       digit6_i=Signal(intbv(0)[7:]),
                       digit7_i=Signal(intbv(0)[7:]),
                       digit8_i=Signal(intbv(0)[7:]),
                       digit_all_i=Signal(intbv(0)[56:]),
                       enable_ascii_to_7seg=True,
                       freq_g=100e6,
                       update_freq_g=1000):
    '''Module for displaying chars on StickIt! LEDDigits board.
    d0_o, ... d7_o: 3-state outputs to drive the StickIt! LEDDigits board.
    clk_i: Input clock.
    digit1_i ... digit8_i: 7-bit input for each digit on the LEDDigits board.
    digit_all_i: Alternate input for driving all 56 LEDs of the LEDDigits board.
    enable_ascii_to_7seg: Set True to interpret input digits as ASCII.
    freq_g: Set to frequency of input clock.
    update_freq_g: Set number of times the display is refreshed each second.
    '''

    initialized = Signal(bool(0))  # Initialization flag - starts off uninitialized.

    # These are shift registers: one for selecting the currently-driven LED digit,
    # and the other for selecting the currently driven segments within that digit.
    digit_shf = Signal(intbv('00000001')[8:])
    seg_mask = Signal(intbv('0010101')[7:])
    # Counter for sequencing through the segments of a 7-segment digit.
    seg_cntr = Signal(intbv(0, 0, len(seg_mask)))
    # Compute how long each segment should be activated based on the input clock
    # frequency, the display refresh frequency, the number of segments in the
    # display, and the number of simultaneously-driven segments.
    num_mask_bits = bin(seg_mask).count('1')
    SEG_PERIOD = int(ceil((freq_g / (update_freq_g * len(digit_all_i)) /
                           num_mask_bits)))
    seg_timer = Signal(intbv(0, 0, SEG_PERIOD + 1))
    # Blanking signal for turning off all the segments.
    blank = Signal(bool(0))

    inst = []  # List of submodule instantiations.

    # Logic for sequencing through the digits and the segments within each digit.
    # One shift register selects the currently active LED digit, while the other
    # selects the active LED segments within that digit. A timer measures the
    # interval each segment will remain active, and a segment counter determines
    # when all the segments for a digit have been processed.
    @always_seq(clk_i.posedge, reset=None)
    def scan_segments_and_digits():
        if initialized != True:
            # Initialize the rotating shift registers.
            seg_mask.next = intbv('0010101')
            digit_shf.next = intbv('00000001')
            initialized.next = not initialized  # Do initialization only once.
        elif seg_timer == 0:  # When done driving the current segments...
            seg_timer.next = seg_timer.max - 1  # Reload the segment timer...
            seg_mask.next[7:1] = seg_mask[6:0]  # Rotate the shift register...
            seg_mask.next[0] = seg_mask[6]  # to activate different segments...
            blank.next = (seg_cntr == 1)
            if seg_cntr == 0:  # When all segments of current digit are done...
                digit_shf.next[8:1] = digit_shf[7:0]  # Shift to the next digit.
                digit_shf.next[0] = digit_shf[7]
                seg_cntr.next = seg_cntr.max - 1  # Reset segment counter for new digit.
            else:  # Current digit is not done being displayed...
                seg_cntr.next = seg_cntr - 1  # So shift to next set of segments.
        else:  # Current segments are not done being displayed...
            seg_timer.next = seg_timer - 1  # So just decrement the timer.

    # Declare the signal that holds the currently active digit code.
    active_digit = Signal(intbv(0)[len(seg_mask):])

    # Select the digit input based on which bit is active in the digit shift
    # register. The active digit is an OR of the individual input digit and the
    # corresponding field of the digit_all_i input. (Either the input digit or
    # the digit_all_i input will be all 0s so the OR output will just be the
    # non-zero input.)
    @always_comb
    def get_active_digit():
        if digit_shf[0] == 1:
            active_digit.next = digit1_i | digit_all_i[7:0]
        elif digit_shf[1] == 1:
            active_digit.next = digit2_i | digit_all_i[14:7]
        elif digit_shf[2] == 1:
            active_digit.next = digit3_i | digit_all_i[21:14]
        elif digit_shf[3] == 1:
            active_digit.next = digit4_i | digit_all_i[28:21]
        elif digit_shf[4] == 1:
            active_digit.next = digit5_i | digit_all_i[35:28]
        elif digit_shf[5] == 1:
            active_digit.next = digit6_i | digit_all_i[42:35]
        elif digit_shf[6] == 1:
            active_digit.next = digit7_i | digit_all_i[49:42]
        elif digit_shf[7] == 1:
            active_digit.next = digit8_i | digit_all_i[56:49]
        else:
            active_digit.next = 0

    # Declare the signal that holds the values driven to the digit segments.
    segments = Signal(intbv(0)[len(seg_mask):])

    # Select whether the active digit code is driven directly to the display,
    # or whether it is interpreted as an ASCII character and needs to be transformed
    # into an activation code.
    if enable_ascii_to_7seg == True:
        # Translate from ASCII into an LED digit activation code.
        inst.append(ascii_to_7seg(segments, active_digit))
    else:
        # Directly drive the LED segments with the active digit code.
        @always_comb
        def pass_thru():
            segments.next = active_digit

    # Declare the signal that holds the segments which will be turned on.
    active_segments = Signal(intbv(0)[len(segments):])

    # AND the segments signal with the segment shift register to select the ON segments.
    @always_comb
    def get_active_segments():
        active_segments.next = segments & seg_mask

    # Declare the signal that holds the LEDDigits board driver outputs.
    drvr_enbls = Signal(intbv(0)[len(active_segments) + 1:])

    # The driver bits are set as follows:
    #   * If digit i is active, then digit_shf[i-1] bit is on and
    #     drvr_enbls[i-1] bit is driven high to source the digit i LED anodes.
    #   * The remaining drvr_enbls bits are filled with the bits from
    #     active_segments as follows:
    #         drvr_enbls[i-1:0] = active_segments[i-1:0]
    #         drvr_enbls[8:i] = active_segments[7:i-1]
    # Essentially, the ON bit at position i in digit_shf is inserted between
    # bits i and i-1 of active_segments.
    @always_comb
    def combine_drivers():
        if blank == True:
            drvr_enbls.next = 0
        elif digit_shf[0] == 1:
            drvr_enbls.next[8:1] = active_segments[7:0]
            drvr_enbls.next[0] = 1
        elif digit_shf[1] == 1:
            drvr_enbls.next[8:2] = active_segments[7:1]
            drvr_enbls.next[1] = 1
            drvr_enbls.next[0] = active_segments[1:0]
        elif digit_shf[2] == 1:
            drvr_enbls.next[8:3] = active_segments[7:2]
            drvr_enbls.next[2] = 1
            drvr_enbls.next[2:0] = active_segments[2:0]
        elif digit_shf[3] == 1:
            drvr_enbls.next[8:4] = active_segments[7:3]
            drvr_enbls.next[3] = 1
            drvr_enbls.next[3:0] = active_segments[3:0]
        elif digit_shf[4] == 1:
            drvr_enbls.next[8:5] = active_segments[7:4]
            drvr_enbls.next[4] = 1
            drvr_enbls.next[4:0] = active_segments[4:0]
        elif digit_shf[5] == 1:
            drvr_enbls.next[8:6] = active_segments[7:5]
            drvr_enbls.next[5] = 1
            drvr_enbls.next[5:0] = active_segments[5:0]
        elif digit_shf[6] == 1:
            drvr_enbls.next[8:7] = active_segments[7:6]
            drvr_enbls.next[6] = 1
            drvr_enbls.next[6:0] = active_segments[6:0]
        elif digit_shf[7] == 1:
            drvr_enbls.next[7] = 1
            drvr_enbls.next[7:0] = active_segments[7:0]
        else:
            drvr_enbls.next = 0

    def tristate_driver(o, i, enbl):
        ''' Tristate driver module.
                o: 3-state output (high, low, Z). Must be declared TriStateSignal().
                i: input.
                enbl: When low, o is Z, otherwise o is i.
        '''

        o_drvr = o.driver()  # Get ShadowSignal for driving output.

        @always_comb
        def drvr_logic():
            if enbl == 1:
                o_drvr.next = i  # Drive output with value on input.
            else:
                o_drvr.next = None  # Equivalent to Z.

        # Dummy signal driven by o so MyHDL recognizes it as an inout.
        dummy = Signal(bool(0))

        @always_comb
        def dummy_logic():
            dummy.next = bool(o)

        return instances()

    # Attach tristate drivers. The bits where drvr_enbls has 1s will be enabled,
    # while the rest will be Z. Of the enabled bits, the bit driving the anode
    # of the active digit will be high and the rest (connected to the cathodes)
    # will be low.
    d = [d0_o, d1_o, d2_o, d3_o, d4_o, d5_o, d6_o, d7_o]
    for i in range(len(d)):
        inst.append(tristate_driver(d[i], digit_shf(i), drvr_enbls(i)))

    return instances()


def led_digits_scroll(d0_o,
                      d1_o,
                      d2_o,
                      d3_o,
                      d4_o,
                      d5_o,
                      d6_o,
                      d7_o,
                      clk_i,
                      enable_ascii_to_7seg=True,
                      freq_g=100e6):
    ''' Example design for scrolling pattern across LED digits.
    d0_o, ... d7_o: 3-state outputs to drive the StickIt! LEDDigits board.
    clk_i: Input clock.
    enable_ascii_to_7seg: Set True to interpret input digits as ASCII.
    freq_g: Set to frequency of input clock.
    '''

    initialized = Signal(bool(0))  # Initialization flag - starts off uninitialized.
    SCROLL_INTERVAL = 1  # Time interval in seconds between digits scrolling.
    cntr = Signal(intbv(0, 0, int(SCROLL_INTERVAL * freq_g)))  # 1-sec interval counter.
    charstring = Signal(intbv(0)[64:])  # Holds the scrolling characters.

    @always_seq(clk_i.posedge, reset=None)
    def cntr_logic():
        if initialized == False:  # Initialize the character string once upon startup.
            initialized.next = not initialized
            charstring.next = 0x0706050403020120
        elif cntr == 0:  # Rotate the character string once each second.
            cntr.next = cntr.max - 1
            charstring.next[64:8] = charstring[56:0]
            charstring.next[8:0] = charstring[64:56]
        else:  # Decrement the 1-second interval counter.
            cntr.next = cntr - 1

    # Attach the scrolling digits to the LEDDigits module.
    drvrs = [TristateSignal(bool(0)) for _ in range(8)]  # LEDDigits drivers.
    disp = led_digits_display(drvrs[0],
                              drvrs[1],
                              drvrs[2],
                              drvrs[3],
                              drvrs[4],
                              drvrs[5],
                              drvrs[6],
                              drvrs[7],
                              clk_i,
                              charstring(8, 0),
                              charstring(16, 8),
                              charstring(24, 16),
                              charstring(32, 24),
                              charstring(40, 32),
                              charstring(48, 40),
                              charstring(56, 48),
                              charstring(64, 56),
                              enable_ascii_to_7seg=enable_ascii_to_7seg,
                              freq_g=freq_g)

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


def led_digits_scroll_tb():
    '''Testbench for the LED digits scroller.'''
    clk = Signal(bool(0))
    drvrs = [TristateSignal(bool(0)) for _ in range(8)]
    dut = led_digits_scroll(drvrs[0].driver(),
                            drvrs[1].driver(),
                            drvrs[2].driver(),
                            drvrs[3].driver(),
                            drvrs[4].driver(),
                            drvrs[5].driver(),
                            drvrs[6].driver(),
                            drvrs[7].driver(),
                            clk,
                            enable_ascii_to_7seg=False,
                            freq_g=100e4)

    @instance
    def clk_gen():
        for i in range(10000):
            clk.next = not clk
            yield delay(10)
        raise StopSimulation

    return instances()


def led_digits_cnt(d0_o,
                   d1_o,
                   d2_o,
                   d3_o,
                   d4_o,
                   d5_o,
                   d6_o,
                   d7_o,
                   clk_i,
                   enable_ascii_to_7seg=True,
                   freq_g=100e6):
    ''' Example design for eight-digit counter.
    d0_o, ... d7_o: 3-state outputs to drive the StickIt! LEDDigits board.
    clk_i: Input clock.
    enable_ascii_to_7seg: Set True to interpret input digits as ASCII.
    freq_g: Set to frequency of input clock.
    '''

    # Increment a 56-bit counter every clock cycle.
    cntr = Signal(intbv(0)[56:])

    @always_seq(clk_i.posedge, reset=None)
    def cntr_logic():
        cntr.next = cntr + 1

    # Attach the upper 32 bits of the counter to the LED module and discard
    # the lower 24 bits.
    drvrs = [TristateSignal(bool(0)) for _ in range(8)]  # LEDDigits drivers.
    disp = led_digits_display(drvrs[0],
                              drvrs[1],
                              drvrs[2],
                              drvrs[3],
                              drvrs[4],
                              drvrs[5],
                              drvrs[6],
                              drvrs[7],
                              clk_i,
                              cntr(28, 24),
                              cntr(32, 28),
                              cntr(36, 32),
                              cntr(40, 36),
                              cntr(44, 40),
                              cntr(48, 44),
                              cntr(52, 48),
                              cntr(56, 52),
                              enable_ascii_to_7seg=enable_ascii_to_7seg,
                              freq_g=freq_g)

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


def led_digits_cnt_tb():
    '''Testbench for the LED digits counter.'''
    clk = Signal(bool(0))
    drvrs = [TristateSignal(bool(0)) for _ in range(8)]
    dut = led_digits_cnt(drvrs[0].driver(),
                         drvrs[1].driver(),
                         drvrs[2].driver(),
                         drvrs[3].driver(),
                         drvrs[4].driver(),
                         drvrs[5].driver(),
                         drvrs[6].driver(),
                         drvrs[7].driver(),
                         clk,
                         freq_g=100e4)

    @instance
    def clk_gen():
        for i in range(10000):
            clk.next = not clk
            yield delay(10)
        raise StopSimulation

    return instances()

# Main routine that does simulation and Verilog conversion.
if __name__ == '__main__':

    Simulation(traceSignals(led_digits_scroll_tb)).run()

    clk = Signal(bool(0))
    drvrs = [TristateSignal(bool(0)) for _ in range(8)]
    toVerilog(led_digits_scroll, drvrs[0].driver(), drvrs[1].driver(),
              drvrs[2].driver(), drvrs[3].driver(), drvrs[4].driver(),
              drvrs[5].driver(), drvrs[6].driver(), drvrs[7].driver(), clk,
              False)
