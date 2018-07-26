'''
The example that attaches a pdf by using AWS SES via boto.
'''

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

import boto
ACCESS_KEY = "" # ACCESS_KEY
SECRET_KEY = "" # SECRET_KEY

msg = MIMEMultipart()
msg['Subject'] = 'Test SES'
msg['From'] = '' # Sender Email
msg['To'] = '' # Reciever Email

# what a recipient sees if they don't use an email reader
msg.preamble = 'Multipart message.\n'

# the message body
part = MIMEText('Howdy -- here is the data from last week.')
msg.attach(part)

# the attachment
part = MIMEApplication(open('/ses/temp.pdf', 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename='temp.pdf')
msg.attach(part)

# connect to SES
connection = boto.connect_ses(aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY)

# and send the message
result = connection.send_raw_email(msg.as_string()
    , source=msg['From']
    , destinations=[msg['To']])
print result