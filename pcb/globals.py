from skidl import *

KICAD_LIBS = r'C:\Program Files\KiCad\share\kicad\kicad-symbols'
XESS_LIBS = r'C:\xesscorp\KiCad\libraries'

skidl.lib_search_paths[KICAD].extend([KICAD_LIBS, XESS_LIBS])

def int2bus(val, width, one, zero):
    bus = Bus(BUS_PREFIX, width)
    for i in range(width):
        if val & (1<<i):
            bus[i] += one
        else:
            bus[i] += zero
    return bus

def make_2pin_units(part):
    """Make two-pin units for a part like a resistor network or DIP switch."""
    num_units = len(part.pins) // 2
    for i in range(0, num_units):
        unit_lbl = str(chr(ord('A')+i))
        part.make_unit(unit_lbl, i+1, 2*num_units-i)
        part.unit[unit_lbl].set_pin_alias('L', i+1)
        part.unit[unit_lbl].set_pin_alias('R', 2*num_units-i)

# Capacitors.
C = Part('device', 'C', dest=TEMPLATE)
C_s = C(footprint='Capacitor_SMD:C_04021005Metric', dest=TEMPLATE)
C_m = C(footprint='Capacitor_SMD:C_0603_1608Metric', dest=TEMPLATE)
C_l = C(footprint='Capacitor_SMD:C_0805_2012Metric', dest=TEMPLATE)
C_byp = C_s(value='0.1uF', dest=TEMPLATE)

# Resistors.
R = Part('device', 'R', dest=TEMPLATE)
R_s = R(footprint='Resistor_SMD:R_0402_1005Metric', dest=TEMPLATE)
make_2pin_units(R_s)
R_m = R(footprint='Resistor_SMD:R_0603_1608Metric', dest=TEMPLATE)
make_2pin_units(R_m)
R_l = R(footprint='Resistor_SMD:R_0805_2012Metric', dest=TEMPLATE)
make_2pin_units(R_l)

# Resistor arrays.
RN2_m = Part('xess', 'RN2', footprint='XESS:742C043', dest=TEMPLATE)
make_2pin_units(RN2_m)
RN4_m = Part('xess', 'RN4', footprint='XESS:742C083', dest=TEMPLATE)
make_2pin_units(RN4_m)
RN8_m = Part('xess', 'RN8', footprint='XESS:742C163', dest=TEMPLATE)
make_2pin_units(RN8_m)

# Jumpers.
JMP2 = Part('Connector_Generic', 'Conn_01x02', footprint='Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical', dest=TEMPLATE)
JMP3 = Part('Connector_Generic', 'Conn_01x03', footprint='Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical', dest=TEMPLATE)

# LEDs.
LED = Part('Device', 'LED', dest=TEMPLATE)
LED_s = LED(footprint='LED_SMD:LED_0402_1005Metric', dest=TEMPLATE)
LED_m = LED(footprint='LED_SMD:LED_0603_1608Metric', dest=TEMPLATE)
LED_l = LED(footprint='LED_SMD:LED_0805_2012Metric', dest=TEMPLATE)

# Buttons.
BUTTON = Part('Switch', 'SW_Push', footprint='Button_Switch_SMD:SW_SPST_CK_RS282G05A3', dest=TEMPLATE)

# Switches.
DIP_SW1 = Part('Switch', 'SW_DIP_x01', footprint='Button_Switch_THT:SW_DIP_SPSTx01_Slide_9.78x4.72mm_W7.62mm_P2.54mm', dest=TEMPLATE) 
make_2pin_units(DIP_SW1)
DIP_SW2 = Part('Switch', 'SW_DIP_x02', footprint='Button_Switch_THT:SW_DIP_SPSTx02_Slide_9.78x7.26mm_W7.62mm_P2.54mm', dest=TEMPLATE) 
make_2pin_units(DIP_SW2)
DIP_SW3 = Part('Switch', 'SW_DIP_x03', footprint='Button_Switch_THT:SW_DIP_SPSTx03_Slide_9.78x9.8mm_W7.62mm_P2.54mm', dest=TEMPLATE) 
make_2pin_units(DIP_SW3)
DIP_SW4 = Part('Switch', 'SW_DIP_x04', footprint='Button_Switch_THT:SW_DIP_SPSTx04_Slide_9.78x12.34mm_W7.62mm_P2.54mm', dest=TEMPLATE) 
make_2pin_units(DIP_SW4)
DIP_SW5 = Part('Switch', 'SW_DIP_x05', footprint='Button_Switch_THT:SW_DIP_SPSTx05_Slide_9.78x14.88mm_W7.62mm_P2.54mm', dest=TEMPLATE) 
make_2pin_units(DIP_SW5)
DIP_SW6 = Part('Switch', 'SW_DIP_x06', footprint='Button_Switch_THT:SW_DIP_SPSTx06_Slide_9.78x17.42mm_W7.62mm_P2.54mm', dest=TEMPLATE) 
make_2pin_units(DIP_SW6)
DIP_SW7 = Part('Switch', 'SW_DIP_x07', footprint='Button_Switch_THT:SW_DIP_SPSTx07_Slide_9.78x19.96mm_W7.62mm_P2.54mm', dest=TEMPLATE) 
make_2pin_units(DIP_SW7)
DIP_SW8 = Part('Switch', 'SW_DIP_x08', footprint='Button_Switch_THT:SW_DIP_SPSTx08_Slide_9.78x22.5mm_W7.62mm_P2.54mm', dest=TEMPLATE) 
make_2pin_units(DIP_SW8)

# I/O.
PMOD_SOCKET = Part('xess', '~PMOD_SCKT-12', footprint='XESS:PMOD_SCKT-12', dest=TEMPLATE)
GROVE_HDR = Part('xess', 'Grove_Male', footprint='XESS:GROVE_MALE', dest=TEMPLATE)
RASPI_GPIO_SOCKET = Part('xess', 'RPi_GPIO', footprint='Connector_PinHeader_2.54mm:PinHeader_2x20_P2.54mm_Vertical', dest=TEMPLATE)
USER_GPIO_HDR = Part('Connector_Generic', 'Conn_02x10_Odd_Even', footprint='Connector_PinHeader_2.54mm:PinHeader_2x10_P2.54mm_Vertical', dest=TEMPLATE)

# Oscillator.
OSCILLATOR = Part('Oscillator', 'ASE-xxxMHz', footprint='Oscillator:Oscillator_SMD_Abracon_ASE-4Pin_3.2x2.5mm', dest=TEMPLATE)

# Serial memories.
I2C_FLASH = Part('xess', 'EEPROM_I2C', footprint='Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', dest=TEMPLATE)
SPI_FLASH = Part('xess', 'SPI_FLASH_SOIC8', footprint='Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', dest=TEMPLATE)

# iCE40 FPGA.
FPGA = Part('Lattice_iCE_FPGA', 'iCE40-HX8K-CT256', footprint='XESS:Lattice_caBGA_256', dest=TEMPLATE)

# SDRAM.
#SDRAM = Part('xess', 'SDRAM_16Mx16_VFBGA-54', footprint='XESS:VFBGA-54', dest=TEMPLATE)
SDRAM = Part('xess', 'SDRAM_16Mx16_TSOPII-54', footprint='XESS:TSOPII-54', dest=TEMPLATE)
