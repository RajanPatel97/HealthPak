import machine
import time

# Get I2C bus
from machine import Pin, I2C
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

while True: 

        i2c.writeto_mem(24,0x20, bytearray([0x27]))
        i2c.writeto_mem(24,0x23, bytearray([0x00]))
        time.sleep(0.5)

        # LIS3DHTR address, 0x18(24)
        # Read data back from 0x28(40), 2 bytes
        # X-Axis LSB, X-Axis MSB
                                                         
        data0 = i2c.readfrom_mem(24, 0x28, 1)[0]
        data1 = i2c.readfrom_mem(24, 0x29, 1)[0]
        xAccl = data1 << 8 | data0

        # Convert the data
        #xAccl = (data1 * 256) + data0
        if (xAccl > 32767):
                xAccl = xAccl - 65536

        # LIS3DHTR address, 0x18(24)
        # Read data back from 0x2A(42), 2 bytes
        # Y-Axis LSB, Y-Axis MSB
        data0 = i2c.readfrom_mem(24, 0x2A, 1)[0]
        data1 = i2c.readfrom_mem(24, 0x2B, 1)[0]

        # Convert the data
        #yAccl = (data1 * 256) + data0
        yAccl = data1 << 8 | data0
        if (yAccl > 32767):
                yAccl = yAccl - 65536

        # LIS3DHTR address, 0x18(24)
        # Read data back from 0x2C(44), 2 bytes
        # Z-Axis LSB, Z-Axis MSB
        data0 = i2c.readfrom_mem(24, 0x2C, 1)[0]
        data1 = i2c.readfrom_mem(24, 0x2D, 1)[0]

        # Convert the data
        #zAccl = (data1 * 256) + data0
        zAccl = data1 << 8 | data0
        if (zAccl > 32767) :
                zAccl = zAccl - 65536

        # Output data to screen
        print(xAccl)
        print(yAccl)
        print(zAccl)
