from globals import *

def i2c_flash(scl, sda, address=None, vcc=None, gnd=None):
    """
    """

    if not vcc:
        vcc = Net.fetch('+3.3V')
    if not gnd:
        gnd = Net.fetch('GND')

    i2c_flash_ic = I2C_FLASH()

    if not address:
        address = 0
    if isinstance(address, int):
        address = int2bus(address, 3, vcc, gnd)

    i2c_flash_ic['A0, A1, A2'] += address[0:2]
    i2c_flash_ic['SCL, SDA'] += scl, sda
    i2c_flash_ic['VCC, GND'] += vcc, gnd
    i2c_flash_ic.WP += vcc

    i2c_pullup = RN2_m()
    i2c_pullup.A['L,R'] += scl, vcc
    i2c_pullup.B['L,R'] += sda, vcc

    C_byp()[1,2] += vcc, gnd  # Decoupling cap for flash chip.


if __name__ == '__main__':
    #i2c_flash(scl=Net('SCL'), sda=Net('SDA'), address=Bus('ADDR',3), vcc=Net('+3.3V'), gnd=Net('GND'))
    i2c_flash(scl=Net('SCL'), sda=Net('SDA'), address=3, vcc=Net('+3.3V'), gnd=Net('GND'))
    ERC()
    generate_netlist()
