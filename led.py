from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port


MATRIX = [[1,2,3,'A'],
		  [4,5,6,'B'],
		  [7,8,9,'C'],
		  ['*',0,'#','D']]
Col1 = port.PA20
Col2 = port.PA10
Col3 = port.PA9
Col4 = port.PA8
Row4 = port.PA19
Row3 = 0
Row2 = port.PC2	
Row1 = port.PC1		

 
gpio.init()
gpio.setcfg(Col1, gpio.INPUT)
gpio.setcfg(Col2, gpio.INPUT)
gpio.setcfg(Col3, gpio.INPUT)
gpio.setcfg(Col4, gpio.INPUT)
gpio.setcfg(Row1, gpio.OUTPUT)
gpio.setcfg(Row2, gpio.OUTPUT)
gpio.setcfg(Row4, gpio.OUTPUT)


gpio.pullup(Col1, gpio.PULLUP)
gpio.pullup(Col2, gpio.PULLUP)
gpio.pullup(Col3, gpio.PULLUP)
gpio.pullup(Col4, gpio.PULLUP)

try:
    print ("Press CTRL+C to exit")
    while True: 
        gpio.output(Row4,0)
        state = gpio.input(Col4)
        if state ==0:
				print("D")
		while(gpio.input(Col3)==0):
			pass
			sleep (0.2)
        if state ==0: 
				print("#")
		state = gpio.input(Col2)
        if state ==0: 
				print("0")
		state = gpio.input(Col1)
        if state ==0:
				print("*")
				
except KeyboardInterrupt:
    print ("Goodbye .")
