---
title: "No-Mix MMX"
publication: "BYTE Magazine"
issue: "December 1996"
section: "Inbox"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x00005a2a"
---

# No-Mix MMX

*Inbox*

To the impressive technical detail Tom Halfhill presented in reply to John Michael Williams' letter about MMX programming (September Inbox), I would like to add one point: Using the Empty MMX State (EMMS) instruction costs 100 cycles. As you must perform this action to clear the in_use attribute of the FPU stack registers, embedding FPU code along with MMX is plain suicide for your program.

Eden Shochat

Senior programmer, Shells I.F.A.

Raanana, Israel

edens@netvision.net.il
