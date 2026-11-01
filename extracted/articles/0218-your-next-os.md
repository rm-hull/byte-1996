---
title: "Your Next OS"
publication: "BYTE Magazine"
issue: "November 1996"
section: "Special Report"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x0084a4d2"
---

# Your Next OS

*Special Report*

What to consider when evaluating next-generation operating systems.

Dick Pountain

In this Special Report, we'll evaluate the next-generation implementations of three major OS platforms: Unix, with its continued enhancement of 64-bit architectures; Windows NT and the stops and starts of what has been known as Cairo; and Apple's Copland, which will arrive piecemeal over the coming months rather than as one integrated package.

Whether you're committed to one of these platforms or you're considering a switch to a different one, the decisions you make today will affect your OS strategy for years to come. How do you begin to evaluate tomorrow's operating systems? Start by analyzing six key areas.

Robustness

An enterprise-level OS ought to run in protected mode and employ preemptive multitasking, so errant programs can be killed off without bringing down the OS itself. Windows NT and Unix both offer such protection now. However, some people are concerned about the robustness of the new kernel-mode graphics driver scheme in NT 4.0 (which will presumably persist in forthcoming versions) compared to the slower but safer scheme in earlier NT versions.

Copland still represents only a partial answer to Macintosh robustness. Copland's new microkernel runs applications, as far as possible, in protected memory, but it must allow kernel access from old applications to maintain System 7.x compatibility.

## Multiprocessing

What's driving the move to multiple CPUs? Partly the performance requirements of network servers; partly processing-intensive client-side applications, such as rendering 3-D graphics and calculating large spreadsheets. These applications don't require massively parallel supercomputers, just rather modest symmetrical multiprocessing (SMP) systems that use shared memory and an OS that automatically distributes multithreaded applications over different CPUs. NT already supports one to four processors, and machines like Intergraph's four-Pentium graphics PCs are exploiting NT's multiprocessing capabilities. At the same time, specialist vendors like Sequent run NT with up to 28 CPUs. The Cairo development effort worked at refining the existing thread-allocation algorithms to achieve better load balancing between the CPUs.

Apple desperately needs to provide SMP ability for Power Macs to keep its traditional high-end graphics users from defecting to NT to reduce rendering times. Copland will introduce SMP with the microkernel's Thread Manager, which can allocate threads to multiple CPUs. However, backward compatibility may constrain Copland's SMP abilities.

Unix has supported multiprocessing for years, and most massively parallel supercomputers run Unix-derived OSes. The main commercial Unix variants, such as SCO, Solaris, and UnixWare, all support SMP, and such systems often run with up to 64 CPUs.

Configuration Management

Perhaps the greatest single disadvantage of PCs today is the nightmarish difficulty of maintaining large numbers of them. Every new peripheral requires new drivers, which get updated frequently. Current PC OSes offer little assistance to a system manager who has to install new drivers on hundreds of machines.

Mature software version control has become a critical issue. OS upgrades commonly overwrite -- without asking -- system DLLs with new versions that break existing software installations. The Windows 95/NT registry scheme, for example, is inadequate and should be strengthened or replaced. Copland will track software revisions with a service called Patch Manager.

Unix management has traditionally been a matter of maintaining many text-based configuration files, the contents of which are a mystery to all but the gurus. Windows NT and the Mac OS have the advantage of GUIs and interactive configuration utilities. Even so, the sheer number of PC peripherals vendors has made management more and more arduous. Hence Plug and Play becomes vital, and its absence has stalled wider acceptance of Windows NT.

The Macintosh has long been blessed with true plug and play and easy configuration (possibly due to less nonproprietary hardware). But with the growth of a clone Mac market, this could become an issue. Copland's hardware abstraction scheme, which organizes device drivers into related families, will maintain some discipline while still allowing third-party vendors to differentiate their products.

Network Configuration

As networks grow, an administrator must get help from the OS to remotely configure systems and share configuration changes. Windows NT centralizes user management onto a single primary domain controller. But if network growth requires

multiple domains

, it becomes a beast. Microsoft's plan is to organize multiple domains into a tree structure like that of arch-rival Novell's NetWare Directory Service (NDS). Future versions of NT will also support multiple master domain controllers, giving remote branch offices connected via WANs more independence while still maintaining system coherence. Microsoft also plans retooled directory services to simplify managing mixed networks by unifying log-in and administration procedures. The Open Directory Services Interface (ODSI) is intended to do for directory services what Open Database Connectivity (ODBC) does for database access: make it vendor-independent.

Distributed Objects

Unix vendors, under the Object Management Group (OMG), have spent several years on the Common Object Request Broker (CORBA) standard for different systems exchanging objects. OMG recently settled on Sun's Universal Networked Objects as the standard for remote interoperability and on OpenDoc as the compound document model for CORBA 2.0. This conflicts with Microsoft's own proprietary Distributed Common Object Model (DCOM) and ActiveX. To complicate matters, Sun's Java Component Architecture offers a way for Java components to talk across the Net. Sun's approach is backed by Netscape's 38 million copies of Navigator, which is ready to accept Java-based plug-ins. Netscape is cooperating with OMG to make Internet Interoperable ORB Protocol (IIOP) the unifying technology for Internet objects in all its future Web browsers.

This seems to have panicked Microsoft into a compromise: It will hand over its ActiveX object technology to a customer-driven open standards body (a first). So perhaps customer pressure might finally force a convergence of object standards.

64-Bitness

Unix vendors worry how Microsoft and Apple plan to push Wintel and the Mac further into traditional Unix domains. The Unix solution is to move up to 64-bit OSes (see "Unix Leads the 64-bit Charge"). Microsoft has only just started offering PC users a fully 32-bit OS: NT, not the 16-/32-bit hybrid that is Windows 95.

The main attraction of these next-generation OSes is that you can access more memory through 64-bit addressing. A 32-bit address space allows up to 4 GB of memory. Until recently, most users have regarded gigabyte memories as quite enough (if not pure fantasy), but the rise of client/server computing has us contemplating servers that cache huge databases entirely in RAM to speed up access rates. Gigabytes of memory suddenly makes sense as a giant disk cache. And a 64-bit address bus and OS can access up to 18 billion gigabytes.

Windows NT already runs on DEC's 64-bit Alpha chips. To push NT as a server OS, Microsoft needs to let Alpha users fully exploit its 64-bitness, or Unix may tempt them away. However, the lack of 64-bit applications, plus Intel holding 64-bit addressing for its next-generation Merced chip, means that this is not a top priority for Microsoft, or most of its users, just yet.

Where from Here?

If you're a Unix user, you just have to choose when or if you'll move up to a 64-bit version. If you really need the huge address space of 64 bits, you probably already know it. Similarly, the question for a Macintosh user is not whether you need Copland but rather how soon you can get it. If your graphics work involves high-resolution rendering, then you need the assistance of multiprocessing now. Because many Mac tools are being ported to NT, it's becoming a race: The longer Copland takes to deliver SMP, the more alluring are the cheaper hardware and existing SMP of NT.

Windows users face the most uncertainty. For intranets, you could use NT, NetWare, or Unix for the server OS, and any of a dozen choices for your Web servers. Microsoft's new Internet orientation might affect your plans in several ways. The next NT shell -- with integrated Internet Explorer -- is currently in beta; it presents an "HTML everywhere" desktop that can display live Web pages. Even the Windows Help file format abdicates to Hypertext Markup Language. Visual Basic's current incarnation is temporary, as its forms engine is not based on HTML. Planning to invest in a hypertext or document management system that doesn't involve HTML? Think hard.

Most important, though, you must decide whether Microsoft can make the more ambitious features of the Cairo project work and, if so, when. OS developments are exciting to watch, but excitement may not be what you want when it comes time to making decisions. If you can do it, waiting for the dust to settle may be the best strategy for the next few months.

## OS Features Checklist

NT Copland 64-bit Unix

>Symmetric multiprocessing Y Y Y

support

>Protected-mode kernel Y Y Y

>Per-process memory protection Y Y

>Preemptive task scheduling Y Not for Y

6 legacy code

>Multithreaded execution Y Y Y

3Automatic hardware detection Y Y

Component architecture ActiveX OpenDoc Various

Extensible OS kernel Y Rebuild

>64-bit address space Y

?Fault-tolerant file system Y Some

Key

Y = yes

mailto:"dickp@bix.com"

`Dick Pountain is a long-time BYTE contributing editor who lives in London. You can reach him at

dickp@bix.com
