import random
import re
import sys
sys.path.append('/home/pi/Desktop/autoh')
from dbconnect import connect

WORDS = ["STATUS"]


def handle(text, mic, profile):

	cursor = connect()
	query = "select * from current_status"
	cursor.execute(query)
	stat = cursor.fetchone()
	lights = stat[:3]
	fans = stat[4:6]
	door = stat[6]
	garage = stat[7]
	lightson=[]
	fanon=[]
	mic.say("Copy that")
	for x in lights:
		if x>0:
			flag=1
		else:
			flag=0
			break	
					
	if flag==1:
		mic.say("All lights are on")
	else:
		i=-1
		on =""
		for x in lights:
			i+=1
			if x>0:
				lno=i+1
				lightson.append(lno)
				if i==0:
					on="Light "+str(lightson[0])
				else:
					on+="and"+str(lightson[i])
		
		if len(fanon) ==1:
			mic.say(on+" is on")
		else:
			mic.say(on+" are on")
		
	for x in fans:
		if x>0:
			flag=1
		else:
			flag=0
			break
			
	if flag==1:
		mic.say("All fans are on")	
	else:
		i=-1
		on = ""
		for x in fans:
			i+=1
			if x>0:
				fno=i+1
				fanon.append(fno)
				if i==0:
					on="Fan "+str(fanon[0])
				else:
					on+="and"+str(fanon[i])
		
		if len(fanon) ==1:
			mic.say(on+" is on")
		else:
			mic.say(on+" are on")

	if door == 1:
		mic.say("Main door is open")
	
	if garage==1:
		mic.say("garage is open")
	
	mic.say("This is your house status")
	
def isValid(text):
	return bool(re.search(r'\bstatus\b', text, re.IGNORECASE))

