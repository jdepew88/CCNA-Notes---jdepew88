Frame and Packets

PDU (Protocol Data Unit) - single unit of information transmitted among peers on a network

L1 – Bits

L2 – Frames

L3 – Packets

L4 – Segments/Datagram

L5-L7 - Data

802.3 Frame

![](data:image/png;base64...)

![](data:image/png;base64...)

What is the default aging timer value on Cisco switches? 300 Seconds

Look up what this timer does

the offset field is the IPv4 header field used when packets are fragmented.

The flow label IPv6 header field can be used to label a set of packets belonging to the same flow and does not contain DSCP markings.

IP Packet Anatomy

![](data:image/png;base64...)

TCP – 3 way handshake –

**TCP Header**

* **destination** port: is the sequence of the called port (16 bits)
* **window** size: is the sequence of the data amount the destination can accept (16 bits)
* **flags**: are control bits (9 bits)

FIFO

**store-and-forward switching method**

NETCONF
REST

**cyclic redundancy check (CRC)**

A cyclic redundancy check is used to generate a CRC value for the FCS field

The FCS field value is computed as a function of the contents of the *destination address, source address, type, and data and padding fields* of the Ethernet frame, in other words, on **all Ethernet frame fields except the FCS field (why no FCS field cuz it’s the field we are calculating.**

**SNMP Messages**

**From agent to manager –** InformRequest, Response, Trap

**From Manager to Agent** - GetRequest, GetNextRequest and SetRequest

Syslog

Syslog message logging to the console terminal is enabled by default.

Syslog Levels

0 Emergency

1 Alert

2 Critical

3 Error

4 Warning

5 Notice

6 Information

7 Debugging

**What are two field names corresponding to the IPv4 header field and the IPv6 header field that contain Differentiated Services Code Point (DSCP) markings?**

High-level summary of the three QoS models to be discussed: Best Effort, IntServ, and DiffServ; with emphasis on DiffServ

Which Cisco DNA Center tool shows source IP addresses, destination IP addresses, source ports, and destination ports?