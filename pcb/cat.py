from globals import *
from grove import *
from hdmi import *
from i2c_flash import *
from leds import *
from osc import *
from pmod import *
from switches import *
from buttons import *
from config_flash import *
from sdram import *
from raspi_gpio import *

# Create power and ground nets.
Net.fetch('GND').drive = POWER
#Net.fetch('+3.3V').drive = POWER
#Net.fetch('+5V').drive = POWER
#Net.fetch('+1.2V').drive = POWER

# Instantiate the FPGA.
fpga = FPGA()
NC += fpga['.*']

# Connect power/ground for FPGA.
Net.fetch('GND').connect(fpga['GND[18]'])
Net.fetch('+3.3V').connect(fpga['VCCIO'])
Net.fetch('+1.2V').connect(fpga['VCC[6]'])

# 2.5V for VPP using a diode to drop 3.3 to 2.5.
Part('device', 'D', footprint='KiCad_V5/Diode_SMD.pretty:D_SOD-323')['A,K'] += Net.fetch('+3.3V'), Net.fetch('+2.5V')
Net.fetch('+2.5V').connect(fpga['VPP_2V5'])
Net.fetch('+2.5V').drive = POWER

# FPGA power bypass caps.
for _ in range(4):
    C_m(value='1.0uF')[1,2] += Net.fetch('+3.3V'), Net.fetch('GND')
    C_s(value='0.1uF')[1,2] += Net.fetch('+3.3V'), Net.fetch('GND')
for _ in range(2):
    C_m(value='1.0uF')[1,2] += Net.fetch('+1.2V'), Net.fetch('GND')
    C_s(value='0.1uF')[1,2] += Net.fetch('+1.2V'), Net.fetch('GND')

# Connect FPGA PLL power with filtering caps and resistors.
def pll_pwr(supply, vccpll, gndpll):
    R_s(value='100')[1,2] += supply, vccpll
    C_s(value='0.1uF')[1,2] += vccpll, gndpll
    C_m(value='10uF')[1,2] += vccpll, gndpll
    gndpll.drive = POWER
    vccpll.drive = POWER

pll_pwr(Net.fetch('+1.2V'), fpga['VCCPLL0'], fpga['GNDPLL0'])
pll_pwr(Net.fetch('+1.2V'), fpga['VCCPLL1'], fpga['GNDPLL1'])

# Reset button for FPGA. The Raspi can also drive the FPGA RESET pin.
buttons(Bus.fetch('RESET',1), rail2=Net.fetch('GND'), pull2='330')
fpga['CRESET_B'] += Bus.fetch('RESET')[0], Net.fetch('BCM22')

# Connect FPGA DONE status pin to Raspi.
fpga['CDONE'] += Net.fetch('BCM17')

# Place pullup resistors on the FPGA RESET and DONE pins.
reset_done_pullups = RN2_m(value='4.7K')
reset_done_pullups.A['L,R'] += Net.fetch('+3.3V'), fpga['CRESET_B']
reset_done_pullups.B['L,R'] += Net.fetch('+3.3V'), fpga['CDONE']

# Add the FPGA configuration serial flash.
fpga_config(fpga)

# Construct the socket for connecting to the Raspberry Pi. 
rpi = RaspiGpioIntfc()
#rpi.v3v3        += NC
rpi.v5v         += Net.fetch('+5V-Raspi')
rpi.gnd         += Net.fetch('GND')
raspi_gpio(intfc=rpi)
rpi.bcm2_sda    += fpga['R16']
rpi.bcm3_scl    += fpga['T16']
rpi.bcm4_gpclk0 += fpga['R9' ]
rpi.bcm5        += fpga['T6' ]
rpi.bcm6        += fpga['T5' ]
rpi.bcm7_ce1    += fpga['T7' ]
rpi.bcm8_ce0    += fpga['T8' ]
rpi.bcm12       += fpga['R6' ]
rpi.bcm13       += fpga['R5' ]
rpi.bcm14_txd   += fpga['T15']
rpi.bcm15_rxd   += fpga['T14']
rpi.bcm16       += fpga['R4' ]
rpi.bcm18_pcm_c += fpga['T11']
rpi.bcm19_miso  += fpga['T3' ]
rpi.bcm20_mosi  += fpga['R3' ]
rpi.bcm21_sclk  += fpga['T1' ]
rpi.bcm23       += fpga['P9' ]
rpi.bcm24       += fpga['T9' ]
rpi.bcm26       += fpga['T2' ]
rpi.bcm27_pcm_d += fpga['R10']

# Add RPi HAT ID flash.
i2c_flash(scl=Net.fetch('BCM1_ID_SC'), sda=Net.fetch('BCM0_ID_SD'), address=0)

# Add the user oscillator that connects to the FPGA.
osc(clk=Net.fetch('USER_CLK'), vcc=Net.fetch('+3.3V'), gnd=Net.fetch('GND'))
Net.fetch('USER_CLK').connect(fpga['C8'])

# Add the LEDs.
leds(Bus.fetch('LED_BUS', 4), Net.fetch('GND'), resistance='330')
fpga['A9, B8, A7, B7'] += Bus.fetch('LED_BUS',4)[0:3]

# Add DIP switch.
switches(Bus.fetch('DIPSW_BUS', 4), rail2=Net.fetch('GND'), pull2='330')
fpga['C6, C5, C4, C3'] += Bus.fetch('DIPSW_BUS',4)[0:3]

# Add pushbuttons.
buttons(Bus.fetch('BUTTON_BUS', 2), rail2=Net.fetch('GND'), pull2='330')
fpga['A16, B9'] += Bus.fetch('BUTTON_BUS',2)[0:1]

# Add PMOD socket.
fpga['A1, A2, B3, B4, B5, A5, B6, A6'] += Bus.fetch('PM1_BUS',8)[0:7]
# Add jumper to select which voltage supplies the socket.
voltage_selector1 = JMP3()
voltage_selector1[1,3] += Net.fetch('+3.3V'), Net.fetch('+5V')
voltage_selector1[2].drive = POWER
pmod_io(Bus.fetch('PM1_BUS',8), vcc=voltage_selector1[2])

# Add another PMOD socket.
fpga['A11, B10, B12, B11, B14, B13, B15, A15'] += Bus.fetch('PM2_BUS',8)[0:7]
voltage_selector2 = JMP3()
voltage_selector2[1,3] += Net.fetch('+3.3V'), Net.fetch('+5V')
voltage_selector2[2].drive = POWER
pmod_io(Bus.fetch('PM2_BUS',8), vcc=voltage_selector2[2])

# Add pure digital GROVE headers sharing PMOD I/O.
grove_io(d1=Bus.fetch('PM1_BUS')[1], d2=Bus.fetch('PM1_BUS')[3], vcc=voltage_selector1[2])
grove_io(d1=Bus.fetch('PM2_BUS')[1], d2=Bus.fetch('PM2_BUS')[3], vcc=voltage_selector2[2])

# Add GROVE headers for digital or I2C peripherals.
grove_io(scl=Net.fetch('GR1-IO1'), sda=Net.fetch('GR1-IO2'))
fpga['C10'] += Net.fetch('GR1-IO1')
fpga['C9']  += Net.fetch('GR1-IO2')

grove_io(scl=Net.fetch('GR2-IO1'), sda=Net.fetch('GR2-IO2'))
fpga['C12'] += Net.fetch('GR2-IO1')
fpga['C11'] += Net.fetch('GR2-IO2')

grove_io(scl=Net.fetch('GR3-IO1'), sda=Net.fetch('GR3-IO2'))
fpga['C14'] += Net.fetch('GR3-IO1')
fpga['C13'] += Net.fetch('GR3-IO2')

# Add general-purpose 0.1" header.
hdr = USER_GPIO_HDR()
GPIO_HDR_BUS = Bus.fetch('GPIO_HDR_BUS', len(hdr['.*']))
for pin, net in zip(hdr[:], GPIO_HDR_BUS[:]):
    net += pin
fpga['J1,K1,H1,J2,H2,G2,G1,F2,F1,E2,F3,D1,E3,D2,C2,C1,B2,B1'] += GPIO_HDR_BUS[0:3, 5:13, 15:19]
GPIO_HDR_BUS[4, 14] += Net.fetch('+3.3V'), Net.fetch('GND')

# Create the SDRAM interface.
sd = SdramIntfc()  # Create the SDRAM interface.
sd.vdd += Net.fetch('+3.3V')
sd.gnd += Net.fetch('GND')
# Instantiate the SDRAM and connect it to its interface.
sdram(intfc=sd)
# Attach the FPGA to the interface.
sd.clk        += fpga['IOR_141_GBIN2'], fpga['G16']
sd.cke        += fpga['G15']
sd.cs         += fpga['H13']
sd.we         += fpga['J14']
sd.ras        += fpga['K16']
sd.cas        += fpga['K15']
sd.dqm[0:1]   += fpga['J13, J15']
sd.ba[0:1]    += fpga['H14, G13']
sd.addr[0:12] += fpga['F13, E14, E13, D14, B16, C16, D15, D16, E16, F15, F14, F16, G14']
sd.data[0:15] += fpga['R14, P14, M13, M14, L13, L14, K13, K14, J16, L16, M16, M15, N16, P16, P15, R15']

# HDMI interface.
hdmi = hdmi_intfc(clk_p=fpga['L4'], clk_n=fpga['L1'],
                    data_p=fpga['K4,P1,R1'], data_n=fpga['M1,M4,N4'],
                    scl=fpga['P2'], sda=fpga['N3'], gnd=Net.fetch('GND'))

ERC()
generate_netlist()
