import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from messages import *
from info import *

# Global Variables
FULL_NAME = FIRST_NAME + " " + LAST_NAME
NUM_LOCATIONS = 0
NUM_EMAILS_SENT = 0

def sendEmails():
    global NUM_LOCATIONS
    global NUM_EMAILS_SENT

    # Connect to gmail
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo()
    server.starttls()  # ensure a secure connection
    server.login(YOUR_EMAIL_ADDRESS, YOUR_EMAIL_PASSWORD)

    # loop through the emails to semd
    for email in emails:
        # create the email
        msg = MIMEMultipart()
        msg['Subject'] = email[1]
        msg['From'] = YOUR_EMAIL_ADDRESS
        msg['To'] = ", ".join(email[0])
        # fill in the name with the inputted name
        msgText = MIMEText(email[2].format(fullname=FULL_NAME))
        msg.attach(msgText)

        # send the email
        server.sendmail(YOUR_EMAIL_ADDRESS, ", ".join(
            email[0]), msg.as_string())  # send email

        # update counts
        NUM_LOCATIONS += 1
        NUM_EMAILS_SENT += len(email[0])
        print ("email: " + str(msg['Subject'] + " sent."))

    server.quit()  # exit the gmail server
    return


start = time.time()
sendEmails()
end = time.time()
print("Time to complete: " + str(end - start))
print("")
print("defundPoliceBot finished and sent " + str(NUM_EMAILS_SENT) +
      " total emails to " + str(NUM_LOCATIONS) + " local governments.")
