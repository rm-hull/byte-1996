---
title: "RISC vs. CISC"
publication: "BYTE Magazine"
issue: "November 1996"
section: "State Of The Art"
source_file: "BYTE.DAT"
source_offset: "0x00762d2c"
---

# RISC vs. CISC

*State Of The Art*

How does the x86 stack up against RISC chips when running Java? Interestingly, the ancient x86 has a few advantages. For example, the x86's PUSH and POP instructions could become more valuable. These combination instructions were some of the first to go with RISC. They were replaced by two instructions: a register increment or decrement followed by a load or a store. So the x86 might handle Java stack operations more efficiently than some RISC processors.

One big difference between RISC and CISC is the number of general-purpose registers for storing integer and floating-point values. RISC chips typically have 32 or 64 registers, while the x86 has only 16. Normally, this puts the x86 at a disadvantage. But Java is a stack language; all the information between subsequent instructions is kept on a stack. RISC registers offer no great advantage unless a just-in-time (JIT) compiler can schedule the use of the registers more efficiently.

Copyright

1994-1997 BYTE

O-v

O-v

3.v

O-v

m.v

O-v

`0v

O-v

n2v

O-v

O-v
