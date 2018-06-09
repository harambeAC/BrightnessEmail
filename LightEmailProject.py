#this is a python project by Alex Chen

"""
the purpose of this project is to send me an email
every time it gets dark
AKA when photoresistor on arduino reads very small value
"""

import serial
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

ser = serial.Serial('/dev/cu.usbmodem1411', 9600)
while True:
    brightness = ser.readline().strip()
    print brightness

    if int(brightness) < 100:
        #send an email to alexyjchen@gmail.com
        #print "Dark"

        me = "ae604655@gmail.com"
        my_password = "5dec1e98ea"
        you = "ae604655@gmail.com"

        msg = MIMEMultipart('alternative')
        msg['Subject'] = "It's Dark"
        msg['From'] = me
        msg['To'] = you

        html = "<html><body><p>Brightness is " + brightness +". "+ "</p></body></html>"
        part2 = MIMEText(html, 'html')

        msg.attach(part2)

        # Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
        s = smtplib.SMTP_SSL('smtp.gmail.com')
        # uncomment if interested in the actual smtp conversation
        # s.set_debuglevel(1)
        # do the smtp auth; sends ehlo if it hasn't been sent already
        s.login(me, my_password)

        s.sendmail(me, you, msg.as_string())
        s.quit()
