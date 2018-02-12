import machine

#same code for peizo buzzer - remember both connect to power on one side not ground

p12 = machine.Pin(12)
p13 = machine.Pin(13)
p14 = machine.Pin(14)

pwm12 = machine.PWM(p12)
pwm12.freq(500)
pwm12.duty(512)

pwm13 = machine.PWM(p13)
pwm13.freq(500)
pwm13.duty(512)

pwm14 = machine.PWM(p14)
pwm14.freq(500)
pwm14.duty(512)
