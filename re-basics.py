#literals
import re

print "Probando"
string = "pruebas.pushmail@ice.co.cr"


patt = re.compile('([A-Za-z0-9\.]*@[A-Za-z0-9.-]+)')
matchobj = re.search(patt, string)

if matchobj:
    print matchobj.groups()
