---
title: "Let's Make It Universal"
publication: "BYTE Magazine"
issue: "November 1996"
section: "BYTE Hardware Lab Report"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x007dfe3e"
---

# Let's Make It Universal

*BYTE Hardware Lab Report*

Dave Rowell

Though it has been on the boards for a while, the catchall Universal Serial Bus (USB) interface is working its way into mainstream desktop computers. The USB standard, sanctioned by Intel and Microsoft and strongly backed by major vendors like IBM, Digital, Compaq, and NEC, will arrive more quickly than did PCI. IBM introduced the first two business PCs with a USB port last summer; Compaq, Siemens Nixdorf, and Sony have, too. Six systems in this Lab Report, including the IBM, provide USB ports. The Digital, Polywell, and Xi have two. Microsoft is preparing Windows drivers, and Intel has developed USB device chips as well as USB support in its latest CPU chip sets.

Like the Apple Desktop Bus (ADB), USB lets you daisy chain peripherals like keyboards and pointing devices into a single port. With its 12-Mbps serial transfer rate, however, USB has enough bandwidth to support printers, scanners, ISDN terminal adapters, and telephony devices, including T1 or E1 lines. (The telephony angle explains Nortel's strong backing of USB.)

USB's convenient bus topology is actually more of a staggered star topology than a chain. Hubs that provide seven USB ports can be chained together with 5 meters between hubs to support as many as 127 USB devices from one host system. The four-line USB cable has two lines to carry differential serial signals, one for ground and a +5-V power line, which largely eliminates the need for power bricks for many peripheral devices. The spec defines three classes of device: low power, bus-powered (100-mA maximum current draw); high power, bus-powered (500-mA maximum); and self-powered. USB devices like scanners and printers will obviously have their own power supplies but could use the USB power to exit power-saving states. The cabling is shielded twisted pair to support the 12-Mbps signaling rate. The spec allows a limited number of low-speed, 1.5-Mbps devices.

You will be able to hot-plug and unplug these devices, and they will automatically register with the host operating system in true Plug and Play manner. Not only is the USB topology LAN-like; its signaling protocols are, too. USB has abstraction layers similar to the first three levels of the Open Systems Interconnection (OSI) protocol stack. USB sets up point-to-point connections, termed pipes, between an application or USB driver program and a USB device on the bus. At the physical hardware level, the host controller (always the initiator) and the USB device send and receive serial signals on the bus. At the middle level, USB system software and a particular device send each other framed data. At the top level, an application talks to one of the device interfaces that a USB device can present.

The upshot is that you'll be able to easily attach external peripherals to a PC without rebooting, without confronting a confusing array of ports, and without having to deal with IRQ settings, DMA channels, and I/O addresses. Bring on those USB peripherals.
