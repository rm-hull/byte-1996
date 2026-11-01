---
title: "ATM Hits the Desktop"
publication: "BYTE Magazine"
issue: "November 1996"
section: "International Features"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x00a06c73"
---

# ATM Hits the Desktop

*International Features*

:The corporate sector demands more powerful connectivity.

Klemens Gaida

Corporate interest in LAN-based asynchronous transfer mode (ATM) is on the rise. Market studies forecast that in the next three years more than 50 percent of ATM LAN implementations will be at the back-bone level. Perhaps even more interesting, these studies also say that about 30 percent of these implementations will reach the desktop. Engineering, telemedicine, and LAN-based telephony and video applications are all fueling this great demand for more powerful desktop connectivity.

From WANs to LANs

Although ATM started out as a carrier technology for WANs and the public network infrastructure, conventional wisdom said it would migrate down to LANs. But this hasn't happened as rapidly as expected, mostly due to the popularity of Fiber Distributed Data Interface (FDDI) and Fast Ethernet during the past couple of years.

Also hindering ATM's growth is the ATM Forum. This nonprofit organization, comprising more than 500 network vendors and telecommunications carriers, has issued so many specifications so quickly that companies are confused about which one to implement. They've found that drivers for ATM network adapters often don't support the heterogeneous structure of their existing LANs. But this is changing, as interest in ATM connectivity to the desktop exceeds idle curiosity.

The concept of ATM was originally developed for digital Broadband ISDN (B-ISDN) WANs. ATM is a connection-oriented protocol that contains a connection identifier in every cell header. This connection identifier explicitly associates a cell with a given virtual channel (see "Virtually Well Connected," August BYTE). Traditional networks, including Ethernet, are not physically connected; systems communicate with each other over a network bus rather than by way of direct connections.

These virtual channel connections (VCCs), which can be set up between any source and any destination on a network, are processed on ISO/OSI Layers 1 and 2 (the ATM layers). This means that network adapters must be able to process real-time communications and connection establishments. Also, adapter cards and switches need to understand the ATM signaling conventions and the quality-of-service (QoS) parameters of the ATM Adaptation Layer (AAL) (see the sidebar "Single-Chip ATM Adapters").

Classical LANs share a common transmission medium and deploy a collision-detection scheme, such as Ethernet, or a token protocol, such as Token Ring. In contrast, on an ATM LAN, no common transmission medium is used. With an ATM network, many simultaneous connections can be set up and maintained with different transmission requirements and without any collisions. This transmission method reserves the necessary bandwidth for each virtual connection.

The general construction of each ATM LAN switch corresponds to that of a public network switch. Typically, in an ATM LAN, terminators connect in a star structure to one or more centralized network nodes; the network sets up a connection via signaling. This technology gives a network's users access to all ATM world services, from the public network to the desktop.

To support nonconnected data transmission in a WAN or public-network environment, carriers deploy dedicated servers, the so-called connectionless servers (CLSes), which process higher-level protocols. However, on a LAN, a dedicated CLS is not cost-effective, so new ways to let LAN users work with ATM must be found.

Current applications and OSes are not designed to work with ATM networks. These applications have no way to talk to the underlying network to communicate the priority or the bandwidth that an ATM connection would require. In addition, the transport protocols of OSes such as Microsoft Windows NT and Novell NetWare are notorious for employing broadcast packets -- a certain way to decrease the performance of ATM networks.

LAN emulation provides the interoperability layer between current, connectionless, LAN-aware protocols and applications and ATM networks, but it cannot take full advantage of ATM's potential to provide a higher QoS. For optimal ATM networks, OSes should minimize broadcast traffic and be smart enough to talk to the underlying network.

Major OS vendors are working on connection-oriented abstraction layers. Microsoft has licensed LAN-emulation code from Olicom (Lyngby, Denmark), and Novell is working with ATM hardware developers in the U.S.

The ATM Forum has focused a great deal of effort on the definition of the User-to-Network Interface (UNI) specification. In this particular context, user refers to an ATM client, and network refers to the ATM switch.

The main thrust of UNI is a standard signaling protocol based on the B-ISDN specification and the provision of a consistent address assignment in WANs and LANs. Another important development of the ATM Forum's UNI Signaling Working Group is the definition of QoS parameters in the connection-setup message for each VCC. These parameters include peak cell rate, peak burst length, and sustainable cell rate.

Today, ATM LANs establish connections as unspecified bit rate (UBR) services; this enables connections to completely depend on the switches' buffers. LAN connections should, however, be requested as an available bit rate (ABR) service, which is more appropriate for bursty LAN traffic. UNI aims at standardizing this service.

The latest UNI 3.1 specification, which was released last year, is not compatible with UNI 3.0. As a result, users have to ensure that their ATM adapters support both specifications. Expect the ATM Forum to release the next version, UNI 4.0, by the end of this year.

Currently, a refused connection in an ATM network leaves the client with just a single option: to try again later. UNI 4.0 will provide a negotiation/renegotiation scheme for QoS parameters and will give a client the option of changing the QoS during connection time. In summary, UNI 4.0 adds more flexibility to the signaling setup, but at the cost of greater protocol complexity.

Many of today's LANs and ATM LANs deploy multiple protocols. For such environments, ATM LAN emulation is a desirable solution because it provides a link between connectionless LAN protocols and the connection-oriented network. For pure TCP/IP networks, the classical IP-over-ATM specifications enable TCP/IP nodes to establish point-to-point connections.

An alternative to multiprotocol routing over ATM is the Multiprotocol over ATM (MPOA) standard, which will be finalized by the ATM Forum early next year. However, it's important to note that MPOA is not a routing protocol in itself. It's more of an architecture that enables ATM clients to query routers or router servers about the best path through an ATM network.

In contrast to IP over ATM, LAN emulation deploys the TCP/IP protocol without modification. In addition, you can use classical LAN adapters, standard Network Driver Interface Specification (NDIS) and Open Data-Link Interface (ODI) drivers, and all LAN protocols at and above Layer 2 over an ATM network. The LAN emulation (LANE) is processed by either the ATM adapter or, if legacy LANs are coupled through an ATM backbone, an ATM switch.

LANE implements a client/server architecture to map Media Access Control (MAC) addresses to ATM addresses (a process known as address resolution). In this terminology, the LANE client is the workstation, and the server is a service implemented in the ATM network. The drawback of this concept is that LANE supports only data transmission, not voice or video transmission.

LANE supports three different network structures (all-ATM, LAN-to-ATM, and LAN-to-LAN) using ATM as the backbone, thus providing a step-by-step migration path. When the coupling of LANs over ATM does not meet the requirements of corporate network traffic anymore, a company can link single workstations or segments to an ATM backbone or create an all-ATM LAN. In connecting the local network to the public ATM infrastructure, users can create a homogeneous enterprise network.

In the future, when more LANs quit the shared-medium era and move on to connection-oriented switching, there's a good chance that even the internal structure of a workstation might follow this trend. Then all peripherals may feature an ATM interface that connects to a PC's internal ATM coupling field.

The big advantage of an ATM I/O bus will not be the resulting high data transfer rates; these may eventually be outperformed by other technologies, such as the Fibre Channel protocol (see "Fibre Channel: Fast and Flexible," May BYTE). Rather, the user of an overloaded computer could expand system resources just by setting up another VCC on a companion workstation without interrupting any other data transmission.

## Where To Find

ATML

Cambridge, U.K.

Phone: +44 1223 566919

Fax: +44 1223 566915

http://www.atml.co.uk

Internet:

http://www.atml.co.uk

Olicom

Lyngby, Denmark

Phone: +45 45 270000

Fax: +45 45 270101

http://olicom.com

Internet:

http://olicom.com

mailto:"editors@bix.com"

_Klemens Gaida is a consultant with Eutelis Consult (Ratingen, Germany). You can contact him at

editors@bix.com
