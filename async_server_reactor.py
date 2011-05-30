#!/usr/bin/env python
#-*- coding:utf-8 -*-

import optparse,os,datetime,errno,select,socket

"""
    Asyncronous server using only the reactor, but not all the twisted abstractions
"""

def parse_args():
"""
    First function to parse the options from the command line interpreter
"""

    usage = '''usage: %prog [options] poetry-file
    
This is the asyncronous Poetry Server, without Twisted

Run it like this:

    python asyncserver.py <path-to-poetry-file>
    
'''

    parser = optparse.OptionParser(usage)
    
    help = "The port to listen on, Default to a random available port"    
    parser.add_option('--port', type='int', help=help, default=10001)
    
    
    help = "The interface  to listen on. Default is localhost"
    parser.add_option('--iface', help=help, default='')

    optparse.OptionParser.
    
    options,args = parser.parse_args()
    
    if len(args) != 1:
        parser.error('Provide exactly a poetry file')
        
    poetry_file = args[0]
    
    if not os.path.exists(args[0]):
        parser.error('No such file: %s' % poetry_file)
        
    return options, poetry_file


