#Class file for Si7021 Sensor

import machine
import time
import micropython
from machine import Pin, I2C
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

#REGISTER ADDRESSES
HUMREG = (0xF5)
TEMPREG = (0xF3)

#REGISTER SIZE
REGSIZE = (2)

class Si7021:

        # Class Constructor
	def __init__(self, i2c, i2cAddress):
		self.i2c = i2c
		self.i2cAddress = i2cAddress

        # Read Humidity
        def ambHum(self):
                #send read humidity command
                self.i2c.writeto(self.i2cAddress, bytearray([HUMREG]))
                time.sleep_ms(20)
                #read 2 bytes for humidity reading
                rawBytes = i2c.readfrom(self.i2cAddress, REGSIZE)
                #convert bytes to integer
                humidcode= int.from_bytes(rawBytes, 'big')
                #convert to % humidity 
                return (float(((125*humidcode)/65536) - 6))
                

        # Read Ambient Temperature
        def ambTemp(self):
                #send read temperature command
                self.i2c.writeto(self.i2cAddress, bytearray([TEMPREG]))
                time.sleep_ms(20)
                #read 2 bytes for temperature reading
                rawBytes = i2c.readfrom(self.i2cAddress, REGSIZE)
                #convert bytes to integer
                tempcode = int.from_bytes(rawBytes, 'big')
                #convert to celcius temperature
                return (float(((175.72*tempcode)/65536) - 46.85))
