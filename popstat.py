#!/usr/bin/python
import poplib,sys

#cuenta=sys.argv[1]
cuenta="cgarcia"
pw="celord23."
mailsrv="icecom.ice.co.cr"

m=poplib.POP3_SSL(mailsrv)

m.user(cuenta)
m.pass_(pw)

print "Hay %d correos para %s." % (m.stat()[0],who)
m.quit
