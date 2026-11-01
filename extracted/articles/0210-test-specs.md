---
title: "Test Specs"
publication: "BYTE Magazine"
issue: "November 1996"
section: "BYTE Hardware Lab Report"
source_file: "BYTE.DAT"
source_offset: "0x007e0e80"
---

# Test Specs

*BYTE Hardware Lab Report*

A workstation with Intel's fastest Pentium Pro processor provides great performance for running applications. A workstation with two 200-MHz Pentium Pros is even better -- but not for everybody. To really get your money's worth, you'll have to be using a technical application that threads well over two processors, or running something computationally intensive as a background task while doing other work. You might, for example, want to write code or answer e-mail while compiling a large application.

The eight systems we tested can all handle this kind of work. For our evaluation, we requested 200-MHz dual-processor Pentium Pros with 64 MB of RAM, at least a 1-GB hard disk, and a 17-inch monitor. All came with at least 2-GB hard drives, mostly SCSI of various flavors; the SAG system came with a 9-GB Wide UltraSCSI drive from Seagate. Seven of the systems arrived with 256-KB-cache versions of the Pentium Pro; the Dell OptiPlex came with the newer CPU that has a 512-KB cache (adding around $1500 to its price). Most came with strong 2-D graphics cards from either Matrox or Number Nine. We evaluated the systems for usability, features, and performance with some consideration of price.

## Performance

We tested performance under Windows NT 3.51 with our usual applications-based benchmarks and low-level InterMark tests, but we also hammered the dual-processor machines with two new tests that evaluate their multiprocessor efficiency under NT. Given the nature of the products, our Performance rating is weighted heavily (50 percent) by the dual-processor tests. After putting NT 3.51 on each system, we installed Microsoft Office and Visual C++ (4.2). We used each system's vendor-specified configurations and executed all the tests at 1024- by 768-dpi graphics resolution and 16-bit color depth (65,536 colors).

To evaluate multiprocessor performance, NSTL's R&D department devised two tests that measure system speed when both processors are being pushed to the limit. In the first test, we ran a floating-point-intensive Fourier transform program that analyzes the spectral content of a WAV file. A shell program loaded two simultaneous copies of the test and timed the results. The spectral analysis test has high data locality and little file I/O, so the test data generally resides in cache and the results are primarily dependent on raw floating-point power.

The second multiprocessor test measures how fast a system can build (compile and link) a large chunk of Visual C++ source code. We ran two simultaneous instances of the test. This benchmark produces results that depend on both CPU and hard disk performance; the test hits the hard disk often with both read and write operations.

Although dual-processor workstations are designed for high-end technical applications, many people will want the second processor to run general software. Our applications-based benchmark employs two 32-bit business programs, Microsoft's Word 7.0 and Excel 7.0. The macro-based tests exercise common functions of each application. For example, the Excel test measures the time it takes to delete a variety of cell ranges and calculate various addition, financial, and statistical functions. The application tests account for 20 percent of the overall Performance score.

To get at the performance of important system components, we also ran NSTL's InterMark tests. In addition to CPU performance, these low-level tests measure the efficiency of such components as CD-ROM drive, hard disk, and video/graphics subsystems. InterMark accounts for 30 percent of the Performance rating.

Features and Usability

We also rated system features and checked how easy the PCs were to set up and upgrade. In coming up with our Features ratings, we rewarded system characteristics that differentiate these top-notch Pentium Pro workstations from each other. Length and completeness of the warranty, number of slots and drive bays free for expansion, built-in security, and amount of dedicated graphics memory to support high screen resolutions (1600 by 1200 pixels) all contributed to better ratings.

For usability, a screwless design that makes it easy to remove the case and install an adapter card is a plus, as are clearly labeled I/O ports. On the other hand, an obstructed expansion slot is a minus. We gave extra points to systems that came with clear, well-indexed documentation. We consider adequately detailed jumper and DIP switch settings to be particularly important.

Evaluations in this report represent the judgment of BYTE editors, based on tests conducted by NSTL, Inc., as documented in a recent issue of their monthly PC Digest. To purchase a copy of the full report, contact NSTL at 625 Ridge Pike, Conshohocken, PA 19428; (610) 941-9600; fax (610) 941-9950; on the Internet, editors@nstl.com. For a subscription, call (800) 257-9402. BYTE Magazine and NSTL are both operating units of the McGraw-Hill Companies.

Copyright

1994-1997 BYTE

i!~

v#~

m%~
