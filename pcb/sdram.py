from globals import *

class SdramIntfc(Interface):
    """
    Instantiate an interface for a synchronous DRAM.
    """
    def __init__(self, addr_width=13, data_width=16, circuit=None):
        super(SdramIntfc, self).__init__(prefix='SD', circuit=circuit)
        prefix = self.name + '_'
        self.clk  = Net(prefix+'CLK')
        self.cke  = Net(prefix+'CKE')
        self.cs   = Net(prefix+'CS')
        self.we   = Net(prefix+'WE#')
        self.ras  = Net(prefix+'RAS#')
        self.cas  = Net(prefix+'CAS#')
        self.dqm  = Bus(prefix+'DQM', 2)
        self.ba   = Bus(prefix+'BA', 2)
        self.addr = Bus(prefix+'ADDR', addr_width)
        self.data = Bus(prefix+'DATA', data_width)
        self.vdd  = Net(prefix+'VDD')
        self.gnd  = Net(prefix+'VSS')

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
    intfc.vdd += sdram_['VDD, VDDQ']
    intfc.gnd += sdram_['VSS, VSSQ']

    # Attach control pins.
    sdram_['CLK'] += intfc.clk
    sdram_['CKE'] += intfc.cke
    sdram_['CS#'] += intfc.cs
    sdram_['WE#'] += intfc.we
    sdram_['RAS#'] += intfc.ras
    sdram_['CAS#'] += intfc.cas
    sdram_['UDQM, LDQM'] += intfc.dqm[1:0]
    sdram_['BA[1:0]'] += intfc.ba[1:0]
    sdram_['A[12:0]'] += intfc.addr[12:0]
    sdram_['DQ[15:0]'] += intfc.data[15:0]

    sdram_['NC'] += NC  # One, lonely no-connect pin.

    # Create a bypass cap for each power pin.
    for pwr in sdram_['VDD, VDDQ']:
        C_byp()[1,2] += pwr, intfc.gnd  # Attach bypass caps from power to ground.

if __name__ == '__main__':
    intfc = SdramIntfc()
    sdram(intfc)
    ERC()
    generate_netlist()
