---
title: "OS Insecurity"
publication: "BYTE Magazine"
issue: "November 1996"
section: "Inbox"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x005ca61d"
---

# OS Insecurity

*Inbox*

In "Air-Tight Windows NT" (August), author Jim Reynolds states that the U.S. National Security Agency granted Windows NT 3.5 C2-level approval. What few people know is that this evaluation was limited to a stand-alone computer and did not include network interfaces. If a user hooks up an NT server to a network, the computer can no longer be considered C2-secure until almost all network functionality is disabled. Failure to mention this is misleading and lures users into a false sense of security. The article also doesn't mention the so-called "boot floppy" vulnerability of Windows NT. By booting from a floppy and using assembly language utilities, a person can bypass NT security and can read, write, and delete files from the hard disk without leaving a trace.

:Karl Pottie

Rumbeke-Roeselare, Belgium

karl@vl-brabant.be

The security features I discussed also apply to networked computers. NT is currently undergoing network evaluation (the NSA usually conducts stand-alone and network evaluations separately). But remember, the evaluated configuration, which includes hardware and software, might not match what you have or need. The NSA team was aware of the boot-with-floppy issue; the evaluated configuration prohibited physical access to the floppy. A less stringent need for security might take advantage of the common PC feature that prevents booting from a floppy. Of course, without physical security this solution can be circumvented. The bottom line is that if you can boot a different OS, then none of the security mechanisms of NT work. This is to be expected with any OS. What makes the NT case appear different is the ubiquitous character of the hardware platform and the fact it is generally designed to boot from floppy, unlike older, time-sharing systems such as Unix. -- Jim Reynolds
