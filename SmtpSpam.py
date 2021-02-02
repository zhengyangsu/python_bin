#!/usr/bin/python

import smtplib

sender = 'joshualzc@sfu.ca'
receivers = ['huixu1990@hotmail.com']

message = """From: Joshua <joshualzc@hotmail.com>
To: To XuHui <huixu1990@hotmail.com>
Subject: Dota 
This is a test e-mail message.
Hello Luke!
"""
counter = 0
while(counter < 300):
	try:
   		#smtpObj1 = smtplib.SMTP('shawmail.vc.shawcable.net')
   		smtpObj1 = smtplib.SMTP('smtp.telus.net')

   		#smtpObj2 = smtplib.SMTP('mx2.hotmail.com')

   		#smtpObj3 = smtplib.SMTP('mx3.hotmail.com')

   		#smtpObj4 = smtplib.SMTP('mx4.hotmail.com')

   		smtpObj1.sendmail(sender, receivers, message)
   		#smtpObj2.sendmail(sender, receivers, message)

   		#smtpObj3.sendmail(sender, receivers, message)

   		#smtpObj4.sendmail(sender, receivers, message)
		counter = counter + 1
		         
   		print "Successfully sent email"
	except smtplib.SMTPException:
   		print "Error: unable to send email"