# -*- coding: utf-8 -*-
"""
Automate WhatsApp - Sending WhatsApp message

@author: DELL Ishvina Kapoor
"""

#importing the necessary modules
import pywhatkit as pkt
import getpass as gp

#displaying a welcome message
print("Automating Whatsapp!")

#capturing the target phone number from the user

phone_num = gp.getpass(prompt = 'Enter the phone number(with country code) : ', stream = None) 

#capture the message
message = "Hi IK this side"

#call the method
#the time is in 24 hr format
pkt.sendwhatmsg(phone_num, message, 22 , 33)

#will be displayed once whatsapp is automated
print("Delivered to the target user")