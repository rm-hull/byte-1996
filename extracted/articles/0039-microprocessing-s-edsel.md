---
title: "Microprocessing's Edsel"
publication: "BYTE Magazine"
issue: "December 1996"
section: "Cover Story"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x001e1f95"
---

# Microprocessing's Edsel

*Cover Story*

After completing the 8080 in 1974, Intel turned its attention to a much more ambitious device, which eventually came to be known as the Intel 432. This processor, which could support object-oriented software, was years ahead of its time. It loaded and stored data using one or more levels of pointers, giving software great flexibility in how it organized memory. Each data element had an associated type (integer, character, pointer, etc.), and the processor always checked that each data value was of the correct type before using it. The 432 also supported features -- such as memory error correction, multiprocessing, and fault tolerance -- that would not become common for another decade or more.

Due to its complexity, the design of the 432 took much longer than anticipated. When Intel finished the initial version of the chip in 1977, the company realized that wading through pointers and checking data types completely bogged down the system. Performance on typical applications was five to 10 times slower than on competitive processors. The 432, still entirely too slow, didn't hit the market until 1980, where it sank without a trace, becoming one of the most spectacular failures in microprocessor history.

When Intel realized the 432 was in a deep hole, it rushed to staff a new project that would become the 8086. The company assigned two engineers to develop the instruction set and basic design of the chip and gave them just three weeks to complete the task. The 8086 went into production in 1978, just one year after its conception. Its design became the basis for the x86s used in all IBM-compatible PCs to date.

Perhaps because of its rushed origins, the 8086 has many unusual features. The programmer's options were limited because certain instructions were tied to specific registers: the ADD instruction can access only register A, the LOOP instruction uses only register C, etc. And the segmented addressing allows confusing situations, such as two program addresses pointing to the same location in memory, or the same address pointing to two different memory locations. Although some of these quirks have been fixed in later processors, programming x86 chips remains a challenge.

## Ahead of Its Time

The 432 supported:

Object-oriented software

)Data store using multiple pointer levels

Memory error correction

## Multiprocessing

## Fault Tolerance
