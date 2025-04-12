#!/usr/bin/python3
"""
Custom topology for the network loop assignment:
 - 4 switches (s1, s2, s3, s4)
 - 8 hosts (h1 to h8) with IP addresses:
     h1: 10.0.0.2/24, h2: 10.0.0.3/24,
     h3: 10.0.0.4/24, h4: 10.0.0.5/24,
     h5: 10.0.0.6/24, h6: 10.0.0.7/24,
     h7: 10.0.0.8/24, h8: 10.0.0.9/24
 - Switch-to-switch links (7ms delay):
     s1-s2, s2-s3, s3-s4, s4-s1, s1-s3
 - Host-to-switch links (5ms delay):
     h1, h2 → s1; h3, h4 → s2; h5, h6 → s3; h7, h8 → s4
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.node import  OVSController# Use the OVSController that comes with Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel

class LoopTopo(Topo):
    def build(self):
        # Create four switches.
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        # Create eight hosts with specified IP addresses.
        hosts = {
            'h1': self.addHost('h1', ip='10.0.0.2/24'),
            'h2': self.addHost('h2', ip='10.0.0.3/24'),
            'h3': self.addHost('h3', ip='10.0.0.4/24'),
            'h4': self.addHost('h4', ip='10.0.0.5/24'),
            'h5': self.addHost('h5', ip='10.0.0.6/24'),
            'h6': self.addHost('h6', ip='10.0.0.7/24'),
            'h7': self.addHost('h7', ip='10.0.0.8/24'),
            'h8': self.addHost('h8', ip='10.0.0.9/24')
        }

        # Define link options.
        host_link_opts = dict(delay='5ms')
        switch_link_opts = dict(delay='7ms')

        # Add host-to-switch links.
        self.addLink(hosts['h1'], s1, cls=TCLink, **host_link_opts)
        self.addLink(hosts['h2'], s1, cls=TCLink, **host_link_opts)
        self.addLink(hosts['h3'], s2, cls=TCLink, **host_link_opts)
        self.addLink(hosts['h4'], s2, cls=TCLink, **host_link_opts)
        self.addLink(hosts['h5'], s3, cls=TCLink, **host_link_opts)
        self.addLink(hosts['h6'], s3, cls=TCLink, **host_link_opts)
        self.addLink(hosts['h7'], s4, cls=TCLink, **host_link_opts)
        self.addLink(hosts['h8'], s4, cls=TCLink, **host_link_opts)

        # Add switch-to-switch links forming the loop and a diagonal.
        self.addLink(s1, s2, cls=TCLink, **switch_link_opts)
        self.addLink(s2, s3, cls=TCLink, **switch_link_opts)
        self.addLink(s3, s4, cls=TCLink, **switch_link_opts)
        self.addLink(s4, s1, cls=TCLink, **switch_link_opts)
        self.addLink(s1, s3, cls=TCLink, **switch_link_opts)

def run():
    topo = LoopTopo()
    # Create the network with the OVSController.
    net = Mininet(topo=topo, link=TCLink, controller=OVSController)
    net.start()
    print("Network started. You are now in the Mininet CLI. Use 'exit' to stop.")
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()