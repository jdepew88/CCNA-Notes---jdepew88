IPv6 Notes – Bomball Course

Ipv6 created due to exhaustion of IPv4 addresses. There are 4,294,467,295 IP addresses available in IPV4

128 bits in length (16 octets) – ipv6 There are 3.4 x 10 ^ 38 addresses in IPv6

32 bits in length (4 octets)– ipv4

![](data:image/png;base64...)

OSI Model

The network layer has been changed

IPv6 – 128 bits

IPv4 – 32 bits

Everything else is essentially the same.

127.0.0.1 – ipv4 loopback

“::1” – ipv6 loopback - ::1 is the same as 0:0:0:0:0:0:0:1

Format of IPv6 address

* X:X:X:X:X:X:X:X where X is a 16 bit hexadecimal field
* Case insensitive
* Leading Zeroes are optional
* Successive fields of zeros can be represented as :: (but only once per address) (algebraic placement, if you had double colon twice you would be uncertain of where the zeros start and stop in the uncompressed format of the address

Example

![](data:image/png;base64...)

* In a URL, enclose the IPv6 address in brackets
  + http://[2001:123:56+8::8]:8080/index.html
* Cumbersome for users
* Mostly for diagnostic purposes
* Use of fully qualified domain names FQDN’s are recommended

IPv6 Address Types

* Unicast
  + There is no need for NAT in IPv6, (NAT was introduced to try to conserve IPv4 addresses)
  + (each IPv6 address is globally unique)
  + Multiple Addresses for a single interface
  + Several types
    - Global unicast address (each address is globally unique and routable
      * No need for NAT in IPv6
    - Reserved unicast address
    - Link Local unicast address
      * Routers do not forward link local addresses
      * Two hosts to communicate with each other without the need for manual designation or a dhcp server. Good for router discovery
      * Many IPv6 routing protocols use link-local addresses to communicate with eachother
      * Site local unicast address (addresses assigned to an entire site within an organization) (only valid within the site network of an organization) (Site Local unicast addresses have been deprecated since September 2004, replaced with “unique local addresses”)
      * **Which IPv6 address type provides communication between subnets and cannot route on the Internet?**
      * A IPv6 Unique Local Address is an IPv6 address in the block FC00::/7. It is the approximate IPv6 counterpart of the IPv4 private address. It is not routable on the global Internet. Note: In the past, Site-local addresses (FEC0::/10) are equivalent to private IP addresses in IPv4 but now they are deprecated.
      * Special purpose unicast
        + Unspecified (:: - used when a device does not know its own IP address, used in the source field of a datagram which is sent by a device when said device seeks to have an ip address configured)
        + Loopback (::1) - same as 127.0.0.1 (ipv4 loopback)
        + IPv4 compatible – allows for the representation of an IPv4 address within IPv6, the most significant 96 bits would be set to 0 and the remaining 32 bits are the ipv4 address being represented) (Deprecated in 2006)
* Multicast
  + One-to-many
  + Enables more efficient use of the network
  + Uses a larger address range
  + The advantage of multicasting is that a single stream from a single server can go to many devices. (e.g. 100 devices can receive the same video stream from 1 MBPS rather than having 100 streams each at 1 MBPS)
* Anycast
  + One to nearest (allocated from unicast address space)
  + unicast address is used, but the same address is configured on two or more devices
  + Multiple devices share the same address
  + All anycast nodes should provide uniform service
  + Routers decide on closest device to reach destination
    - Example servers in New York and LA – each have the same IP address. The server that is closest to the source request is the server that would be used to serve the information
  + Suitable for load balancing and content delivery services

Where are Broadcast Addresses in IPv6?

They don’t exist.

Broadcasts cause issues and as such Broadcasting has been replaced by Multicasting in an IPv6 environment.

We send a multicast if we want to contact multiple devices, rather than a broadcast (as in IPv4 environment).

**IPv6 Unicast Addresses**

* 128 bits in length
* The **Network prefix is the first 64 bits** and the **Interface Identifier is the Last 64 bits**.
* **There is no subnetting in IPv6 as there is in IPv4.**
* Each Link or Interface (when using a unicast address) will have a **mask of a /64** in an enterprise environment.
* There is no NAT in IPv6.
* Addresses in organizations use what are called “Aggregateable Global Unicast Addresses”,
  + There is no need to NAT as these addresses are like public addresses in that they are globally unique
  + Aggregate-able indicates that they can be aggregated or summarized in the global internet. The designers of IPv6 had specifically looked into aggregation of addresses to reduce routing table sizes within the global internet
  + Interface ID can use a Modified EUI-64 format

A Modified EUI-64 format is essentially a modified Mac Address used to create an IPV6 IP address

The EUI address (MAC address modded into IPv6 address) allows us to get the interface ID portion of an IPv6 Address

the interface ID portion of an IPv6 Address is the last 64 bits, aka the host bits

An Ethernet MAC address is only 48bits in length whereas the Interface ID is 64 bits in length

FF FE (16 bits )is inserted into the middle of a MAC address to take the 48 bit address and make it 64 bits long

![](data:image/png;base64...)

This address is written in hexadecimal because IPV6 addresses are written in Hexadecimal

Each two hexadecimal values equate to 8 binary bits

![](data:image/png;base64...)

The U/L bit – 7th bit in the first hextet. Represents uniqueness or lack there of U=unique= 1 L=LackofUnique=0

* This is the second step of the Modified EUI-64 Format – representing whether the address is globally unique
* 000000x0 where x = 1 is unique (globally managed) , if x = 0 it is not unique and is locally managed
* The second step consists of setting the 7th bit of the 64 bit address, this bit identifies the 48 bit MAC addresses uniqueness or lack thereof.
* It is either globally managed or locally managed.
* Globally managed means that you use the vendor mac address.
* Locally managed means that you rewrote the mac address with your own value, in other words you changed the MAC address to a locally significant value.
* The 7th bit (U/L bit) is set to 1 or 0 (1 = unique) (0 = not unique)

000000x0 where x = 1 is unique (globally managed) , if x = 0 it is not unique and is locally managed

![](data:image/png;base64...)

An ISP allocates you /48 leaving you / 16 for subnets. This is 2 ^ 16 or 65k subnets, which will all receive a /64 mask from you, whether it is a point-to-point link or a subnet with many hosts. (this is because there is no need to subnet to save address space, No Nat, equivalent to public ipv4 address)

The IPv6 address is broken up into more fields, as shown below

![](data:image/png;base64...)

SLA ID (Site Level Aggregation Identifier) – 16 bits in length - this is the subnet portion of the address space

NLA ID (Next Level Aggregation Identifier) – used by your ISP

Res (Reserved Bits) – not currently used

TLA ID (Top Level Aggregation Identifier) – Used by internet registries around the World, who assign NLA IDs to large ISPs

FP (Format Prefix) – set to 001

In IPv6 you can assign multiple primary IP addresses on an interface. When you enable IPv6 Address on a Cisco Router’s interface, multiple IP addresses are automatically allocated to that interface.

The whole purpose of this address layout is aggregation and summarization.

![](data:image/png;base64...)

The image above shows how an IPv6 address is delegated and aggregated as it goes from the Internet Registry which operates with a /16 subnet mask.

The ISP allocates a /32 mask to an ISP, the ISP then allocates a /48 address space for the end user, the end user / organization can then allocate subnets from the remaining 16 bits (64-48=16) and give a /64 mask to all interfaces

A single value is Hex is equal to 4 binary bits. So (2001) has 4 hexadecimal values, each with 4 binary bits. (4 x 4 = 16 binary bits) , Thus this is actually a 16 bit address – 2001::/16

2001:1234::/32 (2001 is 16 bits and 1234 is 16 bits, thus a /32 mask

The ISP has an address of 2001:1234::/32 (2001 is 16 binary bits and 1234 is 16 binary bits, thus a 32 bit mask

From the ISP to the Enterprise

2001:1234:1::/48 is the same as 2001:1234:0001::/48 so there is 16 binary bits between colons for a total of a /48 bit mask.

The Enterprise can then delegate subnets with a /64 mask as 2001:1234:0001:0002::/64 leaves us with 64 binary bits used for the Network Prefix portion of the IPv6 Unicast Address

**Cisco Commands for IPv6 unicast routing**

Firstly enable IPv6 unicast routing: R1(config)#ipv6 unicast-routing

To see the interface info in ipv6, be sure to specify IPv6 – As in R1#show ipv6 int brief

To set an ipv6 address on an interface: R1(config-if)#ipv6 address 2001:1:1:1::1/64

To use the EUI – Mac address as the IPv6 address R1(config-i)#ipv6 address 2001:2::/64 eui-64

This will take the MAC address add FF FE in the middle and change the 7th bit of the first octet if this is a globally unique IPV6 address. So if the interface BIA (burn in address was 00:11:22:aa:bb:cc) and the address is globally unique to an ip address as follows 2001:2::02:11:22:ff:fe:aa:bb:cc/64

**IPv6 Link Local addresses**

IPv6 Link Local Addresses are unicast addresses, but restricted to the link, hence the name link-local

They are still 128 bits in length, the Interface Identifier (last 64bits) is automatically configured with the EUI address.

Note: that the most significant 10 bits of the address start with FE80 in hexadecimal 1111= F 1110=E 1000 = 8 0

**Routing protocols use link local addresses to advertise routes to one another.**

In IPv6, a node (device) having a global unicast address on a local link, will use the “link local address” of its default “IPv6 router” rather than “the global unicast address”. This is good because if the network is renumbered, the “default router” can still be used, using the link-local address.

**Link local addresses won't change when you renumber your global unicast addresses.**

![](data:image/png;base64...)

**IPv6 Site Local Addresses**

![](data:image/png;base64...)

Site Local addresses are not enabled by default on nodes, unlike link local addresses

The address starts with FEC0 with the most significant 10 bits set in binary to

1111 1110 11 “F E 1100” = 8+4=12= C thus C0

These are the equivalent of RFC 1918 Addresses in IPv4

This has been deprecated

The idea was that you could have many subnets within your organization as you would have 54bits for subnetting

These are the equivalent of RFC 1918 Addresses in IPv4

Most prominent 10 bits are FEC0::/10 and the remaining 54 bits of the network prefix could be used for subnetting, which is far greater than the 16 bits you get with Globally Unicast addresses

**IPv4 Compatible addresses**

![](data:image/png;base64...)

* Used as a transition mechanism on Hosts and Routers to automatically create IPv4 tunnels to deliver IPv6 packets over IPv4 networks.
* (96 bits are set to zero, remaining 32 bits are set to the IPv4 address)
* This mechanism allowed for the automatic establishment of an IPv6-over-IPv4 tunnel between two nodes over an IPv4 infrastructure using the IPv4 destination address inside the destination IPv6 address
* The IPv4 portion of the address could be written in decimal notation or hexadecimal
* This address format has been deprecated in favor of other more enhanced mechanisms such as dynamic NAT Protocol Translation (Dynamic NAT PT).
* The IPV4 compatible IPv6 addresses use a /96 mask.

192.0.2.100

C0. 00 . 02 . 64

![](data:image/png;base64...)

DAD means Duplicate address Detection.

::1 is used by the host to identify itself and can be used to verify the ipv6 protocol stack in functioning correctly

![](data:image/png;base64...)

**Aggregateable Global Unicast addresses (above) – These are globally unique (thus no need for NAT)**

![](data:image/png;base64...)

![](data:image/png;base64...)

For each unicast and anycast address configured on an interface of a node or router, a corresponding solicited node multicast address is automatically enabled.

The solicited node multicast address is scoped to the local link.

This is an example is used as the replacement for ARP as was used in IP version 4.

If you remember ARP uses broadcasts, but broadcasts are no longer supported in IPv6, so the solicited node multicast address is used by nodes and routers to learn the link layer addresses (MAC addresses) of neighbor nodes and routers on the same link. So very similar in concept to ARP, but we are not using broadcasts, we are using multicasts.

Duplicate Address Detection or DAD can be used by a node to verify whether an IPv6 address is already in use on its local link, before using that address to configure its own IPv6 address with stateless Auto configuration.

Which three statements describes characteristics of solicited-node IPv6 addresses?

The correct answers are They are automatically created by the device, They are multicast addresses, and They have a recognizable prefix. A solicited-node multicast IPv6 address is created using special mapping of the device's unicast address with the recognizable solicited-node multicast prefix of ff02:0:0:0:0:1:ff00::/104. A device can have multiple solicited-node multicast addresses, because the multicast addresses are automatically created for every unicast address on a device.

![](data:image/png;base64...)

Stateless Auto configuration is a new function enabled by IPv6. By having a much larger address space, IPv6 is designed to enable auto-configuration of IP addresses on devices while keeping those addresses unique. This enables basic serverless configuration of nodes as well as easy renumbering. I.E. No need for a DHCP Server

SLAAC Question

**A device has been assigned an IPv6 address through the Stateless Address Autoconfiguration (SLAAC) process. Which three statements about SLAAC are correct? (Choose three.)**

It generates link-local addresses, It generates global unicast IPv6 addresses, and It relies on ICMPv6 router advertisements. SLAAC is an autoconfiguration mechanism that automatically configures the IPv6 address of a device. The device picks its own address based on the network prefix being advertised by the router on their connected interface. As defined in RFC 4862, the autoconfiguration process includes generating a link-local address, generating global addresses through SLAAC, and the duplicate address detection procedure to verify the uniqueness of the addresses on a link. Some devices may choose to use EUI-64 or a randomized value for the interface ID.

Routers same periodic router advertisements using a link local address.

The router uses ICMPv6 type 134, which is known as a “router advertisement” to tell nodes information,

1. what prefix to use (The first 64 bits of an IPv6 address)
2. what the default gateway is
3. the lifetime of this prefix that's advertised to them.

The advertisement period can vary and you can also change the lifetime of the prefix advertised to hosts.

Step 1

![](data:image/png;base64...)

When a host initially boots up, the node will need its IP address as soon as possible and normally in the early stages of the boot process.

It could wait for a long period of time( for the next router advertisement) to get the information it needs to configure its interfaces. Thus a node will **send a router solicitation message to all routers** on the network **asking them (The routers) to reply immediately with a router advertisement,** so that the node can immediately configure its IP address.

The Host’s Link Local Address begins with FE80 followed by its EUI Address (MAC with FFFE in the middle) as the source address,

So the host will send a solicitation to all routers using the **“all router’s multicast address” - (FF02::2)**

IPv6 Frame

“Router Solicitation message”

Source: Link Local

Destination: FF02::2 (All routers)

Reply sought: Router Advertisement

Step 2

A router will reply to that message using ICMPv6 Type 134 (Router Advertisement)

Source is the Router’s Link Local Address (FE80 followed by its EUI Address (MAC with FFFE in the middle)

Destination: (FF02::1 – all nodes on the link)

![](data:image/png;base64...)

Step 3

![](data:image/png;base64...)

![](data:image/png;base64...)

EUI Address = the link local address aka MAC address modified from 48bits to 64 bits

Stateless IPv6 has the advantage in that it enables plug and play configuration of IPv6 devices. You just configure an IP address on the Router and by default “router advertisements” are enabled, PC’s and other devices can be plugged into the network and they will automatically learn the prefix assigned to them and their Default Gateway without the administrator configuring ad DHCP server or manually configuring static IP addresses. Hosts are automatically configured with the prefix received and they then combine that with their link layer address (EUI Address / Mac Address with FF FE in the middle) to configure a local IPv6 address, to allow them to communicate on the network.

Another advanced of Stateless autoconfiguration is the renumbering of devices, a Router can just configure a new prefix and time-out the old prefix if required and hosts will be auto reconfigured with the new prefix

![](data:image/png;base64...)

More control than Stateless (e.g. Cisco IP phones need to learn on Option (option 150) from a DHCP server which points to the TFTP server that has the phone’s configuration files and firmware. As such DHCP is still required in some instances, as DHCP gives us more control and more options.

You can use Stateful DHCP concurrently with Stateless autoconfiguration.

Stateful DHCP can provide IPv6 address in the absence of routers. Node to Node / Device to Device network sans a router

Can be used for network renumbering

Can be used for automatic domain name registration of hosts using dynamic DNS

IPv6 Stateful DHCP (DHCP v6) Example

The process for acquiring configuration data for a DHCPv6 client is very similar to DHCP under IPv4.

However, initially the client will first detect the presence of routers on the link by using neighbor discovery messages

If at least one router is found, the host will examine router advertisements to determine if DHCPv6 can be used

![](data:image/png;base64...)

![](data:image/png;base64...)

Remember, anything starting with FF02 is a multicast address (Again: no Broadcasts in IPv6, in place of them, specific Multicast addresses are used).

The Hosts will use a source address of FE80 (a link-local address).

Both DHCP Servers and DHCP Relays will listen for DHCP solicit messages on the multicast address (FF02::1:2)

DHCP forwarding is very similar in IPv6, as it is in IPv4

If DHCP cannot be used, the Host will revert to stateless autoconfiguration

![](data:image/png;base64...)

FF02::1 Multicast Address to all nodes/routers on the link

FF02::1 Multicast address all routers on the link

FF02::1:FF00:1 Solicited Node multicast address used for mechanisms that replace ARP

In other words this is the address used by Duplicate Address Detection (DAD)

Solicited Node multicast address consist of **FF02::1:FF**XX:X (where X’s represent the unique portion of the interface ID)