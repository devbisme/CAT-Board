from globals import *

def fpga_config(fpga, vcc=None, gnd=None):
    """
    """

    if not vcc:
        vcc = Net.fetch('+3.3V')
    if not gnd:
        gnd = Net.fetch('GND')

    spi_flash_ic = SPI_FLASH()

    # FPGA configuration & flash serial I/O signals.
    sck = Net.fetch('CONFIG_FLASH_SCK') # FPGA config. clock (I/O) and flash serial clock (I).
    si = Net.fetch('CONFIG_FLASH_SI')   # FPGA config. output (O) and flash serial input (I).
    so = Net.fetch('CONFIG_FLASH_SO')   # FPGA config. input (I) and flash serial output (O).
    cs = Net.fetch('CONFIG_FLASH_CS')   # FPGA config. select and flash chip-select (active-low I).

    pullup = RN2_m(value='4.7K')
    pullup.A['L,R'] += vcc, sck  # This keeps the config. clock stable if SCK is not driven.
    pullup.B['L,R'] += vcc, cs   # This keeps the flash disabled unless CS is driven low.

    # The RPi connects to the FPGA & flash configuration signals through these
    # resistors to isolate the RPi from the FPGA & flash interactions.
    # A full explanation of how the RPi, FPGA, and flash interact is at
    # https://hackaday.io/project/7982-cat-board/log/36982-cat-board-all-on-its-own
    series = RN4_m(value='100')
    series.B['L,R'] += Net.fetch('BCM9_MISO'), si
    series.A['L,R'] += Net.fetch('BCM10_MOSI'), so
    series.D['L,R'] += Net.fetch('BCM11_SCLK'), sck
    series.C['L,R'] += Net.fetch('BCM25'), cs

    # Connect the flash to the configuration signals.
    spi_flash_ic['~CS, SO, SI, SCK'] += cs, so, si, sck
    spi_flash_ic['~HOLD'] += vcc  # Disable HOLD.
    spi_flash_ic['~WP'] += vcc  # Disable WRITE PROTECT.
    spi_flash_ic['VCC, GND'] += vcc, gnd  # Power the flash.

    # Connect the FPGA to the configuration signals.
    fpga['_SDO'] += si  # FPGA config. output drives flash serial input.
    fpga['_SDI'] += so  # FPGA config. input driven by flash serial output.
    fpga['_SCK'] += sck # FPGA config. clock drives flash serial clock input.
    fpga['_SS']  += cs  # FPGA config. select drives flash chip-select.
    fpga['VCC_SPI'] += vcc # Power the FPGA config. circuitry.

    C_byp()[1,2] += vcc, gnd  # Decoupling cap for flash chip.
    C_byp()[1,2] += vcc, gnd  # Another decoupling cap for FPGA config. supply.


if __name__ == '__main__':
    fpga_config(FPGA())
    ERC()
    generate_netlist()
