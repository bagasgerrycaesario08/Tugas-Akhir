#!/usr/bin/env python
from mininet.topo import Topo
from mininet.log import setLogLevel, info
class MyTopo( Topo ):
   def addSwitch(self, name, **opts ):
     kwargs = { 'protocols' : 'OpenFlow13'}
     kwargs.update( opts )
     return super(MyTopo, self).addSwitch( name, **kwargs )
   def __init__( self ):
    "Create MyTopo topology..."

     # Inisialisasi Topology
     Topo.__init__( self )
     # Tambahkan node, switch, dan host
     info( '*** Add switches\n')
     s1 = self.addSwitch('s1')
     s2 = self.addSwitch('s2')
     s3 = self.addSwitch('s3')
     info( '*** Add hosts\n')
     h1 = self.addHost('h1', ip='10.1.0.1/24')
     h2 = self.addHost('h2', ip='10.1.0.2/24')
     h3 = self.addHost('h3', ip='10.1.0.3/24')
     h4 = self.addHost('h4', ip='10.1.0.4/24')
     h5 = self.addHost('h5', ip='10.1.0.5/24')
     h6 = self.addHost('h6', ip='10.1.0.6/24')


     info( '*** Add links\n')
     self.addLink(s1, s2)
     self.addLink(s1, s3)
     self.addLink(s2, s3)
     self.addLink(s1, h1)
     self.addLink(s1, h2)
     self.addLink(s2, h3)
     self.addLink(s2, h4)
     self.addLink(s3, h5)
     self.addLink(s3, h6)
topos = { 'mytopo': ( lambda: MyTopo() ) }