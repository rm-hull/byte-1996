---
title: "Test Specs"
publication: "BYTE Magazine"
issue: "December 1996"
section: "BYTE Hardware Lab Report"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x0028d520"
---

# Test Specs

*BYTE Hardware Lab Report*

We picked the best network printers by running performance tests that evaluate a unit's top pages-per-minute print speed at standard (600- by 600-dpi) resolution. We tested on both PC and Macintosh platforms. We also scored print quality, features, and ease of setup, use, and maintenance. The resulting scores are an average of weighted geometric means with scores scaled to 10 for the best-performing printer.

## Performance

To get real-world performance numbers, we tested all the printers on a NetWare 3.12 network. For the PC platform, the client system was a desktop PC running Windows 95; for the Macintosh platform, we printed over the network from an Apple Quadra 640AV workstation with System 7.5 and EtherTalk installed. Our network file server used an NE3200 EISA Ethernet adapter, and the PC workstation had an Intel PCI EtherExpress 16 Ethernet adapter. We tested each printer with the drivers supplied or recommended by its vendor. We disabled all print servers, spoolers, and buffers during testing.

On the PC platform, we used a Windows applet to launch and time printing of test files with each printer. A test was complete when the last page dropped into the printer's output tray. A similar applet measured EtherTalk performance.

We set each printer to poll the network as frequently as possible to get the most consistent times attainable. The performance tests measure how fast a printer can crank out three common elements of a document: text, graphics, and fonts. The text tests represent typical business correspondence; performance in this test correlates with raw engine speed because there are no fonts or graphics for the printer to interpret. The graphics tests use bit-mapped images to simulate documents with complex graphics; they stress the printer's processor and RAM capabilities. We also use a font test to measure the speed of the printer's processor.

Print Quality

Our tests for quality of output measure how well the printers can produce a photographic image; print attractive, legible text in a wide range of sizes; and draw lines. For example, the line-squeeze test forces a printer to draw two lines increasingly closer until the gap between them vanishes, which indicates the printer can no longer make the black-to-white-to-black transition. In another part of the test we determine text legibility by having the printers produce increasingly smaller text. The test suite also gauges other print quality considerations such as how accurately the unit positions paper and how well it displays reversed text and graphics (white on black).

Other Factors

We evaluate each printer's feature set, usability, and technology to come up with our final scores. Feature details include emulations supported, the printer's maximum resolution, and what services the vendor provides with the standard warranty. We also evaluate usability based on such aspects as how easy it is to install the toner cartridge, the intuitiveness of the control panel, ease of driver installation, ease of network setup, and the clarity of the user manuals. Lastly, we judge each printer for the innovativeness of its technology.

Evaluations in this report represent the judgment of BYTE editors, based on tests conducted by NSTL, Inc., as documented in a recent issue of their monthly PC Digest. To purchase a copy of the full report, contact NSTL at 625 Ridge Pike, Conshohocken, PA 19428; (610) 941-9600; fax (610) 941-9950; on the Internet, editors@nstl.com. For a subscription, call (800) 257-9402. BYTE Magazine and NSTL are both operating units of The McGraw-Hill Companies.
