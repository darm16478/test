from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
import time
gpio.init()
led_1=port.PA12
led_2=port.PA11
led_3=port.PA6
led_4=port.PA1
led_5=port.PA0


gpio.setcfg(led_1,gpio.OUTPUT)
gpio.setcfg(led_2,gpio.OUTPUT)
gpio.setcfg(led_3,gpio.OUTPUT)
gpio.setcfg(led_4,gpio.OUTPUT)
gpio.setcfg(led_5,gpio.OUTPUT)


L=[
	[1,0,1,0,0,1],
	[0,1,0,1,0,0],
	[0,0,1,0,1,0],
	[0,0,0,1,0,1],
	[0,0,1,0,1,0],
	[0,1,0,0,0,0],
	
	
]
try:
	while True:
		for i in range(0,3):
			gpio.output(led_1,L[i][0])
			gpio.output(led_2,L[i][1])
			gpio.output(led_3,L[i][2])
			gpio.output(led_4,L[i][3])
			gpio.output(led_5,L[i][4])
			time.sleep(0.5)
except KeyboardInterrupt:
	print("xxxx")
