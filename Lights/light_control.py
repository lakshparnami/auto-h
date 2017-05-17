import serial
import time
import string


	
def light(lightno,brightness):
	ser = serial.Serial('/dev/ttyACM0',9600)
	rot13 = string.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", "NOPQRSTUVWXYZnopqrstuvwxyzABCDE FGHIJKLMabcdefghijklm")
	x=lightno+":"+brightness+"\n\r0"
	print(x)
	ser.write(string.translate(x, rot13))
	
if __name__ =='__main__':
	light('1','10')
