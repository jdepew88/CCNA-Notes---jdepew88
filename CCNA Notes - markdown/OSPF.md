OSPF Notes – David Bombal Course

Open Shortest Path First

Based on the Dijkstra algorithm created in 1959

OSPF is a Link State Routing Protocol

Link State Advertisements (LSAs) are

\

Overview

OSPF – Link State running protocol

Link – Router Interface

State – description of an interface and its relationship to neighboring devices

(IP address, subnet mask, type of network, and the routers that are connected to that network)

Collection of all link states form topological database or Link State Database (LSDB)

Creates neighbor relationship using Multicast to 224.0.0.5 or unicast.

LSAs are flooded throughout the network or “Area” and the LSDB is created from these Link State Advertisements (LSAs).

Uses the Shortest Path First Algorithm to determine the best path to each destination.

OSPF

Resides at Layer 3 – directly on top of IP

Does not use TCP or UDP

Protocol ID 89 (0x59)

Syncs every 30 minutes by default

![](data:image/png;base64...)

**Packet Types**

**Hello**

* dynamically discover neighbors
* **Form and Maintain** Neighbor relationships
* Default intervals
  + 10 Seconds (Broadcast segments – Ethernet)
  + 30 Seconds (Non-Broadcast segments (Serial, NBMA – Non Broadcast Multi Access (frame relay))\
* Dead timer

4 times the hello interval by default (IOS will change dead interval automatically when changing hello timer

**Database Description (DD/DBD)**

Used to exchange brief versions of each LSA

**Link State Request (LSR)** – sent by a router missing information within its LSDB

An LSR requests full LSA information (as opposed to the brief info contained in a DBD)

**Link State Update (LSU)**

Contains LSAs

Typically sent in response to an LSR

**Link State Acknowledgements (LSAck)**

Confirms receipt of an LSU Message

OSPF Hierarchy

Autonomous Systems (AS) – a grouping of routers under a common administrative domain

IGP (Interior Gateway Protocol) – Used within a single AS

![](data:image/png;base64...)

For scalability OSPF is broken into Areas. Cisco recommends no more than 50 Routers in an OSPF Area

OSPF Area 0 – This is the backbone area, always needed if there is to be more than one OSPF Area

Using multiple Areas can be used to make the network more efficient by optimizing summarization and reduce routing table updates and link state advertisements

Area Border Routers (ABRs) – Routers that sit on the border between one or more OSPF Areas

An advantage of ABRs they allow for summarization of routers

Area 1 has routes between 10.1.1.0/24 to 10.1.100.0/24 Summarized as 10.1.0.0/16

Area 2 has routes between 10.2.1.0/24 to 10.2.100.0/24 Summarized as 10.2.0.0/16

Area 3 has routes between 10.3.1.0/24 to 10.3.100.0/24 Summarized as 10.3.0.0/16

![](data:image/png;base64...)

This router is known as an ASBR

Autonomous System Border Router

Borders two AS’s

RIP on the Left and OSPF on the Right

Backbone Routers

All 6 of the Routers withing Area 0 above are known as Backbone Routers as they reside within OSPF Area 0 (The backbone Area)

![](data:image/png;base64...)

When traffic is sent from one area to another Area it has to traverse the backbone area to do so

![](data:image/png;base64...)

Internal Routers

They are internal to their internal areas

**OSPF network Types: Broadcast, Non-Broadcast, Point-to-Point**

**Broadcast** – the default network type for Ethernet and FDDI (Fiber) connections.

DR/BDR election occurs. Multicasts are sent (thus no need for neighbor cmd)

Hello: 10 Dead: 40

Cmd: R1(config-router)#network broadcast

DROTHERs can only communicate with DR/BDR routers, no with other DRothers

**Non-Broadcast –** default network type for Frame Relay and X.25 (Frame Relay predecessor)

DR/BDR election occurs. No Multicasts (thus there is a need for the neighbor cmd)

Hello: 30 Dead: 120

Cmd: R1(config-router)#network non-broadcast

**Point-to Point** – default network type for PPP and HDLC

No DR/BDR election. Multicasts sent (no neighbor cmd)

Hello: 10 Dead: 40

Cmd: R1(config-router)#network point-to-point

**Point-to Multipoint –** non broadcast network

No DR**/**BDR election, no multicasts, (yes neighbor cmd)

Hello: 30 Dead: 120

**OSPF uses Hello Packets to form Neighbor Adjacencies**

The Hello protocol establishes and maintains neighbor relationships by ensuring bi-directional communication between neighbors. Bi-directional communication occurs when a router recognizes itself in a hello packet received from a neighboring router

Hellos are sent using multicast address 224.0.0.5, and contain the following information \

These parameters have to match for an Adjacency to form

Hello and Dead Timer intervals, Area ID, Auth Password, and Stub Area Flag

![](data:image/png;base64...)

**OSPF Process ID**

R1(config)#router ospf ? (1-65535) (Process ID)

Process ID allows for multiple OSPF instances to run on the same router, this can become important in multi-protocol label switching (MPLS) environments

Router ID – Defaults to the highest IP Address on any active physical interface when OSPF was enabled or will default to the highest loopback interface when OSPF was enabled.

Recommended to set the Router ID (RID) manually to avoid an interface going down from changing the RID

Further recommended to set the RID to one of the loopback interfaces

Designated Routers

DR – used to broadcast in multi access environments

What would happen if r1 goes down and there is no DR?

Without a DR each of these routers would have a full adjacency to each other, meaning LSAs are exchanged between routers 5 times more than necessary. R1 to else, R2 to else, R3 to else, etc.

![](data:image/png;base64...)

All of these extra LSAs being sent is wasted resources and bandwidth.

With a Designated Router and Backup Designated Router, the DR would be responsible to multicast LSAs to keep the LSDB updated, should the DR go down, the BDR (Backup) would assume that responsibility. This keeps LSAs to a minimum and is thus more efficient.

**DR and BDR Election**

Criteria: Highest Priority (Default priority is 1, 0 excludes a router from the election)

(Priority Value is from 1-255) when the priority is the same the next criteria (highest RID) is used.

Highest RID (Router ID)

224.0.0.6 – multicast address for Designated Routers

Only the DR and BDR will have Full relationships to all the other routers in an OSPF Area.

Routers 4 and 5 will have a 2way relationship. They are aware of eachother, but do not communicate directly with LSUs/LSAs

DRs are chosen on a per-segment basis. Every ethernet segment requires the election of a DR and BDR

Router 4 could be a non DR/BDR in AREA 0 but could be the DR for Area 1, should it be an ABR (border)

DR and BDR election is not pre-emptive meaning that if a router has its Priority changed after the DR/BDR election, that router will not become the DR unless the OSPF area is recreated

DR OTHER – a designation for Routers that are not the DR or BDR

OSPF Algorithm – Shortest Path First

R1 will decide its best route to R2 based on its Cost

**Cost is a formula 10 ^ 8 / Bandwidth** (Reference Bandwidth = 10 ^ 8)

10^8= 100 Million aka 100 Megabit Refence bandwidth is in Megabit

RIP would approach this based on Hop Count and go from R1 to R2 directly

OSPF would go from R1 to R3 to R2 as the bandwidth considerations make that have a cost of 20 (10 + 10) vs a cost of 64 for going over the T1 connection

![](data:image/png;base64...)

You are able to change the reference bandwidth that OSPF utilizes and this is necessary when using modern Gigabit and 10 Gigabit Connections.

Within the Router settings for OSPF, use the command *auto-cost reference-bandwidth X*

(where X equals \_\_\_ number of Megabits per second). If changed to 1000 than a Gigabit link would be seen as the refence bandwidth). This command will need to be applied to all routers with a gigabit link or greater.

You can also change the cost on an interface, command: *ip ospf cost x* (where x = megabits/sec)

0![](data:image/jpeg;base64...)

![](data:image/png;base64...)

![](data:image/png;base64...)

How many DR’s?

How many BDR’s

How many DRother’s?

DR/BDR election is done on a per-segment basis but only on Broadcast multi-access or non-broadcast multi-access links. In other words, links or interfaces where you can have more than one router connected to that single segment or single subnet. A multi-access network is a segment where we have more than two routers.

* Ethernet interface is considered a multi-access network,
* serial interface is considered a point-to-point interface.

Thus the 10.1.2.0/24 (serial connection between R4 and R5 – a point-to-point connection) does not have a DR or BDR

DR/BDR Election (cont.)

To better manage LSA floods, DR is elected..

DRothers will form adjacency with DR and BDR only. DRother is a router that’s neither a DR nor a BDR.

When OSPF process started, the process will look for existing DR and BDR, if neither exists DR election starts.

During the election process the **highest priority** router wins the DR, the next highest priority wins BDR.

If all routers’ priority is **a tie, then the highest router ID** (RID) will be the tie-breaker.

OSPF Priority – default of 1. If a router has a priority of 0 it will become a DRother, cannot be a DR or BDR

To set the OSPF priority: command: R1(config-if)#*ip ospf priority (#)*

Link State Advertisement Types | LSA Types

![](data:image/png;base64...)

Type 1 – Router LSAs

Interfaces in Area 0

Type 2

Advertised by Designated Routers

Type 3 - Summary LSAs

Advertise Routes from different Areas

Type 4 – ASBR Links

Advertises routes from Autonomous System Border Routers

Type 5 - AS External Links

Comes from Outside of OSPF, in this case from EIGRP on R1

![](data:image/png;base64...)