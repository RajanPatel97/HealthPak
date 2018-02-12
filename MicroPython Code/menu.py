import machine
import ssd1306
import time
spi = machine.SPI(1, baudrate=8000000, polarity=0, phase=0)
oled = ssd1306.SSD1306_SPI(128, 32, spi, machine.Pin(15), machine.Pin(0), machine.Pin(16))
butt_1 = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
butt_2 = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
butt_3 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

oled.fill(0)
oled.text('Hello', 0, 0)
oled.text('World', 0, 10)
time.sleep(10)
oled.show()


def menu():

choice ='0'
while choice =='0':
    oled.fill(0)
    oled.text('Main Choice: Choose 1 of 3 choices', 0 , 0)
    oled.text('1 for insulin', 0 , 10)
    oled.text('2 for IVF', 0, 20)
    oled.text('3 for custom', 0, 30)
    oled.show()
    

    if butt_1.value() == 0:
        oled.fill(0)
        tempthresh = 15
        oled.text('tempthresh = 15', 0 ,0)
        oled.show()
    elif butt_2.value() == 0:  
        oled.fill(0)
        tempthresh = 25
        oled.text('tempthresh = 25', 0 ,0)
        oled.show()
    elif butt_3.value() == 0:
        second_menu()

def second_menu():
    tempthresh = 0
    tempshow = str(tempthresh)
    oled.fill(0)
    oled.text('custom temp bros', 0, 0)
    oled.text(tempshow, 0, 10
    oled.show()
    
    if butt_1.value() == 0:
        tempthresh = tempthresh + 0.1
        timesleep(0.1)

    if butt_2.value() == 0:
        tempthresh = tempthresh - 0.1
        timesleep(0.1)
              
    if butt_3.value() == 0:
        #this goes to final menu        

menu()
