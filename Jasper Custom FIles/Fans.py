# -*- coding: utf-8-*-
import random
import re
import sys
sys.path.append('/home/pi/Desktop/autoh/Lights')

from serial_led import serialControl
 
WORDS = ["TURN", "ON", "ALL", "FANS"]


def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)"""
    
    messages = ["TURNING FANS ON...",
                "BE SURE NOT TO CATCH COLD"]

    message = random.choice(messages)

    mic.say(message)
    
    serialControl("6000")
    serialControl("7000")
    


def isValid(text):
	return bool(re.search(r'\bturn all fans on\b', text, re.IGNORECASE))
