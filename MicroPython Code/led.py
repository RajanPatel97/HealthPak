import machine
import time

led = machine.Pin(13, machine.Pin.OUT)

while True:
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
