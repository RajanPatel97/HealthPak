import machine
import micropython
from machine import Pin, I2C
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

# registers
TMP007_VOBJ = (0x00)
TMP007_TDIE = (0x01)
TMP007_CONFIG = (0x02)
TMP007_TOBJ = (0x03)
TMP007_STATUS = (0x04)
TMP007_STATMASK = (0x05)

# configure bytes
TMP007_CFG_RESET = (0x8000)
TMP007_CFG_MODEON = (0x1000)
TMP007_CFG_1SAMPLE = (0x0000)
TMP007_CFG_2SAMPLE = (0x0200)
TMP007_CFG_4SAMPLE = (0x0400)
TMP007_CFG_8SAMPLE = (0x0600)
TMP007_CFG_16SAMPLE = (0x0800)
TMP007_CFG_ALERTEN = (0x0100)
TMP007_CFG_ALERTF = (0x0080)
TMP007_CFG_TRANSC = (0x0040)

# interrupt configure
TMP007_STAT_ALERTEN = (0x8000)
TMP007_STAT_CRTEN = (0x4000)


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
                self.i2c.writeto_mem(self.i2cAddress,TMP007_CONFIG, bytearray([0xf3]))


	# Reading tmeperature on die
	def dieTemp(self):
		rawByte = self.i2c.readfrom_mem(self.i2cAddress, TMP007_TDIE, 2)
		return (((rawByte[0]*256+rawByte[1])/4)*0.03125)

	# Reading temperature of object
	def objTemp(self):
		rawByte = self.i2c.readfrom_mem(self.i2cAddress,TMP007_TOBJ, 2)
		return (((rawByte[0]*256+rawByte[1])/4)*0.03125)
    
