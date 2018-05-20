from globals import *

def leds(anodes, cathodes, resistance='330',
        led_type = LED_m,
        r_types = [None, R_m, RN2_m, RN4_m, RN4_m, RN4_m, RN8_m, RN8_m, RN8_m],
    ):

    # Either the anode will be connected to VCC or the cathode will be connected
    # to ground and will have a width of 1. The width of the other input bus will
    # determine the number of LEDs.
    width = max(anodes.width, cathodes.width)

    # Create the LEDs that connect to each input.
    leds = width * led_type

    # The bus width indicates the number of LEDs (and, hence, the number of
    # resistors) that are needed. Pick the best resistor array and subtract its
    # size from the number of resistors that are needed. If more resistors are
    # still required, repeat the loop until the number drops to zero.
    r_needed = width  # The number of resistors that are currently needed.
    rs = []           # Store the selected resistors here.
    left_pins = []    # List of pins on the left side of the selected resistors.
    right_pins = []   # List of pins on the right side of the selected resistors.

    while r_needed > 0:  # Loop as long as resistors are needed.

        # Pick the best resistor for the current number of resistors that are needed.
        # If the needed number is larger than the list of resistors, then pick
        # the largest available resistor array (which will be at the end of the list).
        try:
            r_type = r_types[r_needed]
        except IndexError:
            r_type = r_types[-1]  # Pick the largest resistor array.

        r = r_type(value=resistance)  # Instantiate the selected resistor.
        rs.append(r)  # Add the resistor to the list of selected resistors.

        num_pins = len(r.pins)  # Number of pins on the selected resistor's package.
        num_resistors = num_pins // 2  # Each resistor takes up two pins on the package.

        # Store the pins on the left and right sides of the resistor.
        # The pins increase from 1 ... num_pins/2 on the left side, and decrease from
        # num_pins ... num_pins/2+1 on the right side. This keeps the left and
        # right pin of each resistor in the package aligned between the lists.
        left_pins.extend( r[       1:num_pins//2  ])
        right_pins.extend(r[num_pins:num_pins//2+1])

        # Subtract the resistors in the selected package from the number that
        # are needed and loop until that number goes to zero.
        r_needed -= num_resistors

    # The number of resistors needed may not fit exactly into the number of 
    # resistors selected (e.g., an eight-resistor array might be used when seven
    # resistors are needed). Therefore, trim the pin lists to the number of
    # resistors that are needed. (This may leave some pins on the last-selected
    # array unconnected.) Also, put them on buses so they'll be easy to connect to.
    left_pins  = Bus('', left_pins[0:width])
    right_pins = Bus('', right_pins[0:width])

    anodes += [led['A'] for led in leds]     # Connect LED anodes to anode inputs.
    left_pins += [led['K'] for led in leds]  # Connect LED cathodes to left side of resistors.
    cathodes += right_pins                   # Connect right side of resistors to cathode inputs.

if __name__ == '__main__':
    v3_3 = Net('+3.3V')
    gnd = Net('GND')
    mcu = Part('MCU_Microchip_pic18', 'pic18f2450-IML', footprint='xesscorp/xess.pretty:QFN-28')
    mcu['VDD'] += v3_3
    mcu['VSS'] += gnd
    leds(v3_3, mcu['RA[2:6]'])  # Attach 5 common-anode LEDs.
    ERC()
    generate_netlist()
