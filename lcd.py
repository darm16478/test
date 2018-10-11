from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
from blynkapi import Blynk
#from Blynk import *
import time
gpio.init()
led_1=port.PA12
auth_token = "6550d659b4bb4d189509a09e6f7f61ff"
room_light = Blynk(auth_token, pin = "V0")
gpio.setcfg(led_1,gpio.OUTPUT)
while True:
	res = room_light.get_val()
	print res
	
	if res[0]==u'0':
		gpio.output(led_1,1)
		print res
		print "xxxx";
	if res[0]==u'1':
		gpio.output(led_1,0)
		print res
		print("YYYYY");

# set pin value (one)
#amp_power.set_val(["120"])

# set pin value to 1
#room_light.on()
# set pin value to 0
#room_light.off()
#gpio.setcfg(led_1,gpio.OUTPUT)
#gpio.output(led_1,1)

		

