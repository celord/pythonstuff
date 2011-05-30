#!/usr/bin/env python
#coding=utf-8

import os
import sys
import time

#Twisted
from twisted.python import log
from twisted.python.logfile import DailyLogFile

from twisted.internet import defer,  reactor,  inotify
from twisted.internet.protocol import Protocol, ClientFactory

class DirectoryTellProtocol(Protocol):
    
    def __init__(self):
        print 'calling %s.%s' % (self.__class__.__name__, sys._getframe().f_code.co_name)
        factory = self.factory
        
    def announceNewFile(self, path):
        print 'calling %s.%s' % (self.__class__.__name__, sys._getframe().f_code.co_name)
        self.transport.write('new file created at:\n' % path)
    
    def connectionLost(self, reason):
        print 'calling %s.%s' % (self.__class__.__name__, sys._getframe().f_code.co_name)
        log.msg('connectionLost at: %S' % (time.asctime(time.localtime(time.time()))))
        

class DirectoryTellFactory(ClientFactory):
    
    protocol = DirectoryTellProtocol
    
    def __init__(self):
        
        print "calling %s.%s" % (self.__class__.__name__, sys._getframe().f_code.co_name)
        self.protocol_objects = []
        self.watch_path = filepath.FilePath(path)
        self.watch_mask = mask
        self.notifier = inotify.INotify()
        self.defered = defered
        
    def builProtocol(self):
        print "calling %s.%s" % (self.__class__.__name__, sys._getframe().f_code.co_name)
        return DirectoryTellProtocol()
        
    def inotifyEventHappened(self):
        
        print "calling %s.%s" % (self.__class__.__name__, sys._getframe().f_code.co_name)
        protocol.announceNewFile(watch_obj, path, mask)

    def clientConnectionLost(self, connector, reason):
        print "calling %s.%s" % (self.__class__.__name__, sys._getframe().f_code.co_name)

    def clientConnectionFailed(self, connector, reason):
        print "calling %s.%s" % (self.__class__.__name__, sys._getframe().f_code.co_name)
        
        
if __name__ == "__main__":
    
    factory = DirectoryTellFactory('/tmp', IN_CREATE)
        
        
        
        
        
    




