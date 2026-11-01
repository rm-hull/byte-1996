---
title: "More for Your Memory"
publication: "BYTE Magazine"
issue: "December 1996"
section: "BYTE Hardware Lab Report"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x0028e983"
---

# More for Your Memory

*BYTE Hardware Lab Report*

One of the costs of increasing printer resolution comes from needing more memory to represent the page image. Theoretically, a 600- by 600-dots-per-inch (dpi) printer needs four times as much memory as a 300- by 300-dpi printer to store the same raster image. A laser printer typically needs a 2-MB configuration to print a 300-dpi letter-size page, 6 MB to print a 600-dpi letter-size page, and 12 MB for a 600-dpi tabloid page. Not all that memory is used for raster image storage, but much of it is.

You may notice in perusing the features table (page 108 of the print edition; not available on-line) that IBM's NP 17 can support 600-dpi printing on legal-size paper with only 4 MB of memory. It does so thanks to something called Memory Reduction Technology (MRT) licensed from Peerless Systems. Peerless' QuickPrint integrated printer coprocessor chip works with the NP 17's Intel i960 microprocessor to perform this magic using the Peerless Systems firmware.

MRT uses a whole bag of memory-reduction tricks including display list processing, compression, and band processing. Instead of just converting the page-description language into a rasterized page image and storing it in a buffer for printing, MRT compresses the page into a compact page representation that is rasterized on the fly. MRT uses a combination of lossy and lossless compression (anywhere from 4 to 1 up to 25 to 1) and then decompression for rasterizing. The Peerless design cuts the printer's memory requirements by 8 MB.

Reducing memory requirements brings down costs, and so does integration of functions. In addition to providing a hardware assist (not required by MRT) to the memory-reduction process, the QuickPrint chip provides other functions including an IEEE 1284-compliant parallel port interface, memory controller, print engine video controller, and interface to either Intel's i960 or Motorola's 5102 ColdFire processors.

Apple Computer has its own memory compression technology. The LaserWriter 16/600 can print legal-size pages at 600 dpi with only 8 MB of memory.
