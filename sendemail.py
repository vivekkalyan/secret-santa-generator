#! /usr/local/bin/python

from dotenv import load_dotenv
import sys
import os
load_dotenv(verbose=True)

SMTPSERVER = os.getenv("SMTPSERVER")
SENDER = os.getenv("SENDER")
DESTINATION = os.getenv("SENDER")

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

text_subtype = 'plain'

content="""\
Test
"""

subject="Sent from Python"

from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText

try:
    msg = MIMEText(content, text_subtype)
    msg['Subject']= subject
    msg['From'] = SENDER
    msg['To'] = DESTINATION

    conn = SMTP(SMTPSERVER)
    conn.set_debuglevel(False)
    conn.login(USERNAME, PASSWORD)
    try:
        conn.sendmail(SENDER, DESTINATION, msg.as_string())
    finally:
        conn.quit()

except Exception as e:
    sys.exit( "mail failed; %s" % e ) # give an error message

