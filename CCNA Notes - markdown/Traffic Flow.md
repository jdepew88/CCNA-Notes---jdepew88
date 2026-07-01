**Cabling and Packet Flows Notes**

**Types of Communication**

Unicast – One Device speaks to one other device

Broadcast – One Device to All Devices in the network (subnet)

Ex: 192.168.1.0/24 Broadcast: 192.168.1.255 communicates to .1-.254 all at once

Multicast – One Device to Some / Many Devices (but not all)

Only devices that “subscribe” to the multicast address will receive it

224.0.0.5 - IPv4 multicast address for All OSPF routers

Bus Network

![](data:image/png;base64...)

Comp A Comp B Comp C Comp D

{\_\_|\_\_\_\_\_\_\_\_\_\_\_|\_\_\_\_\_\_\_\_\_\_|\_\_\_\_\_\_\_\_\_\_\_|\_\_\_\_}

| represents coupler {+} represent Terminators

Weaknesses:

Baseband Network, i.e., 1 signal at a time, break the cable break the whole network

Baseband – only one signal per wire

10base5 – Called Thicknet (due to thickness of ethernet cables for this spec)

10base2 – implies 10 Mbps shared between all devices in a segment

Because of collisions, you would really only get 30% to 40% of total bandwidth

Terminators – Used at the end of the cable in a bus config to be sure signals do not bounce back, but rather just disappear

CSMA/CD is Carrier Sense Multiple Access / Collision Detection

CS: Carrier Sense: Detects if any port is transmitting data

MA: Multiple Access:

CD: Collision Detection:

If a device recognizes a collision has occurred, it may send a back of jamming signal to indicate a collision has occurred, then the device waits a set amount of time (Called a back off delay) before sending again.

Probability of collisions becomes greater as the cable length increases and the number of devices on the network increase.