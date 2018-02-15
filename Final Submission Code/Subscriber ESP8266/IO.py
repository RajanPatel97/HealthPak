#This is the class file for outputs on the subscriber huzzah

import machine
import time

#Define LED Pins for Humidity status
p12 = machine.Pin(12)
pwm12 = machine.PWM(p12)
p13 = machine.Pin(13)
pwm13 = machine.PWM(p13)
p14 = machine.Pin(14)
pwm14 = machine.PWM(p14)

#Define LED Pins for Temperature status
p0 = machine.Pin(0)
pwm0 = machine.PWM(p0)
p5 = machine.Pin(5)
pwm5 = machine.PWM(p5)
p2 = machine.Pin(2)
pwm2 = machine.PWM(p2)

#Define Peizo Buzzer Pins for Vibration status
p15 = machine.Pin(15)
pwm15 = machine.PWM(p15)

class IO:
        #green output on humidity led
	def humidledgreen():
                pwm12.freq(50) 
                pwm12.duty(0)
                pwm13.freq(50) 
                pwm13.duty(1023)
                pwm14.freq(50) 
                pwm14.duty(1023)

        #red output on humidity led
        def humidledred():
                pwm12.freq(50) 
                pwm12.duty(1023)
                pwm13.freq(50) 
                pwm13.duty(1023)
                pwm14.freq(50) 
                pwm14.duty(0)

        #green output on temperature led
        def templedgreen():
                pwm5.freq(50) 
                pwm5.duty(0)
                pwm0.freq(50) 
                pwm0.duty(1023)
                pwm2.freq(50) 
                pwm2.duty(1023)

        #red output on temperature led
        def templedred():
                pwm5.freq(50) 
                pwm5.duty(1023)
                pwm0.freq(50) 
                pwm0.duty(1023)
                pwm2.freq(50) 
                pwm2.duty(0)

        #start up song also used as alarm on piezo buzzer
        def startnalarm():
                pwm15.freq(587) 
                pwm15.duty(512)
                time.sleep(0.4)
                        
                pwm15.freq(698)
                time.sleep(0.15)
                        
                pwm15.freq(880)
                time.sleep(0.15)
                        
                pwm15.freq(698)
                time.sleep(0.15)
                        
                pwm15.freq(784)
                time.sleep(0.4)
                        
                pwm15.freq(880)
                time.sleep(0.15)
                        
                pwm15.freq(784)
                time.sleep(0.15)

                pwm15.freq(698)
                time.sleep(0.15)

                pwm15.freq(659)
                time.sleep(0.4)

                pwm15.freq(587)
                time.sleep(0.15)

                pwm15.freq(523)
                time.sleep(0.15)

                pwm15.freq(440)
                time.sleep(0.15)

                pwm15.freq(587)
                time.sleep(0.4)

                pwm15.duty(0)
                
    
