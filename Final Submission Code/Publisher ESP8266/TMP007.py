#Class file for TMP007 Thermopile Sensor
import machine
import micropython
from machine import Pin, I2C
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

# REGISTER ADDRESSES
TDIE = (0x01)
TOBJ = (0x03)
TMP007_CONFIG = (0x02)

# REGISTER CONFIGURATION
TMP007CONF = (0xF3)


class TMP007:
        def __init__(self, i2c, i2cAddress):
                # Create I2C device.
                self.i2c = i2c
		self.i2cAddress = i2cAddress
                # Load calibration values.
                self._load_calibration()

        # load calibration to sensor
        def _load_calibration(self):
                #load calibration               
                self.i2c.writeto_mem(self.i2cAddress,TMP007_CONFIG, bytearray([TMP007CONF]))

        # Reading tmeperature on die
	def dieTemp(self):
                #read two bytes from die temp register
		rawByte = self.i2c.readfrom_mem(self.i2cAddress, TDIE, 2)
		#convert to celcius
		return (((rawByte[0]*256+rawByte[1])/4)*0.03125)

	# Reading temperature of object
	def objTemp(self):
                #read two bytes from object temp register
		rawByte = self.i2c.readfrom_mem(self.i2cAddress, TOBJ, 2)
		#convert to celcius
		return (((rawByte[0]*256+rawByte[1])/4)*0.03125)
    
