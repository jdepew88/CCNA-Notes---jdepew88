EIGRP

* Cisco proprietary (at least it was)
* enhanced Distance Vector routing protocol
* based on IGRP,
* considered as a Hybrid Routing Protocol
* characteristics of both Distance Vector and Link State Routing Protocols
* The main DV behavior is the *initial* exchange of full routing tables between EIGRP neighbors
* offer load balancing across six paths (equal or unequal)
* similar metric structures to IGRP
* has faster convergence, and has less network overhead
* uses incremental updates.
* routing loop-free topology
* VLSM
* route summarization
* multicast
* incremental updates and routes for multiple routed protocols (IP, IPX and AppleTalk)
* Uses Diffused Update Algorithm (DUAL) to calculate the shortest path.

The following formula is used to calculate the metric of Enhanced Interior Gateway Routing Protocol (EIGRP).

Metric = [K1\*Bandwidth + (K2\*Bandwidth)/ (256 - Load) + K3\*Delay] \* [K5/(Reliability + K4)]

The default values for K are K1 = 1, K2 = 0, K3 = 1, K4 = 0, K5 = 0.

For default behavior, the formula can be simplified as metric = bandwidth + delay x 256

**DUAL**

DUAL stands for Diffused Update Algorithm, the algorithm used by Enhanced Interior Gateway Routing Protocol (EIGRP) to calculate the shortest path.

**Neighbor table**

Neighbor table contains a list of the EIGRP neighbors. Each routed protocol for EIGRP has its own neighbor table.

**Topology table**

Topology table contains a list of all destinations and paths the EIGRP router learned. There is a separate topology table for each routed protocol.

**Successor**

Successor is the best path to reach a destination within the topology table.

**Feasible successor**

Feasible successor is the best backup path to reach a destination

**Routing table**

Routing table contains all of the successor routes from the topology table. There is a separate routing table for each routed protocol.

**Advertised distance**

Advertised distance is the distance (metric) that a neighboring router is advertising for a specific route.

**Feasible distance**

Feasible distance is the distance (metric) that your router will use to reach a specific route.

**RID (Router-ID)**

Feasible distance is the distance (metric) that your router will use to reach a specific route.

**EIGRP**

* Hybrid of link-state and Distance Vector
* More of a Link-State protocol, than a D-V
* The main DV behavior is the *initial* exchange of full routing tables between EIGRP neighbors
* Rapid convergence (uses feasible successors backup paths, which are calculated before being needed
* VLSM Support – Full Subnet mask support
* Runs over IP using protocol 88
* Metrics – uses distance, not cost
* Takes bandwidth into account when calculating route (no “hop-count”)
* Sends periodic updates
* Doesn’t use link states for advertisements
* Uses Distance Vector elements (such as Split Horizon)
* Uses Link State elements (such as “incremental updates”)

EIGRP Continued

Overcame IGRP Drawbacks

* Hop limitation
* Full Routing Table updates (bandwidth intensive)
* No VLSM support
* Slow to Convergence
* Lack of Loop prevention

EIGRP

* Sends updates when the topology changes
* Default hop count of 100 (255 max)
* Supports VLSM
* Uses “Diffusing Update Algorithm” (DUAL) for loop prevention

**Configuring EIGRP**

Router eigrp [asn] [autonomous system number] (all routers must agree on the ASN) (1-65535)

**Topology Fields**

P – Passive; no EIGRP computation being performed (ideal state)

A – Active; EIGRP computation actively performed (possible issue/SIA)

U – Update; update packet sent to destination

Q – Query; query packet sent to destination

R – Reply; reply packet sent to destination

**EIGRP Metric**

* [90/metric] 90 is the Admin Distance (AD) for EIGRP
* EIGRP uses a composite metric
* K values are used to distribute weights to path aspects
* K values are K1 , K3 = 1 and K2 , K4 , K5 = 0
* Default EIGRP metric is: (10 ^ 7 / least bandwidth path) + (sum of all delays) x 256

This essentially means that, by default, EIGRP uses the minimum bandwidth on the path to a destination network and the total delay to compute routing metrics.

IOS allows admins to set other K values to non-zero values to incorporate other variables into the composite metric. This may be performed using the “metric weights [tos] k1 k2 k3 k4 k5 router config command.

**EIGRP Topology Table**

**Metric = bandwidth (slowest link) + delay (sum of delays)**

* Bandwidth: [107 / minimum bandwidth in the path] \* 256.
* Delay: sums of delays in the path multiplied by 256 (in tens of microseconds).

![](data:image/png;base64...)

The lesser route has a higher value cost. The successor route has a lower value cost

To determine the variance value to configure on the router, we can use the following formula:

Variance = Highest metric for the paths being constructed / Metric for the best route

Using this formula, we can calculate the variance value to configure on R2 as follows:

Variance = Highest metric for the paths being considered / Metric for the best route

Variance = 3847680\*3014400

Variance = 1.28 (rounded up to 2)

This value must then be rounded up to the nearest whole integer, which will be 2. Given this, R2 can be configured to perform unequal cost load sharing by implementing the following configuration in router config mode.

Like IGRP, EIGRP is a distance vector protocols and uses the same composite metrics as IGRP uses.To understand EIGRP, it is useful to first examine the protocol from which it evolved.

**K Values (K1 – K5) (K1 and K3 are default) K1 – bandwidth K3 - delay**

**K=Knob – turn the knop to adjust the metric, applies weighting to metrics**

EIGRP uses different K values to determine the best path to each destination:

These K values are only numbers to scale numbers in the metric calculation. The formula we use for the metric calculation looks like this:

**Metric = [K1\*bandwidth + ((K2\*bandwidth)/(256-load))+K3\*delay]**

If K5 is not equal to 0:

**Metric = Metric\*[K5/(reliability+K4)]**

If you look at the formula, you can see that the **bandwidth, load, delay, and reliability** influence the metric. We can see what K values are enabled or disabled by default:

Router#**show ip protocols**

Routing Protocol is "eigrp 1"

Outgoing update filter list for all interfaces is not set

Incoming update filter list for all interfaces is not set

Default networks flagged in outgoing updates

Default networks accepted from incoming updates

EIGRP metric weight K1=1, K2=0, K3=1, K4=0, K5=0

Router#**show interfaces fastEthernet 0/0**

FastEthernet0/0 is up, line protocol is up

Hardware is AmdFE, address is cc02.58a9.0000 (bia cc02.58a9.0000)

Internet address is 192.168.12.1/24

MTU 1500 bytes, BW 100000 Kbit, DLY 100 usec,

reliability 255/255, txload 1/255, rxload 1/255

Bandwidth Load Delay Reliability MTU

**K1 Bandwidth** is a static value which can be changed by using the bandwidth command. Keep in mind this doesn’t change the actual bandwidth of the interface! This command is ONLY used to influence routing protocols like EIGRP. Bandwidth is expressed in unites of kilobytes per second. It is a number used for metric calculation only and does not necessarily reflect the actual bandwidth of the link.

Bandwidth is the inverse of the bandwidth scaled by a factor of 10^7.

Scaled BW = 10^7/(Interface BW in kbps)

**K2 Load** will show you how busy the interface is based on the packet rate and the bandwidth on the interface. This is a value that can change over time so it’s a dynamic value. It is displayed by show interface command as DLY, in unites of **microseconds**. The default delay of an interface may be changed with the **delay** command, which specifies delay in **tens of micro seconds.**

**Scaled Delay = [Delay on interface/10] in micro seconds.**

**K3 Delay** reflects the time it will take for packets to cross the link and is a static value. Cisco IOS will have default delay values for the different types of interface. A FastEthernet interface has a default delay of 100 usec. If you use the delay command you can change this value to influence routing protocols like EIGRP. It doesn’t actually change the delay for this interface but it is only used to influence routing protocols.

**K4 Reliability** at 255/255 is 100%. This means that you don’t have issues on the physical or data-link layer. If you are having issues this value will decrease. Since this is something that can change it’s a dynamic value. Is measured dynamically and is expressed as an eight-bit-number, where 255 is a 100 % reliable link and 1 is a minimally reliable link.

**K5 MTU** or Maximum Transmission Unit is being exchanged between EIGRP neighbors but not used for the metric calculation.

![](data:image/png;base64...)

By default, **only K1 and K3 are enabled** and we don’t use K2 or K4. This means that only bandwidth and delay are used in the formula.

Why not? Because loading and reliability are dynamic values and they can change over time. You don’t want your EIGRP routers calculating 24/7 and sending updates to each other just because the load or reliability of an interface has changed

Since only K1 and K3 are enabled, we can simplify the EIGRP formula:

**Metric = bandwidth (slowest link) + delay (sum of delays)**

* Bandwidth: [107 / minimum bandwidth in the path] \* 256.
* Delay: sums of delays in the path multiplied by 256 (in tens of microseconds).

**Final Formula**

**Metric = (107 / minimum bandwidth) \* 256 + (sum of delays) \* 256**

The multiplication of 256 is done so EIGRP is compatible with IGRP (predecessor of EIGRP).

**Dynamic Neighbor Discovery**

**To distribute routing information throughout a network, EIGRP uses non-periodic incremental routing updates. That is, EIGRP only sends routing updates about paths that have changed when those paths change.**

**two routers become neighbors when they see hello packets on a common network.**

Performed by sending EIGRP Hello packets to the destination **multicast** group **224.0.0.10**

**Hello messages are multicasted by default but if neighbors are configured statically on a non broadcast medium like Frame Relay they are unicasted.**

Hello packets are sent as soon as the network command has been configured in an EIGRP ASN

![](data:image/png;base64...)

Above: Shows the handshake that occurs when establishing EIGRP neighbors

EIGRP uses the concept of an autonomous system (AS) to identify routers the belong to the same logical group. EIGRP-speaking routers in separate ASes cannot become neighbors

EIGRP sends hello packets every 5 seconds on high bandwidth links and every 60 seconds on low bandwidth multipoint links.

The rate at which EIGRP sends hello packets is called the hello interval, and you can adjust it per interface with the ip hello-interval eigrp command.

![eigrp neighbor hello](data:image/png;base64...)

We have two routers called R1 and R2, and they are configured for EIGRP. As soon as we enable it for the interface, they will start sending hello packets. In this example, R1 is the first router to send a hello packet.

![eigrp neighbor hello update](data:image/png;base64...)

As soon as R2 receives the hello packet from R1 it will respond by sending update packets that contain all the routing information that it has in its routing table. The only routes **not** sent on this interface are the ones that R2 learned on this interface because of **split horizon.** The update packet R2 will send has the *initialization bit set*, so we know this is the “initialization process.”  At this moment, there is still no neighbor adjacency until R2 has sent a hello packet to R1.

![eigrp neighbor hello update hello](data:image/png;base64...)

R1 is, of course, not the only one sending hello packets. As soon as R2 sends a hello packet to R1 we can continue to set up a neighbor adjacency.

![eigrp neighbor ack](data:image/png;base64...)

**After both routers have exchanged hello packets, we will establish the neighbor adjacency**. R1 will send an ACK to let R2 know he received the update packets. The routing information in the update packets will be saved in the EIGRP topology table (once the router receives on ACK from the neighbor).

![eigrp neighbor update](data:image/png;base64...)

R2 is anxious to receive routing information as well, so R1 will send update packets to R2, which will save this information in its EIGRP topology table.

![eigrp neighbor ack return](data:image/png;base64...)

After receiving the update packets, R2 will send an ACK back to R1 to let him know everything is ok.

EIGRP routers will start sending hello packets to other routers just like OSPF does, if you send hello packets and you receive them you will become neighbors. EIGRP neighbors will exchange routing information which will be saved in the topology table. The best path from the topology table will be copied into the routing table:

![EIGRP Tables](data:image/png;base64...)

**Selecting the best path with EIGRP works a bit differently than other routing protocols, so let’s see it in action:**

**![](data:image/png;base64...)**

**We have three routers named R1, R2, and R3. We are going to calculate the best path to the destination, which is behind R3.**

**EIGRP uses a rich set of metrics, namely bandwidth, delay, load, and reliability, which we will cover later. These values will be put into a formula, and each link will be assigned a metric. The lower these metrics, the better.**

**In the picture above I have assigned some values on the interfaces, if you would look at a real EIGRP router you’ll see the numbers are very high and a bit annoying to work with. R3 will advertise to R2 its metric towards the destination:**

**![](data:image/png;base64...)**

**Basically, R3 is saying to R2: “It costs me 5 to get there”. This is called the advertised distance. R2 has a topology table, and in this topology table it will save this metric, the advertised distance to reach this destination is 5.**

The advertised distance is also called the reported distance (RD)

**We are not done yet since there is something else that R2 will save in its topology table. We know the advertised distance is five since this is what R3 told us. We also know the metric of the link between R2 and R3 since this is directly connected. R2 now knows the metric for the total path to the destination, this total path is called the feasible distance, and it will be saved in the topology table:**

**![](data:image/png;base64...)**

**You have now learned two important concepts of EIGRP. The advertised distance, your neighbor tells you how far it is for him to reach the destination, and the feasible distance which is your total distance to get to the destination.**

**Let’s continue! R2 is sending its feasible distance towards R1, which is 15. R1 will save this information in the topology table as the advertised distance. R2 is “telling” R1 the distance is 15:**

**![](data:image/png;base64...)**

**Build the Topology Table**

Now that these routers talk to each other, what do they talk about? Their topology tables, of course! EIGRP, unlike RIP and IGRP, does not rely on the routing (or forwarding) table in the router to hold all of the information it needs to operate. Instead, it builds a second table, the topology table

**EIGRP Neighbor Table**

* Used to maintain state info
* Address and interface recorded
* Used by RTP (Updates/ Queries)

![](data:image/png;base64...)

**Diffusing Update Algorithm (DUAL)**

DUAL is at the crux of the EIGRP routing protocol

Looks at all routes received from neighbor routers, compares them, then selects the lowest metric (best), loop-free path to the destination router, which is the FD – Feasible Distance, resulting in the “Successor Route.”

**Feasible Distance** (FD) includes both the metric of a network as advertised by the connected neighbor plus the cost of reaching that particular neighbor.

![](data:image/png;base64...)

The best route (lowest cost route) is going to go into the routing table. *Successor Route* = Best route

The 2nd best route goes into the Topology table. *Feasible Successor* = 2nd best route

3rd best route doesn’t have a name, would be next in line to become Feasible Successor if the better routes go down

**EIGRP Load Balancing – Equal Paths**

* 4 Paths by default (6 maximum)
* To change that value | R1(config-router)#maximum-paths value (#)

**EIGRP Load Balancing – Unequal Paths**

* Can use a variance multiplier

Which can be an integer between 1-128

Specifying a variance of 5 instructs the router to load share across routes whose metric is less than 5 times the minimum metric.

**Reliable Transport Protocol**

* used for communication between EIGRP-speaking routers
* Ensure reliable packet delivery
* Update/Query and Reply packets
* Every packet sent must be acknowledged
* Multicasts used on NBMA
* Uses Multicasts and Unicasts
* Unicasts used for Acknowlegments always

**Passive Interface**

* stops both outgoing and incoming routing updates
* Causes the router to stop sending and receiving hello packets over an interface.
* Hellos are sent out of all active interface
* This is a waste of resources for loopbacks (which need to be explicitly made passive
* R1(config-router)#passive-interface loopback 0
* If you have a large number of interfaces you want to make passive, just enter the “passive-interface default” command

**EIGRP Router ID**

* Not the same as OSPF (which uses the RID to identify itself to neighbors)
* Used to prevent routing loops
* EIGRP identifies originating route for external routes
* External route with own RID is discarded

**Neighbors Not Forming (EIGRP)**

* Mismatched K values
* ASN don’t agree /match
* Passwords don’t match (when used)
* Neighbor not on a common subnet

**Distance vector routing protocol Features**

* Periodic full routing updates
* Updates are sent to neighbors (on link)
* Broadcasts are used to find neighbors and update routes

**Invalidation Timers**

* Router can degrade a route value
* Value resets each time a route is received
* RIP, a route is invalidated after 180 seconds if no update is received