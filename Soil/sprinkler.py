import RPi.GPIO as GPIO
import time
def CheckSoil(sensorpin,motorpin):
	while GPIO.input(sensorpin)==0:
		time.sleep(1)
		GPIO.output(motorpin,GPIO.LOW)
		print "Sprinkler is off"
	TurnOnMotor(sensorpin,motorpin)
	
		
def TurnOnMotor(sensorpin,motorpin):
	while GPIO.input(sensorpin)==1:
		time.sleep(1)
		GPIO.output(motorpin,GPIO.HIGH)
		print "Sprinkler is on"
	CheckSoil(sensorpin,motorpin)
		
	
def setupGPIO(sensorpin,motorpin):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(sensorpin,GPIO.IN)
	GPIO.setup(motorpin,GPIO.OUT)
	
def main():
	setupGPIO(23,24)
	CheckSoil(23,24)

if __name__ =='__main__':
	main()
