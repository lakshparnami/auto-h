#!/usr/bin/env python
import time
import serial

def serialControl(data):
	test=serial.Serial("/dev/ttyACM0",9600)
	#test.open()

	try:
		a=data
		test.write(str(a))
                #time.sleep(1)
                
	except KeyboardInterrupt:
		pass # do cleanup here
	
	test.close()	
