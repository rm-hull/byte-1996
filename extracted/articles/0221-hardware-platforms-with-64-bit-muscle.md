---
title: "Hardware Platforms with 64-bit Muscle"
publication: "BYTE Magazine"
issue: "November 1996"
section: "Special Report"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x0085b800"
---

# Hardware Platforms with 64-bit Muscle

*Special Report*

What hardware is available to support 64-bit OSes? All the leading RISC architectures currently use 64-bit designs. Intel's Pentium processors use 64-bit arithmetic operations and internal data paths. We expect that its successor, dubbed Merced, will be a full-blown 64-bit architecture.

Processor designers are further along in embracing 64-bit architectures than are OS developers. Today, there are 64-bit implementations for CPUs and for the data buses that interconnect the main processors with memory and I/O modules. Many data buses are 64 bits (or wider) to keep up with the CPUs that first implemented 64-bit arithmetic operations (i.e., load and store, and then add and multiply). The buses first arrived with a 64-bit internal data path and then moved on with a 64-bit external data path and 64-bit addressing. The latter enhancement enables CPUs to talk directly to 64-bit-wide memory.

All this lane-widening helps the CPU shuffle and process more data per cycle than in 32-bit systems. However, 64-bit architectures aren't the only way to boost CPU performance. Other performance enhancments include larger caches, higher clock speeds, more compact silicon wafers, and technologies such as very long instruction word (VLIW) for fewer but more complex instructions per cycle.

Six for 64

The following companies now offer 64-bit RISC processors:

Company Processor platform

Apple/IBM/Motorola PowerPC

*Digital Equipment Alpha

,Hewlett-Packard PA-RISC

+IBM AS/400

*Mips Rx000

+Sun SPARC
