from globals import *

def hdmi_intfc(clk_p, clk_n, data_p, data_n, scl, sda):

    global gnd

    hdmi = Part('xess', 'HDMI-FEMALE', footprint='HD10-001')  # Female HDMI socket.

    hdmi['SHLD$', 'GND'] += gnd

    hdmi['CEC'] += NC  # Leave Consumer Electronics Comm unconnected.

    hdmi['HEAC+'] += gnd

    # Attach +/- differential pairs for the clock.
    hdmi['CLK+, CLK-'] += clk_p, clk_n

    # Attach +/- differential pairs for the data lines.
    for i, (p, n) in enumerate(zip(data_p, data_n)):
        hdmi['D{0}+, D{0}-'.format(i)] += p, n

    # Pullup resistors attach to +5V output from HDMI connector and the I2C
    # clock and data lines. These pass through small serial resistors to limit
    # currents when attached to the 3.3V pins of the FPGA. When the FPGA pulls
    # a line to ground, the HDMI device will see 5V * 100/(2K + 100) = .24V.
    # When the FPGA tristates a line, the HDMI device will see
    # 3.3V + 0.7V + (5V - 4V) * 100/(2K + 100) = 4.05V.
    i2c_pullup = RN2(value='2K0')  # Pullups to +5V for HDMI I2C bus.
    i2c_pullup.unit['A']['PL,PR'] += hdmi['SCL'], hdmi['+5V']
    i2c_pullup.unit['B']['PL,PR'] += hdmi['SDA'], hdmi['+5V']
    i2c_serial = RN2(value='100')  # Serial resistors for level-shift to +3.3.
    i2c_serial.unit['A']['PL,PR'] += scl, hdmi['SCL']
    i2c_serial.unit['B']['PL,PR'] += sda, hdmi['SDA']

    # Connect resistor between +5V and DETECT of HDMI.
    r_detect = R_m(value='10K')
    r_detect[1,2] += hdmi['DETECT'], hdmi['+5V']

    # Attach parallel R-C between HDMI shield and ground.
    r_shield = R_m(value='100K')
    c_shield = C_m(value='1uF')
    r_shield[1, 2] += hdmi['SH'], gnd
    c_shield[1, 2] += hdmi['SH'], gnd

if __name__ == '__main__':
    clk_p, clk_n = Net('CLK+'), Net('CLK-')
    data_p, data_n = Bus('DATA+', 3), Bus('DATA-', 3)
    scl, sda = Net('SCL'), Net('SDA')
    hdmi_intfc(clk_p, clk_n, data_p, data_n, scl, sda)
    ERC()
    generate_netlist()
