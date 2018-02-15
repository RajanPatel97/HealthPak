#Class file to check if real time measurements are within limits for a given
#medicine or organ and to output to leds or buzzer based on current status
#with respect to these limits. 

import machine
import time
import Medicine
import IO

class CondCheck:

        #pass in all relevent parameters in order to make comparsions
        def Checker(parsed, maxtemp, mintemp, maxhum, maxvib, oldx, oldy, oldz):

                #get current values
                realtemp = parsed["Sensor Readings"]["Temperature"]
                realstemp = parsed["Sensor Readings"]["Stemp"]
                realhum = parsed["Sensor Readings"]["Humidity"]
                realx = parsed["Sensor Readings"]["x"]
                realy = parsed["Sensor Readings"]["y"]
                realz = parsed["Sensor Readings"]["z"]

                #if temperature out of limits output red on led
                if (((realtemp + realstemp)/2 > maxtemp) or ((realtemp + realstemp)/2 < mintemp)):
                    IO.IO.templedred()
                #else output green
                else:
                    IO.IO.templedgreen()
                #if humidity out of limits output red on second led
                if(realhum > maxhum):
                    IO.IO.humidledred()
                #else output green
                else:
                    IO.IO.humidledgreen()
                #if vibration to large output alarm on piezo buzzer
                if(abs(realx-oldx)> maxvib or abs(realy-oldy)>maxvib or abs(realz-oldz)>maxvib):
                    IO.IO.startnalarm()
                
               
