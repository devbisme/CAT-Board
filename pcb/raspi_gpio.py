from globals import *

class RaspiGpioIntfc(Interface):
    """
    Instantiate an interface for a Raspi GPIO header.
    """
    def __init__(self, circuit=None, gpio=RASPI_GPIO_SOCKET):
        super(RaspiGpioIntfc, self).__init__(prefix='RASPI_GPIO', circuit=circuit)

        self.gpio = gpio # Store the Raspi GPIO socket template.

        prefix = self.name + '_'  # Prefix for interface signal names.

        self.v5v  = Net(prefix + '5V')
        self.v3v3 = Net(prefix + '3.3V')
        self.gnd  = Net(prefix + 'GND')

        # All the non-power interface signals are lower-case versions of the Raspi GPIO names.
        for non_pwr_pin in self.gpio['BCM[0-9]+.*']:
            setattr(self, non_pwr_pin.name.lower(), Net(prefix + non_pwr_pin.name.upper()))

@subcircuit
def raspi_gpio(intfc):
    gpio_ = intfc.gpio()  # Instantiate the Raspi GPIO socket.

    # Connect power/ground pins of the socket to the interface.
    gpio_['3.3V'] += intfc.v3v3
    gpio_['5V']   += intfc.v5v
    gpio_['GND']  += intfc.gnd

    # Connect socket pins to the interface signals with the same name.
    for non_pwr_pin in gpio_['BCM[0-9]+.*']:
        non_pwr_pin += getattr(intfc, non_pwr_pin.name.lower())

if __name__ == '__main__':
    gpio = raspi_gpio(RaspiGpioIntfc())
    ERC()
    generate_netlist()
