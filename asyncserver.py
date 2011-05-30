#!/usr/bin/env python
"""
   celord's asyncronous server without twisted 
"""


import optparse,os,datetime,errno,select,socket

def parse_args():
    
    usage = '''usage: %prog [options] poetry-file
    
This is the asyncronous Poetry Server, without Twisted

Run it like this:

    python asyncserver.py <path-to-poetry-file>
    
'''

    parser = optparse.OptionParser(usage)
    
    help = "The port to listen on, Default to a random available port"    
    parser.add_option('--port','-p', type='int', help=help, default=10001)
    
    
    help = "The interface  to listen on. Default is localhost"
    parser.add_option('--iface', help=help, default='')
    
    options,args = parser.parse_args()
    
    if len(args) != 1:
        parser.error('Provide exactly a poetry file')
        
    poetry_file = args[0]
    
    if not os.path.exists(args[0]):
        parser.error('No such file: %s' % poetry_file)
        
    return options, poetry_file



def send_poetry(sock, poetry_file):
    
    "Send the poetry in an async way"

    inputf = open(poetry_file)
    
    while sock:
        _, wlist, _ = select.select([],[sock], [])
        bytes = inputf.read()
        
        for sock in wlist:
            if not bytes:
                inputf.close()
                sock.close()
                return
            print "Sending %s bytes" % len(bytes)
        
            try:
                sock.setblocking(0)
                sock.send(bytes)
            except socket.error:
                sock.close()
                inputf.close()
                return
        

def serve(listening_socket, poetry_file):
    while True:
        sock, addr = listening_socket.accept()
        
        print "Someone wants some poetry from %s" % (addr,)

        send_poetry(sock, poetry_file)
        
        
    

def main():
    options, poetry_file = parse_args()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print options.iface, options.port
    sock.bind((options.iface, options.port))
    sock.listen(5)
    #sock.setblocking(0)
    
    print 'Serving %s on port %s.' % (poetry_file, sock.getsockname()[1])
    
    serve(sock, poetry_file)
    
if __name__ == '__main__':
    main()
    
