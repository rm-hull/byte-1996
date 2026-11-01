---
title: "VMS: Alive and Well"
publication: "BYTE Magazine"
issue: "November 1996"
section: "Core Technologies"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x0070f410"
---

# VMS: Alive and Well

*Core Technologies*

`Better reasons than tradition explain why Digital's VMS operating system continues to survive.

Ben Smith

With a face betraying my shame, I mumble, "Hi. My name is Ben, and I am a VMS user." The crowd responds: "Hi, Ben. We're VMS users, too!" But using a 20-year-old OS called VMS -- which unofficially stands for Virtual Memory operating System -- doesn't mean you have a disease, or even a temporary condition.

Besides its longevity and proliferation, due in great part to its robustness and sophisticated management design, VMS is adept at handling mission-critical jobs, and its clustering capabilities make it well-suited for multiprocessing. The OS isn't without flaws, which become more apparent because of its age. But Unix, which is even older, is growing in popularity, whereas VMS is just holding its own. Is VMS at the end of its life cycle?

Who Uses VMS, Anyway?

The VAX computer and VMS have been inseparable since birth. In fact, the VAX is one of the earliest designs in which the software engineers played a major role in the hardware design: They determined what structures and services should be implemented in microcode. Now, with the VAX being supplanted by Alpha VMS servers, VMS survives beyond its original architecture despite the close hardware ties.

VAXes have been applied to every kind of computing, so VMS has been used by every kind of user, from scientists running supercomputing applications to office workers doing word processing. But the days of broad-spectrum computing are past. Personal computers and much simpler LANs have replaced VAXes and terminal servers for low-end office computing. What work can't be handled by desktop computers can be done inexpensively on Unix machines and, despite their immaturity, Windows NT servers. Still, VMS can be found handling the critical, the fault-tolerant, and the secure computing jobs such as bank and stock market transaction processing, record keeping, and billing systems. A hiccup in any of these applications could cost millions of dollars in a flash, or even put lives in jeopardy.

Another important VMS feature is clusters. The basic concept is: If performance isn't adequate, add another server; they all appear as one.

The engineering and research communities have a huge investment in VMS applications. These are the millions of lines of FORTRAN code that also fall into the category of legacy systems. These hoary applications work perfectly well in the VMS environment, and they continue to gain in performance whenever Digital ships a newer, faster, VMS server.

Another reason for the OS's continuing popularity is a feature that all VMS applications exploit: VMS programs can share the same data types, system resources, and process control. Developers can thus seamlessly build a monolithic application in which each individual part is crafted in the language best-suited for its function. For example, an application's general business logic might be coded in COBOL, its bit-manipulation aspects written in C, and its sophisticated numeric operations and utilities composed in FORTRAN.

VMS vs. Unix

VMS, along with its hardware counterpart, the VAX, was over a year in design, not counting the six months of discussions that took place before Gordon Bell (then head of R&D at Digital) wrote a memo, in April of '75, committing to its development. From the very beginning, VMS was built for demanding commercial applications. The VMS/VAX design team tried to anticipate all the levels and details that any commercial operation might need, and to implement them at as low a level as practical. High on the list of VMS features has been its consistency, its rich set of management features, and its security (C2/B1 rating from the U.S. government). Most important, VMS was the VAX's native operating system. Even today Unix, which is VMS's closest competitor, is considerably weaker in all these areas. Conversely, VMS's file system still lacks the ability to handle more than eight levels of subdirectories.

Unix is the quintessential example of ad hoc OS development. Unix grew out of a solution to running a compute-intensive simulation program on a computer that had been all but abandoned (ironically, a DEC PDP-7). Unix has grown as need be. Great leaps in design have been the result of some special application, research project, or academic program. Unix didn't actually become a commercial product (from Interactive Systems Corporation) until 1977, the same year that VAX/VMS was announced at a DEC stockholders' meeting.

While the VMS OS was integral to the VAX and hadn't (until the DEC Alpha) run on anything but VAX computers, Unix has been uniquely portable. Because of its humble roots and minimalist hardware requirements, Unix was quickly ported to all platforms, including the VAX. Despite the system's haphazard beginnings, many Unix features have become models for implementing similar services on other OSes, including Unix's simple file I/O, which was extended to devices and interprocess communications (through sockets); a configurable hierarchical file system; and more than one way for a user to interface with the OS (different command interpreters, or "shells").

Reports of My Death Are Greatly Exaggerated

An OS has reached its terminus when it's no longer breathing with new development. VMS is still alive. And it's drawing new energy from another OS: NT. The connection here is DEC's NT Affinity product and the concept of using VMS servers to do the high-end computing for NT servers and workstations. To support this capability, VMS has incorporated many of NT's data structures and design elements. There is a life-supporting transfusion going on between VMS and NT.

The VMS development group is very much alive and well. Some of the original developers are still there, turning out new releases. The truth is, VMS does just fine for its long-term customers who are running COBOL and FORTRAN applications, as well as for customers writing applications in C/C++, using RDB or Oracle databases and doing distributed transaction processing. Both of these types of users are going to be around for a long, long time.

VMS still serves as a reliable tool for getting the job done, particularly in mission-critical situations. There is no shame in being a VMS user.

## A VMS Time Line

April 1975: DEC's Gordon Bell writes memo that starts formal work

on VAX/VMS.

April 1978: First VAX shipped, with a preliminary version of VMS.

August 1978: VMS 1.0 ships.

April 1980: VMS 2.0, VAX/750 (first new processor) added to DEC

product line.

April 1982: VMS 3.0, VAX/730 rolled out. Ethernet connectivity added.

September 1984: VMS 4.0 and VAXcluster introduced. Many new VAX

$ models introduced.

September 1988: VMS 5.0, the VAX 6000, and symmetric multiprocessor

# VAXes introduced.

;November 1992: VMS 1.0 for the Alpha processor released.

July 1993: VMS 6.0 released. The major features are support for very

E large VAXes and a C2/B1 government security rating.

January 1996: VMS 7.0 released. Kernel-level support for DECthreads

B and 64-bit memory management supported on Alpha.

mailto:"ben@ronin.com"

Ben Smith is an independent contract programmer specializing in Unix and Perl. He used to be a BYTE technical editor. You can reach him at

ben@ronin.com
