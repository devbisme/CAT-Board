from globals import *

def pmod_io(bus, vcc=None, gnd=None):
    """
    """

    if not vcc:
        vcc1 = Net.fetch('+3.3V')
    if not gnd:
        gnd = Net.fetch('GND')

    pmod = PMOD_SOCKET()
    pmod[1,7,2,8,3,9,4,10] += bus[0:7]  # Connect I/O bus to socket.
    vcc += pmod[6,12]
    gnd += pmod[5,11]

if __name__ == '__main__':
    pmod_io(Bus(BUS_PREFIX,8), vcc=Net('+3.3V'), gnd=Net('GND'))
    ERC()
    generate_netlist()
