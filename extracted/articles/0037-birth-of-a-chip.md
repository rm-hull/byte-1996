---
title: "Birth of a Chip"
publication: "BYTE Magazine"
issue: "December 1996"
section: "Cover Story"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x001dc758"
---

# Birth of a Chip

*Cover Story*

^In only 25 years, the microprocessor has become the life-support system of the modern world.

Linley Gwennap

Even in 1971, Intel wasn't shy about its accomplishments. Then only a four-year-old start-up known primarily for memory chips, the company proclaimed "a new era in integrated electronics" when it launched the 4004, the world's first commercial microprocessor. For once, an advertising claim proved to be prophecy rather than hype. The 4004 offered approximately the same performance that the ENIAC, with 18,000 vacuum tubes, did in 1946. The 4004's low cost ($200) and tiny size (12 mm

) enabled engineers to create new categories of world-changing products. Nevertheless, skeptics predicted that the market for a single-chip computer would also be tiny. After all, the total computer market was only thousands of units, and the 4004 was so primitive that part of its package was wood.

But the computer-on-a-chip became bigger than any one company. And chip architects continue their relentless quest to squeeze ever more power out of microprocessors.

Laying Down the Law

The 4004 sprung from Intel cofounder Robert Noyce's realization that the IC manufacturing processes for memory chips could be used for logic circuits as well. But what would be the right logic product? That question had been on Noyce's mind -- and that of Intel cofounder (now chairman) Gordon Moore -- for almost a decade. Shortly after Fairchild shipped the first IC in 1961, several industry visionaries realized it was only a matter of time before someone built a complete computer on a single chip. Most famously, Moore, then with Fairchild, predicted the number of transistors that could be placed on a single chip would double every 18 months, a rule so strong that it has held for 30 years and is now codified as Moore's Law.

In 1969, Moore and Noyce received an auspicious visit from Busicom, a Japanese company that was in the process of developing a desktop calculator. Busicom wanted Intel to design a set of 12 specialized chips for the device. Instead, Intel officials suggested that the calculator be built around a single general-purpose computing chip, which eventually became known as the 4004.

The 4004 design team included Ted Hoff, Stan Mazor, and Federico Faggin (who were all recently inducted into the Inventors Hall of Fame for this work). They borrowed many concepts from the larger computers of the day. But their resources were limited: To fit a computer onto a chip, they had to reduce the size of both the internal data paths and the external data bus to 4 bits rather than 16.

This design minimized the number of transistors that were needed for the storage and calculation units and helped fit the device into a 16-pin package, the largest that was available at the time. By contrast, today's Pentium processor requires a 296-pin package with a 64-bit external data bus. Intel's reduction of an entire CPU into a single chip meant that even low-cost devices could be programmable, which significantly reduced the cost and effort needed to design products and add new features.

Not having to be concerned about compatibility with existing computers, the team created a set of 45 instructions, many still familiar to modern programmers. Rather than encoding all instructions in 16 bits, the team crammed the smaller ones into 8 bits. This compact encoding made the most efficient use of the 256-byte ROMs available for program storage; the entire code for Busicom's calculator had to fit into four of these ROMs, or just 1 KB. Once the 4004's design was finalized, Intel engineer Faggin converted it into actual transistors and created the physical layout.

Next Generation

The 4004

soon begat

bigger and faster microprocessors. Before the 4004 was even completed, Hoff and Mazor began work on an 8-bit version called the 8008. The new chip both pleased and frustrated product designers. For example, the 8008 was the first microprocessor to include interrupts, but they never worked well. Intel's encore to the 8008, the 8080, arrived in 1974. Where the 8008 multiplexed the address and data onto a single bus, the 8080 offered separate buses, simplifying system design. Also, the 8080 provided a much better implementation of interrupts. The 8080 was an 8-bit processor, but certain instructions operated on pairs of registers and processed 16 bits of data at once. While compatible with the 8008, the 8080 added new instructions and features, pushing the transistor count to about 6000. The chip could address a then-enormous 64 KB of memory (today's Pentiums address 2 GB).

After the 8080 appeared, Gary Kildall of Digital Research saw the potential for low-cost computing devices and created an operating system called CP/M. This software simplified basic user tasks such as creating, executing, and debugging programs. By 1975, hobbyists and industrial users could purchase an 8080-based CP/M system from Altair and others for well under $1000.

Microprocessor competition blossomed. Faggin and Masatoshi Shima, who had managed the 8080 project at Intel, left to form Zilog. That company's Z80 chip, which was compatible with the 8080 and thus with CP/M, became popular in low-cost computers. Motorola soon introduced the 6800, and Texas Instruments, National Semiconductor, and Fairchild launched their own microprocessors, most of which were used in embedded applications.

Finally, the largest computer maker in the world paid attention to the ground swell of interest in low-cost computers. After considering microprocessors from Motorola, Zilog, and others, IBM selected the Intel 8088 as the engine of its new personal computer, the IBM PC, introduced in '81.

In 1978, Intel developed two sibling devices, the 8088 and the 8086, as upgrades to the popular 8080. The 8086 had 29,000 transistors, six times more than the 8080, enabling a host of new features, including multiplication and division. By speeding multiply and divide operations, the 8086 performed more-complex calculations (e.g., in a factory setting, calculating the proper rate to pour steel based on its temperature). All computations were available in 16-bit forms, multiplying by 10 the performance of the 8-bit 8080. The designers wanted to extend the address space to 1 MB, but this required 20 bits of address. To retain compatibility with the 16-bit 8080 addresses, Intel added 4-bit segment registers, creating a convoluted addressing scheme that is still the bane of programmers today.

The key difference between the 8086 and the 8088 was the external data bus: The 8086 used a 16-bit bus for better performance, while the 8088 offered an 8-bit bus to reduce cost and retain compatibility with 8080 system designs. The original IBM PC used the 8088; later versions used the 8086 as well.

The popularity of these systems spawned a legion of clone vendors using the 8088 and 8086. Intel was the main beneficiary, although some of the spoils went to Advanced Micro Devices (AMD), a licensed second source for the chips.

The Simpler, the Better

A new microprocessor design philosophy emerged in the early 1980s. RISC called for simplified instruction sets with a fixed instruction length and consistent encodings. The decreasing cost of memory allowed a move to 32-bit instructions rather than the 8- and 16-bit encodings typical of Intel's x86 instruction set. With larger transistor counts available, RISC developers were able to increase the size of the on-chip register file to 32 registers rather than the eight available in Intel's chips. These and other changes were intended to improve performance without increasing chip cost.

Early RISC research included IBM's 801 processor (which was never commercialized) and academic projects at Stanford and Berkeley led by professors John Hennessey and David Patterson, respectively. It is no coincidence this work was done in research rather than commercial product environments; the radical changes in design caused the chips to be incompatible with all existing systems and software.

But a few visionary companies began nurturing the technology. Hewlett-Packard hired Joel Birnbaum and other members of the 801 team to develop PA-RISC. Sun, then a fledgling workstation maker, incorporated much of Patterson's work into its SPARC architecture. Hennessey and others founded MIPS Computer Systems to commercialize the Stanford work.

Apple has now converted its entire product line to PowerPC processors, which are sold by both Motorola and IBM, to give RISC chips 6 percent of the overall PC market. Since the rest of the PC market remains resolutely in the Intel/Windows camp, it is unlikely that this share will rise significantly over the next few years.

In the past few years, several vendors have introduced new RISC product lines intended for embedded applications rather than computers. The Sega Saturn video game machine, for example, uses SH processors from Hitachi; the Apple Newton uses a chip designed by Advanced RISC Machines (ARM). In total, these embedded products consume more RISC processors than all computer systems combined, and this area will grow over the next several years.

Dirt-Cheap Chips

If Moore's Law holds true for the next 25 years, microprocessors in the year 2021 may be as much as 1000 times more powerful than the Pentium Pro chip. Computers built around such processors would be ablt to perform highly accurate simulations, enabling them to predict future events. They'll also understand and synthesize spoken words and render photorealistic 3-D images.

Perhaps more important, the performance of the $1 microprocessor could also increase significantly in 25 years. Even dirt-cheap chips will be many times more powerful than today's Pentium Pro. These low-cost chips will provide intelligence to many everyday devices that interact with users mainly through speech. Microprocessors have already brought tremendous changes to society, but hold on tight -- the ride's not over yet.

## 4004 vs. Pentium Pro

4004 Pentium Pro

5Transistors 2300 5.5 million

1Die size 12 mm2 196 mm2

6Transistor size 10 microns 0.35 microns

1Clock speed 750 kHz 200 MHz

-MIPS rating 0.06 (1) 440

/Memory capacity 4 KB 64 GB

2Package size 16 pins 387 pins

Phone: (1) estimated

mailto:"editors@bix.com"

Linley Gwennap is editor of Microprocessor Report (Sebastopol, CA). Contact him via

editors@bix.com
