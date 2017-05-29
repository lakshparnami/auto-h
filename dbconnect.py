import MySQLdb

def connect():
	db = MySQLdb.connect("localhost","root","lucifer123","autoH" )
	cursor = db.cursor()	
	return cursor
