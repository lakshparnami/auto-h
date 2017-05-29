# -*- coding: utf-8-*-
import random
import re
import sys
sys.path.append('/home/pi/Desktop/autoh/Lights')

from serial_led import serialControl
 
WORDS = ["TURN", "ON", "ALL", "LIGHTS"]


def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)"""
    
    messages = ["TURNING LIGHTS ON...",
                "HOLD ON."]

    message = random.choice(messages)

    mic.say(message)
    
    serialControl("2000")
    serialControl("3000")
    serialControl("4000")
    serialControl("5000")
    


def isValid(text):
	return bool(re.search(r'\bturn all lights on\b', text, re.IGNORECASE))
