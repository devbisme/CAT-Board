# MIT license
# 
# Copyright (C) 2016 by XESS Corporation.
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


# Maximum-length LFSR taps from Table 3 of XAPP 052: 
# http://www.xilinx.com/support/documentation/application_notes/xapp052.pdf
lfsr_taps = {
    3: (3, 2),
    4: (4, 3),
    5: (5, 3),
    6: (6, 5),
    7: (7, 6),
    8: (8, 6, 5, 4),
    9: (9, 5),
    10: (10, 7),
    11: (11, 9),
    12: (12, 6, 4, 1),
    13: (13, 4, 3, 1),
    14: (14, 5, 3, 1),
    15: (15, 14),
    16: (16, 15, 13, 4),
    17: (17, 14),
    18: (18, 11),
    19: (19, 6, 2, 1),
    20: (20, 17),
    21: (21, 19),
    22: (22, 21),
    23: (23, 18),
    24: (24, 23, 22, 17),
    25: (25, 22),
    26: (26, 6, 2, 1),
    27: (27, 5, 2, 1),
    28: (28, 25),
    29: (29, 27),
    30: (30, 6, 4, 1),
    31: (31, 28),
    32: (32, 22, 2, 1),
    33: (33, 20),
    34: (34, 27, 2, 1),
    35: (35, 33),
    36: (36, 25),
    37: (37, 5, 4, 3, 2, 1),
    38: (38, 6, 5, 1),
    39: (39, 35),
    40: (40, 38, 21, 19),
    41: (41, 38),
    42: (42, 41, 20, 19),
    43: (43, 42, 38, 37),
    44: (44, 43, 18, 17),
    45: (45, 44, 42, 41),
    46: (46, 45, 26, 25),
    47: (47, 42),
    48: (48, 47, 21, 20),
    49: (49, 40),
    50: (50, 49, 24, 23),
    51: (51, 50, 36, 35),
    52: (52, 49),
    53: (53, 52, 38, 37),
    54: (54, 53, 18, 17),
    55: (55, 31),
    56: (56, 55, 35, 34),
    57: (57, 50),
    58: (58, 39),
    59: (59, 58, 38, 37),
    60: (60, 59),
    61: (61, 60, 46, 45),
    62: (62, 61, 6, 5),
    63: (63, 62),
    64: (64, 63, 61, 60),
    65: (65, 47),
    66: (66, 65, 57, 56),
    67: (67, 66, 58, 57),
    68: (68, 59),
    69: (69, 67, 42, 40),
    70: (70, 69, 55, 54),
    71: (71, 65),
    72: (72, 66, 25, 19),
    73: (73, 48),
    74: (74, 73, 59, 58),
    75: (75, 74, 65, 64),
    76: (76, 75, 41, 40),
    77: (77, 76, 47, 46),
    78: (78, 77, 59, 58),
    79: (79, 70),
    80: (80, 79, 43, 42),
    81: (81, 77),
    82: (82, 79, 47, 44),
    83: (83, 82, 38, 37),
    84: (84, 71),
    85: (85, 84, 58, 57),
    86: (86, 85, 74, 73),
    87: (87, 74),
    88: (88, 87, 17, 16),
    89: (89, 51),
    90: (90, 89, 72, 71),
    91: (91, 90, 8, 7),
    92: (92, 91, 80, 79),
    93: (93, 91),
    94: (94, 73),
    95: (95, 84),
    96: (96, 94, 49, 47),
    97: (97, 91),
    98: (98, 87),
    99: (99, 97, 54, 52),
    100: (100, 63),
    101: (101, 100, 95, 94),
    102: (102, 101, 36, 35),
    103: (103, 94),
    104: (104, 103, 94, 93),
    105: (105, 89),
    106: (106, 91),
    107: (107, 105, 44, 42),
    108: (108, 77),
    109: (109, 108, 103, 102),
    110: (110, 109, 98, 97),
    111: (111, 101),
    112: (112, 110, 69, 67),
    113: (113, 104),
    114: (114, 113, 33, 32),
    115: (115, 114, 101, 100),
    116: (116, 115, 46, 45),
    117: (117, 115, 99, 97),
    118: (118, 85),
    119: (119, 111),
    120: (120, 113, 9, 2),
    121: (121, 103),
    122: (122, 121, 63, 62),
    123: (123, 121),
    124: (124, 87),
    125: (125, 124, 18, 17),
    126: (126, 125, 90, 89),
    127: (127, 126),
    128: (128, 126, 101, 99),
    129: (129, 124),
    130: (130, 127),
    131: (131, 130, 84, 83),
    132: (132, 103),
    133: (133, 132, 82, 81),
    134: (134, 77),
    135: (135, 124),
    136: (136, 135, 11, 10),
    137: (137, 116),
    138: (138, 137, 131, 130),
    139: (139, 136, 134, 131),
    140: (140, 111),
    141: (141, 140, 110, 109),
    142: (142, 121),
    143: (143, 142, 123, 122),
    144: (144, 143, 75, 74),
    145: (145, 93),
    146: (146, 145, 87, 86),
    147: (147, 146, 110, 109),
    148: (148, 121),
    149: (149, 148, 40, 39),
    150: (150, 97),
    151: (151, 148),
    152: (152, 151, 87, 86),
    153: (153, 152),
    154: (154, 152, 27, 25),
    155: (155, 154, 124, 123),
    156: (156, 155, 41, 40),
    157: (157, 156, 131, 130),
    158: (158, 157, 132, 131),
    159: (159, 128),
    160: (160, 159, 142, 141),
    161: (161, 143),
    162: (162, 161, 75, 74),
    163: (163, 162, 104, 103),
    164: (164, 163, 151, 150),
    165: (165, 164, 135, 134),
    166: (166, 165, 128, 127),
    167: (167, 161),
    168: (168, 166, 153, 151),
}


def uniform_rand_gen(clk_i, enbl_i, load_i, seed_i, rand_o):
    '''Uniform random number generator.'''

    width = len(rand_o)  # Width of random number to be generated.

    shfreg = Signal(intbv(1, 0, rand_o.max)) # Holds random number.

    # Create a mask with 1-bits at each tap position in the random number.
    mask = 0
    for t in lfsr_taps[width]:
        mask = mask | (1 << (t - 1))

    # Sequential process to generate random number.
    @always_seq(clk_i.posedge, reset=None)
    def rand_shift():

        # Mask off the feedback bit values and XOR them.
        bits = shfreg & mask
        xor_bit = 0
        for i in range(width):
            xor_bit = xor_bit ^ bits[i]

        if load_i:
            # Load the random number register with the starting seed value.
            shfreg.next = seed_i
        elif enbl_i:
            # Shift the random number by one bit and push in the XOR bit.
            shfreg.next[len(shfreg):1] = shfreg[len(shfreg) - 1:0]
            shfreg.next[0] = xor_bit

    # Combinational process to output the random number.
    @always_comb
    def rand_out():
        rand_o.next = shfreg

    return instances()


def xorshift_rand_gen(clk_i, enbl_i, load_i, seed_i, rand_o):
    '''Uniform random number generator.'''

    x, y, z, w, t = [Signal(intbv(0,0,2**32)) for _ in range(5)]
    
    # Sequential process to generate random number.
    @always_seq(clk_i.posedge, reset=None)
    def rand_shift():

        if load_i:
            # Load the random number register with the starting seed value.
            # (The seed_i input is ignored.)
            x.next = 123456789
            y.next = 362436069
            z.next = 521288629
            w.next = 88675123
        elif enbl_i:
            t.next = x ^ (x << 11)[32:0]
            x.next = y
            y.next = z
            z.next = w
            w.next = w ^ (w>>19) ^ (t ^ (t>>8))

    # Combinational process to output the random number.
    # The maximum width of the output is 32 bits.
    @always_comb
    def rand_out():
        rand_o.next = w[len(rand_o):0]

    return instances()


import math  # Need this to compute scaling shift. 

sum_length = 16
base_rng = xorshift_rand_gen

def normal_rand_gen(clk_i, enbl_i, load_i, seed_i, rand_o):
    '''Normal (Gaussian) random number generator.'''

    # Instantiate a uniform RNG.
    uni_rand = Signal(intbv(0, 0, rand_o.max))
    uni_rng = base_rng(clk_i, enbl_i, load_i, seed_i, uni_rand)

    # Create a FIFO for storing samples of the uniform random numbers.
    uni_rand_samples = [Signal(intbv(0, 0, rand_o.max)) for _ in range(sum_length)]
    
    # Create a signal with more bits for storing the sum of N random numbers.
    rand_sum = Signal(intbv(0, 0, sum_length*rand_o.max))
    
    # Update the sum of random numbers with a new value on every clock cycle.
    @always_seq(clk_i.posedge, reset=None)
    def uni_sum_to_gauss():
        
        # Create the sum by adding the newest random number and subtracting the oldest.
        rand_sum.next = rand_sum - uni_rand_samples[sum_length-1] + uni_rand
        
        # Then enter the newest into the FIFO while discarding the oldest.
        for i in range(sum_length-1):
            uni_rand_samples[i+1].next = uni_rand_samples[i]
        uni_rand_samples[0].next = uni_rand

    # The sum has to be scaled to be in the same range as the original random numbers.
    scale_shift = int(round(math.log(sum_length,2)))
    
    # Output the scaled sum. This will be a normally-distributed random number.
    @always_comb
    def scale_and_output_sum():
        rand_o.next = rand_sum >> scale_shift

    return instances()


rand_seq = []  # Store the generated random numbers here.

def rand_gen_tb(rng, width, n_cycles):

    # Define the signals that connect to the RNG.
    clk = Signal(bool(0))
    enbl = Signal(bool(0))
    load = Signal(bool(0))
    rand = Signal(intbv(0)[width:])  # This sets the #bits for the random numbers.
    seed = 42  # 42 is the answer for everything, so use it for the RNG seed.

    # Instantiate the given RNG model and connect it to the defined signals.
    dut = rng(clk, enbl, load, seed, rand)

    @instance
    def tb():
        
        enbl.next = 1  # Enable random number generation.
        load.next = 1  # Load the random number seed on the 1st clock pulse.
        for _ in range(n_cycles):
            
            # Generate a new randon number by pulsing the clock.
            clk.next = 0
            yield delay(1)
            clk.next = 1
            yield delay(1)
            
            rand_seq.append(int(rand.val))  # Store the current output of the RNG.
            load.next = 0  # Turn off seed loading for the remaining clock pulses.

    return instances()


if __name__ == '__main__':
    base_rng = xorshift_rand_gen
    Simulation(rand_gen_tb(normal_rand_gen, 16, 2**16)).run()

    import seaborn as sns            # Use the pretty Seaborn coloring for the plots.
    import matplotlib.pyplot as plt  # Load the plotting library.

    # Show a histogram of the random numbers that were generated.
    bins = list(range(0,65535,656)) # Divide the random number range into 100 bins.
    plt.hist(rand_seq, bins)
    plt.show()

    # clk = Signal(bool(0))
    # enbl = Signal(bool(0))
    # load = Signal(bool(0))
    # seed = Signal(intbv(0)[16:])
    # rand = Signal(intbv(0)[16:])
    # toVerilog(uniform_rand_gen, clk, enbl, load, seed, rand)
    # toVerilog(xorshift_rand_gen, clk, enbl, load, seed, rand)
    # toVerilog(normal_rand_gen, clk, enbl, load, seed, rand)
