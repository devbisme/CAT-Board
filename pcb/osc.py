from globals import *

def osc(clk, vcc=None, gnd=None):
    """
    Instantiate an oscillator and a bypass cap.
    """

    if not vcc:
        vcc = Net.fetch('+3.3V')
    if not gnd:
        gnd = Net.fetch('GND')

    try:
        osc_1 = OSCILLATOR()
    except Exception:
        osc_1 = Part('Oscillator', 'ASE-xxxMHz', footprint='Oscillator:Oscillator_SMD_Abracon_ASE-4Pin_3.2x2.5mm')
        logger.warning('No predefined oscillator. Using default oscillator: {}.'.format(osc_1))

    osc_1['vdd, gnd'] += vcc, gnd
    osc_1['en'] += vcc  # Always keep oscillator enabled.
    osc_1['out'] += clk

    C_byp()[1,2] += osc_1['vdd, gnd']  # Attach bypass cap from osc power pin to ground.

if __name__ == '__main__':
    osc(Net('CLK'))
    ERC()
    generate_netlist()
