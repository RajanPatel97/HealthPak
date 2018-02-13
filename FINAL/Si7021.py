import machine
import time
from machine import Pin, I2C
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

class Si7021:

        # Register of Raw Humidity Reading
        humreg = 0xF5
        # Register of Raw Temperature Reading
        tempreg = 0xF3
        # Register Byte Size
        regBytesize = 2

        # Class Constructor
	def __init__(self, i2c, i2cAddress):
		self.i2c = i2c
		self.i2cAddress = i2cAddress

        # Read Humidity
        def ambHum(self):
                self.i2c.writeto(self.i2cAddress, bytearray([Si7021.humreg]))
                time.sleep_ms(20)
                rawBytes = i2c.readfrom(self.i2cAddress,Si7021.regBytesize)
                humidcode= int.from_bytes(rawBytes, 'big')
                return (float(((125*humidcode)/65536) - 6))
                

        # Read Ambient Temperature
        def ambTemp(self):
                self.i2c.writeto(self.i2cAddress, bytearray([Si7021.tempreg]))
                time.sleep_ms(20)
                rawBytes = i2c.readfrom(self.i2cAddress,Si7021.regBytesize)
                tempcode = int.from_bytes(rawBytes, 'big')
                return (float(((175.72*tempcode)/65536) - 46.85))
