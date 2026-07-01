Cisco IP Phones and CUCME

Phone Startup Process

* Phone obtains power (from the wall or POE)
* Loads its locally stored image (and the configuration last saved)
* Switch provides VLAN information via CDP/LLDP-MED
* IP Phone acquires an IP address from as DHCP server
  + (DHCP Option 150 – to point the phone to a TFTP server)
* IP Phone downloads firmware/configuration from the TFTP Server
* IP Phone registers with CUCM (SCCP or SIP)
* IP Phone downloads softkey template (does this if using SCCP)

Powering the IP Phone

* Using a power cord
* Power injector
  + Mid-span power (when the switch does not support POE, this adapter can add POE to the Ethernet cable)
* Power over Ethernet (POE) – Power Source Equipment (PSE devices) have POE / POE+ as a feature.

Phones are known as powered devices (PD)

Types of POE

Traditional/original POE – 6.3 watts, cisco proprietary implementation

802.3af (POE) – Class 3 at 15.4 watts, provides interoperability between multiple vendors phones and networking equipment

802.3af (POE+) – 30 Watts, was developed because Cisco did not want to wait for the ratification of 802.3at

Another advantage of cisco POE is that a switch can automatically discover if a PC or IP Phone is plugged into a given interface. A Fast Link Pulse (FLP) was sent down the wire to determine whether a phone was plugged into a given interface. If a phone is not powered the FLP is sent back to the switch. When the switch receives its FLP back from a device, it knows that the device is POE capable and sends power to it.

FLPs are usually used for speed and duplex information.

802.3af the power sourcing equipment provides a small current limited voltage to the cable (DC voltage) between the transmit and received pairs.

PSE sends low voltage across the cable and expects to receive 25k ohm back to indicate the device is POE capable. From there the PSE can determine the 802.3af class of the device to determine how much voltage is required to power the device.

802.3af Classes

![Table  Description automatically generated](data:image/png;base64...)