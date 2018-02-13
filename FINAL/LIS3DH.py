import machine
import time
from machine import Pin, I2C
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

class lis3dh:
        # Class Constructor
	def __init__(self, i2c, i2cAddress):
		self.i2c = i2c
		self.i2cAddress = i2cAddress
                self.i2c.writeto_mem(self.i2cAddress,0x20, bytearray([0x27]))
                self.i2c.writeto_mem(self.i2cAddress,0x23, bytearray([0x00]))
                time.sleep(0.5)

        #Read x-axis Acceleration
        def xRead(self):
                # X-Axis LSB, X-Axis MSB
                data0 = i2c.readfrom_mem(self.i2cAddress, 0x28, 1)[0]
                data1 = i2c.readfrom_mem(self.i2cAddress, 0x29, 1)[0]
                # Convert the data
                xAccl = data1 << 8 | data0
                if (xAccl > 32767):
                        xAccl = xAccl - 65536
                return (xAccl)

        #Read y-axis Acceleration
        def yRead(self):
                # Y-Axis LSB, Y-Axis MSB
                data0 = i2c.readfrom_mem(self.i2cAddress, 0x2A, 1)[0]
                data1 = i2c.readfrom_mem(self.i2cAddress, 0x2B, 1)[0]
                # Convert the data
                yAccl = data1 << 8 | data0
                if (yAccl > 32767):
                        yAccl = yAccl - 65536
                return (yAccl)

        #Read z-axis Acceleration
        def zRead(self):
                # Z-Axis LSB, Z-Axis MSB
                data0 = i2c.readfrom_mem(self.i2cAddress, 0x2C, 1)[0]
                data1 = i2c.readfrom_mem(self.i2cAddress, 0x2D, 1)[0]
                # Convert the data
                zAccl = data1 << 8 | data0
                if (zAccl > 32767) :
                        zAccl = zAccl - 65536
                return (zAccl)

