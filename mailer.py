
#!/usr/bin/env python
#coding=utf-8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MILOGIN='cgarcia'
MI_PASS='celord23.'
COMMASPACE = ', '
toList = ['sincronizate@ice.co.cr']

texto = '87000522'


msg = MIMEMultipart()
msg['Subject'] = '87000522'
msg['From'] = 'mailcop@ice.co.cr'
msg['To'] = COMMASPACE.join(toList)
msg.preamble = 'Posibles Spammers'

body = MIMEText(texto, 'plain')

msg.attach(body)
    
s = smtplib.SMTP('mail.ice.co.cr')
#s.set_debuglevel(1)
s.login(MILOGIN,MI_PASS)
s.sendmail('cgarcia@ice.co.cr',toList,msg.as_string())
s.close()
