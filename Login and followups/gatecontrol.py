import RPi.GPIO as GPIO
import time

def closeDoor(servopin):
	p=GPIO.PWM(servopin,100)
	p.start(5)
	p.ChangeDutyCycle(20.5)#20.5 to reverse
	time.sleep(1)
	p.stop()
def CheckDoor(i,irpin,servopin):
	time.sleep(1)
	while GPIO.input(irpin)==1:
		i #just messing with the compiler 
	if i<4:
		CheckDoor(i+1,irpin,servopin)
	else:
		closeDoor(servopin)
		
def setupGPIO(irpin,servopin):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(irpin,GPIO.IN)
	GPIO.setup(servopin,GPIO.OUT)
	
def openDoor(irpin,servopin):
	GPIO.setup(servopin,GPIO.OUT)
	p=GPIO.PWM(servopin,100)
	setupGPIO(irpin,servopin)
	p.start(5)
	p.ChangeDutyCycle(2.5)#20.5 to reverse
	time.sleep(1)
	p.stop()
	CheckDoor(0,irpin,servopin)

def CheckRoom2Door(irpin,servopin):
	time.sleep(2)
	while GPIO.input(irpin)==0:
		irpin #just messing with the compiler again
	openDoor(27,servopin)
	

'''def main():
	setupGPIO(22,17)	
	CheckRoom2Door(22,17)

if __name__ =='__main__':
	main()'''

