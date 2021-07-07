from globals import *

@subcircuit
def pmod_io(bus, vcc1=None, vcc2=None, gnd=None):
    """
    """

    if not vcc1 and not vcc2:
        vcc1 = Net.fetch('+3.3V')
    if not gnd:
        gnd = Net.fetch('GND')

    # If two voltage supplies are available, create a 3-pin jumper to select
    # which one powers the PMOD connector.
    if vcc1 and vcc2:
        voltage_selector = JMP3()
        voltage_selector[1,3] += vcc1, vcc2
        vcc = voltage_selector[2]  # PMOD power supply comes off the middle pin.
        vcc.drive = POWER  # Make the pin capable of driving power to other parts.
    else:
        vcc = vcc1 or vcc2

    pmod = PMOD_SOCKET()
    pmod[1,7,2,8,3,9,4,10] += bus[0:7]  # Connect I/O bus to socket.
    vcc += pmod[6,12]
    gnd += pmod[5,11]

if __name__ == '__main__':
    pmod_io(Bus(BUS_PREFIX,8), vcc=Net('+3.3V'), gnd=Net('GND'))
    ERC()
    generate_netlist()
