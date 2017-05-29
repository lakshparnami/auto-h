# -*- coding: utf-8-*-
import random
import re
import sys
sys.path.append('/home/pi/Desktop/autoh/Lights')

from serial_led import serialControl
 
WORDS = ["TURN", "THE", "LIGHT", "ON"]

def lightno(mic):
	text=mic.activeListen()
	if text=="ONE" or text=="1":
		mic.say("Turning light one on")
		serialControl("2000")
	elif text=="TWO" or text=="2":
		mic.say("Turning light two on")
		serialControl("3000")
	elif text=="THREE" or text=="3":
		mic.say("Turning light three on")
		serialControl("4000")
	elif text=="FOUR" or text=="4":
		mic.say("Turning light four on")
		serialControl("5000")	
	else:
		mic.say("Sorry I don't think I can do that")
		lightno(mic)
		
		
def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)"""
    
    messages = ["WHICH ONE, SIR?",
                "WHICH LIGHT DO YOU WANT ME TO TURN ON?	"]

    message = random.choice(messages)

    mic.say(message)
    lightno(mic)


def isValid(text):
	return bool(re.search(r'\bturn the light on\b', text, re.IGNORECASE))
