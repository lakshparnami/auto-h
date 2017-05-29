#!/usr/bin/env python
import time
import MySQLdb
import RPi.GPIO as GPIO
import serial
import MySQLdb
import sys
sys.path.append('/home/pi/Desktop/autoh')
from dbconnect import connect


def input_log(data):
	
	col=""
	if data[0]=="2":
		col="l1"	
	elif data[0]=="3":	
		col="l2"
	elif data[0]=="4"	:
		col="l3"
	elif data[0]=="5"	:
		col="l4"
	elif data[0]=="6"	:
		col="f1"
	elif data[0]=="7"	:
		col="f2"
	
	db = MySQLdb.connect("localhost","root","lucifer123","autoH" )
	cursor = db.cursor()
	intensity = data[1:]
	query=	"UPDATE current_status SET `f1`=123"
	cursor.execute(query)
	try:
		db.commit()
		print "Inserted"
	except MySQLdb.IntegrityError:
		print "Faild"
	'''insert into log (l1,l2,l3,l4,f1,f2,pump) select l1,l2,l3,l4,f1,f2,pump from current_status'''
	
	
def serialControl(a):
	test=serial.Serial("/dev/ttyACM0",9600)
	#test.open()

	try:
		test.write(str(a))
		input_log(str(a))
                
	except KeyboardInterrupt:
		pass # do cleanup here
	
	test.close()	

if __name__=="__main__":
	input_log("7123")	
