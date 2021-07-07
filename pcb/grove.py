from globals import *

@subcircuit
def grove_io(d1=None, rx=None, scl=None, d2=None, tx=None, sda=None, vcc=None, gnd=None):
    """
    Instantiate a GROVE male connector.
    """

    if not vcc:
        vcc = Net.fetch('+3.3V')
    if not gnd:
        gnd = Net.fetch('GND')

    d1_sum = sum([int(bool(v)) for v in [d1,rx,scl]])
    if d1_sum == 0:
        logger.error('No connection on GROVE pin D1, RX or SCL. Must connect one and only one.')
        raise Exception
    if d1_sum > 1:
        logger.error('Must connect one and only one of the Grove D1, RX, and SCL pins.')
        raise Exception
    io1 = d1 or rx or scl  # This will get the one valid I/O net.

    d2_sum = sum([int(bool(v)) for v in [d2,tx,sda]])
    if d2_sum == 0:
        logger.error('No connection on GROVE pin D2, TX or SDA. Must connect one and only one.')
        raise Exception
    if d1_sum > 1:
        logger.error('Must connect one and only one of the Grove D2, TX, and SDA pins.')
        raise Exception
    io2 = d2 or tx or sda  # This will get the one valid I/O net.

    # This triggers if only one or the other of SCL or SDA is used.
    if bool(scl) ^ bool(sda):
        logger.error('Must use both SCL and SDA for GROVE I2C I/O.')
        raise Exception

    # This triggers if only one or the other of TX or RX is used.
    if bool(rx) ^ bool(tx):
        logger.error('Must use both RX and TX for GROVE UART I/O.')
        raise Exception

    # Put in the I2C pullup resistors if SCL and SDA are being used.
    if scl and sda:
        i2c_pullup = RN2_m(value='4.7K')
        i2c_pullup[1,2] += scl, sda
        i2c_pullup[3,4] += vcc

    # Finally, instantiate the GROVE connector.
    grv = GROVE_HDR()
    grv[1, 2, 3, 4] += io1, io2, vcc, gnd

if __name__ == '__main__':
    grove_io(scl=Net('SCL'), sda=Net('SDA'), vcc=Net('+5V'), gnd=gnd)
    #grove_io(rx=Net('SCL'), sda=Net('SDA'), vcc=Net('+5V'), gnd=Net('GND'))
    #grove_io(d1=Net('D1'), vcc=Net('+5V'), gnd=Net('GND'))
    grove_io(d1=Net('D1'), d2=Net('D2'), vcc=Net('+5V'), gnd=gnd)
    grove_io(d1=Net('D1'), d2=Net('D2'))
    ERC()
    generate_netlist()
