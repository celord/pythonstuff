from twisted.internet.protocol import Protocol, ClientFactory
from sys import stdout


class TmpTell(Protocol):
    def __init__(self, factory):
        print "calling %s.%s" % (self.__class__.__name__, sys._getframe().f_code.co_name)
        self.factory = factory

    def announceNewFile(self, watch_obj, path, mask):
        print "calling %s.%s" % (self.__class__.__name__, sys._getframe().f_code.co_name)
        self.transport.write("new file created at %s\n" % path)

    def connectionLost(self, reason):
        print "calling %s.%s" % (self.__class__.__name__, sys._getframe().f_code.co_name)
        self.factory.removeProtocolObject(self)


class TmpTellClientFactory(ClientFactory):
    def __init__(self, path, mask):
        print "calling %s.%s" % (self.__class__.__name__, sys._getframe().f_code.co_name)
        self.protocol_objects = []
        self.watch_path = filepath.FilePath(path)
        self.watch_mask = mask
        self.notifier = inotify.INotify()

    def startFactory(self):
        print "calling %s.%s" % (self.__class__.__name__, sys._getframe().f_code.co_name)
        self.notifier.startReading()
        self.notifier.watch(self.watch_path, mask=self.watch_mask, callbacks=[self.inotifyEventHappened])

    def startedConnecting(self, connector):
        print "calling %s.%s" % (self.__class__.__name__, sys._getframe().f_code.co_name)

    def buildProtocol(self, addr):
        print "calling %s.%s" % (self.__class__.__name__, sys._getframe().f_code.co_name)
        new_protocol_object = TmpTell(factory=self)
        self.protocol_objects.append(new_protocol_object)
        return new_protocol_object

    def inotifyEventHappened(self, watch_obj, path, mask):
        print "calling %s.%s" % (self.__class__.__name__, sys._getframe().f_code.co_name)
        for p in self.protocol_objects:
            p.announceNewFile(watch_obj, path, mask)

    def clientConnectionLost(self, connector, reason):
        print "calling %s.%s" % (self.__class__.__name__, sys._getframe().f_code.co_name)

    def clientConnectionFailed(self, connector, reason):
        print "calling %s.%s" % (self.__class__.__name__, sys._getframe().f_code.co_name)

    def removeProtocolObject(self, dead_protocol_object):
        print "calling %s.%s" % (self.__class__.__name__, sys._getframe().f_code.co_name)
        self.protocol_objects.remove(dead_protocol_object)

if __name__ == "__main__":
    from twisted.internet import reactor, inotify
    from twisted.python import filepath
    import sys
    factory = TmpTellClientFactory('/tmp', inotify.IN_CREATE)
    for port in sys.argv[1:]:
        reactor.connectTCP("localhost", int(port), factory)
    reactor.run()
