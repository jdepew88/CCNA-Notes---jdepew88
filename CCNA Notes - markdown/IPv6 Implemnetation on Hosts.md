Implementing IPv6 on Hosts

SLAAC or DHCPv6

SLAAC: Stateless Address Autoconfiguration – Dynamically allocate IP Addresses to hosts

IPv6 Hosts require the following info to operate

1. They need an IP address
2. A subnet mask
3. Default gateway
4. DNS server

Neighbor Discovery Protocol (NDP) handles a number of functions with regards to IPv6

A host can use its MAC address for the host portion of the IPv6 Address, but it needs to know what subnet or prefix it belongs, plus subnet mask / prefix length

Router Discovery is how IPv6 hosts discover routers. Hosts use Router Discovery to learn what subnet they belong in

Duplicate Address Detection (DAD) is used by hosts to determine that no other host is using the same IP address.

An IPv6 host will first check whether another host is using the same IPv6 unicast address as itself before it tries to use that address.

Neighbor Discover Protocol is used for Neighbor Mac Discovery, this is in place of ARP (no ARP in IPv6)

If a PC with an IPv6 address wants to ping another PC on the same subnet, it will use Neighbor Mac Discovery to acquire a MAC address so the two hosts can communicate

ICMPv6 vs IPv4

|  |  |
| --- | --- |
| IPv6 | IPv4 |
| Echo Request + Echo Replies (pings) | Echo Request + Echo Replies (pings) |
|  |  |
|  |  |
|  |  |
|  |  |

Neighbor Discover Protocol Messages – NDP Messages

Router Solicitation (RS)

* Sent to all IPv6 routers Multicast address: FF02::2 (All routers address) Routers on the local segment reply with Router Advertisements (RA)

Router Advertisement (RA)

* Sent by routers
* Includes Information such as the Link-local IPv6 address of the Router and the local segment
* Multicast address: FF02::1 (All devices address)

![](data:image/png;base64...)

Above: PC sends an RS across the local segment requesting all routers to id themselves. Routers receiving the RS will send an Router Advertisement in response the RS with their Link-local address)

Occasionally, Routers will send ***unsolicited RA messages***

By leveraging NDP RS and RA messages, hosts can discover which subnet they belong to