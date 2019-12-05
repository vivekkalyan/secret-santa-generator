#! /usr/local/bin/python

from dotenv import load_dotenv
import sys
import os
import json
import random
load_dotenv(verbose=True)

SMTPSERVER = os.getenv("SMTPSERVER")
SENDER = os.getenv("SENDER")
USERS = json.loads(os.getenv("USERS")) #list of emails

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

n_users = len(USERS)
available = set(range(n_users))
random.shuffle(USERS)
# choices = []
# for i, user in enumerate(USERS):
#     temp_available = available - set([i])
#     choice = random.choice(list(temp_available))
#     available = available - set([choice])
#     choices.append(choice)
# prevent isntances where last person is left with themselves
choices = list(map(lambda a: (a+1)%n_users), USERS)

subject="Your Santa"
text_subtype = 'plain'

from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText

def generate_content(user1, user2):
    content=(
        f"hello!\n\n"
        f"this is Vivek's consciousness uploaded to the cloud. and I have decided the gifts list :D\n"
        f"you are {USERS[user1]} and you will be gifting {USERS[user2]}.\n\n"
        "have fun!!!"
    )
    return content

def send_email(destination, content):
    try:
        msg = MIMEText(content, text_subtype)
        msg['Subject']= subject
        msg['From'] = SENDER
        msg['To'] = destination

        conn = SMTP(SMTPSERVER)
        conn.set_debuglevel(False)
        conn.login(USERNAME, PASSWORD)
        try:
            conn.sendmail(SENDER, destination, msg.as_string())
        finally:
            conn.quit()

    except Exception as e:
        sys.exit( "mail failed; %s" % e ) # give an error message

for i in list(range(n_users)):
    c = choices[i]
    content = generate_content(i,c)
    send_email(USERS[i], content)
    print(f"sent --- {USERS[i]}")
