#!/usr/bin/env python

# Copyright (c) 2009 Twisted Matrix Laboratories.
# See LICENSE for details.

from twisted.conch.ssh import transport, userauth, connection, common, keys, channel
from twisted.internet import defer, protocol, reactor
from twisted.internet import reactor
from twisted.python import log
import struct, sys, getpass, os

#USER = 'cesar'  # replace this with a valid username
HOST = 'localhost' # and a valid host
debug = 1
class SimpleTransport(transport.SSHClientTransport):
    '''
    SSHClientTransport handles the negotiation of encryption 
    and the verification of keys for you
    '''
    
    def verifyHostKey(self, hostKey, fingerprint):
        '''
        This method is called with two strings: 
        the public key sent by the server and its fingerprint
        '''
        if debug: print 'At verifyHostKey'
        print 'host key fingerprint: %s' % fingerprint
        return defer.succeed(1) 

    def connectionSecure(self):
        '''
        '''
        if debug: print 'At connectionSecute'
        self.requestService(
            SimpleUserAuth(os.getlogin(),
                SimpleConnection()))

class SimpleUserAuth(userauth.SSHUserAuthClient):
    def getPassword(self):
        if debug: print 'At getPassword'
        
        return defer.succeed(getpass.getpass("%s@%s's password: " % (os.getlogin(), HOST)))

    def getGenericAnswers(self, name, instruction, questions):
        if debug: print 'At getGenericAnswers'
        
        print name
        print instruction
        answers = []
        for prompt, echo in questions:
            if echo:
                answer = raw_input(prompt)
            else:
                answer = getpass.getpass(prompt)
            answers.append(answer)
        return defer.succeed(answers)
            
    def getPublicKey(self):
        if debug: print 'At getPublicKey'
        
        path = os.path.expanduser('~/.ssh/id_dsa') 
        # this works with rsa too
        # just change the name here and in getPrivateKey
        if not os.path.exists(path) or self.lastPublicKey:
            # the file doesn't exist, or we've tried a public key
            return
        return keys.getPublicKeyString(path+'.pub')

    def getPrivateKey(self):
        if debug: print 'At getPrivateKey'
        
        path = os.path.expanduser('~/.ssh/id_dsa')
        return defer.succeed(keys.getPrivateKeyObject(path))

class SimpleConnection(connection.SSHConnection):
    def serviceStarted(self):
        if debug: print 'At serviceStarted'
        
        self.openChannel(TrueChannel(2**16, 2**15, self))
        self.openChannel(FalseChannel(2**16, 2**15, self))
        self.openChannel(CatChannel(2**16, 2**15, self))

class TrueChannel(channel.SSHChannel):
    name = 'session' # needed for commands

    def openFailed(self, reason):
        print 'true failed', reason
    
    def channelOpen(self, ignoredData):
        self.conn.sendRequest(self, 'exec', common.NS('true'))

    def request_exit_status(self, data):
        status = struct.unpack('>L', data)[0]
        print 'true status was: %s' % status
        self.loseConnection()

class FalseChannel(channel.SSHChannel):
    name = 'session'

    def openFailed(self, reason):
        print 'false failed', reason

    def channelOpen(self, ignoredData):
        self.conn.sendRequest(self, 'exec', common.NS('false'))

    def request_exit_status(self, data):
        status = struct.unpack('>L', data)[0]
        print 'false status was: %s' % status
        self.loseConnection()

class CatChannel(channel.SSHChannel):
    name = 'session'

    def openFailed(self, reason):
        print 'echo failed', reason

    def channelOpen(self, ignoredData):
        self.data = ''
        d = self.conn.sendRequest(self, 'exec', common.NS('cat'), wantReply = 1)
        d.addCallback(self._cbRequest)

    def _cbRequest(self, ignored):
        self.write('hello conch\n')
        self.conn.sendEOF(self)

    def dataReceived(self, data):
        self.data += data

    def closed(self):
        print 'got data from cat: %s' % repr(self.data)
        self.loseConnection()
        reactor.stop()

protocol.ClientCreator(reactor, SimpleTransport).connectTCP(HOST, 22)
reactor.run()