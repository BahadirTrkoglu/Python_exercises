#send an email
import smtplib

sender   = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "pasword123"
subject  = "Python email test"
body     = " I wrote an email ! :D"

#header
message = f""" From : Snoop Dogg {sender}
 To: Nicholas Cage {receiver}
 Subject: {subject}\n
 {body} 
"""

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

try:
 server.login(sender,password)
 print("Logged in...")
 server.sendmail(sender, receiver, message)
 print("Email has been sent1")

except smtplib.SMTPServerDisconnected:
    print("unable to sign in")