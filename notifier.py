#!/usr/bin/env python
#coding=utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from twisted.internet import inotify, reactor
from twisted.python import filepath

#Mailing stuff
MYLOGIN='bodega'
MI_PASS='b0d3g4'
COMMASPACE = ', '
toList = ['87000522@sms.ice.cr']

#Watcher stuff
filepath = filepath.FilePath("/tmp")
mask=inotify.IN_CREATE

def notify(watch_object, filepath, mask):

    #print "new file created on %s " % (filepath)
    texto = str(filepath)
    msg = MIMEMultipart()
    msg['Subject'] = 'New File Created'
    msg['From'] = 'bodega@ice.co.cr'
    msg['To'] = COMMASPACE.join(toList)
    msg.preamble = 'New File Created'
    body = MIMEText(texto, 'plain')
    msg.attach(body)

    s = smtplib.SMTP('mail.ice.co.cr')
    s.set_debuglevel(1)
    s.login(MYLOGIN,MI_PASS)
    s.sendmail('bodega@ice.co.cr',toList,msg.as_string())
    s.close()


notifier = inotify.INotify()
notifier.startReading()
notifier.watch(filepath, mask, callbacks=[notify])
reactor.run()
