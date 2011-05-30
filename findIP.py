#!/usr/bin/env python
import urllib2
#request the page
def GetIP(server):
    page = urllib2.urlopen(server)
    body = page.read()
    return body

def main():
    server = 'http://www.whatismyip.com/automation/n09230945.asp'
    IP = GetIP(server)
    print IP

main()
