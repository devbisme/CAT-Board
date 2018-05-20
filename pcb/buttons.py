from globals import *

def buttons(button_bus, rail1=None, rail2=None, pull1='', pull2='',
            button_type = BUTTON,
            r_types = [None, R_m, RN2_m, RN4_m, RN4_m, RN4_m, RN8_m, RN8_m, RN8_m],
    ):
    """
    Passed a button bus of a certain width, this function will:
        1. Create a button for each wire in the bus.
        2. Connect one side of each button to a bus wire.
        3. Connect a resistor of value pull1 from each bus wire to rail1.
           (This resistor is omitted if pull1 is an empty string.)
        4. Connect a resistor of value pull2 from the other button terminal to rail2.
           (The button terminal connects directly to rail2 if pull2 is an empty string.)
    """

    if button_bus is None:
        return # No need  to make any buttons.

    width = len(button_bus)

    buttons = width * button_type

    # The bus width indicates the number of buttons (and, hence, the number of
    # resistors) that are needed. Pick the best resistor array and subtract its
    # size from the number of resistors that are needed. If more resistors are
    # still required, repeat the loop until the number drops to zero.
    r_needed = width  # The number of resistors that are currently needed.
    rs1 = []          # Store the selected resistors here.
    rs2 = []          # Store the selected resistors here.
    left_pins1 = []   # List of pins on the left side of the selected resistors.
    right_pins1 = []  # List of pins on the right side of the selected resistors.
    left_pins2 = []   # List of pins on the left side of the selected resistors.
    right_pins2 = []  # List of pins on the right side of the selected resistors.

    while r_needed > 0:  # Loop as long as resistors are needed.

        # Pick the best resistor for the current number of resistors that are needed.
        # If the needed number is larger than the list of resistors, then pick
        # the largest available resistor array (which will be at the end of the list).
        try:
            r_type = r_types[r_needed]
        except IndexError:
            r_type = r_types[-1]  # Pick the largest resistor array.

        if pull1 != '':
            r = r_type(value=pull1)  # Instantiate the selected resistor.
            rs1.append(r)  # Add the resistor to the list of selected resistors.

            num_pins = len(r.pins)  # Number of pins on the selected resistor's package.
            num_resistors = num_pins // 2  # Each resistor takes up two pins on the package.

            # Store the pins on the left and right sides of the resistor.
            # The pins increase from 1 ... num_pins/2 on the left side, and decrease from
            # num_pins ... num_pins/2+1 on the right side. This keeps the left and
            # right pin of each resistor in the package aligned between the lists.
            left_pins1.extend( r[       1:num_pins//2  ])
            right_pins1.extend(r[num_pins:num_pins//2+1])

        if pull2 != '':
            r = r_type(value=pull2)  # Instantiate the selected resistor.
            rs2.append(r)  # Add the resistor to the list of selected resistors.

            num_pins = len(r.pins)  # Number of pins on the selected resistor's package.
            num_resistors = num_pins // 2  # Each resistor takes up two pins on the package.

            # Store the pins on the left and right sides of the resistor.
            # The pins increase from 1 ... num_pins/2 on the left side, and decrease from
            # num_pins ... num_pins/2+1 on the right side. This keeps the left and
            # right pin of each resistor in the package aligned between the lists.
            left_pins2.extend( r[       1:num_pins//2  ])
            right_pins2.extend(r[num_pins:num_pins//2+1])

        # Subtract the resistors in the selected package from the number that
        # are needed and loop until that number goes to zero.
        r_needed -= num_resistors

    # The number of resistors needed may not fit exactly into the number of 
    # resistors selected (e.g., an eight-resistor array might be used when seven
    # resistors are needed). Therefore, trim the pin lists to the number of
    # resistors that are needed. (This may leave some pins on the last-selected
    # array unconnected.) Also, put them on buses so they'll be easy to connect to.
    if pull1 != '':
        left_pins1  = Bus('', left_pins1[0:width])
        right_pins1 = Bus('', right_pins1[0:width])
    if pull2 != '':
        left_pins2  = Bus('', left_pins2[0:width])
        right_pins2 = Bus('', right_pins2[0:width])

    button_bus += [button[2] for button in buttons]
    if pull1 != '':
        rail1 += left_pins1
        button_bus += right_pins1
    if pull2 != '':
        left_pins2 += [button[1] for button in buttons]
        rail2 += right_pins2
    else:
        rail2 += [button[1] for button in buttons]

if __name__ == '__main__':
    btn_bus = Bus('BTN_BUS', 3)
    buttons(btn_bus, Net('+3.3V'), Net('GND'), '10K', '100')
    ERC()
    generate_netlist()
