---
title: "Visual Programming for Science"
publication: "BYTE Magazine"
issue: "December 1996"
section: "Codetalk"
source_file: "BYTE.DAT"
source_offset: "0x004b54d1"
---

# Visual Programming for Science

*Codetalk*

/New tools that go far beyond GUI construction

Rick Grehan

Until recently, if you had asked me to define what visual programming means, I would have pointed you to Visual Basic or Visual C++ and said, "That is visual programming incarnate." However, visual programming as exemplified by those two tools is not much more than building GUIs. Yes, you can construct a Visual Basic application using "nonvisual components" such as a database object. Those nonvisual components appear on the form as small bit maps that hint at the functionality lurking underneath, but do little more than act as reminders that a database is in the application.

I sometimes think another category of tools has a greater claim to the visual-programming title than the tools mentioned above. An excellent example from this other category is acroScience's Visual Science (VS). Prices start at $395, and discounts are available.

VS is similar to Oberon's Prospero (see "Prospero's Magic Application Integrator," February BYTE), but Prospero is primarily a data-manipulation tool. VS is a mathematical programming and simulation tool. Programming in either involves dragging "blocks" onto a workspace and wiring them together to form programs. In this scheme, the blocks represent execution objects. Wires represent data flow. Programming is therefore visual in the sense that the programming language itself is visual. With Visual Basic and Visual C++, the visual elements are part of the final application, not an aspect of the language.

The idea behind VS is not new. VisSim uses it (see "Travels and Travails," January 1994 BYTE), as does Prograph (see "Prograph CPX: Purely Visual," January 1995 BYTE). However, VS lets you encapsulate other external applications as building blocks.

Let's say you are building a VS application by populating a worksheet with blocks taken from a tool palette and wiring the blocks together. Functions a given block performs can range from primitive to complex. A good example of a primitive block is a decision block that works much as a simple multiplexer with two inputs and two outputs. One input acts as a selector; the other accepts arbitrary data. If the selector is set to zero, it routes the data input to the first output; if the selector is set to one, the data appears on the second output.

A complex block encapsulates more elaborate behavior and can be an entire program in the classic sense of the word. That is, the block can consist of a function written in a procedural language. VS includes its own language, MathCalc, which is a powerful mathematical language in its own right. MathCalc easily handles vector and matrix operations (matrix multiplication and division are built into the language). It includes over 100 math functions.

However (and this is important to note), a complex block could also be an entire MatLab program or an entire Interactive Data Language (IDL) program. (IDL is marketed by Research Systems of Boulder, Colorado.)

VS links into MatLab through DDE. (Developers at acroScience hinted that a higher-throughput connection into MatLab would be available in the near future.) The connection to a MatLab block is as seamless as with any of VS's primitive blocks. Consequently, you can easily integrate arbitrarily large and powerful MatLab or IDL programs into a VS application. You identify which variables in the program act as inputs and which act as outputs. VS makes connections available so that you can wire the block into your VS application. This lets VS programs tap into capabilities beyond those available in a single application. Currently, acroScience is working to integrate other mathematics packages into VS; more should be supported by the time you read this.

The ramifications of VS are interesting. If you have a problem you can't solve in MathCalc, you can call on MatLab for help. If MatLab doesn't include the feature mix you need to solve the problem, you can try another package.

I hope to see more of this trend, where visual languages act as large-scale macro languages for automating diverse applications. This allows you to work visually for the coarse-grained components of the application and then drop into traditional procedural code for the fine-grained elements.

## Where To Find

acroScience

Boulder, CO

+Phone: (800) 600-MATH or (303) 541-0089

Fax: (303) 541-0089

E-mail: info@acroScience.com

http://www.acroscience.com/

Internet:

http://www.acroscience.com/

mailto:"rick_g@bix.com"

Rick Grehan is a senior technical editor for BYTE reviews and a coauthor of The Client/Server Toolkit. You can reach him by sending e-mail to

rick_g@bix.com

Copyright

1994-1997 BYTE

5UK

dUK

;VK

>YK

mZK

g`K

RbK

LcK

ifK

tgK

*iK

hiK

'jK

fjK

?kK
