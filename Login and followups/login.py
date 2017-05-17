import RPi.GPIO as GPIO
import time
import MySQLdb
import sock


def numpad():
	GPIO.setmode(GPIO.BCM)
	inp=[2,3,5]
	GPIO.setup(inp,GPIO.IN)
	out = [26,19,13,6]
	GPIO.setup(out, GPIO.OUT)
	try:
		GPIO.output(out,0)
		pressed=0
		printed=0
		x=""
		while printed<4:
			GPIO.output(out,0)
			if (not GPIO.input(2) or not GPIO.input(3) or not GPIO.input(5)) and pressed ==0:
				pressed=1    
				GPIO.output(out,1)
				GPIO.output(26,0)
				if not GPIO.input(2):
					x+="1"
				if not GPIO.input(3):
					x+="2"
				if not GPIO.input(5):
					x+="3"
				GPIO.output(26,1)
				GPIO.output(19,0)
				if not GPIO.input(2):
					x+="4"
				if not GPIO.input(3):
					x+="5"
				if not GPIO.input(5):
					x+="6"
				GPIO.output(19,1)
				GPIO.output(13,0)
				if not GPIO.input(2):
					x+="7"
				if not GPIO.input(3):
					x+="8"
				if not GPIO.input(5):
					x+="9"
				GPIO.output(13,1)
				GPIO.output(6,0)
				if not GPIO.input(3):
					x+="0"            
				GPIO.output(6,1)
				GPIO.output(out,0)
				printed+=1
				return x
			if (GPIO.input(2) and GPIO.input(3) and GPIO.input(5)):
				pressed=0
			
		dbconn(x)

		
    
	except KeyboardInterrupt:
		pass
	finally:
		GPIO.cleanup()
def dbconn(x):
	db = MySQLdb.connect("localhost","root","lucifer123","autoH" )
	cursor = db.cursor()
	query = "select * from user where pin = '"+x+"'"
	cursor.execute(query)
	data = cursor.fetchone()
	return not data==None
		#gatecontrol.openDoor(12,21)
			

	
	
	
def main():	
	numpad()

if __name__ =='__main__':
	main()
