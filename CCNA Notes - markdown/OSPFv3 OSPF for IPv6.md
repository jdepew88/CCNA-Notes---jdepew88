OSPFv3 aka OSPF over IPv6

OSPFv3 expands on version 2 to provide support for Routing IPv6 prefixes and 128 bit IPv6 addresses

OSPFv2 🡪 IPv4 Networks

OSPFv3 🡪 IPv6 Networks

OSPFv2 and OSPFv3 run independent of each other and can run simultaneously should the router be routing both IPv4 and IPv6 traffic.

The two versions of OSPF:

cannot communicate with each other

are both link-state routing protocols

use the same area design concept and terms

both check various settings before a neighbor relationship is established

both use Link-state advertisements (LSAs) and build Link-state databases (LSDBs)

networks are based on the cost of an interface (they have the same default metric based on a 100Mbps interface)

both use a 32-bit router ID to identify a router (if running a pure IPv6 network, you will have to manually set this)

In OSPFv3 there is no network command in (config-rtr), rather OSPFv3 is configured on the interface level

LSAs: Link=state advertisements differ in OSPFv3

OSPFv3 uses IPv6 link local addresses for neighbor relationships (doesn’t use unicast address), v2 uses IPV4 int ip add

OSPFv3 uses multicast address FF02::5 (all OSPF Routers) – similar to the 224.0.0.5 broadcast address in IPV4

FF02::5 (all OSPF Routers) – similar to the 224.0.0.5 broadcast address in IPV4

FF02::6 (all OSPF DR and BDRs) – similar to the 224.0.0.6 broadcast address in IPV4

OSPFv2 - IPv4 Protocol number 89

OSPFv3 - IPv6 Protocol number 89