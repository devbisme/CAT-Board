from globals import *

@subcircuit
def sdram(intfc):
    """
    Instantiate an SDRAM and bypass caps.

    Args:
        clk: Clock.
        clk_en: clock enable.
        cs: Chip select.
        we: Write enable.
        ras: Row address strobe.
        cas: Column address strobe.
        dqm: Data bus qualifier mask (2-bit bus).
        ba: Bank address (2-bit bus).
        addr: Address bus.
        data: Data bus.
    """

    try:
        sdram_ = SDRAM()
    except Exception:
        sdram_ = Part('xess', 'SDRAM_16Mx16_VFBGA', footprint='XESS:VFBGA-54')
        logger.warning('No predefined SDRAM. Using default SDRAM: {}.'.format(sdram_))

    # Attach power & ground pins.
    sdram_['VDD, VDDQ'] += intfc.vdd
    sdram_['VSS, VSSQ'] += intfc.gnd

    # Attach control pins.
    sdram_['CLK'] += intfc.clk
    sdram_['CKE'] += intfc.cke
    sdram_['CS#'] += intfc.cs
    sdram_['WE#'] += intfc.we
    sdram_['RAS#'] += intfc.ras
    sdram_['CAS#'] += intfc.cas
    sdram_['UDQM, LDQM'] += intfc.dqm[1:0]
    sdram_['BA[1:0]'] += intfc.ba[1:0]
    sdram_.n['A[12:0]'] += intfc.addr[12:0]  # Force name search to avoid BGA pin numbers like A1.
    sdram_['DQ[15:0]'] += intfc.data[15:0]

    sdram_['NC'] += NC  # One, lonely no-connect pin.

    # Create a bypass cap for each power pin.
    for pwr in sdram_['VDD, VDDQ']:
        pwr & C_byp() & intfc.gnd

if __name__ == '__main__':
    intfc = Interface(
        clk = Net("SDRAM_CLK"),
        cke = Net("SDRAM_CKE"),
        cs = Net("SDRAM_CS"),
        we = Net("SDRAM_WE#"),
        ras = Net("SDRAM_RAS#"),
        cas = Net("SDRAM_CAS#"),
        dqm = Bus("SDRAM_DQM", 2),
        ba = Bus("SDRAM_BA", 2),
        addr = Bus("SDRAM_ADDR", 13),
        data = Bus("SDRAM_DATA", 16),
        gnd = Net.fetch("GND"),
        vdd = Net.fetch("+3.3"),
    )
    sdram(intfc)
    ERC()
    generate_netlist()
