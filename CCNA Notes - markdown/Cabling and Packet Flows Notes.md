**Cabling and Packet Flows Notes**

![](data:image/png;base64...)Comp A Comp B Comp C Comp D

{\_\_|\_\_\_\_\_\_\_\_\_\_\_|\_\_\_\_\_\_\_\_\_\_|\_\_\_\_\_\_\_\_\_\_\_|\_\_\_\_}

| represents coupler “{“ + “}” represent Terminators

**Weaknesses:**

Baseband Network, i.e.1 signal at a time, break the cable break the whole network

Baseband – only one signal per wire

10base5 – Called Thicknet (due to thickness of ethernet cables for this spec)

10base2 – implies 10 Mbps shared between all devices in a segment, rather than 10 mbps per device. Quite slow as you add more devices

Note: Because of collisions, you would really only get 30% to 40% of theoretical max speed, so 3 to 4 megabits per second shared across the entire network

**Terminators** – Used at the end of the cable in a bus config to be sure signals do not bounce back, but rather just disappear

More weaknesses of 10Base2 Networking

Single Collision Domain

Single Broadcast Domain – so if any device sends a broadcast, that broadcast is received by every other device. Meaning every device would need to process that broadcast, wasting resources

![](data:image/png;base64...)

**CSMA/CD is Carrier Sense Multiple Access / Collision Detection**

**CS**: Carrier Sense: Detects if any port is transmitting data

**MA**: Multiple Access:

**CD**: Collision Detection:

**Traffic Flow on a Bus Topology Network (**CSMA/CD**)**

In Ethernet, when a bus topology is used, devices use what's called carrier sense, multiple access / collision detection.

This operates as follows When a device wants to send traffic, it should first check to hear if any other device is speaking so the device will not communicate onto the network.

If it hears another device that's called Carrier Sense.

**Carrier Sense** - listening on the network to hear if another device is speaking before attempting to send frames out

**Multiple access** - any device can communicate across that segment as long as no other device is communicating.

In Ethernet, we're using a distributed environment where each device can independently communicate across the network without permission from other devices.

However, a device should only send traffic if no other device is speaking, and that's because we want to avoid collisions in an Ethernet environment.

**Collisions**

**Since this is a baseband network (as opposed to broadband), only one signal is allowed through the network at any given time. Should two signals be traversing the line simultaneously, a collision will occur.**

When a device detects that a collision has taken place, it may send a **back off or jamming signal** to indicate that a collision has taken place and to wait a given period of time (Called a **back off delay)** before sending again.

Probability of collisions becomes greater as the cable length increases and the number of devices on the network increase.

Terminators are used at the ends of a bus topology to ensure that signals do not bounce back and cause more collisions.

MAC Addresses

![](data:image/png;base64...)![](data:image/png;base64...)

**Unicast Traffic** - is a conversation between two devices where one device is sending

the traffic and the other device is receiving the traffic.

So device A is talking to device B.

**Multicast Traffic** is where one device is sending traffic to multiple devices that have subscribed

to the multicast.

**Unicast Traffic** – has the Last Bit of the first Octet of the OUI set to a “0”

**Multicast Traffic** – has the Last Bit of the first Octet of the OUI set to a “1”

When multicast traffic is received by a layer two switch, that traffic is flooded out of all ports,

whereas unicast traffic is typically not flooded.

10 Base T networking

Modern Standard – 10 Base 2 is deprecated\

* 10 Base T or “Twisted Pair Ethernet” refers to the use of cable that contains insulated copper wire, twisted together is pairs
* Has a max distance of 100 meters.
* cable is much thinner and more flexible, as compared with coaxial wire (used is 10-base-2 + 10-base-5 networks)
* tends to use unshielded twisted pair cables
* also uses shielded twisted pair cables in noisy environments where there’s a shield around each pair of wires and another shield around all four pairs of wire
* this shielding protects the signal from excessive electrical and magnetic interference

![](data:image/png;base64...)

T568A and T568B will both result in a straight through cable, meaning that pin 1 on both ends of the cable will match, as will pins 2 through 8.

![](data:image/png;base64...)

in a standard straight through cable, each pin of the connector on one end is connected to the corresponding pin on the other connector.

MDI – Media Independent Interface – an ethernet port connection typically used on network interface cards (NICs) of PCs. MDI is also used by routers and can be used on uplink ports on Ethernet switches

On certain older switches you’ll see a button normally on the uplink port that allows you to change how that port operates, so you can change the port to MDI or MDIX or back again.

This allows you to connect from one switch to another using a straight through cable as opposed to using a crossover cable.

Straight-through cables are used in situations where you connect a PC to a switch/bridge/hub.

IN the past, when connecting devices of the same type, such as two PCs or two routers, a crossover cable would be used.

![](data:image/png;base64...)

In the example above, two MDI devices (2 PCs) are connected via a crossover cable.

Pin 1 (Side A) TX+ goes to Pin 3 (Side B) Rx+

Tx (Transmits) and Rx (Recive) are correctly cabled so one side is receiving what the other is transmitting and vice versa

![](data:image/png;base64...)

Note: The gigabit standard requires all 8 wires be used

In the past you would have to know when to use a crossover cable vs a straight-through cable

Auto MDI / MDIX

Introduced in 1998 and mage the requirement for crossover cables obsolete

MDI devices are typically routers or PCs

MDIX devices are typically switches or hubs, so they are “medium dependent interface crossover devices.

In the past, you would need to connect an MDI device (PC) to a switch or hub. Certain ports would have a button to flip the role from MDIX to MDI, which would allow you to connect a switch to a switch using a straight through cable (rather than needing a crossover cable)

Today, Auto-MDI allows for automatic switching once the cable is connected. Note: you may run into older switches in the real world that do not support auto mdi

![](data:image/png;base64...)

![](data:image/png;base64...)

![](data:image/png;base64...)

![](data:image/png;base64...)

![](data:image/png;base64...)

![](data:image/png;base64...)

Connect from a serial port (outdated – often using a serial-to-usb adapter today) to the Console port on a CISCO device (hub, router, switch)

You can also use USB to connect to the Console Port

**Single-Mode Fiber**

Multi-Mode Fiber