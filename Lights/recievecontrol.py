# Tcp Chat server
 
import socket, select
import serial_led
import codecs
import sys
sys.path.append('/home/pi/Desktop/autoh')

from dbconnect import connect

def dbpref(col=[], pin=[]):
	cursor = connect()
	col = col[0]+col[1]
	pin = pin[0]+pin[1]+pin[2]+pin[3]
	query = "select "+col+" from pref where pin='"+pin+"'"
	cursor.execute(query)
	print "reached here"
	data = cursor.fetchone()
	return str(data[0])
 
def main():
	# List to keep track of socket descriptors
    CONNECTION_LIST = []
    RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
    PORT = 1234
     
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this has no effect, why ?
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("192.168.1.11", PORT))
    server_socket.listen(10)
 
    # Add server socket to the list of readable connections
    CONNECTION_LIST.append(server_socket)
 
    print "server started on port " + str(PORT)
 
    while 1:
        # Get the list sockets which are ready to be read through select
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
 
        for sock in read_sockets:
            #New connection
            if sock == server_socket:
                # Handle the case in which there is a new connection recieved through server_socket
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print "Client (%s, %s) connected" % addr
                 
             
            #Some incoming message from a client
            else:
                # Data recieved from client, process it
                try:
					serialdata=""
                    #In Windows, sometimes when a TCP program closes abruptly,
                    # a "Connection reset by peer" exception will be thrown
					data = sock.recv(RECV_BUFFER)
					print data
					if len(data)>1:
						serialdata=""
						if data[:2]=="l1":
							serialdata+="2"	
						elif data[:2]=="l2":	
							serialdata+="3"
						elif data[:2]=="l3"	:
							serialdata+="4"
						elif data[:2]=="f1"	:
							serialdata+="6"
						elif data[:2]=="f2"	:
							serialdata+="7"	
						elif data[:2]=="d1"	:
							"""func"""
						elif data[:2]=="d2"	:
							"""funtion"""	
	
						if data[2]=="0":
							serialdata+="255"
						elif data[2]=="1":
							s= dbpref(data[:2],data[3:])
							serialdata+=s
						if(len(serialdata)==2):
							serialdata=serialdata[0]+"00"+seriadata[1:]
						elif(len(serialdata)==3):
							serialdata=serialdata[0]+"0"+serialdata[1:]
						
						print serialdata			
						serial_led.serialControl(serialdata)
						
						
							
                except:
                    print "Client (%s, %s) is offline" % addr
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue

    server_socket.close()
    main() 
if __name__ == "__main__":
     main()
