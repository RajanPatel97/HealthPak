import time
from machine import Pin, I2C
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

i2c.writeto(64, bytearray([0xF5]))
time.sleep_ms(100)
data = i2c.readfrom(64,2)
read = int.from_bytes(data, 'big')
print(read)
