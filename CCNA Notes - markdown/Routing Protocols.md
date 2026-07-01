Udemy Course – Routing Notes

Routed vs Routing

**Routed**

* Carries user data/information (e.g., ipv4/ipv6)
* Each router (along a given path) makes independent decisions in determining path

Ipv4

Ships in the night – what is happening on one ship is different from another.

What is configured for ipv4 is separate and distinct from ipv6 and vic versa

**Static Routes**

* Admin manually enters the route
* There is no overhead, as there would be with a routing protocol such as RIP.

(RIP sends its entire routing table every 30 seconds)

* Manual updates required when a topology changes.
* Not scalable in larger topologies

***Default Static Route*** (Candidate default route) – a static route that sets a gateway of last resort, so if a ping is made outside of the routes listed in your routing table, the device named as the gateway of last resort will field that traffic.

Setting an interface that is on the edge of the network (closest to the internet) to a static route of 0.0.0.0 0.0.0.0 (next hop ip address – in my case the ip add of the pfSense Router) will create a link to the internet, allowing all ip through to pfSense which then connects to ATT Gateway, which then connects to ATT ISP router.

**Dynamic Routes**

Uses a routing protocol (RIP, EIGRP, OSPF, ISIS, BGP)

Automatically adjust based on topology changes or traffic changes

Exchange network information with each other

Learn and maintain routes by exchanging routing updates

OSPF uses link-state updates to advertise info about routes available on the topology.

Can be enabled with a few commands.

More overhead for the routers (updates related to routing protocol sent all the time)

Less work for the network admin (would be too much work to manually update static routes)

Can automatically learn about any new network

Best Routes

Routing Protocols use different criteria to determine the best path to a destination

* Static Routes – the admin would decide
* RIP = hop count
* OSPF = bandwidth
* EIGRP = bandwidth and delay (Cisco Proprietary)

**AS** (*autonomous system)* – a grouping of networks under a single administrative domain

**Various IGPs** (Interior Gateway Routing Protocols) can be used within an AS.

Such as RIP, EIGRP, OSPF

**EGPS** (Exterior Gateway Routing Protocols) are used between Autonomous Systems

Such as BGP

Autonomous System Numbers – AS members are assigned a number to register

Before you would connect to the internet using BGP, you would need to be assigned a AS# by the AS admin, who registers membership

AS 1 (ATT ISP) ----🡪 connects via BGP ---🡪 to AS 2 (Verizon ISP)

ATT may run OSPF as there EGP while Verizon runs ISIS as there EGP

There are private AS numbers, that can be used without registration. When connecting to the internet you would need to apply for a publicly registered AS Number.

Public Autonomous System Number

Private Autonomous System Number

**Types of Routing Protocols**

**Distance Vector**

Uses hop count as its metric to determine the best path to a destination

“Routing by rumor” – only know what neighbors tell them

Determines the direction (next-hop address) and distance to destination (vector of distance)

* Uses vectors of distance/direction
* Vector for Distance is ***hops***
* Vector for Direction is ***next hop router***
* RIP uses hop count to determine the direction and distance
* Easy to configure
* Very limited visibility – only know what neighbors tell them
* Uses the Bellman-Ford algorithm:

RIP advertises entire routing table every 30 sec, sends triggered update when topology changes

Routers advertise routes as a vector of distance (local exit int and next-hop address) and direction (metric = hop count)

Mechanisms/features used to stop routing loops

* Split-horizon
* Poison reverse
* Triggered updates

• Metric changes for better or worse

• Update is sent before timer expires

• This allows our routing table to have a fresher route

**Link State**

* Visibility of entire network (or area)
* Each router builds its own internal map of the network topology
* Can make a much more informed decision about how to get to the destination network
* OSPF uses cost (routing metric based on bandwidth)
* Each router originates information about itself, its directly connected links, and the state of those links (up/down), this information is passed to other routers, and each router makes its own copy of the routing table (topological database) OSPF command: show ip ospf lsdb
* Uses an algorithm called Shortest Path First (SPF) (used by OSPF and ISIS)
* Every router constructs a map of the connectivity to a network in the form of a graph
* Better visibility of the network, therefore better routing decisions
* More difficult to configure, require a hierarchical network topology (Backbone area and multiple other areas)
* Requires more memory and processing power (as it maintains multiple routing tables; such a neighbor table, a link state database table (LSDB) and routing table)

**Advanced Distance Vector**

**EIGRP** – a hybrid routing protocol with combined elements of both distance vector and Link State into a single routing protocol. This definition isn’t entirely true though.

Forms neighbor relationships (like LS routing protocols)

Easy to configure (as few as two commands)

Cisco Proprietary

**Administrative Distance**

Believability factor of a route

Which protocol will the router listen to if OSPF says the destination is off Int g0/0, but EIGRP says the destination is off int g0/1? Administrative Distance is used as a tie breaker to determine which direction to send traffic. The lowest administrative distance is more “believable” and that route is inserted into the RIB (routing information base) (aka the routing table).

EIGRP has a lower AD than OSPF (internal EIGRP = 90 while OSPF = 110)

Takes bandwidth and delay into account when determining best path

![](data:image/jpeg;base64...)

**Classful Routing Protocols**

Do not advertise subnet mask, consistency of subnet mask assumed

Example:
10.0.0.0 (no subnet mask or CIDR notation) (is that a /8 or a /24?)

Autosummarization: summarizes routes across classful boundaries

consistency of subnet mask assumed (the same mask is used throughout the network)

Not used in today’s networks

Example of a classful routing protocol: RIP v1 and IGRP

**Classless Routing Protocols**

Do advertise subnet mask

10.0.0.0/24 or 10.0.0.0/30

Supports VLSM (Variable Length Subnet Mask) - /30 mask on point-to-point link /24 on ethernet segment

Summary routes can be manually configured

Example:
OSPF supports summarization on ABRs (Area Border Routers)

EIGRP supports summarization on any interface – it acts as a classful routing protocol and automatically summarize along /8 /16 /24?

Administrative Distance vs Mask Length

R1 (10.1.1.0 /27)--------------🡪 RIPv2 (10.1.1.0/27) (AD 120) ---🡪

R2 (10.1.1.32/27)--------------🡪 BGP (10.1.0.0/16) (AD 200) ----🡪 R4 (10.2.0.0/27)

R3 (10.1.1.64/27)--------------🡪 OSPF (10.0.0.0/8) (AD 110) ----🡪

ping sent to 10.1.1.1 which routing protocol will be listened to

Answer: has nothing to do with AD as mask length (longest match) take priority

RIPv2 to 10.1.1.0/27 will take priority as it has the longest match to10.1.1.1

Classful Routing Protocols

Benefits of Link State Routing

* Fast Convergence
  + Changes reported immediately
* Robustness against routing loop
* Routers know topology
* Link state packets are sequenced and acknowledged
* Hierarchical design enables optimization of resource
* Can scale to much larger environments that DV routing protocols

Downsides of Link State Routing

High system over head (CPU and RAM)

RAM:

Uses 3 tables:

* adjacency (peer or neighbor table),
* topology (link state database [LSDB]),
* forwarding table (Routing Table)

CPU:

Uses Dijkstra’s algorithm (aka the Shortest Path First Algorithm) which can be processor intensive

Require strict designs (Area 0 always required when there is more than one area)

Configuration and design can be complex

Static Routing

Using next hop

R1(config)#ip route 192.168.3.0 255.255.255.0 (next hop address)

R1 is directly connected to Router 2 on the 192.168.2.0/24 subnet, R1 = x.x.2.1 R2 = 192.168.2.2

R1(config)#ip route 192.168.3.0 255.255.255.0 192.168.2.2

R2 is in between R1 and R3

If Router 3 does not know how to get back to R1 – pings will fail

R3 is directly connected to Router 2 on the 192.168.3.0/24 subnet R3: 3.2 R2:192.168.3.1

R3 thusly needs a static route back to Router 1’s 192.168.1.0 subnet

R3(config)#ip route 192.168.1.0 255.255.255.0 192.168.3.1

Now Router 1 and Router 3 are aware of each other’s respective subnets and use interfaces on R2 to forward the packets

Show IP routing table

![Text  Description automatically generated](data:image/jpeg;base64...)

Notice the Brackets after 192.168.3.0/24 on the last line, the [1/0]

[1/0] = [administrative distance / path cost]

Note the AD default = 1 and the Cost default = 0