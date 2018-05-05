from globals import *

def leds(rail_a, rail_k, current_limit_resistance):
    """
    Passed a bus of a certain width, this function will:
        1. Create an LED and resistor for each wire in the bus.
        2. Connect the resistor and LED in series.
        3. Connect the cathode of the LED to rail_k.
        4. Connect the other end of the resistor to rail_a.
    If rail_a is a multi-bit bus and rail_k is a single GND wire, then the
    set of LEDs will be activated by high levels on the rail_a bus.
    OTOH, if rail_a is a single VCC wire and rail_k is a multi-bit bus, then
    the LEDs will be activated by low levels on the rail_k bus.
    """

    # Only one bus should be multi-bit.
    assert rail_a.width==1 or rail_k.width==1

    # Number of LEDs is the maximum width of the buses.
    num_leds = max(rail_a.width, rail_k.width)

    try:
        # Determine the right size for the resistor network based on # of LEDs.
        res_ntwk = [R_s, RN2_m, RN4_m, RN4_m, RN8_m, RN8_m, RN8_m, RN8_m][num_leds-1]
    except IndexError:
        # Use this if there are more than 8 switches.
        res_ntwk = RN8_m

    # Find the number of resistor network packages that are needed.
    res_per_ntwk = len(res_ntwk.pins)//2  # Number of resistors in the resistor network package.
    num_res_ntwks = ((num_leds-1) // res_per_ntwk) + 1

    # Create resistor units for limiting current through the LEDs.
    res = []
    for _ in range(num_res_ntwks):
        rn = res_ntwk(value=current_limit_resistance)
        rn[:] += NC
        for unit in 'ABCDEFGH'[0:res_per_ntwk]:
            res.append(rn.unit[unit])

    # Create the required number of LEDs.
    if num_leds < 2:
        leds = [LED_m(),]
    else:
        leds = LED_m * num_leds  # Make sure it's a list, even if there's only one LED.

    # Connect LEDs and resistors is series.
    for r, led in zip(res, leds):
        r['R'] += led['A']  # Resistor connects to LED anode (+).

    # Connect the LED+resistor combos to the buses.
    if rail_a.width > rail_k.width:
        # The anode bus is multi-bit and the cathode bus is a single wire,
        # so connect the other end of the resistors to the anode bus and
        # connect the LED cathodes (-) to the single cathode wire.
        rail_a[:] += [r['L'] for r in res[0:num_leds]]
        rail_k += [led['K'] for led in leds[0:num_leds]]
    else:
        # The cathode bus is multi-bit and the anode bus is a single wire.
        # so connect the other end of the resistors to the single anode wire and
        # connect the LED cathodes (-) to the cathode bus.
        rail_a += [r['L'] for r in res[0:num_leds]]
        rail_k[:] += [led['K'] for led in leds[0:num_leds]]


if __name__ == '__main__':
    leds(Bus('DRVA',5), Net.fetch('GND'), '330')
    leds(Net('DRVB'), Net.fetch('GND'), '330')
    ERC()
    generate_netlist()
