import random
import re
 
WORDS = ["TURN","OFF"]


def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)"""
    
    messages = ["SHUTTING DOWN...",
                "I WILL MISS YOU."]

    message = random.choice(messages)

    mic.say(message)
    


def isValid(text):
	return bool(re.search(r'\bturn off\b', text, re.IGNORECASE))
