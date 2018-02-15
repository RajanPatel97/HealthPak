#Class file for OLED Screen Menu, so we can quickly change the menu format.

import machine
import ssd1306

#Define OLED pins
spi = machine.SPI(1, baudrate=8000000, polarity=0, phase=0)
oled = ssd1306.SSD1306_SPI(128, 32, spi, machine.Pin(15), machine.Pin(0), machine.Pin(16))

#Define Class of Screen Display functions that require no inital parameters
class Screen:
        #Menu Display
	def menu():
                oled.fill(0)
                oled.text('(1)', 0, 0)
                oled.text('Insulin', 20, 0)
                oled.text('(2)', 0, 10)
                oled.text('IVF', 20, 10)
                oled.text('(3)' , 0, 20)
                oled.text('Heart', 20, 20)
                oled.show()
    
