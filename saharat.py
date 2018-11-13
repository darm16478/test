import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


led_1 = 2 	#G
led_2 = 3 	#Y
led_3 = 4 	#R

led_4 = 17	#G
led_5 = 27 #Y
led_6 = 22 #R

led_7 = 10	#G
led_8 = 9	#Y
led_9 = 11#R

led_10= 5
led_11= 6
led_12= 13
GPIO.setup(led_1,GPIO.OUT)
GPIO.setup(led_2,GPIO.OUT)
GPIO.setup(led_3,GPIO.OUT)
GPIO.setup(led_4,GPIO.OUT)
GPIO.setup(led_5,GPIO.OUT)
GPIO.setup(led_6,GPIO.OUT)
GPIO.setup(led_7,GPIO.OUT)
GPIO.setup(led_8,GPIO.OUT)
#GPIO.setup(led_9,GPIO.OUT)
#GPIO.setup(led_10,GPIO.OUT)
#GPIO.setup(led_11,GPIO.OUT)
#GPIO.setup(led_12,GPIO.OUT)





L = [
		[1,0,1,0,1,0,1,0],
		[0,1,1,0,0,1,1,0],
		[0,1,0,1,1,0,1,0],
		[0,1,1,0,1,0,0,1],
		
		
]

try:
	while True:
		for i in range(0,4):
			GPIO.output(led_1,L[i][0])
			GPIO.output(led_2,L[i][1])
			GPIO.output(led_3,L[i][2])
			GPIO.output(led_4,L[i][3])
			GPIO.output(led_5,L[i][4])
			GPIO.output(led_6,L[i][5])
			GPIO.output(led_7,L[i][6])
			GPIO.output(led_8,L[i][7])
			#GPIO.output(led_9,L[i][8])
			time.sleep(3)

except KeyboardInterrupt:
	print ("Bye")

