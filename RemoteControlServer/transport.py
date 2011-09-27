# -*- coding: utf-8 -*-

# Copyright (c) 2010 Naranjo Manuel Francisco manuel@aircable.net
# Copyright (c) 2009 Twisted Matrix Laboratories.
# See LICENSE for details.

from twisted.conch.ssh.transport import SSHServerTransport

class ForwardTransport(SSHServerTransport):
    def connectionLost(self, reason):
        SSHServerTransport.connectionLost(self, 
            reason)
        self.avatar.logOut()
        