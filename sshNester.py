#!/usr/bin/env python

"""This runs 'ls -l' on a remote host using SSH. At the prompts enter hostname,
user, and password.

$Id: sshls.py 489 2007-11-28 23:40:34Z noah $
"""

import pexpect
import getpass, os

def ssh_command (port, user, host, password):

    """This runs a command on the remote host. This could also be done with the
pxssh class, but this demonstrates what that class does at a simpler level.
This returns a pexpect.spawn object. This handles the case when you try to
connect to a new host and ssh asks you if you want to accept the public key
fingerprint and continue connecting. """

    ssh_newkey = 'Are you sure you want to continue connecting'
    child = pexpect.spawn('ssh -p %s -l %s %s'%(port, user, host))
    i = child.expect([pexpect.TIMEOUT, ssh_newkey, 'Password: '])
    if i == 0: # Timeout
        print 'ERROR!'
        print 'SSH could not login. Here is what SSH said:'
        print child.before, child.after
        return None
    if i == 1: # SSH does not have the public key. Just accept it.
        child.sendline ('yes')
        child.expect ('password: ')
        i = child.expect([pexpect.TIMEOUT, 'password: '])
        if i == 0: # Timeout
            print 'ERROR!'
            print 'SSH could not login. Here is what SSH said:'
            print child.before, child.after
            return None       
    child.sendline(password)
    print "sshing..."
    n = child.sendline('ssh cgarcia@sjop01')
    child.expect('cgarcia@sjop01\'s password: ')
    child.sendline('C3g00r2T6F')
    child.expect('SJOP01#')
    child.sendline('show clock')
    return child

def main ():
    port = 10022
    host = '200.91.75.3'
    user = 'cgarcia'
    password = 'Zezar24.'
    child = ssh_command (port, user, host, password)
    child.expect
    child.expect(pexpect.EOF)
    print child.before
    print child.after

if __name__ == '__main__':
    try:
        main()
    except Exception, e:
        print str(e)
        traceback.print_exc()
        os._exit(1)

