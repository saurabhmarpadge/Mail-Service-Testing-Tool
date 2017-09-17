DATA = "input.txt"
CLIENT_SECRET_FILE = 'client_secret.json'
#Custom Edit the above files as needed
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://mail.google.com/'
APPLICATION_NAME = 'Gmail API Quickstart'

def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,'gmail-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatability with Python 2.6
            credentials = tools.run(flow, store)
        print 'Storing credentials to ' + credential_path
    return credentials

import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
from httplib2 import Http
import threading
from apiclient import errors
import random
from apiclient.discovery import build
credentials = get_credentials()
try:
    service = build('gmail', 'v1', http=credentials.authorize(Http()))
except:
    print 'Not able to connect to server'

def SendMessage(service, user_id, message):
  try:
    message = (service.users().messages().send(userId=user_id, body=message).execute())
    print 'Message Id: %s' % message['id']
  except errors.HttpError, error:
    print 'An error occurred: %s' % error

def CreateMessage(sender, to, subject, message_text):
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  return {'raw': base64.b64encode(message.as_string())}

def SendMail(to,subject,body):
    Message = CreateMessage('me',to,subject,body)
    SendMessage(service, 'me', Message)

def getData():
    with open(DATA) as inputFile:
        log = inputFile.readlines()
    del log[:8]
    recipents = log.pop(0).strip('\n').split(',')
    subjects = log.pop(0).strip('\n').split(',')
    duration = log.pop(0).strip('\n')
    mail_count = log.pop(0).strip('\n')
    bodys = []
    for item in log:
        bodys.append(item.strip('\n'))
    return recipents,subjects,duration,mail_count,bodys

def getRandomSubject():
    global subjects
    rand = random.randint(0,len(subjects)-1)
    return subjects[rand]

def getRandomBody():
    global bodys
    rand = random.randint(0,len(bodys)-1)
    return bodys[rand]

def SendMailInBulk():
    global bodys
    for mail in recipents:
        subject = getRandomSubject()
        body = getRandomBody()
        SendMail(mail,subject,body)

def SendPeriodicMail(mail_count):
    if(mail_count<=0):
        return
    SendMailInBulk()
    mail_count = mail_count - 1
    threading.Timer(duration, SendPeriodicMail,args=(mail_count,)).start()

recipents,subjects,duration,mail_count,bodys = getData()
duration = float(duration)
mail_count = int(mail_count)

if __name__ == '__main__':
    thread1 = threading.Timer(duration, SendPeriodicMail,args=(mail_count,))
    thread1.start()
