from globals import *

def buttons(button_bus, rail1=None, rail2=None, pull1='', pull2=''):
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

    num_buttons = len(button_bus)
    try:
        # Determine the right size for the resistor network based on # of buttons.
        res_ntwk = [R_s, RN2_m, RN4_m, RN4_m, RN8_m, RN8_m, RN8_m, RN8_m][num_buttons-1]
    except IndexError:
        # Use this if there are more than 8 buttons.
        res_ntwk = RN8_m

    # Find the number of resistor network packages that are needed.
    res_per_ntwk = len(res_ntwk.pins)//2  # Number of resistors in the resistor network package.
    num_res_ntwks = ((num_buttons-1) // res_per_ntwk) + 1

    # Create resistor units for pulling button bus to rail1 when button is open.
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

    # Connect buttons and resistors to rails and button bus.
    for i, wire in enumerate(button_bus):
        btn = BUTTON()  # Create button.
        btn[2] += wire  # Connect button to wire in button bus.
        # Connect pull1 resistor between button and rail1 if pull1 value was given.
        # Otherwise, leave it open with no connection to rail1.
        if pull1 != '':
            res_pull1s[i]['L,R'] += btn[2], rail1
        # Connect pull2 resistor between button and rail2 if pull2 value was given.
        # Otherwise, connect button directly to rail2.
        if pull2 != '':
            res_pull2s[i]['L,R'] += rail2, btn[1]
        else:
            btn[1] += rail2

if __name__ == '__main__':
    btn_bus = Bus('BTN_BUS', 3)
    buttons(btn_bus, Net('+3.3V'), Net('GND'), '10K', '100')
    ERC()
    generate_netlist()
