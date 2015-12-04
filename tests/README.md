# CAT Board Tests


# Description

These are some simple test designs for the CAT Board:

* Display a counter or a scrolling pattern of characters on a StickIt! LEDDigits display.
* Display the hex value of the four-bit `SW3` DIP switch on first and last digits of the LEDDigits display and blank them if pushbuttons `SW1` or `SW2` are pressed.


# Test Procedures

## LED Digits Test

1. Attach the CAT Board to the Raspberry Pi (RPi) GPIO header.
1. Connect the RPi to an HDMI display, mouse, keyboard and power supply.
1. Attach the StickIt! LEDDigits board to the `PM3` PMOD socket on the CAT Board.
1. Compile the led\_digits\_display.py test design:

		python led_digits_display.py

1. Download the bitstream to the CAT Board:

		sudo bash config_cat iceriver/catboard.bin

1. Sit back and watch the digits roll by...

## Buttons Test

1. Attach the CAT Board to the Raspberry Pi (RPi) GPIO header.
1. Connect the RPi to an HDMI display, mouse, keyboard and power supply.
1. Attach the StickIt! LEDDigits board to the `PM3` PMOD socket on the CAT Board.
1. Compile the buttons_display.py test design:

		python buttons_display.py

1. Download the bitstream to the CAT Board:

		sudo bash config_cat iceriver/catboard.bin

1. The digits on the far left and right of the LEDDigits display should both come on and display the digit representing the hex value of DIP switch `SW3`. Changing the DIP switches should change the displayed value.
1. Pressing `SW1` should turn off digit `LED1` for as long as the button is held down.
1. Pressing `SW2` should turn off digit `LED8` for as long as the button is held down.


