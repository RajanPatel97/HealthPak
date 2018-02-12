import machine
import time

#same code for peizo buzzer - remember both connect to power on one side not ground

p12 = machine.Pin(12)
p13 = machine.Pin(13)
p14 = machine.Pin(14)
p15 = machine.Pin(15)

pwm12 = machine.PWM(p12)
pwm12.freq(500)
pwm12.duty(512)

pwm13 = machine.PWM(p13)
pwm13.freq(500)
pwm13.duty(0)

pwm14 = machine.PWM(p14)
pwm14.freq(500)
pwm14.duty(0)

while True:
    
    pwm15 = machine.PWM(p15)
    pwm15.freq(500) 
    pwm15.duty(512)
    pwm12.duty(512)
    time.sleep(0.25)
    
    pwm15.freq(500)
    pwm12.duty(0)
    pwm13.duty(0)
    time.sleep(0.25)
    
    pwm15.freq(500)
    pwm12.duty(512)
    pwm13.duty(0)
    time.sleep(0.25)
    
    pwm15.freq(350)
    pwm12.duty(0)
    pwm13.duty(512)
    time.sleep(0.25)
    
    pwm15.freq(150)
    pwm12.duty(512)
    pwm13.duty(0)
    time.sleep(0.25)
    
    pwm15.freq(500)
    pwm12.duty(0)
    pwm13.duty(512)
    time.sleep(0.25)
    
    pwm15.freq(350)
    pwm12.duty(512)
    pwm13.duty(0)
    time.sleep(0.25)
    
    pwm15.freq(150)
    pwm12.duty(0)
    time.sleep(0.25)
    
    pwm15.freq(500)
    pwm12.duty(1023)
    time.sleep(0.1)
