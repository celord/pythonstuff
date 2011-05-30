#!/usr/bin/env python
#coding=utf-8

import optparse, sys,subprocess,re
import os
#Script para obtner las direcciones ip  de la LAN a la cual se esta
#actualmente conectado


#Definiendo algunas variables

#outfile=subred+"_ip.list"

def usage():
     print "ip_list.py [INTERFACE] [IP]/[MASKBITS]"

def check_arp_scan():
    proc = subprocess.Popen("dpkg --status arp-scan | grep 'ok installed'", shell=True, stdout=subprocess.PIPE)
    stdout_value = proc.communicate()[0]

    if "installed" in stdout_value:
        pass

    else:
        print "please install arp-scan: apt-get install -y arp-scan"


def arp_scan():
    '''
    '''
    if len(sys.argv) < 3:
        usage()
    else:

        proc = subprocess.Popen("arp-scan --interface="+sys.argv[1]+" "+sys.argv[2]+" | grep -E '([[:digit:]]{1,3}\.){3}' | cut -f 1",
            shell=True, stdout=subprocess.PIPE)
        stdout_value = proc.communicate()[0]
        print stdout_value

def check_root():
    if os.getuid() != 0:
        return False
    else:
        return True

if __name__ == '__main__':
    if check_root():
        check_arp_scan()
        arp_scan()
    else:
        print 'You need to be root!'
