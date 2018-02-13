import machine
import ssd1306
import time
spi = machine.SPI(1, baudrate=8000000, polarity=0, phase=0)
oled = ssd1306.SSD1306_SPI(128, 32, spi, machine.Pin(15), machine.Pin(0), machine.Pin(16))
butt_1 = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
butt_2 = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
butt_3 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

class UI:

    def oled_test():

        oled.fill(0)                    #oled.fill(0) clears the screen, used as initialisation before every menu show
        oled.text('Hello', 0, 0)
        oled.text('World', 0, 10)
        oled.show()                     #oled.show() displays the rendered text and shape
        time.sleep(10)                  #time.sleep() keeps the display on the screen before moving on to futher code          

    def menu():

        while True:
            oled.fill(0)
            oled.text('Main Choice: Choose 1 of 3 choices', 0 , 0)
            oled.text('1 for insulin', 0 , 10)   #Insulin between 2-15 degrees celcius nominally 
            oled.text('2 for IVF', 0, 20)        #gonaw 8 between 2-8 degrees celcius
            oled.text('3 for custom', 0, 30)
            oled.show()


            if butt_1.value() == 0:         #Buttons are pull up, so when pressed outputs 0
                oled.fill(0)
                tempthresh = 15
                oled.text('tempthresh = 15', 0 ,0)
                oled.show()
                time.sleep(10)
                final_menu()
                
            elif butt_2.value() == 0:
                oled.fill(0)
                tempthresh = 25
                oled.text('tempthresh = 25', 0 ,0)
                oled.show()
                time.sleep(10)
                final_menu()
                
            elif butt_3.value() == 0:
                second_menu()

    def second_menu(): #Menu state for introducing a custom variable, tempthresh is set by the user
        
        tempthresh = 0
        tempshow = str(tempthresh)
        oled.fill(0) 
        oled.text('Custom Temp:', 0, 0)
        oled.text(tempthresh, 0, 10
        oled.show()

        if butt_1.value() == 0:
            tempthresh = tempthresh + 0.1
            timesleep(0.1)

        if butt_2.value() == 0:
            tempthresh = tempthresh - 0.1
            timesleep(0.1)

        if butt_3.value() == 0:
            #this goes to final menu
            final_menu()

    def final_menu(): #Final state for the UI, shows all parameters that are relevant

        oled.fill(0)
        oled.text('Tempthresh = ', 0, 0)
        oled.text(tempthresh, 30, 0)
        oled.text('Current Temp =', 0, 10)
        oled.text(currenttemp, 30, 10)
        oled.text('Current Humid =', 0, 20)
        oled.text(currenthumid, 30, 20)
                  
                  #Potentially introduce a vibration parameter
                  
                  #Maybe be we can do this as a scroller with some nice sun emojis or something
                  #The data will be more clear if it was all on one page and easily accessible
