---
title: "Visual Age for BASIC...Sort Of"
publication: "BYTE Magazine"
issue: "November 1996"
section: "Codetalk"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x009e53e0"
---

# Visual Age for BASIC...Sort Of

*Codetalk*

Rick Grehan

Regular readers of this column may recall that in October 1995, I examined IBM's Visual Age for C++ on OS/2. Since then, IBM has extended the Visual Age product line to new OSes and languages. Visual Age for Smalltalk existed before the C++ variant. Visual Age for C++ is now available on Windows NT. IBM has also released Visual Age for COBOL. The most recent addition to the product line, Visual Age for BASIC (the product had a code name of Bart), however, more closely resembles Microsoft's Visual Basic than it does any of the other Visual Age products.

The Visual Age paradigm encourages construction by parts (in IBM lingo, a part is a visual or nonvisual component). The developer specifies the interactions of parts and, therefore, the execution behavior of the application by wiring together parts and defining activities associated with those connections.

For example, suppose you're building a data-input screen that consists of a listbox and a "clear" button. You want the clear button to erase whatever is in the listbox. Using the Visual Age construction methodology, you connect the button to the box -- the Visual Age integrated development environment (IDE) will draw a line from button to box -- and associate an event with that connection. In this case, you tell the system that a click event on the button triggers the erase() method of the listbox. This construction technique applies to nonvisual objects as well as the visual ones I used in the example.

Thus, when Visual Age for BASIC appeared (I examined a late beta version running under NT, but IBM says it will also release versions for OS/2 and AIX), I was eager to explore the Visual Age interface elements of the package and investigate how IBM had whipped BASIC into object-oriented shape. Unfortunately, although I was looking forward more to the former aspect -- the program's Visual Age-ness -- it was the latter aspect -- the object-oriented features -- that proved to be more interesting.

Bluntly put, it appears that the sole reason the package carries the Visual Age prefix is that IBM chose to call it Visual Age for BASIC. Were Visual Age for BASIC and Visual Age for C++ presented to me as siblings, I'd suggest that the presenter go back and check the parentage. Visual Age for BASIC's interface is obviously descended from Visual Basic.

Missing from all the documentation (available in the beta version only in on-line format) is any mention of the word part. Instead, the documentation speaks of components. Though some might suggest that I'm nit-picking, I can't shake the feeling that there's some sort of capitulation going on here.

Applications construction under Visual Age for BASIC proceeds along lines similar to those of Visual Basic and draws from a similar cast of characters. Forms are the fundamental window units, and you populate them with controls by selecting from a toolbar. Once a control is situated, you can summon an associated properties window and a code-editing window. However, if you are familiar with Visual Basic, you've seen all this before.

On a more positive note, Visual Age for BASIC does a good job of clothing BASIC in object-oriented garb. It supports class hierarchies and multiple inheritance as well as inheritance-based polymorphism. Also, Visual Age for BASIC can digest System Object Model (SOM) objects as well as OLE objects.

Finally, if your design work tends toward client/server database development using DB2 on NT, Visual Age for BASIC recognizes a separate stored procedure project, which allows you to build and test stored procedures much as you would build BASIC applications. (Admittedly, I did not experiment with that portion of the package.)

Visual Age for BASIC's first release amounts to a somewhat improved Visual Basic. (If you've been wondering, from what I've seen so far, the syntax differences between Visual Age for BASIC and Visual Basic are so minor that porting programs written for the latter to the former should be -- and I stress the words should be -- painless.) IBM representatives have suggested that future versions might incorporate more of the original Visual Age environment. I'd like to see that.

## Product Information

## IBM

http://www.software.ibm.com/ad/vabasic/

Internet:

'http://www.software.ibm.com/ad/vabasic/

mailto:"rick_g@bix.com"

Rick Grehan is a senior technical editor for BYTE reviews and the coauthor of The Client/Server Toolkit. You can reach him by sending e-mail to

rick_g@bix.com
