![](data:image/png;base64...)

Point-to-Point / Serial Links (also called a leased line) provide a dedicated permanent Point-to-Point connection between 2 sites.

![](data:image/png;base64...)

![](data:image/png;base64...)

![](data:image/png;base64...)

1. When the traffic is sent across the LAN (using ethernet) the IP packet is encapsulated in an Ethernet frame.

The layer 2 encapsulation used is Ethernet

1. When the frame arrives at the router, the router will strip the layer 2 headers and then send the frame across the WAN using, for example, HDLC.

This Point-to-Point connection is configured with a layer 2 encapsulation of HDLC.

From there, the ethernet headers are removed and the original IP packet that was sent by PC1 is encapsulated in HDLC and is forwarded across the serial link to Router 2

1. When Router 2 receives the HDLC frame it strips the HDLC headers and forwards the original IP packet sent by PC1 onto the local area network using an Ethernet header, so the packet is encapsulated in Ethernet and an Ethernet frame is sent from router 2 to PC2 using ethernet.

OSI Model of WAN Technologies

![](data:image/png;base64...)

For the CCNA, focus on HDLC and PPP encapsulation rather than modern ethernet WAN connections

The physical layer will use X.21 or V.35 couplers rather than RJ-45 as is common is a LAN environment

CSU / DSU

A Channel Service Unit/Data Service Unit is a device that seats at the provider's client site used to connect the digital WAN line (Leased lines) to the client's DTE device which is usually a router.

A modem connects an analog line (phone line) to a digital device (the computer) and a CSU/DSU connects a digital line to a digital device.

The DTE would be the router and the DCE (providing clock) would be the CSU/DSU, like this:

![](data:image/jpeg;base64...)

![](data:image/png;base64...)

Telco Demarc = Telco Demarcation point – refers to the location that demarcates the ISP from the internal network and who would be responsible to solve any issues; the ISP/Telco or their customer

VPNs (Virtual Private Networks) have largely replaced deployments of leased lines.

Leased lines are an example of Synchronous Serial Communication, where one party provides the clocking

for the communication.

Two devices will synchronize their clocks before data transmission takes place. The two devices synchronize their clocks and agree on parameters for data transfer, including the data interval between bits of data.

CSU/DSU provides the clocking and is the master for the communication, the router is acting as a slave and is receiving its clocking from the CSU.

So essentially before communication can start, the two devices have to align their clocks or agree on the clock intervals to ensure that the data doesn't get corrupted.

Data Communication Equipment (DCE) enhance data transfer between Data Terminal Equipment (DTE).

Routers are referred to as DTEs, Channel Service Unit/Data Service Units (CSU/DSU) are dedicated DCEs.

Cisco Routers have embedded functionalities to act a DCEs. This is to enhance communication between the two DTEs on a Point-to-Point (serial) link.

A DTE therefore can act as DCE by clocking, while retaining its ability as a DTE.

Therefore, when two routers are connected on a point-to-point link, one must provide clocking. Configured with the interface sub-command (Config-if)# clock rate *clock\_rate\_in\_bps*, which can be verified with the command show controllers *interface*.

The CSU DSU is the DCE side of the communication and the Router is the DTE side

The Data Communication Equipment (DCE) provides clocking for the communication and is the side that Terminates the connection from the carrier.

The CSU DSU (which is the DCE) is providing clocking to the router and physically controls the speed and timing at which the router serial interfaces can send and receive bits over the serial cable.

WAN Interface Cards (WICs)

![](data:image/png;base64...)

![](data:image/png;base64...)

The advantage of using this card over an external CSU/DSU is that you have fewer devices and cables to deploy and manage.

also allows you to remotely configure monitor and troubleshoot using the well-known Cisco CLI

![](data:image/png;base64...)

Leased Line Speeds

T1 vs E1

American Standard

![](data:image/png;base64...)

![](data:image/png;base64...)

![](data:image/png;base64...)

**WAN Encapsulation**

Two main types – HDLC (High Level Datalink Control) and PPP (Point-to-Point)

HDLC (High Level Datalink Control)

Layer 2 Encapsulation

Used across a leased line providing layer 1 service or connectivity from one site to another.

![](data:image/png;base64...)

Cisco added the Type field to allow multiple higher layer protocols to traverse the link at the same time.

Indicate if its an IPV4 or IPv6 Packet

Cisco adds the “type” field to the HDLC header, whereas this is not present in the Industry standard HDLC Header

If you want to create a serial connection between a cisco router and a non-cisco router, it is suggested to change the encapsulation to PPP (the industry standard version of encapsulation)

The Type field as shown in the HDLC packet is shown in wireshark as the protocol field and this allows for HDLC to use multiple protocols (such as using both IPv4 and IPv6)

HDLC links are point-to-point thus there is no need for mac addresses

A PC (PC1) connected to R1 R1 via serial to R2 R2 to a second PC (PC2)

PC1 pings PC2

A ethernet 2 packet goes from PC1 to R1 with the IPv4 protocol and ICMPv4

R1 encapsulates the packet with HDLC and sends it to R2

R2 de-encapsultes the packet remocing HDLC and then forwards a standard eth2 packet to PC2

ICM<