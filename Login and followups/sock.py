import socket,select
import login
import RPi.GPIO as GPIO
import time
import gatecontrol

def setupGPIO():
	GPIO.setmode(GPIO.BCM)
	inp=[2,3,5]
	GPIO.setup(inp,GPIO.IN)
	out = [26,19,13,6]
	GPIO.setup(out, GPIO.OUT)
	
def senddata():
	while True:
		read_sockets,write_sockets,error_sockets=select.select(CONNECTION_LIST,[],[])
		for sock in read_sockets:

			if sock==server_socket:
				sockfd,addr=server_socket.accept()
				CONNECTION_LIST.append(sockfd)
				print(addr[0])
				loggedin2=False
				pressed=0
				i=0
				num=''
				while i<4:
					setupGPIO()
					if (not GPIO.input(2) or not GPIO.input(3) or not GPIO.input(5)) and pressed ==0:
						pressed=1
						pin = login.numpad()
						sockfd.send("%s" % pin)
						print pin
						i+=1
						num+=pin
					setupGPIO()
					if (GPIO.input(2) and GPIO.input(3) and GPIO.input(5)):
						pressed=0
				if(login.dbconn(num)):
					loggedin2=True
					server_socket.close()
					gatecontrol.openDoor(12,21)
				return loggedin2

				'''if not sock==server_socket:
					data=sock.recv(RECV_BUFFER)
					print(data)
					CONNECTION_LIST.remove(sock)
					break'''
	'''server_socket.close()'''

	
def con():
	global CONNECTION_LIST
	global loggedin
	loggedin=False
	CONNECTION_LIST=[] #listofsocketclients
	RECV_BUFFER=4096
	PORT=1234
	global server_socket
	server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	server_socket.bind(("192.168.1.12",PORT))
	server_socket.listen(10)

	CONNECTION_LIST.append(server_socket)

	print"Server started on port "+str(PORT)
	while not loggedin:
		time.sleep(0.1)
		loggedin=senddata()
		time.sleep(0.1)
	
def main():
	setupGPIO()
	con()
	server_socket.close()
	main()
	
if __name__ == '__main__':
	main()
