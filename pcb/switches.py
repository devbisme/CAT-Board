from globals import *

def switches(switch_bus, rail1=None, rail2=None, pull1='', pull2=''):
    """
    Passed a button bus of a certain width, this function will:
        1. Create a button for each wire in the bus.
        2. Connect one side of each button to a bus wire.
        3. Connect a resistor of value pull1 from each bus wire to rail1.
           (This resistor is omitted if pull1 is an empty string.)
        4. Connect a resistor of value pull2 from the other button terminal to rail2.
           (The button terminal connects directly to rail2 if pull2 is an empty string.)
    """
    if switch_bus is None:
        return # No need  to make any switches.

    num_switches = len(switch_bus)
    try:
        # Determine the right size for the resistor network based on # of switches.
        res_ntwk = [R_s, RN2_m, RN4_m, RN4_m, RN8_m, RN8_m, RN8_m, RN8_m][num_switches-1]
    except IndexError:
        # Use this if there are more than 8 switches.
        res_ntwk = RN8_m

    # Find the number of resistor network packages that are needed.
    res_per_ntwk = len(res_ntwk.pins)//2  # Number of resistors in the resistor network package.
    num_res_ntwks = ((num_switches-1) // res_per_ntwk) + 1

    # Create resistor units for pulling switch bus to rail1 when button is open.
    res_pull1s = []
    if pull1 != '':
        for _ in range(num_res_ntwks):
            rn = res_ntwk(value=pull1)
            rn[:] += NC
            for unit in 'ABCDEFGH'[0:res_per_ntwk]:
                res_pull1s.append(rn.unit[unit])

    # Create resistor units for pulling button bus to rail2 when button is closed.
    res_pull2s = []
    if pull2 != '':
        for _ in range(num_res_ntwks):
            rn = res_ntwk(value=pull2)
            rn[:] += NC
            for unit in 'ABCDEFGH'[0:res_per_ntwk]:
                res_pull2s.append(rn.unit[unit])

    try:
        # Determine the right size for the DIP switch package based on # of switches.
        switch_pack = [DIP_SW1, DIP_SW2, DIP_SW3, DIP_SW4, DIP_SW5, DIP_SW6, DIP_SW7, DIP_SW8][num_switches-1]
    except IndexError:
        # Use this if there are more than 8 switches.
        switch_pack = DIP_SW8

    # Find the number of DIP switch packages that are needed.
    switches_per_pack = len(switch_pack.pins)//2
    num_switch_packs = ((num_switches-1) // switches_per_pack) + 1

    # Create switch units for connecting to the switch bus.
    switches = []
    for _ in range(num_switch_packs):
        swpack = switch_pack()
        swpack[:] += NC
        for unit in 'ABCDEFGH'[0:switches_per_pack]:
            switches.append(swpack.unit[unit])

    # Connect buttons and resistors to rails and button bus.
    for i, wire in enumerate(switch_bus):
        switches[i]['R'] += wire  # Connect switch to wire in switch bus.
        # Connect pull1 resistor between switch and rail1 if pull1 value was given.
        # Otherwise, leave it open with no connection to rail1.
        if pull1 != '':
            res_pull1s[i]['L,R'] += switches[i]['R'], rail1
        # Connect pull2 resistor between switch and rail2 if pull2 value was given.
        # Otherwise, connect button directly to rail2.
        if pull2 != '':
            res_pull2s[i]['L,R'] += rail2, switches[i]['L']
        else:
            switches[i]['L'] += rail2

if __name__ == '__main__':
    switch_bus = Bus('SWITCH_BUS', 3)
    switches(switch_bus, Net('+3.3V'), Net('GND'), '10K', '100')
    ERC()
    generate_netlist()
