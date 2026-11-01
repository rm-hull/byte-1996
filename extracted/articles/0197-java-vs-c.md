---
title: "Java vs. C"
publication: "BYTE Magazine"
issue: "November 1996"
section: "State Of The Art"
source_file: "BYTE.DAT"
source_offset: "0x00763f08"
---

# Java vs. C

*State Of The Art*

Designing a dedicated chip to run Java software is very different than designing a RISC chip to run C code. Here's why.

Java is much more regimented than C. The Java virtual machine (VM) stores all its temporary data, including the results of each computation, on a stack. C uses a stack optionally.

C compilers rarely know much about the pointers they manipulate. Java objects, by contrast, have a type from a strictly defined hierarchy, and this type information is available to the processor. The Java bytecode interpreter uses the structured information for security purposes and to optimize the code.

Java centrally controls memory by allocating and reclaiming memory for all objects. Central control means engineers can tune the memory/processor interface to keep the most important information available to the CPU. By contrast, RISC chips offer little support for memory control and simply rely upon the cache to deliver the data at the right time.

Java dynamically links procedure calls and method invocations at run time. This may involve searching several tables and chasing several pointers. C programs have the branches and jumps hard-coded during linking so the CPU can't intervene to speed up the process.

The Java specification explicitly identifies thread synchronization in the instruction stream. This means that picoJava chips can support synchronization primitives in hardware. In contrast, C programs that are running on a RISC chip carry out thread synchronization only through additional layers of software.

Copyright

1994-1997 BYTE

t?v

+?v

+?v

+?v

F@v

+?v

+?v

+?v

+?v

Cv

+?v

+?v

+?v

]Gv

+?v

+?v

+?v
