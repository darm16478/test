from pyA20.gpio import gpio
from pyA20.gpio import port
import time

TRIG = port.PA13
ECHO = port.PA14

led = port.PA20



gpio.init()
gpio.setcfg(led,gpio.OUTPUT)
print "Distance Measurement In Progress"

gpio.setcfg(TRIG, gpio.OUTPUT)
gpio.setcfg(ECHO, gpio.INPUT)

gpio.output(TRIG, 0)

print "Waiting For Sensor To Settle"

def light(i):
	gpio.output(led, 1)
	time.sleep(i)
	gpio.output(led, 0)
	time.sleep(0.001)

while True :
	time.sleep(1)
	gpio.output(TRIG, 1)
	time.sleep(0.00001)
	gpio.output(TRIG, 0)

	while gpio.input(ECHO) == 0:
		pulse_start = time.time()
		gpio.output(led, 1)

	while gpio.input(ECHO) == 1:
		pulse_end = time.time()
		gpio.output(led, 0)

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150

	distance = round(distance, 3)

	print("Distance: " + str(distance) + "cm")
	
	if distance > 50 :
		gpio.output(led, 1)
		
	else :
		light(1);