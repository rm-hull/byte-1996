---
title: "How to Turbocharge Chips"
publication: "BYTE Magazine"
issue: "December 1996"
section: "Cover Story"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x001e2fd1"
---

# How to Turbocharge Chips

*Cover Story*

Chip architects have wrung out performance in microprocessors in two basic ways: improved manufacturing techniques that boost clock rates and additional circuits that mean chips can do more work per clock cycle.

Early microprocessors took several cycles to execute a single instruction, and the number of cycles varied depending on the type of instruction. In the mid-1980s, a key innovation of RISC processors was to overlap instructions in a pipeline so that each took only a single cycle to execute. Intel and other CISC vendors figured out how to add pipelining to their chips, starting with the 486 in 1989.

As manufacturing processes continued to improve, more and more circuits could fit onto a single chip, so designers began adding capabilities like superscalar execution. In 1989, Intel introduced the i960CA, which could execute not one but two instructions per cycle, making it the first superscalar processor.

By 1995, the state of the art was four instructions per cycle. This summer, IBM introduced a six-instruction microprocessor. By doing more work in parallel, overall performance improves significantly. The complexity of superscalar chips adds to their cost, but since chip prices drop continually, this hasn't been an issue except in low-cost embedded applications.

Even though processors can execute several instructions per cycle, today's software typically executes one instruction at a time (for compatibility with older processors). If an instruction cannot be executed immediately (for example, because its data must be fetched from external memory), most processors grind to a halt until that instruction can be completed.

To get around this problem, several new microprocessors, including the PowerPC 604 and Pentium Pro, implement out-of-order execution. If one instruction has to wait, the processor simply begins work on the next instruction instead of stalling. This subsequent instruction thus completes before the first instruction, reversing the order that was originally intended. In order for everything to appear to the software to be executing in the correct order, the CPU must be smart enough to know when this shuffling is appropriate.

Designers have also taken advantage of the growth in transistor volume. In the 1980s, vendors began adding memory management units (to handle large programs) and floating-point units (to handle large calculations) onto their microprocessors. Today, some microprocessors contain special circuits to connect directly to memory and I/O chips.

Cache memory is another popular way to take advantage of burgeoning transistor counts. By the early 1990s, microprocessors with several kilobytes of on-chip cache became common. This memory responded much quicker than external memory, so if critical data were kept there, the CPU could operate more efficiently. Over time, designers increased the size of this memory. Digital's 21164 Alpha processor contains 112 KB of cache organized as three separate memories.

Next year's processors will have even more transistors, CPUs will execute more instructions per cycle, and out-of-order algorithms will get more efficient. In time, developers may build new instruction sets that allow programs, rather than the processor, to put instructions into superscalar groups. This new technique will eliminate the complex grouping and out-of-order circuitry found in current superscalar processors. Intel is expected to take this path with its Merced (aka P7) processor, which is due to be released in 1998 or '99.

## The World According to Moore

Transistor counts that double about every 18 months enable new chips

!to do more work per clock cycle.

Year 1971 1974 1978 1982 1985 1989 1993 1995

Chip 4004 8080 8086 80286 386DX 486 Pentium Pentium Pro

Transistors 2300 6000 29,000 134,000 275,000 1.2M 3.1M 5.5M1

1 for CPU, excluding cache
