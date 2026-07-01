**IPv6 Routing Protocols**

IPv6 uses a different address structure, so the Routing Protocols for IPv4 cannot be used with IPv6

**IPv6 Routing Types:**

* **Static**
* **RIPng (RIP Next Generation) [RFC2080]**
* **OSPFv3 [RFC2740]**
* **IS-IS for IPv6**
* **MP-BGP4 - Multi-protocol Border Gateway Protocol version 4 [RFC 2545/2858]**

**Supports Multiple Protocols; including IPv4, IPv6, and VPN v4**

* **EIGRP for IPv6**

**Before you can enable any IPv6 routing protocol you need to enable IPv6 routing**

**R1(config):ipv6 unicast-routing**

**RIP ng**

**Notes**

**Similar to RIP under IPv4**

* **Distance Vector RP**
* **Radius of 15 hops (16 is set to infinity)**
* **Split Horizon and Poison Reverse**
* **Based on RIPv2**

**Updates for RIPng**

* **Supports the IPv6 prefix, next hop addresses are set to the IPv6 address**
* **Uses a multicast group of FF02::9 (the all RIP routers multicast group) as the destination for RIP updates**
* **IPv6 is used for the transport of RIP updates**
* **RIPng sends updates on UDP port 521**

**Commands in IOS for RIPng**

**Step 1: Enable IPv6 unicast-routing**

**The command “ R1(config)# ipv6 unicast-routing “ is required to enable IPv6 before any routing protocol is configured**

**To enable RIPng, you will need to use a string to identify the RIP process**

**R1(config)ipv6 router rip \_\_\_\_ (blank is WORD – User selected string identifying this process)**

**R1(config)ipv6 router rip RIPNG01**

**(For instance, RIPNG01 will be the name of the RIP process in this RIP Process)**

**R1(config-rtr)#int f0/0**

**R1(config-if)#ipv6 rip RIPNG01 enable**

**This command is copied to all interfaces that you want routed through RIPng, do the same for the interfaces on a separate router, however change the name of the Process ID**

**R2(config)#ipv6 router rip RIPNG02**

**R2(config-rtr)#int f0/0**

**R2(config-if)#ipv6 rip RIPNG02 enable**

**To see your Routing Table with IPv6 type: R1#show ipv6 route**

**RIPng and other routing protocols designed for IPv6 use the link-local addresses to advertise routes. They do NOT use the global unicast address**

**OSPFv3 (i.e. OSPF for IPv6)**

**Be sure to enable Ipv6 unicast-routing**

**R1(config)#ipv6 router ospf 1**

**If there is no ipv4 address assigned to an interface on the router that you are attempting to enable OSPFv3 on, you will get an error message stating the OSPFv3 process cannot identify a Router-ID. So you will need to configure that manually or add a ipv4 address to at least one interface. The router-id needs to be in IPv4 format (x.x.x.x).**

**Despite the error (re: router-id), you will still enter router config mode for the OSPF process number you just supplied.**

**To add interfaces to the OSPF process, go into the interface config mode for a specific interface and then enter a command to assign OSPFv3 to a specific OSPF process and assign an area**

**R1(config)#int se 0/0/0**

**R1(config-if)#ipv6 ospf 1 area 0**

**Go to the next interface and do the same**

**R1(config)#int g0/0**

**R1(config-if)#ipv6 ospf 1 area 1**

**Then go to the next router and apply OSPF to individual interfaces**