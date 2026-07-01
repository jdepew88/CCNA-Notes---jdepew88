**Software Defined Access (SDA):**Cisco Software-Defined Access (SDA) uses a software defined networking approach to build a converged wired and wireless campus LAN. The word access in the name refers to the endpoint devices that access the network.

centralized controller - DNA Center-

with southbound and northbound protocols.

It also includes a completely different operational model inside SDA, with a network fabric composed of an underlay network and an overlay network.

SDA fills the position as Cisco’s campus offering within **Cisco Digital Network Architecture (DNA).** Cisco DNA defines the entire architecture for the new world of software defined networks, digitization, and Cisco’s re-imagining of how networks should be operated in the future.

SDA uses the DNA Center controller to configure and operate SDA. However, DNA Center also acts as a complete network management platform. To understand DNA Center, you also need to understand traditional network management as well as the new management models using controllers.

**Cisco Digital Network Architecture (DNA)**offers centralized, intuitive management that makes it fast and easy to design, provision, and apply policies across the network environment. The Cisco DNA Center GUI provides end-to-end network visibility and uses network insights to optimize network performance and deliver the best user and application experience. Cisco Digital Network Architecture (Cisco DNA), a software-driven platform that helps to create an intuitive and automated network. This allows network administrators to use software to execute policy and configuration changes they want to be made throughout the network. Many other operational tasks are streamlined through drag-and-drop provisioning, proactive troubleshooting, immediate remediation guidance and fast network segmentation.

The architecture uses Cisco’s Software-Defined Access (SD-Access) feature, which provides policy-based automation from the edge to the cloud through a virtual overlay network. Automating day-to-day tasks such as configuration, provisioning and troubleshooting, SD-Access is done using SD Access. With SDA, the underlay exists to provide connectivity between the nodes in the SDA environment for the purpose of supporting VXLAN tunnels in the overlay network. VXLAN, short for Virtual Extensible LAN is a flexible encapsulation protocol used for creating tunnels.

**Cisco DNA Center has four general sections:**

**Design:** Design your network using physical maps and logical topologies for quick visual reference. The direct import feature brings in existing maps, images, and topologies directly from Cisco Prime Infrastructure and the Cisco Application Policy Infrastructure Controller Enterprise Module (APIC-EM), making upgrades easy and quick. Device discovery is automatic and can be done either through Cisco Discovery Protocol or simply by entering an IP address range.

**Policy:**Define user and device profiles that facilitate highly secure access and network segmentation based on business needs. Cisco DNA Center takes the information collected in a policy and translates it into network-specific and device-specific configurations required by the different types, makes, models, operating systems, roles, and resource constraints of network devices. Using Cisco DNA Center, you can create virtual networks, access control policies, traffic copy policies, and application policies.

**Provision:**Once you have created policies in Cisco DNA Center, provisioning is a simple drag-and-drop task. Categories of identities (users, devices, applications, etc.) in the Cisco DNA Center inventory list are assigned a policy, and this policy will always follow the identity. The process is completely automated and zero touch. New devices added to the network are assigned a policy based on identity- greatly facilitating remote office setups.

**Assurance:**Cisco DNA Assurance provides a comprehensive solution to help assure better and consistent service levels to meet growing business demands. It addresses not just reactive network monitoring and troubleshooting, but also the proactive and predictive aspects of running the network, and improving client, application, and service performance. The outcome is a consistent experience and proactive optimization of your network, with less time spent on troubleshooting tasks.

**Cisco DNA Center has two notable roles:**

1. As the controller in a network that uses Cisco SDA

2. As a network management platform for traditional (non-SDA) network devices, with an expectation that one day DNA Center may become Cisco’s primary enterprise network management platform

**Cisco DNA components: Cisco DNA comprises:**

1. Cisco DNA solutions: SD-Access, SD-WAN, Cisco DNA Assurance,and Cisco DNA Security.

2. Cisco DNA Center appliance: Command-and-control appliance and software for policy, automation, and analytics.

3. Cisco DNA-ready physical and virtual infrastructure: Switching,routing, and wireless.

4. Cisco DNA software that can be purchased through three licensing tiers.

![Cisco DNA Center](data:image/jpeg;base64...)

Cisco DNA Center includes **northbound REST API**along with a **series of southbound APIs**. For most of network engineers, the northbound API matters most, because as the user of SDA networks, interact with SDA using Cisco DNA Center’s northbound REST API or the GUI interface. Cisco DNA Center supports several southbound APIs so that the controller can communicate with the devices it manages.

The DNA center provides **Path trace feature** that allows the operator to visualize the path of an application or service from the client through all devices and to the server. A common, and critical, troubleshooting task that normally requires 6 to 10 minutes is displayed instantly upon clicking on a client or application. Troubleshoot issues along the network path.