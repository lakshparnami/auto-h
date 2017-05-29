# -*- coding: utf-8-*-
import random
import re
import sys
sys.path.append('/home/pi/Desktop/autoh/Lights')

from serial_led import serialControl
 
WORDS = ["TURN", "THE", "FAN", "ON"]

def whichfan(mic):
	text=mic.activeListen()
	if text=="ONE" or text=="1":
		mic.say("Turning fan one on")
		serialControl("6000")
	elif text=="TWO" or text=="2":
		mic.say("Turning fan two on")
		serialControl("7000")
	else:
		mic.say("Sorry I don't think I can do that")
		whichfan(mic)
		
		
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
                "WHICH FAN DO YOU WANT ME TO TURN ON?	"]

    message = random.choice(messages)

    mic.say(message)
    whichfan(mic)


def isValid(text):
	return bool(re.search(r'\bturn the fan on\b', text, re.IGNORECASE))
