from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
import time

gpio.init()
led_1 = port.PA12 	
led_2 = port.PA11 	
led_3 = port.PA6
gpio.setcfg(led_1,gpio.OUTPUT)
gpio.setcfg(led_2,gpio.OUTPUT)
gpio.setcfg(led_3,gpio.OUTPUT)
try:
	while True:

			gpio.output(led_1,1)
			gpio.output(led_2,1)
			gpio.output(led_3,1)
			sleep(0.25)
			gpio.output(led_1,0)
			gpio.output(led_2,0)
			gpio.output(led_3,0)
			sleep(0.25)
except KeyboardInterrupt:
	print ("Bye")

