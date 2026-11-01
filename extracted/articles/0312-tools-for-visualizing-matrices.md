---
title: "Tools for Visualizing Matrices"
publication: "BYTE Magazine"
issue: "November 1996"
section: "International What's New"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x00ac8737"
---

# Tools for Visualizing Matrices

*International What's New*

Available in 16- and 32-bit versions, SimplePlot Visualization for DOS and Windows helps you draw surfaces, contours, lines, and polygons from matrices. The Motif version of SimplePlot allows for the interactive display of 3-D data and has an interface to the DOS/Windows version. The advanced version, SimplePlot Plus, includes C functions and FORTRAN routines for standard graphing and mapping projections.

Price: Call company.

Company: Bradford University Software Services, Ltd., Bradford, U.K.

Phone: +44 1274 841396

Fax: +44 1274 841388

E-mail: info@buss.co.uk

http://www.buss.co.uk/buss

Internet:

http://www.buss.co.uk/buss

Circle 986 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Editorial

## Editorial

## Wanted: New Software

Today's shrink-wrapped applications are the last place you'll find innovation.

Mark Schlack, Editor in Chief

The search for the killer desktop app is dead, judging from the dearth of anything really interesting outside of the graphic arts/multimedia and geographic-information markets. Amidst a golden era of OSes, server software, Web stuff, and development tools, the best you can say about most desktop apps is that they are easier to install now that they come on CD-ROMs instead of floppies.

Too harsh? What was the last new client application authored by Microsoft? I come up with Access, in 1992, and even it wasn't totally homegrown in Redmond. This year's FrontPage was acquired in full, although it has since been seriously reworked. Lotus's now-defunct Improv came out for Next in 1990 and for Windows in 1993. Apart from these few, all we've seen are continuing improvements (albeit not unappreciated ones) to existing suites, accompanied by feature bloat.

"Who cares?," ask the Webmeisters. "With Hypertext Markup Language [HTML], Java, a browser, and plug-ins, shrink-wrapped software is a dinosaur."

The Web is a powerful tool, and it really has changed everything. The ferment in Web tools and server applications will obviously produce profound innovations -- probably even one of those legendary paradigm shifts.

But I'm not buying into the idea that server apps will completely replace desktop apps in this decade. The bandwidth and network reliability are just not there. And ultimately, whether software vendors write applications in giant hunks of C++ code and deliver them on CD-ROMs -- or write them in small pieces of Java code and wire them to us -- apps will still need to be more innovative.

Nor will custom development replace packaged software, even if the most optimistic scenarios about programmer productivity and code reuse come true. No company has the time or money to be its own sole source of software.

The greatest innovation in computing since the invention of the microprocessor has been shrink-wrapped software. The ability of computer professionals to deliver fast, inexpensive solutions will, for the foreseeable future, depend on the weaving together of custom and shrink-wrapped server and client applications.

My hope is that the industry will do something more than just add HTML converters to five-year-old apps. For example, seven years after Hewlett-Packard unveiled its ultimately unsuccessful NewWave shell for Windows, I'm still waiting for easy-to-use but powerful agents.

Want thankful users? Give them software that automates the repetitive yet complex tasks that consume most workdays. I would love something that I could "program" to gather memos, spreadsheets, e-mail, and whatever else I need to assemble monthly reports.

My impression that the software industry has entered a slacker phase was reinforced by a recent trip to Xerox's fabled Palo Alto Research Center. At PARC, you can see real innovation in areas as conceptually simple and practically difficult as viewing large amounts of data (an entire company organization chart, for example) quickly and easily. The kinds of inexpensive graphics hardware discussed in this month's cover story open up even more possibilities in this arena.

Maybe it's hard for concepts like data visualization and cross-application agents to clear the hurdles that large software companies put in front of new product development. I imagine that any product manager with fire in the belly still has to answer to company bean counters who ask, "Is there a $100 million market for the product this year?" I sure hope that someone out there is looking beyond today's installed base.

http://www.byte.com/vpr/vpr.htm

http://www.byte.com

When I go to Comdex next month, I'll be looking for interesting and practical new desktop applications to present our Best of Comdex awards to. (Vendors: See

http://www.byte.com/vpr/vpr.htm

R for details.) Tell me what you need from shrink-wrapped software in our forum at

http://www.byte.com

9; I'll carry the message back to the software industry.

mailto:"mschlack@bix.com"

Mark Schlack, Editor in Chief,

mschlack@bix.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Inbox

## Inbox

## You're Welcome!

Tom Thompson's "The Network in the Server" (July) is the most lucid and helpful explanation of Tandem's ServerNet system area network and its potential applications that I have seen. That includes our own internal publications. Thank you.

<Matt Riesz

Senior advisory systems analyst

Tandem Computers

I just read "The Network in the Server" and am impressed by the clarity with which you explained the NUMA-Q architecture. Congratulations.

?Kevin Joyce

Marketing manager, NUMA-Q

Sequent Computer Systems

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Inbox

## Inbox

## NT Trade-Offs

I enjoyed the excellent article about Windows NT, "4.0 Isn't for Everyone," by David Linthicum in the July issue. I was puzzled, however, by the absence of a fairly obvious conclusion: The considerable performance penalty imposed by the new shell and the questionable architectural changes made to accommodate it may make sense on a workstation, but they are of dubious worth on a server. With 4.0, the design center of NT seems to have shifted decisively toward the client. That's fine for me; I'm interested in NT primarily as a workstation OS -- interest motivated primarily by stability. But my guess is that Microsoft will have a hard time converting server owners, whether from NT 3.51 or from other OSes.

Will Kling

Milford, NH

"4.0 Isn't for Everyone" was informative, but you make too much commotion about the kernel-mode issue. Although moving the graphical device interface (GDI) into the NT Executive gives it the potential to crash the OS, this does not seem likely. The current GDI/Window Manager subsystem is highly stable and rarely faults. The move to kernel mode only simplifies its design, making it easier to debug. Since version 3.1, all of NT's other low-level device drivers (disk device drivers, SCSI controller drivers, etc.) have operated within the Executive with a high degree of reliability. There is no reason to suggest that the graphics subsystem need be any different. If, in NT 3.51, CSRSS.EXE faults for any reason, the whole OS shuts down, as it is considered a critical process. What is the practical difference if the graphics subsystem crashes and the OS subsequently shuts down, or if the graphics subsystem crashes and takes the OS with it?

(Rene Gollent

100642.1147@compuserve.com

The GDI issue involves the potential for OS failure due to reengineering of NT. The claim that the NT 3.5 kernel is inherently stable does not automatically carry forward to the next instance of the OS, considering the changes that Microsoft has made. At the beta stage (Build 1234), it was unclear how moving GDI to Ring 0 might affect stability in the final release -- we were not able to crash the beta system. However, as with other operating systems that exploit Ring 0, the trade-off is stability for performance. Microsoft is selling NT as an OS that is more stable than Windows 95 and as an OS reborn for the client. The changes made to NT to sell it as a high-performance client could jeopardize its traditional use as a server OS. That's why I made an issue of it. As I write, Windows NT 4.0 is just leaving beta. We'll know who's right about the GDI issue very soon. -- David Linthicum

http://www.process.com

"NT and the Net" (July) provides a good overview of Microsoft's strategies surrounding its Internet Information Server (IIS). The discussion of the benefits of the Internet Server API (ISAPI), however, failed to give credit where credit is due. The interface now known as ISAPI was first developed as a proprietary interface by Process Software (

http://www.process.com

) for its Purveyor Web server for Windows NT. Late last year Microsoft and Process announced their collaboration on an open standard -- ISAPI -- based on the Purveyor API. To both companies' credit, DLLs written to the original API still function under ISAPI using both Purveyor and IIS.

9Steve Loper

Amadeus Consulting Group

sloper@wolfgang.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Inbox

## Inbox

## You Can Teach an Old Chip

Kudos (again) to Tom Halfhill for his detailed yet clear explanation of how the MMX instructions work with Intel-type CPUs ("x86 Enters the Multimedia Era," July). The article's nuts-and-bolts focus typifies why BYTE is a valuable resource for all of us.

First, if my browser requests <URL:http:&#47

http://www.zeus.co.uk/

It works, but it generates extra traffic, which contributes to an already crowded Net. Second, consider a Web server, like Zeus (

http://www.zeus.co.uk/

), that actually does content negotiation. You don't, for example, put extensions on image files. Instead of <IMG SRC="/images/mypic.gif">, you would write <IMG SRC="/images/mypic">.

The server looks at the HTTP_ACCEPT string and determines whether the browser can display GIF, JPEG, XBM, etc., then serves the best or smallest image accordingly. So, if we have a directory called /images/mypic/ but refer to it as /images/mypic, aren't we potentially in trouble?

Adam Shaun Nealis

adam@lbs.lon.ac.uk

I think you're right on both scores. I do try to include the trailing slash to avoid the extra bit of negotiation you describe. That's pretty well known. But the second case you bring up is really interesting. I've been only vaguely aware of progress in standards for content negotiation, but if it ends up working in the way you describe (i.e., no file extension means negotiate best type), then that would certainly be another reason we should all try to be more precise about trailing slashes. -- Jon Udell, executive editor

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Inbox

## Inbox

## Free PCs!

How is the system Gary Tripp describes in "Forget $500 PCs: How About Free Ones?" (Bits, August) fundamentally different from the old mainframe model? The details may differ, but we still have terminals gaining access via communication lines to a central store of information and using a central, remote processor for anything beyond trivial or presentation-related tasks. Isn't this what personal computers were invented to get us away from? And isn't it a recipe for generating insatiable demand (presuming the cost can be made acceptable) for bandwidth? The basic idea of the personal computer was and is personal control over the physical computing machinery, as well as avoidance of the bureaucracy and high priesthood that inevitably develops around a mainframe or its network equivalent, along with the requirement that you pay every time you use it. Recall how IBM became great: by leasing computing power, not selling it. When networks become the computer, at least in the form promoted by the "Web PC" types and Microsoft, computing is no longer personal; it has returned to the mainframe orientation we once rebelled against.

%Mike Brady

73720.1544@compuserve.com

The PC revolution has brought us cheap computing power, but it's not cheap enough. The only way to get computing into the hands of the 75 percent of the U.S. population and 95 percent of the rest of the world that currently lack access is to change the model from a software and hardware base to a service base. Leasing won't work. Most people who need access wouldn't qualify, and necessary hardware and software upgrades require short amortization cycles. The "free PC" is a return to the central computing model, but with two changes: It is offered to the public, and it is fundamentally mobile. A service-based approach that uses PC servers connected via radio modems can give everyone access to e-mail, faxing, accounting, word processing, and the Internet, plus secure personal data storage, for about $20 a month. This approach recognizes bandwidth limitations by placing the central processor close to the user at the local ISP and connecting everyone by radio-frequency cells. Using templates stored in the "free PC" rather than applications to do most tasks reduces local processing and the amount of data transmitted. Internet usage is the bandwidth hog in the model, but if you strip out the graphics, the data stream becomes small. The "free PC" will provide mobile access but will not replace the PC for more intensive computing uses. -- Gary Tripp

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Inbox

## Inbox

## MMX Misaligned

On reading your article on MMX performance optimization ("Programming Strategies for Intel's MMX," August), I find the example stack prologue code on page 64 does nothing to cause 64-bit alignment, only 32-bit alignment. The alignment mask should be 0FFFFFFF8, not 0FFFFFFFC.

Jan Bottorff

janb@pmatrix.com

You are correct. The assembly code listing in the text box "Maintaining Stack Alignment contained an error and, as a result, aligns the stack to 32 bits. In order to align the stack to 64 bits, the alignment mask should be 0FFFFFFF8, as shown below.--Bev Bachmayer, Intel Corp.

Prologue:

*push ebp ;save old frame ptr

*mov ebp, esp ;make new frame ptr

/sub ebp, 4 ;make room for stack ptr

(and ebp, 0FFFFFFF8 ;align to 64-bits

*mov [ebp], esp ;save old stack ptr

*mov esp, ebp ;copy alignment ptr

&sub esp, FRAMESIZE ;allocate space

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Inbox

## Inbox

## Fixes

Due to an editing error in "Adieu, Pentafluge...Hello Cyrus" (August), we described Jerry Pournelle's new Cyrix 6x86 machine as having an "EIDE CD-ROM drive running off an Adaptec Ultra SCSI board." We meant to say it has an EIDE CD-ROM drive, and a 4-GB Fast SCSI-2 hard drive running off an Adaptec Ultra SCSI board.

Due to an editing error in "Future Watch" (Bits, August, page 28), we wrote: "Because it runs at only 70 nanoseconds, EDO RAM incurs wait states at higher speeds." The sentence should have said: When running at 70 nanoseconds, EDO RAM incurs an additional wait state in systems with 66-MHz or faster bus frequency.

In our news story "Cyrix 6x86 Matches Pentium" (Bits, September), we neglected to include the SYSmark/32 benchmark results for a baseline Cyrix 6x86-based PC, without 64-MB cache. That number, 159, is comparable to the score of a 200-MHz Pentium Dell, which pegged a 161.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Bits

## Bits

"Self-Help Software to the Rescue

Call-avoidance software helps companies improve customer support and reduce expenses.

Dave Andrews

New programs for the Web let beleaguered technical-support departments reduce costs and improve service by helping users help themselves. Tech-support calls are the bane of the computer industry. They cut into profits -- as much as $20 per call -- and often make frustrated users wait, usually at their own expense. To reduce the number of support calls a help desk has to field, companies are turning to a new breed of product known as call-avoidance software.

Expert systems are not new: Companies have used them for years to help their support personnel find solutions more quickly. The new trend is to put answers directly into the hands of the user, potentially bypassing the tech-support phone call altogether. And the new vehicle for delivering that knowledge is -- you guessed it -- the Web.

"Call-avoidance programs such as our Web Advisor and Knowledge Builder won't solve every problem out there," says Keith Loris, vice president of development at ServiceSoft (Needham, MA), which recently released its first authoring tools for building Web-based problem-solving systems. "But they can reduce the number of phone calls a technical-support department has to handle. They can also ensure that the answers users get are consistent."

Some call-avoidance software goes a step beyond telling users how to fix a problem: Instead, the program fixes the problem automatically. For example, SystemWizard, from SystemSoft (Natick, MA), will detect, diagnose, and, in some cases, automatically fix common PC problems. SystemWizard, which should start appearing in several vendors' Win 95 and NT PCs by the end of this year, comprises several components, including a client application with a built-in local knowledge base of problem/resolution data, a server that provides a second level of support, and a knowledge builder for use by a PC vendor or MIS department to add solutions as new problems occur. If SystemWizard doesn't find a solution in the local database, the program can dial up a server, either over the Internet or the phone lines. The server can also automatically fix the problem by downloading a software solution or making some other modification.

By including a prebuilt database of solutions in SystemWizard, SystemSoft also eliminates a potential drawback to expert systems: the amount of time required for an organization to develop a comprehensive help system.

"Authoring is clearly the biggest issue," says Keith Sturdivant, manager of advanced support technology at Microsoft, which is increasing the number of self-help solutions it puts on the Web. "Maintaining the content and ensuring that the information is accurate and current in the database is important. And if you have a broad range of issues to address, as we do at Microsoft, that becomes much harder to deal with."

One difficulty is that technical-support people are often too busy solving the latest customer problem to sit down for half a day or even an hour to get information out of their brain and into the expert system. Writing a self-help program that solves problems for people who have little or no inkling about what is causing their technical difficulties still involves extensive work, even when using authoring tools that require little or no programming.

"Providing a solution for a user who doesn't have any idea what's wrong requires pretty intense authoring," says Erik Stackhouse, technical-support representative at Internet service provider UltraNet (Marlboro, MA), which is currently developing solutions using authoring products from ServiceSoft. "In that situation, you have to ask the user a

lot of questions

. There are so many factors involved that, from an authoring standpoint, it might be more work than it's worth." This is why companies such as UltraNet often start with a self-help system that specifically addresses a subset of common problems that can be easily solved, usually by an intermediate or advanced user. Situations involving more complex questions, novice users, or a computer that can't even get onto the Net will still require a voice call.

But even if the first implementations of Web-based self-help systems divert only 20 percent of incoming tech-support calls, this would be a huge improvement. And many vendors say that after an initial pilot phase, they plan to roll out larger, more comprehensive applications that will eventually handle 50 percent or more of incoming calls. In those situations, it's critical that call-avoidance authoring tools be able to integrate with legacy problem/resolution databases and call-tracking programs. And here the Web may again play an important role. A browser can be a single access point to a myriad of data sources, provided those databases can export into the Hypertext Markup Language (HTML) format. "If you're making the effort to author, you want it to be accessible to as wide an audience as possible," says UltraNet's Stackhouse. "Doing it on the Web is probably the best way to make this work on a large scale.

Web Self-Help Sources

Advantage kbs:

Phone: (908) 287-2236

http://www.akbs.com

Internet:

http://www.akbs.com

Inference:

Phone: (415) 893-7200

http://www.inference.com

Internet:

http://www.inference.com

ServiceSoft:

Phone: (617) 449-0049

http://www.servicesoft.com

Internet:

http://www.servicesoft.com

SystemSoft:

Phone: (508) 651-0088

http://www.systemsoft.com

Internet:

http://www.systemsoft.com

## Service Solutions

Programs developed with ServiceSoft's tools provide users with several possible solutions, with the most likely presented at top.

## Visual Resolution

Problem resolution can be more visual than with a phone call, as shown in this application using Inference's Casepoint.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Bits

## Bits

## Geek Mystique

Jason Krause and Win Treese

By our count, viewers watching the Summer Olympics on TV were, on one night, inflicted with 91 ads between 8 p.m. and midnight. Of those 91 ads, seven (about 8 percent) listed Web addresses. The Web-aware advertising companies were Reebok, Kodak, NBC, and Xerox and IBM (both twice). The next day, in the Boston Globe, we counted 121 display ads, six (5 percent) of which had Web addresses.

Other Web Statistics

Estimated percentage of adults in the U.S. using the Web: 7.7

Estimated volume of sales generated by the World Wide Web in 1995 (in millions of dollars): 436

Projected sales to be generated by the Web in 1998 (in millions of dollars): 46,000

Number of U.S. states with organized programs for schools on NetDay '96: 27

Number of Internet service providers worldwide (as of July): 3054

Estimated size of Internet access market in 1997, in billions of dollars: 2.5

Proposed tax on Internet access providers serving Tacoma, Washington: 6 percent

Number of U.S. states taxing on-line services: 6

Number of domains in .COM: 316,271

Number of private Internet providers in Egypt: 7

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Bits

## Bits

## Yeah, But

A controversy swirling around the release of NT 4.0 involves Microsoft's limiting to 10 the number of computers that can connect simultaneously to NT Workstation. To support more than 10 people, you have to use the more expensive NT Server, which sells for about $1100. Microsoft officials say they are justified in this practice, since they have not tested NT Workstation to ensure it can support heavy usage (for example, as an Internet Web server).

Yeah, but this practice puts other vendors of Web server programs at a disadvantage. Microsoft provides a free Web server program with NT Server. Microsoft's 10-user licensing restriction essentially prevents other vendors from selling Web software that runs on the less expensive ($319) NT Workstation at an overall cost that's less than NT Server. Competing on the NT Server field means Microsoft's competitors have to play against a free product.

Microsoft can put whatever restrictions it wants on its products. If people want to use NT to host Web sites, they can upgrade to NT Server.

Yeah, but Microsoft's policy will make customers who want to use NT as a platform for Web servers pay more. And other vendors say NT Workstation easily supports more than 10 users connected simultaneously to a Web site. They also argue that Microsoft already backed down from its plan to build the 10-user limitation into the NT Workstation software. But then why did Microsoft reintroduce the limitation by putting it into its licensing agreement?

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Bits

## Bits

## Security Gets a New Face

Russell Kay

Here's a twist on security that gives new meaning to the word "facetime." The old definition of facetime involves trying to remember people's names as you mingle at parties. But for the U.K. company Visage Development, facetime refers to an authentication mechanism that requires users to recognize a series of faces before they can access their computers.

Instead of asking a user to remember a password or carry an authentication token, the Visage program presents a row of three faces, some of which the user has learned to recognize. Faces are typically 16-level gray-scale images, 50 pixels square, and each has a number. The faces appear for about a second before they're covered up by a masking image that hides the pictures from bystanders. Then another row of faces appears for a second and is covered up. Finally, a third row (

see the screen

). The user types in or clicks on the three numbers of the faces recognized; this is verified, and access is granted or denied.

The faces are taken from a database of generic faces. Each time, the three key faces appear in different positions, and the surrounding faces are randomly selected from the rest of that database.

Visage requires an initial training period of five to 10 minutes, during which the user chooses three faces from the image database, then practices recognizing those faces. What's innovative about Visage is that it's a genuine one-time password that requires no extra hardware, does away with password changes and the attendant administrative hassles, and is easier than ever for users. No smart cards, no challenge-response number pairs, and no fingerprint readers are required. In one test, a user who left on maternity leave returned six months later and was able to successfully log in right away. Tests conducted by University of Cardiff psychologist Hadyn Ellis have verified the reliability and recallability of facial recognition as an authentication mechanism. Another test involved one group of people using Visage and another using personal identification numbers (PINs). After three months of no usage at all, the subjects were tested on their recall: Faces scored 100 percent, PINs 0.

The strength of Visage is based on our ability to recognize a face almost instantly (i.e., in about 20 milliseconds), combined with our inability to describe it in words that would let someone else pick out that same face from a group of similar ones. Also, the number of faces displayed per row, the number of rows in the grid, and the number of matches required, can all be configured to individual situations. Asking the user to pick three faces from five rows of four faces each and then to repeat with a new grid provides enough security to meet the standards of the British Computer-Electronics Security Group.

The company (contact William Visick, +01442 230471; fax +01442 212142; bvisick@cix.compulink.co.uk) is primarily interested in licensing the Visage technology, not in developing user-level products itself. Visage is currently available for NetWare 3 and 4, and a Windows NT version is nearing completion.

$One Picture's Worth a Thousand PINs

_Visage asks users to recognize faces, rather than remembering personal identification numbers.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Bits

## Bits

## Future Watch

Coffee, Tea, or FTP?

Dave Andrews

Communications for air travelers in the future won't be so disconnected or rely so heavily on battery-powered notebooks. Delta Air Lines (Atlanta, GA), in partnership with Olin Aerospace Company (Redmond, WA), has already begun testing its first in-seat power supply system. Passengers on the airline's Spirit of Delta Boeing 767 can sit down, plug in their computers, and not worry about battery power. Other airlines are also evaluating similar in-flight power systems.

Further out are communications systems that would let airplane passengers browse the Web live. Systems such as Airview, from a company called The Network Connection (Alpharetta, GA), combine video entertainment, catalogs, PC games and applications, and possibly Web access. With Web access, travelers could send e-mail or browse competitors' sites. However, before live Web access is possible, the satellite network that planes currently use for in-flight phone and fax services will need upgrading. And there's another matter. "Before deploying any next-generation communication system," says a spokesman for United Airlines, "we're going to take a close look at how much weight they add to the airplane.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Bits

## Bits

/Vendors Battle Over Next Internet File System

Steven J. Vaughan-Nichols

Browser wars, step aside. The next battle looming in cyberspace is over which file system will provide the underpinnings for better file transfer and group collaboration services on the Internet. Such a file system, whether from Sun or Microsoft or some other vendor, would improve upon the Internet's current HTTP and FTP.

Sun's proposed new standard, the Web Network File System (WebNFS), is just what the Web needs, claims Brian Croll, director of marketing for Solaris Servers at Sun. "The Internet is like a dirt road with a lot of potholes. One of these potholes is the slow speed of file transfers," Croll says. An advantage of WebNFS is its superior performance over FTP and HTTP for transferring large blocks of data, Sun says. WebNFS also lets you edit documents instead of simply viewing them as you do in today's browsers. This read/write capability will allow vendors to develop applications that let you collaborate with others from within your Web browser or Web-enabled application, without having to cut and paste text from the browser into another program.

Sun's NFS has been the TCP/IP file distribution standard for more than a decade. Not tied to any architecture or operating system, NFS is the glue that holds together heterogeneous file systems. Until recently, there hadn't been an open implementation that would work consistently over Internet connections. But with Sun's submission of WebNFS to the Internet Engineering Task Force as a proposed open standard, that's no longer true.

WebNFS springs ahead of the Net's hypertext (HTTP) and data transfer (FTP) protocols because neither of them are network file systems. HTTP must constantly close and open sockets to transfer information, and both HTTP and FTP require high latency between packets. WebNFS cuts down on both the interprocess communication and latency factors. This results in WebNFS offering block file transfers that are up to 10 times faster than the current versions of HTTP and FTP, Sun claims.

WebNFS already has powerful supporters, including Oracle and Spyglass, who are incorporating it into their browsers. Auspex, IBM, and Sequent plan to include WebNFS in their Web servers. Sun, of course, is putting all its resources behind WebNFS. The most visible sign of this support is the Netra NFS file servers, which depend as much on WebNFS as they do on HTTP for data transfer.

However, two prominent names are missing from the list of WebNFS adopters: Microsoft and Netscape. HTTP and FTP leave much to be desired for seeking, reading, and writing operations, agrees J Allard, a program manager at Microsoft. But Microsoft's remote file access protocol, called Common Internet File System (CIFS), complements HTTP. CIFS is based on the company's service message blocks (SMBs),which are already used in existing network components of Windows and NT, Allard notes, as well as on Unix.

Allard finds Sun's WebNFS speed claims to be somewhat disingenuous. "Byte Read-Range and HTTP connection keep-alive is evolving HTTP into a rival for WebNFS," he says. According to Allard, it may be too late to expect the entire Internet community to make a fundamental shift from HTTP to a new standard for file transfers.

Netscape, usually a staunch Sun ally, is still evaluating WebNFS, according to Andreas Cook, product PR manager. "Even if we turn it down now, we may use it in the future," he says.

"The big powers of the Web will fight over WebNFS. If Sun is successful, adding WebNFS will require many companies to retrofit their servers and browsers," says Ross Rubin, senior analyst for Jupiter Communications (New York City), a research firm that covers consumer on-line services and the Internet.

WebNFS is a threat to Netscape, says Stephen Auditore, president of Zona Research, an Internet market research house. "WebNFS plus Java is a direct competitor to HTTP and HTML," he says. "If Sun is successful in replacing the existing infrastructure, all the other major Web companies are in serious trouble." According to Auditore, Netscape is balking because WebNFS/Java would undercut all its technology dollars.

As for Microsoft, "Redmond already has its own distributed file system oriented to the NT environment and SMB, and they would love to see it expanded onto the Net," Auditore says. After all, whichever company controls the standards also controls the marketplace: WebNFS's success or failure could drastically influence Sun's and other companies' revenue streams.

Will WebNFS become the Net standard? "A lot will depend on whether Sun can gain the mind share of people using other third-party HTTP servers," says analyst Rubin. "If someone ports WebNFS to popular freeware servers, like Apache, it will be a matter of time until people start hacking together WebNFS add-ons for both Netscape's and Microsoft's browser and server product lines." If that happens, then the Web could be completely reinvented with WebNFS as its standard.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Bits

## Bits

## Bug of the Month

cc:Mail: Not OK

A BYTE editor found this interesting dialog when attempting to read new e-mail using cc:Mail 2.01 under Win 95. After the editor logged in, cc:Mail announced that he had new mail. When the editor attempted to read the new e-mail, the dialog

message shown

appeared. When he attempted to close the dialog box, he got the dreaded ringing-bell error sound. Clicking on another application minimized the dialog, and attempting to read cc:Mail caused another instance of the same error message. Now bells were ringing in stereo. The quick-and-dirty solution: Close cc:Mail and all other applications, reboot, and try again. The next time, everything worked as expected.

mailto:edejesus@bix.com

Send yours to

edejesus@bix.com

## cc:Mail Death Knell

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Bits

## Bits

-Photo Quality Arrives for Low-Cost Printers

Jon Pepper

Ink-jet printers were once the poor substitute for people who couldn't afford a laser printer. Now, these inexpensive devices are delivering much that laser printers can't, including near-photorealistic images at a fraction of the price.

Improvements in ink formulations, dot-placement accuracy, and better software are all combining to produce the best-looking color

ink-jet output

o yet for personal desktops. And the prices are coming down to staggeringly low levels for this type of output.

An excellent example is Epson's Stylus Color 500C, which puts the company's 720- by 720-dots-per-inch (dpi) output technology in a printer expected to sell for about $279. The 500C produces sharp black text, but the real attraction is the photo-quality output. Samples printed on coated stock were as close to conventional photographs as we've seen from a color ink jet, regardless of price. The Epson prints black text at up to 4 pages per minute (ppm) and color at about 1 ppm or slower.

Hewlett-Packard is countering with its midrange model, the 693C. This printer produces laudable photo-quality output in its basic mode, but HP has added an optional ($49) photo cartridge for even higher-quality output. Inserting the photo cartridge in place of the black ink cartridge produces a much wider range of possible colors, resulting in smoother and better looking output. The results we saw were very impressive, making the HP competitive with the Epson, though it is somewhat more expensive ($349) and does not come ready to work with a Mac.

Canon's latest iteration of its BubbleJet technology is the BJC-4200, which prints at 720 dpi for crisp, lifelike images. Canon offers specialty neon inks for the BJC-4200, though it has no photo-specific inks like HP. List price is $399. Canon's BJC-240, also new, sells for $179, but it's slower than the BJC-4200: 4 ppm in black and white and way under 1 ppm in color

Lexmark's latest, the Color Jetprinter 2050 ($299), prints black or four-color output at 600-dpi resolution. The company rates its speed as up to 5 ppm in black and 2 ppm in color. Lexmark offers an accompanying line of special paper for high-quality photographic reproduction.

These color ink jets aren't perfect. They are slower than laser printers when it comes to high-volume black-and-white output, and they can be very slow when producing photo-quality color pages (as much as 3 minutes or more a page). Still, at these prices, they make color printing very affordable.

## Color Ink-Jet Printers

F Text Color Resolution Cost Photo

E Speed Speed Color

Epson Stylus Color 500 4 ppm 2 ppm 720 x 720 $279 Yes

Canon BJC-4200 5 ppm 1 ppm 720 x 360 $299 Yes

DHP DeskJet 693C 3 ppm 1 ppm 600 x 600 $349 Yes

LexMark Color 5 ppm 2 ppm 600 x 600 $299 Yes

JetPrinter 2050

9Note: HP and Canon require optional cartridges for true

photo color output.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Bits

## Bits

## Survey

Internet/Intranet Survey

## Survey Results

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Bits

## Bits

%New Products Make Backing Up Easier

Jon Pepper

Most PC users look forward to backing up their files about as much as they look forward to a visit to the dentist. They know they have to do it, but they would prefer not to. A new round of products seeks to make the system-backup chore a little less painful.

http://www.iomega.com

With its Zip drive, Iomega (801-778-1000;

http://www.iomega.com

) made backup peripherals, if not the process itself, fashionable. With 100-MB data cartridges, a cool design, and the right price (under $200), the Zip became a best seller, with a claimed installed base of more than 2 milion units. Now, Iomega and others are evolving their backup products into devices that perform a multitude of operations, such as exchanging large data files, archiving, protecting hard drives from viruses, and many other functions. Iomega has followed its 1-GB Jaz drive ($499) with a new version of its tape-backup line, called the Ditto2GB, that offers an intuitive user interface, 2-GB storage capacity, and $149 drive price ($20 per additional tape).

http://www.syquest.com

Syquest (510-226-4000;

http://www.syquest.com

; sales@syquest.com), known for its tape backup products, counters with its EZFlyer, a 3-1/2-inch 230-MB removable-cartridge hard drive ($299). The EZFlyer offers more storage than the Zip, but it's also more expensive. The media itself is inexpensive at $29.95. The EZFlyer is available in both parallel and SCSI versions.

Only about 5 percent of PC users currently have some type of backup or archive device, according to Jim Porter, president of Disk/Trends (Mountain View, CA), a market research firm. "It is too early to tell what technology will dominate, but I am inclined to think none will take over a very high percentage of the PC base," Porter says. "It is like life insurance: People don't need it until they are dead, and they feel the same about backup against failures." However, when the dark day comes that your hard drive fails, you will wish you were among the fashionable minority that uses a backup product.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Bits

## Bits

3Book Review: How Free Should Internet Speech Be?

Mark Schlack

Sex, Laws, and Cyberspace by Jonathan Wallace and Mark Mangan; Henry Holt & Company

If you believe, as I do, that free speech should prevail on the Internet, you'll find this book a friendly and informative aid the next time you argue this subject. You won't, however, find it a comforting one.

Authors Jonathan Wallace and Mark Mangan take on disturbing denizens of the Net to show why the likes of snuff fiction writers and bomb makers should not be used as excuses for restricting the Internet. Civil-libertarian-minded readers will be chilled to the bone -- and their convictions tested -- upon reading about the university professor who posted, in an open newsgroup, fantasies of raping and murdering a female student.

Keeping the Net accessible will ultimately place a greater responsibility on all of us to counter that which we find offensive by social, instead of legal, means. In the above case, the authors argue persuasively that prosecuting the professor for conspiracy to commit the acts he'd written about was misguided; more effective and entirely justifiable was his removal by the university from his teaching post.

After an admirable attempt to boil down the legalese of several landmark court cases, the authors conclude that we should treat the Net as a series of printing presses and book stores. They chose this metaphor carefully: A long history of U.S. Constitutional law extends the fullest protection of the First Amendment to those two institutions. In contrast, virtually every advanced communications technology, from telegraph to television, has in some way been restricted by the government.

I found the printing press/book store comparison useful; it cuts through the colorful attempts by some people to portray the Internet as an invasive, irresistible deluge of information. On the contrary, it takes an act of will to connect to the Internet. And this paradigm leaves a place for responsible filtering by on-line services and parents (and room for argument about just what "responsible" means).

Mangan and Wallace sound the alarm about the political and commercial forces who hide behind outmoded arguments to gradually roll back freedom of speech. The Net has the same chance of moving humanity forward as did the first books. Also, like the printing press, new electronic media will disseminate communications ranging from the objectionable to the subversive to the broadly acceptable.

mailto:"mschlack@bix.com"

Mark Schlack is BYTE's editor in chief. You can send mail to him at

mschlack@bix.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Bits

## Bits

.Book Review: Practical Help for the Disabled

Rick Cook

Adapting PCs for Disabilities by Joseph J. Lazzaro; Addison-Wesley Publishing; ISBN 0-201-48354-8; $39.95

The personal computer is a powerful tool for opening the world to people with disabilities. How to make it happen is less obvious -- and the subject of this book.

The focus and tone are relentlessly practical. Joseph J. Lazzaro (an occasional contributor to BYTE) is less concerned with theory than with what you can buy and use today. You'll find a surprising range of hardware and software to aid people with impaired vision, motor skills, or hearing. The descriptions that make up most of the book (and the shareware and demo programs on the accompanying CD-ROM) summarize the capabilities of each product well enough to let you make a preliminary judgment on its usefulness.

Software developers aren't forgotten. The book includes a developer's guide for writing accessible software; it's full of tips on how to design programs that don't shut out people with disabilities. As Lazzaro demonstrates, a little thought in the design phase can make the difference between software anyone can use and software that excludes people using nonstandard I/O. If you know someone who is disabled, or if you are disabled yourself, Adapting PCs for Disabilities is invaluable.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Bits

## Bits

## Web Address COMbat

Steven J. Vaughn-Nichols

While the Internet community wrestles with implementing the new version of the Internet protocol that increases the number of possible IP addresses, another struggle is taking place over the shortage of domain names. The situation stems from the fact that Network Solutions Inc.'s InterNIC controls more than 90 percent of all domain names in this country, including the top-level domains such as .com, .edu, .gov, and .net. With such a limited number of domains, the selection of good domain names appears to be shrinking.

http://www.netcreations.com/

But is there really a shortage? Rosalind Resnick, president of NetCreations (Brooklyn, NY;

http://www.netcreations.com/

), an Internet software and marketing company, doesn't think so. The problem of companies who can't get their favorite name into the domain of their Web address is analogous to trademarks, she says. "If someone already has your name [in their Web address], then you have to come up with another name. After all," Resnick points out, "in the real world, you can't start up a fast-food chain called McDonald's because that's already been trademarked."

http://www.alternic.net

But that doesn't stop people from wanting just one name and no other for their domain. In that sticky sort of situation, a vendor can turn to AlterNIC (

http://www.alternic.net

), which lets a company get the key words it wants in its Web address by using alternative top-level domain names. By giving enterprises more opportunities to have the name they want, AlterNIC argues, it fulfills consumers' desires and helps prevent businesses from slugging it out over who gets what domain name.

Sounds good, but there's a storm looming. InterNIC believes it is the sole gatekeeper of top-level domain names and that attempts by other companies to infringe on that responsibility interfere with its legal right to control domains. Whether AlterNIC is successful in freeing up top-level domains is an open question. But it seems certain that as more companies put marketing and sales operations on the Web, some opening up of top-level domains is certain to happen.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Bits

## Bits

## Datapro Report

Unix Survey: Users Like Reliability, Scalability, and Performance

Mary I. Hubley

While many users are including Microsoft operating systems in their purchasing plans, that doesn't mean they are downsizing their plans for Unix. According to Datapro's 1996 International

User Ratings Survey

on Unix and Open Systems, Windows NT is used in 38 percent of the organizations surveyed, and 23 percent more are planning to add NT this year. However, Unix remains popular due to its flexibility, scalability, and power, with which Microsoft currently cannot compete.

NT is the logical upgrade path for organizations that have outgrown Windows, and NT is making major inroads into Unix's low-end server market. Over the past two years, Unix vendors have reacted to market shifts caused by NT by moving to the high-end server market. For example, SCO, once considered the premier low-end Unix vendor, now markets its OS as an enterprise-class product for client/server and host-based systems.

Although users like Unix's reliability, high performance, scalability, interoperability, and client/server support, they also complained that Unix systems still cost too much, and that installation, ease of use, and user interfaces could be better. One version of Unix that received high marks for affordability is Linux, which is available for free or for a nominal CD-ROM charge. The Linux ratings cannot be considered statistically valid, but it's interesting to note that the OS scored quite well in ease of use, development tools and utilities, and of course price. It didn't score as well as the others in scalability. One reason could be that ports of Linux to RISC processors are newer to the market than versions for Intel-based PCs.

Over the years, one common complaint with Unix has been that it's too expensive. If Linux had been available 10 years ago, one can't help wonder what its impact would have been.

## Unix Results Summary

Product IBM Digital HP-UX SCO* SunOS/ System V Linux

; AIX Unix Solaris

Number of responses 181 81 224 202 297 114 33

Client/server 3.5 3.6 3.7 3.4 3.9 3.5 3.4

support

Development 3.1 3.2 3.4 3.1 3.6 3.1 3.8

tools/utilities

Interoperability/ 3.6 3.7 3.6 3.2 3.9 3.5 3.7

communications

Performance 3.6 3.9 3.8 3.4 3.7 3.7 3.6

Scalability 3.6 3.5 3.8 3.2 3.7 3.7 3.1

Security 3.2 3.3 3.3 3.2 3.2 3.3 2.8

User interface 3 3.2 3.4 2.7 3.2 2.8 3

Ease of installation 2.9 3.1 3.2 2.8 3.2 3 3

Ease of use 3.1 3.3 3.3 2.9 3.1 3.1 3.4

Price 2.7 3 2.9 2.8 3 2.9 4.7

Reliability 3.6 3.7 3.9 3.4 3.8 3.8 3.8

Maintenance/support 3.4 3.3 3.6 2.9 3.3 3.4 3

Overall satisfaction 3.3 3.4 3.5 3.1 3.5 3.3 3.5

Ratings are on a 5-point scale:

<1 = poor, 2 = fair, 3 = good, 4 = very good, 5 = excellent.

** (Unix, Xenix, Open Desktop, OpenServer)

http://www.datapro.com

Mary I. Hubley, principal analyst. For more information on Datapro Information Services: (800) 328-2776; (609) 764-0100;

http://www.datapro.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Bits

## Bits

4CD-ROM Review: Use Multimedia to Learn Multimedia

Jason Krause

With today's new point-and-click authoring tools, anyone can toss together a multimedia project. But mastering the text, audio, video, hyperlinks, and varied production skills often required in creating a CD-ROM, Web page, or business presentation is another matter. The Sonic CD-ROM for Desktop Audio Production focuses on one special aspect of multimedia: sound.

The disc offers a thorough lesson in

audio production

basics, and it makes good use of plentiful examples. This product will be most useful for technicians who want to polish their sound skills.

Another valuable CD-ROM for audio production is the IEEE's Standards in Computer Generated Music. This CD offers essays and documents concerning desktop music publishing, MIDI, high-level music programming, digital audio, 3-D sound, multimedia, and computer-assisted instruction.

The amount of information varies from subject to subject. The CD may disappoint people interested in a specific angle (e.g., only one study covers 3-D sound). Overall, however, this disc delivers practical information for audio developers on a wide variety of topics.

## Product Information

The Sonic CD-ROM for Desktop Audio Production

Company: AP Professional

Phone: (800) 321-5068

http://www.hbuk.co.uk/app/approf.htm

Internet:

$http://www.hbuk.co.uk/app/approf.htm

Price: $44.95

Standards in Computer Generated Music

Company: IEEE

Phone: (800) CS-BOOKS

http://www.computer.org

Internet:

http://www.computer.org

3Price: $49.95 for IEEE Computer Society members

$69 for nonmembers

## Let the Sound Begin

4The Sonic CD covers techniques of audio production.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Bits

## Bits

## Web Cameras Hit the Road

Dave Andrews

http://www.microplex.com

http://www.axisinc.com

A new type of diminutive network gadget -- cameras that snap images you can view with a Web browser -- could start showing up in some unusual places, like highways and hallways and even your front door. Current network cameras from Microplex (800-665-7798;

http://www.microplex.com

) and

Axis Communications

(800-444-AXIS;

http://www.axisinc.com

) are 1-pound devices that can take color images and put them on self-contained Web servers at a rate of about 1 frame per second. Anyone with a standard browser can view those images, opening up all kinds of possibilities for remote surveillance and other types of applications that can take advantage of the Web.

The drawback with current versions of the Axis and Microplex products is they don't have serial ports; instead they use standard Ethernet UTP connections to a network. Both companies say they are planning new versions with serial ports. That would let a modem transmit the images over a standard phone line, thus providing much more flexibility in camera location. Who knows? Maybe one day commuters will rely on Web-enabled cameras placed along popular travel lanes to avoid rush-hour traffic; or maybe high-tech workers on the coast will use a network camera to see when the surf is up.

$Time Will Tell What Uses These Have

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Bits

## Bits

## Vendors Ready Better E-Mail Boxes

Dave Andrews

If you live in e-mail, your house may be about to undergo a major reconstruction. Lotus, Microsoft, SoftArc, and others have renovated their mail client programs to make them more tightly integrated with contact management, scheduling, and other business tasks.

Microsoft's new Outlook program, which will be part of the next version of MS Office, offers a wealth of new features (for more information, see the What's New Software Preview "E-Mail Meets Personal Information Management"). And Lotus has similar developments in the works for cc:Mail (

see the screen

cc:Mail Release 7's new capabilities include basics like the ability to apply styles to individual words in a message. More comprehensive design overhauls include a user interface that more closely resembles that of Notes Mail and tighter synchronization for remote users. The interface for creating rules for handling messages automatically has been improved, and you can test those rules before making them operational. Remote users can access files on the LAN, and new message-sorting capabilities help you tailor your mailbox interface.

SoftArc's FirstClass 4.0 (slated to ship in early 1997) will integrate new calendaring features with its e-mail, collaboration, and other capabilities. Further in the future, expect closer integration of e-mail and telephony, SoftArc officials say.

## New Face for E-Mail

The new cc:Mail finally lets you apply styles to individual words.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Bits

## Bits

## A Dark Cloud of Bugs

Bruce Brown

n, president of BugNet, discusses beta software, the proliferation of bugs, and their threat to the industry.

Dave Andrews

BYTE: How did you decide to get into the bug reporting business?

Brown: About two years ago, I saw that compatibility, glitches, and bugs were going to become an increasing concern to PC users. It seemed clear to me that the bowl of jelly was going to shake when Windows 95 and Windows NT 4.0 hit. I felt this was going to create a need for products and services that would help users get over -- or around -- these problems. At the outset, we published a traditional newsletter, but the newsletter is now 100 percent electronic on the Web. We also sell a database of bug/fixes in HTML, and are syndicated in a half dozen major dailies, as well as InfoWorld and Computer Currents. Recently, BugNet also signed an exciting new mass marketing deal with Online Interactive.

BYTE: With all the free beta software available today, do you feel that people are more willing to put up with more bugs these days?

Brown: That's a complex question which has to be addressed from a couple of angles. Because of the need to generate revenue and sustain stock prices, there is a lot of pressure on vendors to release products as quickly as possible, and to deal with bugs later. This is a fact of the business, and if anything, it is becoming more prevalent, even though vendors obviously don't want to put out products which are so buggy that they depress sales. Beta is a little different issue, but it also plays into the software vendors' almost maniacal desire to curtail support costs. Beta looks like a dream come true to the vendors because they can say up front, "We're not going to support this," and at the same time they derive certain testing benefits from users who use a beta product and inform the company of problems. But for the user, beta software can pose a threat that is real and significant.

BYTE: Why is beta software a threat?

Brown: The threat is that installing beta can screw something else up in your system. For example, in a bug story that BugNet recently broke, it was revealed that Internet Explorer 3.0 Beta 2 running under Windows 95 replaces one or more system files with versions which are incompatible with some commercial products that you pay money for. So you install the beta, and all of a sudden, some commercial products may not work as they should. And you go to the vendor you paid money to, and now the vendor may very well say to you, "Our product doesn't work because you are running someone else's beta program, and we don't support beta. You're on your own." Users don't realize that the "free" program that they download may in fact cost them a lot of time and money.

BYTE: Do you think there will be any change in this situation?

Brown: This gets into an issue that I think is really societal. We have come to a point where the expectations of computer users are changing, and there is actually conflict between the expectations of the traditional users of PCs, the PC enthusiasts, and the new PC users, normal people who may not want to spend their weekend screwing around with their printer drivers. To make the PC an everyday appliance, this large new group must be satisfied. But these folks expect the darn thing to work when they turn it on, like a toaster or a razor, and of course the PC fails this basic test far too often. So even though the industry as a whole may be doing a better job in the minds of traditional users, it may be doing worse in the minds of the users that the vendors most want to reach. And this, in turn, may be part of why such a shockingly small percentage of PC sales are made to first-time purchasers.

BYTE: It seems like your site and database have quite a few Win 95 bugs. Is it the mother of all bugs?

BB: Well this is an interesting question. The number of issues involving bugs or compatibility problems is huge with Windows 95. In our database, the BugMaster database, Windows 95 now makes up over half of it. That means Windows 95 equals everything in Windows 3.x plus all of the Apple and OS/2 and assorted other bugs that we have in there. In terms of bulk or volume of issues, it's more than anything else combined. [laughs]. And that's over the last two years.

But that's only part of the picture. One of the things that BugNet does is we try to provide software vendors the carrot and the stick. We hold the vendors feet in the fire for issues that are causing problems and make them turn and give their attention and come up with solutions. But at the same time, we want to praise them and give them credit for those situations where they do respond, where they do a good job, or they give it their attention and actually provide their users with a useful workaround or a fix. So one of the things we do is to measure the success rate of all the major vendors, in terms of their success in providing fixes or workarounds that their users bring to them. We do this on an annual and quarterly basis with all the vendors.

We also have taken a look at Windows 95 compared to Windows 3.x. We look at it in terms of the success rate of Microsoft and its allied vendors in providing solutions for this tidal wave of problems which have emerged in connection with Windows 95. And what we see is there are a really large and significant number of issues here which have arisen over the last 12 months, but the success rate in dealing with these issues is at this point a little better than it was with Windows 3.x. So on the one hand, yes there have been a lot of problems, but on the other hand, Microsoft and its allies are doing a better job of shepherding their users through the minefield and helping them over the fence than was the case before Windows 95. You can't just look at the thousands of issues that have arisen with Windows 95 and its applications and say "Aha." That's only part of the story. The other part of the story is what vendors do in response. I think vendors are doing a somewhat better job than they did before. Whether that means the users are better or worse off depends on the person's individual situation and whether you've got a problem you can't come up with a solution.

BYTE: What about call avoidance software, where users can go to a database or Web site and find solutions to some of the more generic or mundane bugs, while letting the technical support people concentrate on the more challenging bugs? Do you feel these will provide relief to the poor beleaguered technical support departments?

BB: [laughs]. Well they certainly are poor and beleaguered. I believe in call avoidance software, we are a vendor of exactly that type of product. In one sense, the BugMaster database is the broadest collection of bug fixes for the PC world. We sell it to individuals and corporations alike with the thought that this system can allow users in many situations to come up with solutions to a problem before they have to waste time, either calling in the case of a corporation, their own IS or IT people, or in the case of an individual, spending 45 minutes on hold waiting for a technical support person to pick up the phone. We are in the business of doing this and I believe it can help. I have sheaves of documents and letters of correspondence who thank us for this service, folks for whom we save an hour of their time. And I know that it can work. The thing that I have not seen proven to my satisfaction yet is the automatic systems. And this is something that's arriving. I don't want to speak against them because it's a great idea and holds tremendous promise, but I haven't actually seen it at work.

BYTE: By automated systems, do you mean something that actually goes in to your PC and makes changes for you, instead of just telling you what to do?

BB: Yes. I have some concern that people may find that this may cause more problems than it fixes, or can even create problems where problems didn't exist. The variety of the hardware/software stew that people are trying to combine is so extreme that it's very hard to create a system that can automatically deal with it. Also, I think these self-help systems may be more useful to expert users. Less experienced users may still require personal assistance from a human.

BYTE: So sending a novice user out to the Web may not be the best solution. Instead, the answer should be don't have bugs?

BB: Right, but that's impossible, because the human hand inevitably carries with it imperfections. I think some users or some situations will always require human attention. I just don't think there's any way around it.

BYTE: Are there any ways to improve customer support, are there any deep dark secrets that people ought to know?

BB: First, folks should know there are differences in terms of the level of support they give and their success in providing solutions for the problems their users bring to them. I refer to the first quarter of 1996, we did a break out or comparison of the major vendors. Look for example at Corel, which is a vendor primarily of graphics software, with the exception of the suite they recently bought from WordPerfect, and Adobe, which is more or less in the same part of the forest. Our figures showed Corel had about an 85 percent success rate, and Adobe's was under 50 percent for the first quarter. This is not the only criteria that an individual can bear in deciding whether to buy an Adobe or Corel product, but it is a consideration. I think folks should realize that these programs are not cookies that come out of a cookie cutter. And vendors have their own personality, their own priorities, their own staffing situations, and their performance is different.

BYTE: How do you measure that, the 85 percent versus 50 percent?

BB: We collect all issues and we determine for each one whether or not an acceptable workaround or fix is available. What we require for an acceptable workaround is essentially a situation where the vendor comes up with a solution that preserves functionality. So an acceptable solution would not be to tell a customer, "The way to avoid this problem with the printer is to not use this printer." The functionality must be preserved in some fundamental fashion to avoid whatever it is that is causing the difficulty. We are the only organization that I know of that makes any measure of the success of the vendors in this area. And I don't think it's the be all or end all, but I think it is a very significant measure of what's going on in the industry and what kind of experience that a purchaser, whether corporation or individual, may have six months down the road. The other thing that people ought to know is that we feel that people that have paid good money for software, sometimes $500 or $600, should insist on a satisfactory answer, and if you can't get it from the first person, ask for their supervisor or a second-level tech. Make them stay on the phone until you get the thing resolved. I think there's a tendency psychologically for users to come on bended knee to the vendor, as if to the Oracle of Delphi. The basic relationship is one where the vendor is the provider of services and the user is a purchaser who should be able to insist on satisfactory performance from the product they paid money for. We get dozens of bug reports daily and a lot of them, at least 90 percent of the time, the user turned the bug in, they wrote the vendor e-mail, and they are not getting a response. And one of the reasons vendors may be afraid of BugNet is we will sometimes go to the vendor and shake that tree. This is a sad reflection on the industry, because it means that people that are paying good money can't get minimum service out of the people that are taking their money, and they have to go to someone else like us. I mean, this is part of our business, but sometimes I take a step back and I have to shake my head, because it shouldn't be this way.

BYTE: What is the gnarliest bug you have heard of?

BB: I've become a connoisseur of these kinds of things. I respond on a different aesthetic. My favorite is one that BugNet broke is the one in Bill Gates The Road Ahead book, which will bomb some machines if you try to run it at more than 256 colors, which is of course the color palette standard of three or four years ago. And then you find that Microsoft doesn't support the thing. But that's kind of a humorous thing. An example of a more serious bug is one that's ongoing right now, is the major incompatibility problem between WordPerfect for Windows 7's address book and Microsoft Exchange. I've gotten a lot of reports of problems with this. And the most recent that we got was that Corel was working to fix this.

But one sophisticated guy got enmeshed in this problem and said he spent 90 minutes with Corel, and the tech rep had him uninstall and then reinstall Exchange as part of the troubleshooting process. That resulted in him no longer being able to run Exchange, at which point the Corel tech rep told him that he was on his own, because Corel does not support Exchange. This is another example of one thing screwing up another thing where the user is left holding the bag. And this is not as it should be. To me, this is symptomatic of the sort of thing that troubles me. It generates ill will, it generates all sorts of negative fallout which the industry as a whole will have to deal with down the road.

http://www.bugnet.com/~bugnet

For more information, see

http://www.bugnet.com/~bugnet

## Bruce Brown, BugNet President

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Blasts From The Past

## Blasts From The Past

## 5 Years Ago in BYTE

.Promises, promises...and not much delivered.

Desqview/X from Quarterdeck finally brought the X Window System to DOS, to tepid response from the market. Microsoft admitted that NT wouldn't support OS/2. Bill Gates said sales of special Presentation Manager versions of Excel and Word were dismal. Meanwhile, Lotus released the first version of 1-2-3 for Windows and the Mac. Lotus later turned its back on the Mac version. And rifts started appearing in the Advanced Computing Environment when it turned out you really would need at least two versions of source code and four compilers. Meanwhile, Compaq's new systems promised Plug and Play, but not The Plug and Play. Compaq's version mostly promised that you'd be able to upgrade the processor.

Another important flash from our industrious news department, this time in

## October 1991

NEWS: Microbytes: Quarterdeck X-Tends DOS with Desqview/X

by Ellen Ullman

With the long-delayed release of Desqview/X from Quarterdeck, the X Window System finally comes to DOS. X is closely identified with Unix, but the windowing protocol was designed from the outset to offer device independence, and there never was anything inherently Unix-based about X. It already runs on VMS and Macintosh platforms.

Why would DOS users want X? The answer is interoperability. With an X server running on a DOS machine, you can remotely run programs on any machine on the network--including Sun workstations--while interacting with the program using your own DOS machine. And Unix users can remotely run all the character-based DOS programs. You can display Unix/X and DOS applications simultaneously on either platform, and you can copy and paste between Unix and DOS programs. What more could you want?

You would probably like to run Windows 3.0. You can, but only locally, and not in tandem with X applications.

Desqview/X consists of an upgraded Desqview 2.3 with the ported X server and Xlib and Xt libraries. Quarterdeck also includes its own X-compliant Desqview Window Manager. DWM is relatively small (approximately 70 KB) compared to the separately priced window managers based on 0SF/Motif (700 KB), Xol Open Look (1.5 MB), and Xview Open Look (300 KB). Support for NetBIOS and IPX is included, with an optional package available that provides support for TCP/IP, DECnet, and PC NFS.

Current Desqview users will find Desqview/X familiar. The desktop has been updated with the new DWM three-dimensional look, but the commands are unchanged. The X version adds some new features, including the ability to customize menus. Desqview/X also provides an icon editor and a new graphical program manager, tentatively called Appman.

A significant feature of Desqview/X is built-in support for scalable fonts from Adobe. The new X desktop will come with Adobe Type Manager, so when you resize a DOS window, the text will stretch or shrink to fit.

X applications are known for their large memory requirements, and Quarterdeck has gone to some trouble to accommodate the memory problem on the DOS platform. Desqview/X is built on top of Quarterdeck's new memory-extending QEMM 6.0. And to reduce the amount of memory that applications require, Desqview/X incorporates a new shared DOS extender and shared libraries from Rational Systems. Programs share a single instance of the DOS extender and X libraries, which are implemented as virtual, shared 16- and 32-bit OS/2-style dynamic link libraries.

## October 1991

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Blasts From The Past

## Blasts From The Past

## 10 Years Ago in BYTE

Preservation is better for archaeologists than computer companies, or why the II GS didn't make a bigger splash.

The Apple II GS received mixed reviews. We liked its new 16-bit processor but worried that the GS cost too much and didn't offer graphics superior to the Amiga or Atari. Also, we wondered why Apple would invest such energy in preserving 10-year-old technology.

## October 1986

's issue contained the following Product Preview written by former senior technical editor Gregg Williams, and Rick Grehan. See Rick's newly expanded "Code Talk" column (last page of print issue; also here on the website):

PRODUCT PREVIEW: The Apple II GS

The 65C816 processor brings the Apple II into the 16-bit world.

by Gregg Williams and Rick Grehan

Editor's note: The following is a BYTE product preview. It is not a review. We provide an advanced look at this new product because we feel it is significant. A complete review will follow in a su bsequent issue.

The Apple II has a curious history. It was originally designed by Steve Wozniak and Alan Baum in 1976 as a homebrew computer that squeezed maximum features out of minimum parts. Over the years, it evolved into the Apple II+, then the IIe, then the IIc. Once, Apple tried to kill it off with the Apple III (which itself died) and, later, with the Macintosh and the IIc. Despite corporate attempts to ignore it and retard its evolution, the Apple II continued to bring in the major part of Apple's income. Finally, in May 1984 Apple acknowledged the reality of the Apple II's success when it titled its day-long introduction of the Apple IIc "Apple II Forever." (Despite Apple's wishes to the contrary, the IIe continued to sell better than the nonexpandable IIc--people wanted their expansion slots.) By mid-1985, though, the Apple II began to lose its sales appeal, and Apple engineers were already working on a product called, at various times, Phoenix, Columbia, Cortland, and Granny Smith: the Apple II GS.

The Apple II GS looks back to the past and forward to the future, and the machine might best be summarized by saying that it takes a giant step in both directions. Its new styling and modularity (see photo 1) foreshadows a day when Macintosh and Apple II products will use the same keyboard and 3-1/2-inch disk drives.

System Description

Here are the most important features of the Apple lI GS:

Apple II compatibility: The Apple II GS will run most Apple II software and expansion cards. It can run at normal Apple II speed or at a higher rate that makes most software run two to three times faster. [Editor's note: In this article, "Apple II" refers to the traditional Apple II computer as defined by the Apple II, II+, lIe, and IIc.] The Apple II GS composite video signal has been corrected so that it will be recorded correctly by a videotape recorder. Apple lie owners can upgrade to complete II GS compatibility by replacing the motherboard and back/bottom plate with a II GS retrofit kit.

A 16-bit, 6502-compatible processor: With a 16-bit address bus and 8 "bank address" lines, the Western Design Center's W65C816 can address 256 banks of 64K bytes each, for a total of 16 megabytes. It can also go into a 6502 mode, where it emulates the 65C02A used in the Apple lIe and IIc. The processor's accumulator, stack pointer, and all its registers are 16 bits wide, and its instruction set includes 11 new addressing modes.

Greatly expanded memory capacity: The machine's architecture reserves space for 8 megabytes of user RAM and 1 megabyte of system ROM. It comes with 256K bytes of RAM, 128K bytes of system ROM, and 64K bytes of dedicated sound-wave-form memory, but you will have to wait for new programs to use most of the memory above the first 128K bytes. Apple currently has plans for 1- and 4-megabyte expansion cards, although an 8-megabyte card is possible.

New graphics capabilities: The Apple II GS adds two "super hi-res" graphics modes: 200 by 320 pixels with a 16-color palette and 200 by 640 pixels with a 4-color palette: the colors come from a color set of 4096. The machine can use up to 16 palettes per screen and change palettes and resolution on a line-by-line basis. Programmers can use two experimental modes: a 640- by 200-pixel, 16-color (with restrictions) palette mode, and a high-speed "fill mode" variation of the 200 by 320, 16-color mode.

New sound capabilities: The 32-voice Ensoniq Digital Oscillator Chip (DOC), used in the Ensoniq Mirage sampled-sound music synthesizer, and system firmware can drive the chip to produce up to 15 musical "instruments."

Mouse, keyboard, and disks: A one-button mouse and a detachable keyboard with keypad are standard equipment. The Apple II GS does not have an internal disk drive, but you can daisy-chain up to two 800K-byte 3-1/2-inch drives and two 140K-byte 5-1/4-inch drives to the disk drive port on the rear panel. The system software will come on 3-1/2-inch disks, which silently but forcefully indicates Apple's intent to phase out the 5-1/4-inch floppy disk.

The Toolbox: Application programs can use built-in code (some in ROM, some in RAM) to provide a mouse-driven desktop environment and orderly use of system resources.

The Finder: Finder software, supplied with the basic system, allows users to interact with disks and files using windows, icons, and a mousedriven cursor (as popularized by the Apple Macintosh).

Desk accessories: The Apple II GS makes available Macintosh-like desk accessories; some are available from all programs, and others work only with programs specifically designed for the Apple II GS. The Control Panel, accessible from any program, allows the user to change the date, slot assignments, operating speed, and similar parameters.

New languages and tools: For the software developer, Apple will offer a 6502/65C02/65816 assembler and versions of C and Pascal; the three languages share a standard editor and linker and allow object code modules from any source to be used together. For the hobbyist, Apple has extended the Apple IIe monitor to work in the Apple II GS 16-bit environment and has added new functions to it.

No enhanced, built-in language: Like the Macintosh (and unlike most other computers), the Apple II GS contains no built-in language (such as Microsoft BASIC) that interacts with the machine's new features. Applesoft BASIC is available in system ROM, but it has no way of directly interacting with the new Apple II GS features.

A new 16-bit operating system: ProDOS 16 extends Apple's ProDOS (which runs on the Apple II+, IIe, and IIc) to be the standard Apple II GS operating system; it runs on the 65816 in native 16-bit mode, is functionally similar to the 8-bit ProDOS, and shares an identical file structure with ProDOS. Apple has also made slight modifications to the 6502-based ProDOS so that it will run on the Apple II GS's Apple II emulation mode; this operating system is named ProDOS 8.

Two Machines

The case of an Apple II GS contains, in a sense, two machines: the full Apple II GS, with all its memory and new features, and a 128K Apple IIe. Much of this article will explain the design elements that allow these two "machines" to exist together. You may want to refer to figure 1, which is a block diagram of the Apple II GS.

The Mega II

The Mega II is a custom CMOS chip containing about 3000 gates and a 2K-byte by 8 ROM (for the character generator). It replaces the following chips from the Apple IIe and IIc: character generator ROMs for eight languages, several TTL chips that perform logic functions, and the MMU (memory management unit), IOU (input/output unit), TMG (timing generator), and GLU (general logic unit) custom chips.

In previous Apple II designs, the refreshing of memory was tied directly to the Apple II video mode. The Mega II includes an 8-bit counter for refreshing the 128K bytes of (slow) memory associated with the Apple IIe/IIc model; it does five cycles of RAM refresh during the horizontal retrace of each video scan line and refreshes the 128K bytes of memory in 3.25 milliseconds. By taking care of RAM refresh, the Mega II chip opens the Apple II design to new video modes that were impossible before.

Speeding UP the II GS

The Apple II GS designers had many conflicting goals. They wanted to make a machine that runs as much existing Apple II software as possible and to make it run software (both old and new) faster than on an Apple II. In order to accomplish this, they changed the memory map and employed a technique called shadowing. Figure 2 shows the Apple II GS memory map. Remember that many memory areas in the Apple II are special; the memory-mapped "soft switches" in the C000-C0FF hexadecimal region control many key functions, interaction with the peripheral cards occurs through locations in the C100-CFFF hexadecimal region, and several areas of memory determine what graphics and/or text are shown on the video display. Many of these areas are limited by the original Apple II design to being accessed at 1 MHz. A straightforward expansion of the Apple II design would put the slow memory in banks 00 and 01, their location in the Apple IIe and IIc. (A bank is defined as the 64K-byte address space from hexadecimal location XX0000 to XXFFFF. Actually, the two 64K-byte banks of memory in the Apple IIe and IIc are called simply the main and auxiliary banks, but you can imagine the bank select as the 17th bit of the corresponding Apple II GS memory address.)

Instead, the designers put the slow memory (with the corresponding control circuitry) in banks E0 and El hexadecimal and assigned fast memory to banks DO through 7F. This gives you 8 megabytes of linearly addressed memory (something new to Apple II programmers), and all existing Apple II programs (which must run in banks 00 and 01) will run in fast, not slow, memory, (The 65C816 runs at 2.8 MHz, but the overhead of dynamic memory refreshing slows the average speed of RAM memory access to about 2.5 MHz; ROMs are accessed at the full 2.8-MHz speed.)

This scheme gives us speed but not compatibility. Programs that do I/O using the peripheral slots and video display write to addresses in banks DO and 01, but the hardware they need to interact with is tied to the slow memory in banks ED and El hexadecimal. How can we get this scheme to work?

The answer is shadowing. The Apple II GS engineers designed the Fast Processeor Interface (FPI) custom chip to monitor any attempt to write to the area to be shadowed (in bank 00 or 01), then slow itself down to 1 MHz and write to the location and its equivalent in bank E0 or El hexadecimal. In many locations (video display memory, for example) read operations from the same location have no timing constraints and can proceed at the higher 2.5-MHz speed. Because other locations (like the ones associated with peripheral card I/O) must always be written to and read from at 1 MHz, the speedup of Apple II software depends on the memory locations the software uses.

Note that this scheme gets two things done. First, it allows existing Apple II programs to write to bank 00 and 01 locations at the correct speed and have the associated hardware perform the expected interaction. Second, it allows programs to execute in the fast 2.5-MHz memory, slowing down only at specific times.

By default, the Apple II GS shadows text page 1 in both banks, hi-res pages 1 and 2 in bank 00, a 32K-byte area (2000-9FFF hexadecimal) in bank 01 used for the new super hi-res graphics modes, and the 4K-byte section of memory at CXXX hexadecimal in bank 00. However, programs can access a "shadow register" that can disable shadowing in individual areas. This speeds up program execution and allows the program to use the unshadowed areas and their EO/El (hexadecimal) counterparts for other things.

(The bit that shadows the CXXX [hexadecimal] area also uses the actual memory in locations C000-CFFF hexadecimal to hold the 4K-byte alternate language-card areas for both banks. When this shadowing is turned off, the language cards of banks 00 and 01 are no longer present, and the 65C816 sees a completely linear address space in banks 00 and 01. [However, all Apple system software requires the CXXX shadowing to be enabled.] The FPI chip controls shadowing and, in general, the intercepting and translating of all the address requests from the 65C816.)

Slots and Ports

The II GS's expansion slots are identical in function and configuration to the Apple IIe's slots with the exception of one added signal, /M2SEL, which appears at pin 39, replacing the 6502 SYNC signal. /M2SEL is an active-low signal that indicates when the II GS is executing at slow speed (1 MHz) and the address lines A0-A1 5 are valid (i.e., the II GS is talking to the slow RAM or I/O). In some ways, this signal is redundant with the old IOSEL and DEVSEL signals in the II+/IIe, and boards that use these signals should have no problem operating in an Apple II GS. Control-signal generation and clock-signal buffering on the ports are handled by the SlotMaker custom IC.

Associated with each I/O expansion slot are built-in circuits and firmware that form an "invisible" port. The default settings for the seven slots are

Slot 1 serial printer port

Slot 2 serial modem port

Slot 3 80-column display

Slot 4 mouse

Slot 5 3-1/2-inch disk drives

Slot 6 5-1/4-inch disk drives

Slot 7 AppleTalk

It is as though you had an Apple IIe with boards for all the above devices already plugged in. Unfortunately, this wealth of built-in interfaces carries with it some restrictions, the most severe being that if you have an expansion board you want to run in your II GS, you must give up the built-in port of whatever slot you plug the board into. (You use the Control Panel to choose whether a slot is using its associated default port or a plug-in board: this information is retained in battery-backup RAM.) The serial ports of the Apple II GS appear on the rear of the cabinet in the form of a pair of 8-pin mini-DIN connectors. They are pin- and signal-compatible with the serial connectors on the back of the Macintosh Plus--in fact, the USART in the II GS is the same as the Macintosh's: a Zilog 8530 serial communications chip. If you access the serial ports through the firmware, they "appear" identical to the Apple Super Serial Card (SSC) even though the SSC uses a different UART, a 6551. This has dire consequences for software that talks directly to the serial-port hardware on Apple IIs equipped with SSCs. Such software--and this includes practically all of the commercial communication packages-- will certainly fail on the II GS.

Programs that bypassed the SSC's firmware did so to break the speed limitations of the firmware's noninterrupt-driven, unbuffered I/O routines, which were virtually useless for dependable communications at 1200 baud. The II GS's serial port firmware solves these troubles: It is interrupt-driven, and each serial port has input and output buffers that default to 2K bytes each but can be set to up to 64K bytes each.

The Apple II GS's built-in disk port is a 19-pin miniature D-type connector in the middle rear of the machine. You can daisy-chain up to four drives, up to two 3-1/2-inch drives followed by up to two 5-1/4-inch drives. Owners of Apple IIs who might want to use their drives on the II GS can simply plug their Disk II controller into slot 5 or 6 and override the default setting for that slot.

Memory Expansion Slot

The Apple II GS motherboard has a special memory-expansion slot designed for a card with up to 8 megabytes of RAM and 896K bytes of ROM (bringing the system's total ROM to 1 megabyte). The RAM maps into banks 02 to 7F hexadecimal, and the ROM maps into banks F0 to FD hexadecimal. It is easiest to design 1- and 4-megabyte RAM cards (using 256K-bit by 1 chips and 1 megabit by 1 chips, respectively), but the II GS engineers said that, with a few extra chips for interfacing, you could design an 8-megabyte RAM card; however, since the machine is not designed to hold user RAM above bank 7F hexadecimal, an 8-megabyte RAM card would be unable to access the top two banks (128K bytes) of its memory.

SmartPort

SmartPort is a set of assembly language routines (held in firmware) for accessing block and (as yet undesigned) character I/O devices on the Apple II GS. The SmartPort routines provide support for 3-1/2-inch disk drives, a RAM memory disk (called the /RAM device), or a ROM memory disk (5-1/2-inch drives, though part of the daisy chain, are controlled by the Disk II firmware, and future hard disks can be designed to respond to SmartPort routines without being part of the daisy chain). SmartPort handles I/O in blocks of 512 bytes; since the routines permit up to a 4-byte block number, SmartPort can manage devices with storage capacities up to 2,199,023,255,552 bytes. SmartPort's basic functions include get device status, reset a device, format a device, read a block from a device, Write a block, and send control information.

Any I/O expansion card that adheres to SmartPort conventions will have signature bytes at specific locations in its on-board ROM. The II GS's firmware will hunt for and recognize these at boot-up time, just as ProDOS currently does on the Apple II.

As its name implies, the ROM disk is the equivalent of a RAM disk emulator in nonvolatile read-only memory. This could come in handy for keeping frequently used programs like assemblers, compilers, or the like on hand for rapid execution. The II GS memory space has eight 64K-byte banks set aside for ROM disk expansion, located just beneath the firmware ROM in banks F0-F7 hexadecimal.

Desk Accessories and the Control Panel

You can think of a desk accessory as a mini-application that can be run from within another program. Macintosh owners are already familiar with desk accessories -- those utility programs from the menu bar that appear when you click on the apple symbol. The II GS supports two types of desk accessories (with a tip of the hat, perhaps, to Coca-Cola): classic desk accessories (CDA) and new desk accessories (NDA). A classic desk accessory can be activated only by a keypress. Classic desk accessories can be run with older Apple II programs (such as Appleworks) and new II GS programs. A new desk accessory runs in the II GS's desktop environment and is available from a pull-down menu similar to the Macintosh's desk-accessory menu.

One classic desk accessory is built into the II GS: the Control Panel. You call up the Control Panel by simultaneously pressing open-apple-Control-Escape, which presents you with a menu containing the following system configuration options:

Display selects color or monochrome monitor, display width, and colors for text, background, and border.

Sound displays two "slider switches" used to adjust the II GS speaker's, pitch and volume.

Speed selects 1.0-MHz or 2.8-MHz ("normal" or "fast") operation of the 65C816 CPU.

Clock sets the II GS system clock time and date.

Options alters parameters of the II GS's keyboard: keyboard layout, keyboard buffering on or off, repeat speed and delay, and others.

Slots lets you indicate for each of the II GS's seven I/O slots whether the slot is running an "invisible" port or a plug-in board.

Other selections from the Control Panel let you set parameters for the serial ports and enable a RAM disk. You can use the Control Panel from within any program; we even used it in the middle of a disk access with no adverse effects.

Video Modes and the VGC

Because the Apple II GS emulates the Apple II, it contains all the text and graphics modes of the Apple II: 24 by 40 text, 24 by 80 text, 48 by 40 low-resolution and 48 by 80 medium-resolution graphics with 16 predefined colors, 192 by 140 hi-res graphics with 6 predefined colors, and 192 by 140 double hi-res graphics with 16 predefined colors and 192 by 560 monochrome graphics. (Apple claims double the above numbers for hi-res resolutions in the horizontal directions, but the numbers here more accurately reflect the true nature of hi-res graphics because Of the color limitations between adjacent pixels.)

As stated earlier, removing the banks E0 and E1 (hexadecimal) dynamic RAM refreshing from the video display circuitry makes new video modes possible. A new custom chip, the Video Graphics Controller (VGC), implements both old and new video modes as well as unrelated support functions for the built-in clock chip, the disk drives. the interrupt system and built-in chip and board testing routines. The VGC enhances current text modes by allowing the user to choose from the Control Panel the color (or gray scale value) of the text, its background, and the border outside the active text/graphics area. These modes are available only when using an RGB color or monochrome monitor.

Super Hi-Res Graphics

The new modes are called "super hi-res." Actually, there are three modes that can be used in four ways; two of them are pretty straightforward and useful, while the other two are more experimental.

Associated with the super hi-res modes is a 32K-byte chunk Of memory in bank El ranging from addresses 2000 to 9FFF (assume that the addresses in this section are hexadecimal and the quantities are decimal). The pixel map occupies the range from 2000 to 9CFF, an important set of pointers occupies locations 9D00 through 9DFF, and color palette information fills the remainder of the area, from 9E00 to 9FFF. (To get into these modes, write C1 hexadecimal to location C029, and write 41 hexadecimal into it to restore the Apple II modes.)

The pixel map contains exactly 32,000 bytes arranged as 200 rows of 160 bytes each. Apple II programmers, who have always struggled with a convoluted pixel-to-memory mapping scheme, will be surprised by the fact that the super hi-res modes are completely linear, with a row-first stream of pixels corresponding to an unbroken, increasing progression of memory addresses. In other words, the first pixel on the first line uses the high bits of location 2000, while the same pixel in the second line uses location 20A0(160 bytes later), and so on.

There are two super hi-res modes. Both have 200 lines per screen, but one has 320 pixels per line (see photo 2), while the other has 640 pixels per line. Since each line is represented by 160 bytes, each pixel has 4 bits of memory in the 320 mode and 2 bits in the 640 mode (see figure 3). This scheme gives you 16 colors in the 200 by 320 mode and 4 colors in the 200 by 640 mode, with no restrictions on the color of adjacent pixels (a problem that complicates the Apple II hi-res modes).

With the old Apple II hi-res modes, the electronic characteristics of both the Apple II and its video display determined the colors that were available; for example, the hi-res mode gave you the colors violet, blue, green, orange, black, and white. The Apple II GS, through the VGC chip, gives you more control over the colors in your graphic display. The super hi-res mode lets you choose your palette of 16 colors from a color set of 4096.

But which of these 16 colors are used in the 640 by 200, 4-color mode? The answer is all of them, the details of which lead us to one of the experimental super hi-res modes. The two bits of a pixel in this mode can have four values, so they are used in this mode to choose from 4 colors in the 16-color palette. Which 4 colors? Apple II programmers will recognize the answer as yet another convoluted video mode in the Apple II tradition: The 4 colors available for a pixel depend on its position within a byte (see figure 3b).

Palettes and Pointers

Actually, the Apple II GS defines a 512-byte area starting at location 9E00 hexadecimal; this area contains 16 color palettes of 32 bytes each, numbered from 0 to F hexadecimal. Each color in a palette is defined in 2 bytes, using 4 bits each to describe the red, green, and blue components of the color. The first byte contains the values for green (bits 7-4) and blue (bits 3-0); the second byte contains the red value (bits 3-0), with the remaining bits set to zeros.

Why are there 16 palettes? Because each scan line can use any of them in any order. This brings the total number of colors that can appear onscreen to 16 x 16 = 256 colors. Expect to see some uncharacteristic graphics as soon as programmers learn their way around the machine.

The final surprise of the super hi-res graphics modes comes from the pointer area. The pointer byte at location 9D00 hexadecimal corresponds to the top line of the video display, with each successive scan line getting the next byte: 9D01, 9D02, ... , etc. This byte is read and interpreted during the horizontal retrace of the previous video line.

Within each pointer byte, bits 3 through 0 determine which of the 16 color palettes is to be used. Bit 4 is not used and should be set to 0. Bit 6 does nothing if set to 0. If it and an interrupt register at address C023 hexadecimal are both set to 1, the VGC generates an interrupt at the beginning of the line; this will allow the advanced programmer to wring extra performance out of the super hi-res screen by altering palette values (or making other useful changes) "on the fly"--that is, while the machine is drawing the video display, Bit 7 determines the resolution: 0 for 320 pixels, 1 for 640.

This leaves bit 5, which does nothing if set to 0 but which activates the final, experimental super hi-res mode, called fill mode (see photo 2). In fill mode (which works in 200 by 320 resolution only), you have access to 15 colors (numbers 1 through F, hexadecimal). A pixel value of 0 means that its color is the same as the last nonzero pixel to the left. In other words, pixels with the values

3 0 0 0 2 0 0 0 0 0 0 0 9 0 0 0

would appear as colors

3 3 3 3 2 2 2 2 2 2 2 2 9 9 9 9

and you could change the large area painted with color 2 to, say, color 5 by changing one pixel (the fifth one) from a 2 to a 5. (Note that the first pixel in a line must always be nonzero.) This mode will be good for drawing large areas and changing their colors very quickly.

Sound

The heart of the II GS's sound system is the Digital Oscillator Chip manufactured by Ensoniq and used in the Mirage digital synthesizer. The DOC is attached to its own personal bank of 64K memory into which programs store wave tables that the DOC uses to generate sound. This memory is accessible only through special registers in the Sound General Logic Unit, a custom chip that acts as an interface between the DOC and its memory and thus allows sound generation to proceed independent of other processing in the Apple II GS. Additionally, registers within the Sound GLU chip regulate the gain of the II GS's audio amplifier, providing control of the speaker's volume.

The Ensoniq DOC contains 32 oscillators that the II GS firmware operates in pairs to generate a tone. Since one of the oscillators is used by the system to generate a time-slice interrupt for the DOC, the Apple II GS can produce up to 15 independent tones simultaneously.

A wave table is a series of bytes in the DOC's memory such that each byte represents the instantaneous value of the amplitude of the sound's output waveform. An oscillator on the DOC will step through this table fetching bytes and passing them to an on-chip digital-to-analog converter that produces the analog waveform that, after filtering, goes to the speaker. This technique allows generation of a theoretically limitless range of sounds, bounded only by the amount of memory available. The limit of 64K dedicated memory is no impediment, since the II GS allows you to fill one portion of a wave table while the DOC is fetching information out of another. The II GS passes the unamplified monophonic signal of the sound system's output to a mini stereo phone jack on the back panel of the machine. This output is capable of driving a pair of Walkman-style headphones or, with the proper adapter cable, the input of a stereo amplifier. The designers of the II GS have also provided a connector on the motherboard that gives direct access to several useful DOC signals, including an unfiltered audio output, channel selection logic signals (can be used to implement eight independent audio channels), and an input to the DOC's analog-to-digital converter (for a sound sampler/digitizer).

The Apple II GS Toolbox

In the past, the Apple II could be almost completely described by its hardware features. The Apple II GS ends this tradition with its inclusion of significant amounts of system software in both ROM and RAM meant to be available to all programs. It is not accidental that these routines are similar in name and function to those in the Macintosh computer. The Mac toolbox is an elegant, powerful system proven to work and improved by two years of intensive use.

The Apple II GS toolbox implements the most useful Macintosh toolbox functions, though sometimes it does so in a different way; the Memory Manager, for instance, works quite differently from its Macintosh counterpart because of the way the Apple II GS's memory is divided into 64K-byte banks. However, the Apple II GS doesn't duplicate all of the Macintosh toolbox.

The code in the Apple II GS toolbox is divided into tool sets, and the individual routines are called tool calls. The tool sets that are in ROM are the Tool Locator, Memory Manager, SANE (Standard Apple Numerics Environment) Numerics, Desk Accessory Manager, Event Manager, Sound Manager, Integer Math Tools, Text Screen Tools, Scheduler, and Miscellaneous Tools. QuickDraw II is divided between ROM and RAM.

The remaining tool sets are stored on disk and loaded into RAM by the application that needs them. Once in memory. they are indistinguishable from tools stored in ROM. They are the Menu Manager, Window Manager, Control Manager, Line Editor, Dialog Manager, Scrap Manager, and Print Manager.

Tool Set Structure

The Apple II GS tool set has no fixed routine entry points and only four fixed addresses associated with its toolkits, yet any program can execute any toolbox routine in RAM or ROM, even if a routine is changed or moved to a different location after the program is written. Both tool sets and tool calls are numbered (starting with 1), and any tool call can be executed by the following assembly language sequence:

push inp1

|dx #CallID

js| Dispatch

This pushes any input onto the stack, loads the 16-bit X register with a call ID constant that has the tool call number in the high byte and the tool set number in the low byte, and does a subroutine jump to a fixed entry point. A high-level language would compile a normal procedure call as a series of 0 or more push instructions, followed by a jump to a different location that performs the above function while handling an extra 3-byte return value on the stack. The Apple II GS designers estimate that this type of call has an overhead of about 118 microseconds. Parameters can be passed in several ways, based on the needs of the individual routine: on the stack, in a known block of memory, or in the A, X, and Y registers.

To increase the usability and extensibility of the II GS, its designers provided an identical but parallel structure that allows programmers to build and use their own tool sets without "borrowing" tool set numbers that Apple may later use. The only difference between the two is a different entry point, "UDispatch" instead of "Dispatch."

Toolkit Memory Usage

Many tool calls need their own memory -- sometimes page zero locations to speed up their execution, sometimes other memory for passing parameters or sharing or storing data. The Apple II GS designers resolved the conflicting memory needs of many different tool calls by regulating memory usage as follows: The program using the tool sets will itself allocate page zero memory. and tool sets will allocate the other memory they need by asking for it through the Memory Manager. They can then point to it with the WAPT (Work Area Pointer Table) entry reserved for that tool set, and their tool calls will always be able to access that memory in whatever way they wish.

QuickDraw II

QuickDraw II deserves mention because of its importance for desktop-based Apple II GS software. It is a tool set, partly in ROM and partly in RAM, that provides a standard set of useful graphics routines for drawing window/menu-oriented screens. Wherever possible and appropriate, it attempts to work equivalently to a subset of Macintosh QuickDraw routines. The pre-release documentation lists 146 QuickDraw II tool calls, of which 114 are listed as being the same as their Macintosh equivalents, 22 are listed as being similar, and 10 are entirely different or absent. The degree of consistency between QuickDraw and QuickDraw II will be very important to Macintosh software developers attempting to convert their software to the Apple II GS.

ProDOS

Apple has crowned ProDOS the operating system for the Apple II series of computers, and the company will be guiding ProDOS along a carefully controlled development path that proceeds as follows:

ProDOS 1.1.1 will continue to be supported for the Apple IIe and IIc computers and many ProDOS 1.1.1 programs will run on the II GS.

ProDOS 8, an altered version of ProDOS 1.1.1, will become the standard 8-bit operating system for the Apple II. It will work on the IIe, IIc, and II GS.

ProDOS 16 will be the 16-bit operating system used for Apple II GS software. Version 1.0, supplied with the machine at its introduction is built on a ProDOS 16 framework but is implemented by a ProDOS 8 core surrounded by a shell handling ProDOS 16-style calls. ProDOS 16 version 2.0 will be released in the first quarter of 1987.

The Finder

We did not see the Finder working when we saw the Apple II GS but its preliminary documentation describes it as "a combination Program Selector/Disk Utility for managing documents and directing traffic between the user and storage devices." It seems to be a pretty faithful imitation of the Macintosh desktop interface, with several exceptions.

First, the "Special" menu has two new items -- "Check Drives" and "Format." The first causes the Finder to update its knowledge of what disk is in each drive (remember that, in an Apple II system, you can change the floppy disk in a drive without the computer knowing what you've done). The second will eventually allow you to format a disk in either ProDOS, Apple Pascal, DOS 3.3, or Apple CP/M formats; the initial release, however, will only format disks for ProDOS.

Second, the Finder will interact most fully with ProDOS disks and programs. Since only the ProDOS operating system has subdirectories, only ProDOS disks will have folders in their windows. When you exit a ProDOS program, it will return you to the Finder.

Third, the Finder does not support custom file icons. Each icon will have a shape determined by its file type.

Finally, the Finder will support rudimentary printing of text files.

A future version of the Finder will probably add the Macintosh MFS (old) and HFS (hierarchical) disk formats, Apple Pascal 1.3, and Apple CP/M to the file types supported.

Apple Desktop Bus

The Apple Desktop Bus (ADB) is used for the generalized connection of the computer with up to 16 input devices daisy-chained to a single connector on the back panel: it currently supports multiple keyboards (for educational and other programs) and a mouse (ending the daisy chain), but the design can accommodate other kinds of devices. Devices are connected through a shielded 3-conductor cable using mini-DIN-4 connectors.

The ADB is controlled by a dedicated 8-bit processor called the ADB microcontroller (abbreviated here as ADBM); in addition, the mouse and keyboard are controlled by custom microcontrollers that interact with the ADBM. The ADBM and the intelligent devices "talk" on a bus where only the ADBM can issue commands: the devices reply as appropriate with data or requests for service.

In general, the ADBM handles low-level interaction with the keyboard, mouse, and other input devices, thus freeing the 65C816 processor from having to handle such tasks.

AppleTalk

Unlike any other Apple Computer product, the Apple II GS includes built-in AppleTalk code in RAM and ROM. Through the Control Panel, you can configure slot 7 as AppleTalk; the II GS then uses one of the two serial ports as its AppleTalk port.

The II GS implements the bottom two (of seven) levels of AppleTalk protocol; Link Access Protocol (LAP) and Datagram Protocol (DDP). Delivery protocol (DDP) also implements enough of the next two levels, Name Binding Protocol (NBP) and AppleTalk Transaction Protocol (ATP), to boot the II GS from a remote file server (thus allowing it to be used in a network environment without its own disk drive).

Pricing

The price for the Apple II GS had not been set at the time of this writing, but we expect the price for a starter system with one 3-1/2-inch disk drive and a monochrome monitor to be in the $1400 to $1600 range.

Compatibility

For many users, especially current owners, software and hardware compatibility will be the make-or-break factor in their decision to buy an Apple II GS. The II GS engineers did an incredible job of designing a new, more powerful computer that is largely compatible with the existing body of Apple II hardware and software. One engineer estimated the II GS's hardware compatibility at "about 80 percent" and its software compatibility at "95 to 99 percent."

Complete software compatibility is impossible, largely because of the completely unregulated way the Apple II has been programmed in the last 10 years. People wrote code that jumped into the middle of ROM routines, used machine language op codes that were unimplemented in the 6502 (but that are in the 65C816), and implemented countless copyprotection schemes, many of which depended on particular hardware details that were replaced in later Apple II designs.

The final verdict must wait until we get to test a production-line machine, but we tested several Apple II game and business programs and found two that fail trying to execute formerly unimplemented op codes (THE Spreadsheet and Serpentine) and one (HomeWord running under ProDOS 1.1.1) that doesn't work because the 65C816 does not completely emulate the way the 6502 wraps an X-register address from FFFF hexadecimal to 0000 (it wraps to 10000 hexadecimal).

Most peripheral cards that do not implement "phantom slots" (where a multifunction card appears to be several cards in different slots) will work, but some cards won't; we were told, for example, that the Mountain Computer Music Card set won't work because of the way it uses interrupts.

As with previous enhancements to the Apple II line, such differences cause problems for the first year or so, then they fade from consciousness as companies revise their products and users find patches or workaround measures for products that don't work. In general, the more recent your Apple II software or hardware, the more likely it is to run properly.

Caveats

We wrote this product preview in July 1986, after two days with the Apple II GS engineering staff, much study of seven volumes of developers' technical documentation, and subsequent telephone conversations with the engineers. When we saw the Apple II GS, the firmware was about to be "frozen," and the machine itself was in "final preproduction"; only minor changes are likely to be made at this point. We did not get to see the Finder software, but we had several hours of hands-on experience and ran several impressive sound and graphics demos.

(We wish to thank Rob Moore, Harvey Lehtman, and many other Apple people for their help.)

Conclusions

What do you say about such innovative energy that has been directed primarily toward preserving a hardware design that is 10 years old? The Apple II GS designers achievements are remarkable, but the burden of the classic Apple II architecture, now as venerable (and outdated) as COBOL and batch processing, may have weighted them down and denied them any technological leaps beyond an exercise in miniaturization. Also, the 65C816 may prove to be an IC of mixed blessings: While it does provide a means of supporting the 6502 within a processor that also operates in a 16-bit mode, to programmers it represents yet another instruction set that has to be learned and whose oddities will have to be dealt with.

The Apple II GS affirms several trends in microcomputer design that we should not ignore: improved graphics and sound, larger processor and memory capacity, and the use of a mouse and a desktop/icon/windows user interface. The machine also follows a trend but breaks new ground in the Apple II line by including large amounts of system firmware that is as important as the machine's new hardware features.

Because Apple perceives itself as a "premium label," its pricing will not be as aggressive as many users would like it to be. Apple is becoming -- dare we say it? -- more and more like IBM, selling more on name, reputation, and installed base of software and hardware (not a strong selling point, in the case of Apple II software) than on computing-power-per-dollar value.

The Apple II GS, hog-tied by Apple II compatibility, approaches but does not match or exceed current microcomputer capabilities. The 8086-like segmented memory of the 65C816 is not as elegant as that of the 68000, used in the Apple Macintosh, the Commodore Amiga, and the Atari 520ST. In addition, the 65C816 lacks the hardware multiply and divide instructions available in both the 8086 and the 68000 processors. The Apple II GS's graphics, though now competitive, do not offer any advantages over the Amiga's or the Atari ST's, nor is its price competitive with either. Its only clear superiority is in its sound capabilities, which for many buy ers will not outweigh graphics and price.

Ironically the Apple II GS will suffer from the traditional lack of software and hardware upon its introduction. Vendors will take longer than they expect to come out with new products, and many will enhance existing products for the Apple II instead of writing new software that fully exploits (and is limited to) the Apple II GS. Granted, a tremendous amount of software is already out there, but the Apple IIe and IIc will run it with fewer compatibility problems and at a significantly lower cost. As with new machines before it, people will buy the Apple II GS because they see the unrealized promise of its new features.

## October 1986

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Blasts From The Past

## Blasts From The Past

## 15 Years Ago in BYTE

Years before Team OS/2 tangled us up in Big Blue, we were impressed with IBM's new PC.

In their first good look at the brand new IBM PC, BYTE's editors were impressed and even surprised that Big Blue, known then for its big iron, could do such a swell job on a PC. We also ran a long tutorial on an up-and-coming new technology for PCs known as the local-area network.

Our review of the new PC showed that in

## October 1981

bigger was not always better:

FIRST IMPRESSIONS: The IBM Personal Computer

by Phil Lemmons

IBM (International Business Machines Corporation) has at last introduced the keenly anticipated IBM Personal Computer. Based on Intel Corporation's 8088 microprocessor, the new machine is slated to appear in stores this month, with various hardware options, at prices ranging from $1565 to more than $5000. Color graphics are built in, and up to 256 K bytes of user memory may be installed.

The hardware is impressive, but even more striking are two decisions made by IBM: to use outside software suppliers already established in the microcomputer industry, and to provide information and assistance to independent, small-scale software writers and manufacturers of peripheral devices.

The list of software sources includes Microsoft, Digital Research, Personal Software, Peachtree Software, Softech Microsystems, and Information Unlimited Software. For hardware configurations including floppy-disk drives, IBM will sell three different disk operating systems: CP/M-86 from Digital Research, the UCSD p-System from Softech Microsystems, and IBM Personal Computer DOS, developed by Microsoft in imitation of CP/M. IBM isn't trying to force the world to choose between the IBM DOS and other popular operating systems. The published documentation of IBM Personal Computer DOS will include the source-code listing of the BIOS (basic input/output system), and of the diagnostic programs executed automatically when the computer is turned on.

The hardware uses an interconnection scheme different from the industry-standard S-100 bus, but IBM doesn't want to exclude anyone from developing plug-compatible printed-circuit boards for installation in any of the vacant expansion slots inside the chassis. In fact, the company plans to publish a hardware manual with drawings and industry-standard specifications. IBM's attitude toward support for independent hardware and software efforts was summarized by Don Estridge, Director of Entry Systems Business for the IBM Personal Computer. "IBM will provide information for the existing cottage industry to design boards," Estridge said. "We're open to any software proposals."

General System Characteristics

The entry-level version of the IBM Personal Computer consists of the System Unit, which contains the 8088 microprocessor, a 40 K-byte built-in ROM (read-only memory) containing the extended version of Microsoft BASIC, a built-in speaker that can be programmed to play music, a power-on automatic self-test of system components, 16 K bytes of user memory in the form of semiconductor RAM (random-access read/write memory), a combination video-monitor and printer adapter, and empty space for two 5-inch floppy-disk drives. In this minimal configuration, the system uses an audio-cassette recorder for mass storage and an ordinary television set as a video monitor.

Not including the cassette recorder and monitor, the minimal system will sell for $1565. With a single 5-inch, 160 K-byte floppy-disk drive and 64 K bytes of user RAM, the price increases to $3005. An expanded business system with powerful color graphics, two floppy-disk drives, and an IBM-labeled Epson MX-80 dot-matrix printer costs $4500. In addition to the 40 K-byte ROM, the system has a 16 K-byte RAM buffer for graphics operations. None of the user memory is required by the system software.

Plug-in circuit cards of user RAM are available in three denominations: 16 K bytes ($90), 32 K bytes ($325), and 64 K bytes ($540). The user can increase the memory capacity to 256 K bytes using the available IBM boards and slots. (Outside companies could make a single memory board containing 256 K bytes of RAM, or expansion boards that contain even more.) All user memory is 9-bit, with one bit devoted to parity check. An edge connector on the back of the System Unit looks as if it is longing for a hard-disk drive, but IBM is mum on that possibility.

The 8088 processor communicates with memory and peripheral devices through an 8-bit data bus, but it conducts its internal affairs using the 16-bit instruction set of Intel's 8086 microprocessor. In the IBM Personal Computer, the 8088 operates at 4.77 MHz, with a cycle time for main storage of 410 nanoseconds; for access, the cycle time is 250 nanoseconds.

Together, the System Unit, keyboard, and a monitor make a very smart, full-feature terminal. A six-foot coiled cable connects the separate keyboard to the System Unit. You can adjust the keyboard's tilt toward you when it rests on a desktop, or you can hold it in your lap. The system supports both uppercase and lowercase characters, and all 83 keys have automatic repeat. Ten keys on the right side are for a numeric keypad and cursor controls, and ten special-function keys can be used for editing. The keyboard provides access to 256 characters, including all the ASCII (American Standard Code for Information Interchange) characters and many other characters useful for producing virtually any sort of graphics display.

IBM sells an 11-1/2-inch green-phosphor video monitor for $345. The monitor displays 25 lines of 80 characters each. You can adjust brightness and contrast or use software to activate underlining, high-intensity blinking characters, and reverse video.

With a color monitor, the IBM Personal Computer will support 16 foreground and eight background colors. In the medium-resolution graphics mode, screen resolution is 320 pixels (picture elements) across by 200 down. In the high-resolution graphics mode, resolution is 640 by 200 pixels. Text and graphics can be mixed, allowing you to label items in a graphics display.

One Centronics-compatible parallel printer port and one RS-232C serial I/O (input/output) port are standard. An asynchronous communications adapter ($150) enables you to connect a modem to the serial port.

IBM is even offering a Game Control Adapter ($55) that permits connection of user-supplied joysticks and paddles to the IBM Personal Computer.

Sales and Service

IBM's sales and service strategies show the computer giant's determination to develop quickly into a major force in the microcomputer market. Beginning this month, the company is marketing the Personal Computer nationwide in four ways:

through Computerland retail stores

through Sears, Roebuck and Company's new business-machine stores (IBM will train the Sears sales personnel)

through a special sales unit in the IBM Data Processing Division (for high-volume sales)

through IBM Product Centers, which will make provisions for installment purchases

Only four Product Centers exist now, but IBM has selected many more cities around the country as sites for future centers. "In the course of the next two years," said C B Rogers, Jr, IBM vice president and group executive of the General Business Group, "we expect to be fairly well represented."

IBM will offer a 5 percent discount on sales of 20 to 49 units, 10 percent on sales of 49 to 150 units, and 15 percent on sales of 151 units or more. Educational institutions will also receive discounts.

IBM's service plans should meet or exceed those offered by other microcomputer manufacturers. For a start, IBM offers a 90-day warranty. Owners can extend warranties to a full year for between 7 and 9 percent of the purchase price of various system components, or buy annual service contracts for 10 to 15 percent of the purchase price of components. For example, an extended warranty for the System Unit costs $88; a maintenance contract for the System Unit costs $112. For the System Unit, disk drive, and disk-drive adapter, an extended warranty costs $154, and a maintenance contract costs $196.

Service will be available at Sears, Computerland, and from the IBM Product Centers, regardless of where you bought the computer. Service contracts with the IBM Product Centers call for exchange of major system components. IBM will send a replacement keyboard, printer, or System Unit by courier within 48 hours of the owner's call.

Three Ways to Generate Software

Recognizing the advantage that an existing broad software base gives to CP/M-compatible, Radio Shack, and Apple computers, IBM plans to meet the problem headon with a three-part strategy.

First, when the Personal Computer reaches stores this month, it will be accompanied by a software offer including some application programs ready to run with IBM DOS. Here's a quick look at what IBM is offering:

IBM Personal Computer DOS. This CP/M look-alike from Microsoft offers the familiar "A>" prompt character along with features for copying files and disks, comparing files and disks, initializing disks, displaying a directory, renaming files, and other housekeeping chores. Although it has a debugger and a line editor, IBM DOS does not yet have an assembler. It seems safe to speculate that Microsoft is hard at work on that.

a cassette-level enhanced Microsoft BASIC interpreter that supports input/output instructions, use of the keyboard, display, light pen, and printer, and many editing and mathematical functions.

a disk-level Microsoft BASIC that provides extensions including more powerful graphics, date and time-of-day functions, and communication capabilities; the enhanced graphics include such features as point, circle, and get/put display, and increased light-pen support for design work ($40)

a Pascal compiler, also from Microsoft ($300)

VisiCalc, the electronic-worksheet program from Personal Software

Easywriter, the word--processing program from Information Unlimited Software ($175)

an asynchronous communications program ($40) (This is written in BASIC and is menu-driven; the menu includes an option for the Dow Jones Information Services, another for The Source, and another for teletypewriter-like communications. IBM soon will also offer a full subset of Mod-el 3270 emulation capabilities so that the Personal Computer can appear to larger IBM systems as an IBM 3270 terminal.)

general-ledger, accounts-payable, and accounts-receivable packages, from Peachtree Software, but with color and other enhancements for ease of use ($595 each)

Adventure, the fantasy-simulation game, from Microsoft ($30)

The second part of IBM's software-development strategy is to offer Digital Research's CP/M-86 operating system and Softech Microsystem's UCSD p-System (which includes UCSD Pascal). Purchasers of these operating systems will have access to many third-party programs as they become available. IBM says it expects the availability of these operating systems to provide the opportunity for many current applications to be transferred to the IBM Personal Computer with minimal modifications. This approach will enable owners of the IBM Personal Computer to use a tremendous amount of software originally written for other common machines. Users can have everything that IBM offers without giving up software for the other two operating systems.

The third part of the IBM software strategy is to establish its own Personal Computer Software Publishing Department. The new department will solicit software from outside authors, both professional and amateur. IBM will send software-submission information packets to anyone who writes to IBM Personal Computer Software Submissions, Dept 765, Armonk NY 10504. IBM will also encourage its employees to write software for the personal computer (on the employees' own time). Authors will receive quarterly royalties based on actual sales.

A Shaking Out?

For those of us who dislike giants, the IBM Personal Computer comes as a shock. I expected that the giant would stumble by overestimating or underestimating the capabilities the public wants and stubbornly insisting on incompatibility with the rest of the micro computer world.

But IBM didn't stumble at all; instead, the giant jumped leagues in front of the competition. Although the IBM Personal Computer has not (as of this writing) reached store shelves, it already seems to hold a firm position in the field. Its prices seem to compare favorably with available 16-bit S-100 systems. Furthermore, the cost of an IBM Personal Computer configured for word-processing is not much more than that of an Apple II Plus, an Intertec Superbrain, or most other 8-bit machines fully equipped for word processing. A superior machine from the start, the IBM Personal Computer should grow in capability as outside vendors begin producing peripheral devices and add-on hardware for special applications.

In fact, the only disappointment about the IBM Personal Computer is its dull name. One rumor claimed that IBM referred to this computer internally as the Acorn. To me, it looks more like a Mighty Oak.

At a Glance

Product Name

The IBM Personal Computer

Manufacturer

,International Business Machines Corporation

Information Systems Division

Entry Systems Business

FOB 1328

Boca Raton FL 33432

When Available

## October 1981

Where Available

6Sears, Roebuck and Company's business-machines stores

Computerland stores

IBM Product Centers

,IBM Data Processing Division (volume sales)

Components

System Unit

Size: width 20 inches, depth 16 inches, height 5.5 inches; weight

B(without disk drives) 21 pounds, (with two disk drives) 28 pounds

1Electrical needs: 120 VAC Processor: Intel 8088

Cycle Time: main storage, 410 nanoseconds; access, 250 nanoseconds

Memory: 40 K bytes of built-in ROM (read-only memory), 16 K bytes of

Guser RAM (random-access read/ write memory); expandable to 256 K bytes

Standard: keyboard for data and text entry; audio-cassette recorder

>connector; five expansion slots for memory, display, printer,

>communications, and game adapters; built-in speaker for music

@programming; power-on automatic self-test of system components;

DBASIC-language interpreter; 16 K bytes of user RAM (all user RAM is

9-bit parity memory)

Keyboard: 83 keys for data and text entry, 10 keys for numeric entry

Cand cursor control, 10 special function keys, and ASCII characters

Band special graphics characters (total 256 characters); automatic

Frepeat on all keys; adjustable typing angle; detachable six-foot coil

cable

Disk drives: up to two 5-inch floppy-disk drives, 160 K bytes each

Operating Systems

&IBM Personal Computer DOS (Microsoft)

CP/M-86 (Digital Research)

%UCSD p-System (Softech Microsystems)

-Software Available for IBM Personal Computer

;DOS BASIC interpreter (Microsoft) standard; extended BASIC

?interpreter (Microsoft) $40; Pascal compiler (Microsoft) $300;

VisiCalc (Personal Software) $200; Easywriter (Information Unlimited

Software) $175; General Ledger, Accounts Receivable, Accounts Payable

E(Peachtree Software) $595 each; asynchronous cornmunications support

$40; Adventure (Microsoft) $30

Hardware Prices

4System Unit, 16 K-byte RAM, keyboard $1265

%System Unit, 48 K-byte RAM, keyboard

4 single floppy-disk drive, disk-drive adapter 2235

4Monochrome video display 345

'Combination monochrome-display adapter

4 and printer adapter 335

4Color-graphics-monitor adapter 300

416 K-byte memory-expansion kit 90

432 K-byte memory-expansion kit 325

464 K-byte memory-expansion kit 540

4Disk-drive adapter 220

4Disk drive (5-inch floppy disks) 570

4Asynchronous communications adapter 150

4Game-control adapter 55

4Keyboard 270

## October 1981

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Core Technologies

## Core Technologies

!Windows 95: Aiding the Disabled

New Windows 95 features assist computer users who have disabilities.

Joseph J. Lazzaro

If you run an office staffed with more than 15 employees, you must comply with the Americans with Disabilities Act. This may require that you provide adaptive hardware and software on office workers' computers. Such equipment enables workers with disabilities to accomplish many tasks independently. For example, if you are blind, it can transform on-screen text to synthesized speech or braille. If you can't hear, adaptive hardware transforms a computer's audible cues into a visual format.

So far, adaptive technology has consisted of third-party add-ons to OSes, with the exception of the Mac. This has resulted in adaptive equipment that only sometimes works. Fortunately, because of lobbying by the disabled community, OS vendors have begun to embed adaptive-access features directly into their OSes. This makes such features widely available right out of the box, more reliable, and a lot less expensive.

Microsoft began to build a suite of disability-access features starting with Windows 3.x. Win 95 offers access to a built-in set of utilities that accommodate users with hearing, motor, and some visual disabilities. Furthermore, the Win 95 Help system includes information on these built-in accessibility features.

The control and configuration of most of these features are centralized in an Accessibility Options Control Panel, as shown

in the screen

. This Control Panel lets you activate or deactivate specific access features and customize timings and feedback for certain utilities. It also lets you set hot keys so that you can activate these features quickly.

Keyboard and Mouse

Using a keyboard requires a significant amount of hand dexterity, particularly when using the modifier keys, such as Shift, Control, and Alt. For persons unable to use a standard keyboard or mouse easily -- if at all -- several Win 95 utilities can help by altering the keyboard's behavior. You can configure these utilities in a pane on the Accessibility Options Control Panel.

The StickyKeys utility, for instance, helps you type capital letters or manage complex key sequences, like Control-Alt-Delete, that require the use of both hands. StickyKeys lets you press one key at a time in a sequence instead of pressing multiple keys simultaneously.

Another powerful utility, FilterKeys, helps users who accidentally strike keys by filtering out those keystrokes that do not fall under a user-definable time duration. In other words, for a key press to become a valid keystroke, it must be held down long enough to register. Any keystrokes that don't last for the specified duration are discarded.

ToggleKeys is a utility that provides audio feedback for certain keystrokes. This is a useful tool for computer users who are unable to determine the status of the keyboard's modifier keys by using any other method. The ToggleKeys utility provides both high- and low-pitched beeps that indicate the current status of the Caps Lock, Num Lock, and Scroll Lock keys.

Driving a mouse demands strong hand/eye coordination and good hand/arm agility. It's a prerequisite for using the GUIs on many of today's desktop computers. MouseKeys assists users who have difficulty pointing the rodent. The program lets you use the arrow keys on the keyboard's numeric keypad to move the mouse pointer around the screen and emulate mouse actions, such as clicking, double-clicking, dragging, and dropping. Holding down the Control key accelerates pointer movement, while holding down the Shift key propels the pointer a pixel at a time, offering fine-grained control.

Video and Sound

For persons who have difficulty seeing images on a standard computer screen, Win 95 offers several features that make the monitor easier to see. Some of these features are simply a matter of adjusting certain Control Panel settings. For example, if you are visually impaired, you can use the Display Panel to scale the size of various user-interface elements, such as window titles, scroll bars, borders, menu text, and icons.

The Mouse Control Panel allows you to adjust the mouse pointer's characteristics. You can select from among several sizes (small, medium, and large), which is valuable for users with limited vision or learning disabilities. You can also adjust the pointer's color and apply animation effects to increase its recognition factor and visibility.

For users with limited vision, color plays an important role in their ability to read comfortably -- or at all. Again, Win 95's built-in customization features enable you to modify the color scheme of the environment. You can select a high-contrast mode or choose from several ready-made appearance schemes that make it easier for users with limited vision to focus on the screen. The Accessibility Options Control Panel allows you to set a global flag that instructs your applications to employ the high-contrast color scheme, as shown

in the screen

o. It also enables you to avoid schemes that are difficult to see, such as text that's displayed over pictures.

For users who are deaf or hearing-impaired, Microsoft has implemented several useful features into Win 95 that increase access to the computer and its data. This is of vital importance as many applications begin to use text-to-speech or audio playback.

Win 95's SoundSentry lets you have sounds presented in an alternative format, such as visually or through text captions. ShowSounds lets you set a global flag that displays sounds in a visual format. This can be accomplished by several methods, depending on your preference. For instance, you can have the active window flash every time a sound is generated or display text captions that represent the sounds.

Third-Party Speech-Access Products

Despite all these improvements, Win 95 still lacks critical support for users who are totally blind and must rely on speech-synthesis systems to read the information on a computer screen. Microsoft plans to implement an off-screen model that captures on-screen information so that special-purpose software can perform a text-to-speech conversion on it or drive a braille-output device.

Unfortunately, the hooks to this mechanism might still be unavailable when this article sees print. This sorry state of affairs presents an opportunity for third-party access technology, chief among them speech- and braille-output packages designed to read the screen.

The Automatic Screen Access program for Windows (ASAW), from MicroTalk, is one of the latest Win 95 screen readers to enter the market. ASAW works with Win 3.x and Win 95 applications. Biolink's ProTalk32 is a screen reader for Win 95. A Win 3.x and NT version is also available. Winvision, from Artic Technologies, runs on both Win 3.x and 95 and supports several commercially available speech synthesizers. Winvision also drives braille displays, providing a tactile representation of Windows screens. Syntha-Voice's Window Bridge, which runs under Win 3.x, Win 95, and DOS, was the first Windows-based screen reader to enter the adaptive market.

Computers play a major role in our society; they're used at home, at school, and on the job. It only makes sense for OSes to provide adaptive-access features. This makes the computer accessible to everyone, no matter what their abilities, so they can make a contribution in the workplace. Microsoft has done a commendable job so far with much-needed improvements to Win 95. But the company still has a lot of work to do if Windows is going to provide OS-level support for blind computer users.

## Where To Find

Artic Technologies

Troy, MI

Phone: (810) 588-7370

Fax: (810) 588-2650

Biolink

*North Vancouver, British Columbia, Canada

Phone: (604) 984-4099

Fax: (604) 985-8493

http://biz.bct6l.net/biolink

Internet:

http://biz.bct6l.net/biolink

MicroTalk

Texarkana, TX

Phone: (903) 792-2570

Fax: (903) 792-5140

http://www.screenaccess.com

Internet:

http://www.screenaccess.com

Syntha-Voice

Stoney Creek, Ontario, Canada

Phone: (905) 662-0565

http://www.synthavoice.on.ca/~davidk

Internet:

$http://www.synthavoice.on.ca/~davidk

%Win 95 Eases Disability Accomodation

You can configure Win 95 to accommodate users with hearing, motor, and some visual disabilities.

## High-Contrast Not Always Supported

A high-contrast layout makes for easy reading, but not all applications (such as the toolbar on the left) support this feature.

mailto:"lazzaro@world.std.com"

mailto:"lazzaro@bix.com"

Joseph J. Lazzaro is the author of Adapting PCs for Disabilities (Addison-Wesley, 1996). He is also project director of the Adaptive Technology Program at the Massachusetts Commission for the Blind in Boston. You can reach him at

lazzaro@world.std.com

or at

lazzaro@bix.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Core Technologies

## Core Technologies

## The Backbone of the Web

@A look at HTTP version 1.1, a necessary new Internet standard.

William Stallings

The Hypertext Transfer Protocol is the foundation protocol of the World Wide Web. The name is somewhat misleading. HTTP is not a protocol for transferring hypertext; it is a protocol for transmitting information with the efficiency necessary to make hypertext jumps. The data transferred by the protocol can be plain text, hypertext, audio, images, or any Internet-accessible information. Information in this article is based on the most recent (June 7, 1996) specification -- HTTP 1.1, draft 05 -- which has been forwarded to the Internet Engineering Standards Group as a proposed standard.

HTTP is a transaction-oriented client/server protocol. To ensure reliability, HTTP uses TCP. Nevertheless, HTTP is a "stateless" protocol: It treats each transaction independently. A typical implementation will create a new TCP connection between client and server for each transaction, then terminate the connection as soon as the transaction completes. However, the specification does not require this one-to-one relationship between transaction and connection lifetimes; i.e., the connection can stay open so that more transactions can be made.

The stateless nature of HTTP is well-suited to its typical application. A normal Web session involves retrieving a sequence of pages and documents. The sequence is, ideally, performed rapidly, and the locations of the various pages and documents may be widely distributed among a number of servers, located across the country or around the globe.

The figure

"Types of HTTP Transfers"

illustrates three examples of HTTP operations. The user agent is the client, such as a Web browser, that initiates the request. The origin server is the server on which a resource resides; an example is a Web server where a desired home page is located. The simplest case is one in which a user agent establishes a direct connection with an origin server. The client opens a TCP connection that is end-to-end between the client and the server. The client then issues an HTTP request. The request consists of a specific command (referred to as a method), a URL, and a message containing request parameters, information about the client, and perhaps additional content information.

When the server receives the request, it attempts to perform the requested action and then returns an HTTP response. The response includes status information, a success/error code, and a message containing information about the server, information about the response itself, and possible body content. The TCP connection is then closed.

The middle section of the figure shows a case in which there is not an end-to-end TCP connection between the user agent and the origin server. Instead, there are one or more intermediary systems with TCP connections between logically adjacent systems. Each intermediary system acts as a relay, so that a request initiated by the client is relayed through the intermediary systems to the server, and the response from the server is relayed back to the client.

The Machine in the Middle

The HTTP spec defines three forms of intermediary systems: proxy, gateway, and tunnel (see the figure

"Intermediary HTTP Systems"

). A proxy acts on behalf of other clients and presents requests from other clients to a server. There are several scenarios that call for the use of a proxy. In one scenario, the proxy acts as an intermediary through a firewall. In this case, the server must authenticate itself to the firewall to set up a connection with the proxy. The proxy accepts responses after they have passed through the firewall. Another scenario involves handling different versions of HTTP. If the client and the server are running different versions of HTTP, then the proxy can implement both versions and perform the required mapping.

A gateway is a server that appears to the client as if it were an origin server. It acts on behalf of other servers that may not be able to communicate directly with a client. There are several scenarios in which servers can be used. As with the proxy, a gateway manages transfers through a firewall. In this case the client must authenticate itself to the proxy, which can then pass the request on to the server.

Another common scenario involves working with a non-HTTP server. Browsers have built into them the capability to contact servers that use protocols other than HTTP, such as FTP and Gopher servers. This multiprotocol capability can also be provided by a gateway.

A tunnel is simply a relay point between two TCP connections. HTTP messages are passed unchanged as if there were a single HTTP connection between user agent and origin server. Tunnels are used when there is an intermediary system between client and server, but it is not necessary for that system to understand the contents of messages.

Now let's take a look at another type of HTTP operation. A cache is a facility that stores previous requests and responses for handling new requests. If a new request arrives that uses the same stored request, then the cache can supply the stored response rather than access the resource indicated in the URL. The cache can operate on a client or on a server or on an intermediary system other than a tunnel. In the figure

"Types of HTTP Transfers,"

a server has cached a request/response transaction, so a corresponding new request from the client need not travel the entire chain to the origin server; instead, the cache server handles it. Not all transactions can be cached, and a client or a server can dictate that a certain transaction may be cached only for a given amount of time.

HTTP Messages

HTTP messages comprise two types: request and response. A request message is sent by an agent to a server to initiate some action. A response message is returned by a server to an agent in response to a request. Some possible actions are:

GET: A request to retrieve information.

POST: A request to accept the attached entity as a new subordinate to the identified URL.

PUT: A request to accept the attached entity and store it under the supplied URL. This may be a new resource with a new URL, or it may be a replacement of the contents of an existing resource with an existing URL.

DELETE: Requests that the origin server delete a resource.

A response message may include an entity body containing hypertext-based information. In addition, the response message must specify a status code, which indicates the action taken on the corresponding request. Status codes are organized into the following categories:

Informational: The request has been received and processing continues. No entity body accompanies this response.

Successful: The request was successfully received, understood, and accepted.

Redirection: Further action is required to complete the request.

Client error: Request contains a syntax error or request cannot be fulfilled.

Server error: The server failed to fulfill an apparently valid request.

We Need This Standard

HTTP is the foundation of the World Wide Web. This request/response protocol used on top of TCP carries commands from browsers to servers and responses from servers back to browsers. As the explosive growth of the Web continues, and as new features are added to both browsers and servers, a standardized transfer protocol is essential to maintain the Web's growing functions and interoperability. HTTP provides the standardized definition required to meet these needs.

## Types of HTTP Transfers

SHTTP supports operations via direct connection, intermediary systems, or a cache.

## Intermediary HTTP Systems

^HTTP allows requests and responses to pass through disparate systems that build the network.

mailto:"ws@shore.net"

William Stallings is a consultant and author of over a dozen books on data communications and networking. This article is based on material from his most recent book, Data and Computer Communications (Prentice-Hall, 1996). You can reach him at

ws@shore.net

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Core Technologies

## Core Technologies

## The Server's Helper

=RISC powers Intel's intelligent I/O controller for servers.

Tom Thompson

The changing nature of information that office workers use has had an impact on the role the network server plays. Today's server must pump out digital video, audio, and 3-D graphics on demand; handle complex database queries; and manage Web transactions. As a consequence, a server requires a more efficient architecture than just a souped-up desktop-computer design. A faster processor and system bus aren't enough. The computer must manage the vast amounts of I/O this type of data demands. Radical architectures from Tandem and Sequent address this problem on high-end server designs, as described in "The Network in the Server" (July BYTE).

Moderate-size servers must also work with the same type of data, on a smaller scale. When it comes to handling I/O, such servers must work smarter, not harder. Even a multiprocessor server can grind to a halt if each processor is supervising a peripheral or -- worse -- waiting to access a congested system bus.

To this end, Intel just started sampling the i960 RP, a 32-bit RISC processor that functions as an intelligent I/O controller. It supports DMA transfers, address translation, various memory types, and multiprocessor interrupt control. Thus, it can manage most of a server's peripheral I/O traffic without CPU intervention, eliminating many throughput bottlenecks.

The i960 RP also acts as a PCI-to-PCI bridge unit, which lets you add more slots to the design. At the same time, the bridge unit reduces the number of components required to build a server that uses state-of-the-art high-speed PCI peripherals. This enables a server to provide high throughput yet remain affordable.

RISC at the Core

Like other chip vendors' smart I/O processors, Intel took the core of its tried-and-true i960 JF embedded processor and wrapped I/O support logic around it. Our tour of the processor begins with this RISC core. The i960 JF core consists of 32 32-bit registers. Sixteen of them are local (general-purpose); the other sixteen are global registers used for parameter passing or storing critical variables. An on-chip local-register cache stores up to eight copies of the local registers. This provides hardware support for the rapid entry and exit of function calls, a useful feature for time-critical interrupt handlers.

The core consists of 700,000 transistors and has a four-stage pipeline. It has several independent execution units (EUs): one for instruction processing and address generation, a multiply-divide-unit (MDU) for 32-bit math computations, and a memory interface unit that handles load/store operations. The core can scoreboard individual registers, so the processor can execute certain instructions in parallel, or out of order, to maintain single-cycle instruction execution.

The core includes a 4-KB two-way set-associative instruction cache, a 1-KB direct-mapped data cache, and 1 KB of on-chip data RAM. You can enhance interrupt processing by locking sections of interrupt-handler code within the instruction cache and by storing a number of interrupt vectors in the on-chip memory. At 33 MHz, the core delivers 31 VAX MIPS.

A bus-control unit (BCU) supports 8-, 16-, and 32-bit memory addressing, plus big-endian and little-endian addressing modes. This lets the i960 connect to a large variety of memory and peripherals. Up to eight sections of memory, each 512 MB in length, can be defined with different memory-width attributes. Regions of memory ranging in size from 4 KB to 4 GB can also be defined as cacheable (typically for program memory) and noncacheable (typically for I/O devices).

Device Interfaces

The i960 RP provides a wealth of device interfaces and control functions, such as a memory controller, DMA controller, and PCI-to-PCI bridge unit, as shown in the figure

"The i960 RP Architecture."

\ These features can be used to both simplify a server design and improve system throughput.

The built-in memory controller generates the appropriate timing and signals for three different RAM types: fast page-mode (FPM), extended data out (EDO), and burst extended data out (BEDO). The controller supports memory interleaving for FPM RAM. The controller also handles 8- or 32-bit-wide ROM, static-RAM (SRAM), and flash-memory devices.

The i960's integrated DMA controller has three DMA channels that perform high-speed transfers between PCI peripherals and local memory (i.e., memory directly managed by the memory controller). Each DMA channel has a hardware packing and unpacking unit that can handle unaligned data transfers.

The DMA controller also implements chain descriptors. A chain descriptor is a data block that describes a DMA transfer, such as the amount of data to move, the source and destination addresses, a control value, and a pointer to the next descriptor. The pointers let you link descriptors into a "chain" of operations that can gather scattered blocks of data and transfer them in one chunk to the destination. These chains can implement sophisticated data transfers, perhaps moving data from a hard drive into memory and then to a network device, as shown in the figure

"An Intelligent I/O Operation."

{ Such a chain can supervise this type of complex transfer without interrupting the host processor, unless an error occurs.

A Built-In Bridge

The most versatile feature of the i960 RP is its PCI-to-PCI bridging capability. It supports two PCI buses: a primary PCI bus, which connects to the host CPU, and a secondary PCI bus that's maintained by the i960. These interfaces let you add the i960 to a PCI-based server design without using additional glue logic. This secondary bus complies with the 5-V PCI standard, and at 33 MHz, it provides nine extra PCI loads. This lets the server design offer more PCI devices or card slots. You can attach additional i960 RP processors to the secondary bus to build a hierarchy of PCI buses, so that the system can handle a large number of network interfaces and storage devices.

The i960's PCI bridge logic can forward memory, I/O, and command transfers between the two PCI buses. However, you can program the bridge logic to "filter" certain PCI transactions. This reduces traffic in other buses on the server and aids in the implementation of intelligent I/O subsystems. For example, suppose a hard drive is streaming video data to an Ethernet interface, and both these PCI-based devices reside on the PCI secondary bus. The bridge logic blocks these transfers from the primary PCI bus, so that it can independently handle a different set of I/O operations.

The DMA controller works in tandem with the PCI-to-PCI bridge unit to boost throughput. Also, properly written descriptor chains can add smarts to low-cost PCI peripherals, so that their use improves performance while minimizing CPU overhead.

As you can see, the i960 RP offers many capabilities to a server design. Certain functions, such as the DMA controller, allow the systems designer to hand off data transfers between memory and peripherals to the i960, thus relieving the server's CPUs of this chore. Other functions, such as the memory controller and the PCI-to-PCI bridging capability, allow the engineer to eliminate some parts from the design, thus reducing the server's cost and complexity.

## Product Information

Intel Corp.

Santa Clara, CA

phone: (800) 628-8686

Fax: (503) 264-6835

http://www.intel.com/DESIGN/IIO

Internet:

http://www.intel.com/DESIGN/IIO

## The i960 RP Architecture

This intelligent I/O controller manages DMA transfers and memory timing. It also acts as a PCI-to-PCI bridge.

## An Intelligent I/O Operation

Sequences of DMA commands can manage complex I/O transfers without CPU support.

mailto:"tom_thompson@bix.com"

Tom Thompson is a BYTE senior technical editor at large. He has a B.S.E.E. degree from the University of Memphis. You can reach him on the Internet at

tom_thompson@bix.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Core Technologies

## Core Technologies

'Make Access and the Web Work Together

Add an interactive database to your Web pages with a few simple tools.

Rick Dobson

Perhaps you've seen one of those cool Web pages where you type in a request to obtain up-to-the-minute product information. Microsoft's Internet Information Server (IIS), with its Internet Database Connector (IDC), simplifies the process of building dynamic Hypertext Markup Language (HTML) pages so that you can add such a mechanism into your Web pages. This lets you develop and maintain intranet and Internet Web sites that allow the interactive search, display, and modification of information in a Microsoft Access database.

It's important to note that such applications can support only low to intermediate hit rates. However, it's easy to upsize them to full-blown SQL Server applications. Thus, Access shines as a rapid prototyping tool for building frequently visited Internet sites.

This approach requires three items. First, Web-site visitors must have Web browsers. Second, the IIS/IDC must be running on the server. The IDC is a DLL named HTTPODBC.DLL. Third, you must install the Access 7 for Windows 95 Open Database Connectivity (ODBC) driver on the server. The IDC requires such a "thread-safe" ODBC driver so that multiple clients can launch concurrent queries against the same data source.

Dynamic Access Parts

The Web browser handles any user events and typed input, and it displays the information returned by the database. An .mdb file stores the tables, forms, queries, and modules that comprise your Access database. Two key developer-designed files on the IIS manage the interactive process, as shown in the figure

!"How Access Generates Web Pages."

The .idc file defines specific valid data fields and operations; the .htx file formats the returned data for display by the client browser.

The key field in an .idc file is SQLStatement. It lets you perform all the functions permitted by Access's SQL. Two other required fields are Datasource and Template. Datasource ultimately points the query embedded in SQLStatement to the appropriate .mdb file. Finally, Template names the .htx file that's responsible for formatting the result.

You can include several optional fields that refine your application's behavior. MaxRecords designates the maximum number of records a query returns. With DefaultParameters, you can supply default criteria for a query when the client fails to do so. Use RequiredParameters instead to generate an error when the client browser does not provide a parameter. Username and Password act as a gateway to security features. These fields, in conjunction with Access's users, groups, and permissions features, can restrict admittance to tables with sensitive data, such as salaries.

The .htx file is a template for the HTML file passed back to the client Web browser from the IIS. The .htx file includes special tags for processing the query results returned by the ODBC driver. These vendor-specific tags, in conjunction with traditional HTML tags, let developers control what a client browser views.

A Sample Program

I constructed a simple database application based on the Northwind database sample that ships with Access. My test database includes two tables. The first, tblCustomers, contains the CustomerID, CompanyName, ContactName, and Phone fields. The second, tblSalesByCustomer, houses the CustomerID and Sum fields. Sum contains the total sales for each customer.

My initial .idc file (shown in the listing

"Query Input and Control"

) creates a listing of the top 10 customers ranked by sales in descending order. This file contains four fields. The first one, Datasource, points to the target .mdb file, as routed through an ODBC data source. The ODBC-driver dialog box has a New button that allows the developer to create the data source that points to the .mdb file. However, Datasource eliminates this bit of manual intervention for the user, which is necessary to support a self-contained Web site.

The second field, Template, names an .htx file that serves as a template for formatting the HTML page to appear on the client's browser. The third field, MaxRecords, restricts the lists of returned records to 10. Finally, SQLStatement includes the SQL string that controls the query. Each line, including the first one, must begin with a plus sign.

An .htx file can contain all the graphic files and formatting touches that regularly adorn the HTML pages at your favorite Web sites. The .htx file displays the query results within a pair of <%BeginDetail%> and <%EndDetail%> vendor-specific tags. To display a particular query, bracket its name inside these vendor-specific tags (e.g., <%Sum%>). The IIS repeatedly merges all .idc fields between <%BeginDetail%> and <%EndDetail%> for each record in the return data set.

You create drill-down hyperlinks to other pages by use of HTML anchor tags. You do this by placing another .idc filename between the anchor tags, which in turn creates a drill-down page. A question mark must follow the .idc filename. This is demonstrated in the first listing's .htx file. When you need to pass a parameter to the second .idc file, insert a phrase such as CustomerID=<%CustomerID%> after the .idc filename. The left term, CustomerID, designates a field in SQLStatement for the second .idc file. The term that's on the right of the equal sign references the value in the current hyperlink.

The listing

"Data Close Up"

shows the .idc and .htx files that generate the drill-down page from the top 10 CustomerID displays. This .idc file extracts the company and contact names along with the phone number for the CustomerID that matches the one in the hyperlink jump. It accepts a passed argument with an expression such as CustomerID=%CustomerID% in the Where clause of its SQLStatement. The term on the left of the equal sign corresponds to a field in the Select list of the query. The term on the right of the equal sign represents the passed parameter. Its value is set by the calling hyperlink jump.

The .htx file in the listing

"Data Close Up"

demonstrates some basic HTML tag techniques for controlling the display of records returned by an .idc file. Its corresponding .idc file returns a single record with four fields. The BR tag positions each field on a different line. The other tags adjust the font and the position of the results.

Closing Issues

The IIS/IDC plus Access provides a quick, easy way to start publishing dynamic HTML pages from a database. Many more options beyond those in the code listings are feasible. For example, you can populate combo boxes on HTML forms, or you can accept values directly from HTML forms for selecting or updating an Access database.

I found the new functionality easy to use, but experienced Access developers will appreciate enhancements. First, Access developers are used to more flexibility in processing return sets than the .htx file permits. Among the features missing are event programming and expressions. Second, no error-trapping techniques are available with this release. While errors do not cause the system to abruptly halt without user recovery, you can still be confronted with error messages that may not be meaningful. Third, wizards and more graphical development aids would help promote the acceptance of this Web development strategy among Access developers.

## Query Input and Control

.idc file that shows top 10 customers

Datasource: WebSales

Template:

SalesByCustomer.htx

MaxRecords: 10

Qlstatement:

+SELECT CustomerID, Sum

+FROM tblSaesByCustomer

+ORDER BY Sum DESC

).htx file to display customers and sales

<HTML>

<HEAD>

<TITLE>Drill-Down List</TITLE>

</HEAD>

<BODY>

<FONT FACE=ARIAL SIZE="2">

<UL>

<%BeginDetail%>

B<LI><A HREF="/Byte/CustomerDetail.idc?CustomerID=<%CustomerID%>">

Customer ID:

<%CustomerID%></A>,

<%Sum%><BR>

<%EndDetail%>

</UL>

</BODY>

</FONT>

</HTML>

## Data Close Up

.idc file that drills down to detail a particular customer

Datasource: WebSales

Template: CustomerDetail.htx

SQLstatement:

!+SELECT CustomerID, CompanyName,

+ContactName, Phone

+FROM tblCustomers

+Where CustomerID=%CustomerID%

..htx file that displays a particular customer

<HTML>

<HEAD>

'<TITLE>Customer Contact Detail</TITLE>

</HEAD>

<BODY>

<%BeginDetail%>

<FONT SIZE="4">

1Here is the contact information for Customer ID:

<%CustomerID%><BR>

<P>

<FONT SIZE="3">

CompanyName:

<%CompanyName%><BR>

ContactName:

<%ContactName%><BR>

Phone:

<%Phone%><BR>

<%EndDetail%>

</BODY>

</FONT>

</HTML>

## How Access Generates Web Pages

_The developer provides several files to create an interactive database connection on the Web.

mailto:"Rick_Dobson@msn.com"

Rick Dobson is president of CAB, Inc., a database and Internet consultancy. You can reach him at

Rick_Dobson@msn.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Cover Story

## Cover Story

## 3-D for Everyone

Seeing isn't believing: 3-D must face growing pains before it can become essential for business applications.

Udo Flohr

Now that low-cost 3-D is reaching our desktops at little or no extra cost, cynics might respond with a resounding, "So what?" They counter that, unless you're hooked on shoot-'em-up games, low-cost 3-D is just another check-off item from board vendors vying for your business.

But proponents counter that 3-D's potential for general-purpose computing is wide open. Just as GUIs and the mouse changed the face of computing during the past decade, 3-D will bring about new ways of viewing and analyzing data.

Timing puts the truth somewhere between these two opposing views. Innovators at places such as Xerox's Palo Alto Research Center (PARC) are already showing early software designs that use 3-D to add layers of information to databases and interfaces, making today's 2-D software look Spartan by comparison. But commercial versions of these products are at least a year or two from widespread use.

In the meantime, buyers beware: Not all the chips, boards, and APIs that spawned this year's crop of low-cost 3-D products will have the ability to run tomorrow's applications. To keep their designs affordable, vendors of low-end 3-D products made some compromises. As a result, some game-optimized chips cannot provide the processing power that professional-level 3-D accelerators now deliver for simulations and CAD applications.

The bottom line is that today's low-cost 3-D world is neither insignificant nor fully formed. This situation forces us to look beyond the glittering graphics to make judicious choices about 3-D.

Real 3-D

How might 3-D eventually change the way in which we work? The first phase of mass-market 3-D products will bring traditional 3-D applications, such as architectural walk-throughs, virtual reality, animation, and state-of-the-art games, to mainstream desktops. Next we'll see 3-D applied to standard applications, such as graphics editors, spreadsheets, and even word processors.

To see the 3-D possibilities for general business applications, consider the advanced spreadsheets and databases that already work in three dimensions. Today you can populate a structural cube with data and then slice and dice it horizontally, vertically, or across a 3-D plane.

For instance, you might set up a 3-D spreadsheet to hold a year's worth of sales data, with each 2-D sheet listing the sales of a number of products for one month. Each layer of the spreadsheet holds information for a different month. To view the annual sales of a single product, you simply cut across the cube to retrieve the product's data for all 12 months.

The problem with this approach lies in viewing such a data cube on a flat surface. Once you cut across the cube, today's 3-D spreadsheets simply build a new 2-D view. Developers have tried to simulate the 3-D experience by adding slick interface tricks, such as drilling down on data by double-clicking on a functional heading or displaying the data within complicated 2-D matrices.

But in the end, 3-D spreadsheets have not met their potential because of the inherent weaknesses of working with 3-D data in 2-D space. In a true 3-D environment, you will be able to not only build a data cube but also rotate the cube in 3-D space and arrange the data in enlightening new ways.

Before that happens, we may see many examples of gratuitous 3-D. Developers and marketing wizards will concoct spinning logos and other graphical gimmicks, eye-catchers with little or no real value. But user-interface (UI) design is evolving to grasp 3-D's potential and turn it into something useful.

Whether or not software developers quickly turn 3-D into something that is useful for business applications, there is no doubt that ubiquitous 3-D is on the way. Consider Intel's MMX technology. MMX adds 57 new instructions to the x86 instruction set to accelerate multimedia applications, such as 3-D and 2-D graphics, video, audio, speech synthesis and recognition, and communications. According to Intel's simulations, we can expect to see performance boosts of between 50 percent and 100 percent.

MMX is slated to appear first in a new version of the Pentium processor, code-named the P55C, which is due early next year. Look for MMX support in APIs such as OpenGL and DirectX. (For an in-depth look at MMX technology, see the sidebar "MMX Accelerates the x86".) AMD and Cyrix are both planning to support MMX instructions in their future microprocessors.

There are various ways to distribute 3-D tasks between the CPU and the graphics chip. Graphics boards work with integer values; therefore, at the very least, the CPU must translate an application's floating-point values into integers.

Most often, the graphics

chip works

as a rendering engine, while tessellation (breaking up a 2-D image into polygons) and geometry (adding lighting and perspective) are left to the PC. For the third processing step, rendering (adding surface characteristics), low-cost 3-D boards often economize by combining frame, texture, and z-buffers (stored depth values) and allocating memory dynamically.

For example, if an application doesn't need a z-buffer (many games do not), the available memory can be used for the texture or frame buffer. Many applications set up the frame buffer in main memory, which is a mixed blessing: This approach saves cost by requiring less memory on the card, but it introduces a

major bottleneck

?, as hidden surface removal has to be done across the PCI bus.

The majority of high-end 3-D accelerators employ separate buffers for frame, texture, and depth information, with each buffer having a capacity of at least 2 MB. However, the cost of buffer memory alone keeps these products out of the mainstream market.

The 3-D Hardware Wave

Although 3-D accelerators divvy up processing tasks in similar ways, 3-D

chip architectures

can vary considerably. Some chips are programmable, such as Rendition's RISC-based V

rit

and Chromatic's Mpact, which uses a very-long-instruction-word (VLIW) architecture. Two other programmable chips, the TM-1 from Philips and the Mfast from IBM, were not yet shipping at press time.

The performance of programmable 3-D chips depends to a large extent on the low-level software that drives them. Both Rendition and Chromatic currently supply such firmware. OEMs that write their own low-level software can enhance these processors with new features, data formats, or algorithms.

The Mpact's Mediaware microcode modules allow systems designers to enable or disable specific functions -- such as 3-D graphics, videoconferencing, and telephony -- to create a single hardware design with a number of different personalities. Unlike the Mpact, the V

rit

was designed specifically for 3-D acceleration. It includes a hardwire "pixel pipeline" for critical 3-D operations, such as texture mapping and blending, while the RISC core is responsible for geometry setup and filtering; this relieves the CPU of the majority of the 3-D work load.

Hard-wired solutions, such as those from Nvidia, 3Dfx Interactive, and 3Dlabs, sacrifice this flexibility but often achieve higher performance. As

APIs

and other standards evolve, customers must depend on these vendors to update their designs quickly or, in some cases, to develop new software drivers to support the emerging standards.

Nvidia's NV1 requires additional developer support because of its proprietary curve primitive. Instead of building curved surfaces from small polygons, the NV1 generates curves directly to dramatically improve performance when an application requires textured curves. The drawback is that developers must port applications to the Nvidia chip before they can take advantage of these curve primitives.

Many of the graphics companies now offering low-cost 3-D chips and boards have been selling to the 2-D graphics market for years. They offer their customer base a terrific advantage: The new 3-D chips are pin-compatible with the previous generation, so the 3-D chips can slip into a proven card design. For example, the S3 Virge is pin-compatible with the popular S3 Trio64V+. On the downside, not all of these mainstream graphics vendors have the expertise of the established 3-D companies.

3Dfx is one of the few companies in the low-cost 3-D market with a strong 3-D r

sum

. The firm has made a business of replacing the expensive proprietary engines used in dedicated arcade machines with high-performance Pentiums. Focusing on this specialty, 3Dfx has designed a dedicated 3-D chip that delivers impressive 3-D acceleration but lacks integrated functionality, such as standard GUI acceleration and motion-video playback.

A dedicated 3-D solution does not replace a PC's graphics card; instead, it complements it with a "pixel pump" that works in parallel with the graphics accelerator that's on a separate PCI board. After the 3-D chip calculates the pixels, they pass across the PCI bus to the graphics card.

Like the 3Dfx Voodoo Graphics accelerator chip set, VideoLogic's PowerVR is a dedicated 3-D chip that requires an existing graphics accelerator. To compete with integrated solutions, 3Dfx has formed a partnership with Alliance semiconductor to combine the Voodoo with Alliance's ProMotion graphics controllers.

Bring on the Boards

Now that 3-D chips are appearing on commercial boards, we are seeing some 3-D warts along with the glitter. One particularly unpleasant surprise is that 3-D acceleration in many low-cost boards works only in one mode -- namely, at a resolution of 640 by 480 pixels with 64,000 colors.

This is fine for play, since today's 3-D games don't require any more screen real estate than that. But this situation will eventually change. As more business applications use 3-D, 640 by 480 is becoming all but useless, and switching back and forth between resolutions quickly gets tedious. It's better to instead consider cards that accept additional memory to support 3-D acceleration at 800 by 600.

Many vendors bundle games with their 3-D boards. Some of these games use special features of that vendor's hardware; we've even heard of programs that use a high-level API, such as Microsoft's DirectX family of interfaces, and still use hardware references to stop users from switching horses. In addition, games developers are fond of squeezing every last bit of performance out of the hardware.

Since the jury is still out on how much of a performance penalty the multiple software layers in Microsoft's 3-D APIs will inflict, some people might be tempted to bypass them. In the long run, only hardware and software that supports the relevant APIs will survive. Until then, shoppers should select a board that has all the drivers needed for it to perform with the software they expect to use.

If you have a high-performance graphics board and just want 3-D acceleration, then something like VideoLogic's PowerVR, working in parallel with the main graphics board on a separate PCI card, could be an ideal solution.

Nonstandard 3-D

Currently there are about 50 APIs for 3-D. This situation is not conducive to matching the hardware flood with the ground swell of cool mass-market applications.

APIs -- the libraries of boilerplate routines that define standard sets of graphics functions -- give programmers "hooks" into an otherwise-closed environment, such as an OS, a database, or hardware drivers. In the 3-D arena, APIs also function as an isolating layer to protect applications programmers from the idiosyncrasies of proprietary hardware.

The three leading API contenders for mainstream 3-D are OpenGL, QuickDraw 3D (QD3D), and Direct3D. The latter has the advantage of Microsoft's marketing might, while the cross-platform capabilities of the other two make them important for developers not tied to Windows.

OpenGL originated as the Graphics Library for the Silicon Graphics, Inc. (SGI), Iris graphics systems. It's the oldest of the three APIs and now has the broadest base among Mac, PC, and Unix developers. It focuses on drawing 2-D and 3-D objects quickly and is generally more low-level than the other two APIs.

For instance, it does not include complex predefined objects, automatic shadows, ray-tracing, or radiosity functions. It's currently the undisputed standard for scientific and engineering applications, and it is associated more with high-end CAD, simulation, and visualization than with photo-realistic games. In a move to broaden the API's appeal from the professional market to general-purpose desktops, SGI recently teamed up with Sun Microsystems to develop CosmoGL, which is a variant of OpenGL that speeds texture mapping for 3-D Web applications and games in Windows 95 and NT.

OpenGL offers an impressive, if basic, array of approximately 120 functions for polygon shading, rotation, scaling, atmospheric effects, depth cueing, and other functions. But OpenGL lacks the object-oriented design of QD3D and Direct3D. You use the API as a state machine, which means that parameters "stick" until you change them. This saves work for developers, but nasty bugs can arise if the programmer forgets to save states and restore them when exiting from a routine.

OpenGL uses a client/server model, so it enables you to process compute-intensive tasks in a distributed environment. Because it does not include windowing functions, it works independently of the UI. It attaches to OSes and GUIs through extension libraries.

OpenGL is complemented by Open Inventor, a higher-level, object-oriented library. You can use Open Inventor as a layer above OpenGL to add features such as geometry, motion and lighting, and material editors. Like OpenGL, Open Inventor has been licensed to other companies. For instance, the Virtual Reality Modeling Language (VRML) format for virtual worlds on the Internet is based on Open Inventor.

QD3D, which premiered in early 1995 as a graphics extension to the Mac OS, now includes Windows support. Because QD3D is fully object-oriented, new object instances can inherent complex features (including lighting, geometry, and textures) to simplify the construction of 3-D images.

QD3D stores scene and object infor-mation with its own portable data format, which is called 3D Metafile (3DMF); it offers a choice between a compact binary and a human-readable version and supports the cutting and pasting of 3-D objects via the Clipboard. You can store QD3D objects in image databases and use simple drag-and-drop techniques to move objects from the database into a 3-D scene.

QD3D includes standard 3-D primitives, but, unlike OpenGL, it knows about complex geometry, such as nonuniform rational B-splines (NURBS). Its extensible architecture enables you to add new software-rendering engines and access hardware accelerators. Another nice detail is the interactive renderer, which lets you see and manipulate objects directly during design. Many applications let you work with the interactive renderer directly.

For developers who'd rather work with a low-level, but still hardware-independent, 3-D API, Apple offers the Rendering Acceleration Virtual Engine. RAVE can act as a plug-in module within QD3D to provide a hardware abstraction layer (HAL). RAVE includes basic graphics primitives; however, it doesn't offer high-level functions, such as the importing of objects. Like QD3D, RAVE supports Macs and Windows-based machines.

Microsoft's Direct3D, the latest member of the DirectX family of interfaces, is part of a three-layered structure (Direct3D itself is actually the middle layer). The lowest layer is the HAL, which contains the hardware-specific device drivers. Above that is the low-level API layer, which grants access to hardware features while maintaining hardware independence. The layer above it contains Microsoft's own high-level API, previously known as RealityLab (which was snagged in Microsoft's acquisition of RenderMorphics). This highest layer can also accept other APIs as plug-ins, including OpenGL. Above these three layers is the applications layer; below them lies the hardware.

Applications built on the DirectX family can query the system to determine what functions are implemented in hardware. For functions that are not supported, the application might substitute a simpler algorithm. However, Direct3D can also emulate any function in software, thanks to the Hardware Emulation Layer (HEL).

Like QD3D, Direct3D offers a clean, object-oriented, extensible architecture. What functions are actually available depends to some extent on the high-level layer. With the default RealityLabs API on top, Direct3D is not as versatile as QD3D because it lacks basic 3-D objects, such as cylinders, spheres, and cones. Still, it offers functions that go beyond OpenGL's, including animation features, which are particularly useful for games developers. Direct3D's main drawback it that it's limited to Win 95.

The 3-D Future

Eventually we may take 3-D for granted, much like gigabyte-capacity hard drives and 16 MB of memory. However, because 3-D adds complexity to applications, it will take a fair amount of time for software developers to master the technology. Therefore, we probably won't see 3-D hit critical mass until 1997 or later. Until then, only games publishers, who stand to profit first and most by 3-D, will be willing to devote significant resources to the development of 3-D.

Just like the GUI-enhanced software that seemed so cumbersome to users for many years, 3-D will suffer many development blunders along the way before killer 3-D apps emerge and 3-D UI elements become as natural and efficient to use as today's dialog boxes and scroll bars. And as 3-D becomes pervasive, business users will need, rather than just want, 3-D enhancements.

http://www.byte.com

What can you do with 3-D besides play games? To find out, join BYTE editors and 3-D chip designers in an on-line discussion from October 21 through 25 at

http://www.byte.com

## Where To Find

ATI Technologies, Inc.

Thornhill, Ontario, Canada

Phone: (905) 882-2600

Fax: (905) 882-2620

http://www.atitech.ca

Internet:

http://www.atitech.ca

Chromatic Research, Inc.

Sunnyvale, CA

Phone: (415) 254-0729

http://www.chromatic.com

Internet:

http://www.chromatic.com

Matrox Graphics, Inc.

Dorval, Quebec, Canada

+Phone: (800) 361-1408 or (514) 969-6320

Fax: (514) 969-6363

http://www.matrox.com

Internet:

http://www.matrox.com

Nvidia

Sunnyvale, CA

Phone: (408) 720-6100

Fax: (408) 720-6111

Oak Technologies

Sunnyvale, CA

Phone: (415) 962-9550

Rendition, Inc.

Mountain View, CA

Phone: (415) 335-5900

http://www.rendition.com

Internet:

http://www.rendition.com

S3, Inc.

Santa Clara, CA

Phone: (408) 980-5400

Fax: (408) 980-5444

http://www.S3.com

Internet:

http://www.S3.com

3Dfx Interactive

Mountain View, CA

Phone: (415) 934-2400

Fax: (415) 934-2424

E-Mail: info@3Dfx.com

3Dlabs, Inc.

San Jose, CA

Phone: (408) 436-3455

Fax: (408) 436-3458

http://www.3Dlabs.com

Internet:

http://www.3Dlabs.com

Trident Microsystems

Mountain View, CA

Phone: (415) 691-9211

VideoLogic, Inc.

San Bruno, CA

Phone: (800) 578-5644

Fax: (415) 875-4167

http://www.videologic.com

Internet:

http://www.videologic.com

## 3-D Chip Features

k ATI 3Dfx 3Dlabs Chrom- Matrox Nvidia Oak Rendi- S3 Trident Video-

j Rage Voodoo Permedia atic MGA- NV3 OTI64311 tion Virge T3D9695 Logic

l Mpact 1064SG V

rit

PowerVR

Memory/buffering

Memory required 1 2 2 2 2 2 1 2 2 2 2

(MB)

Memory type SGRAM EDO SGRAM RDRAM SGRAM SGRAM EDO EDO EDO SGRAM EDO

Texture buffer y y y y

required

?Z-buffer required y y y

3-D features

Antialiasing y y y y y

Trilinear filtering y y y y y y y

Subpixel posi- y y y y y y y y y

tioning

Atmospheric y y y y y y y y y

effects

Integrated features

c2-D acceleration y y y y y y y y y

Video acceleration y y y y y y y y y

cRAMDAC y y y y y

Video out Optional Optional y y

*All chips support the following features:

Alpha blending Perspective correction

:Filtering (point-sampled, bilinear) Textures

BPCI interface (glueless) Double-buffering

=Shading (flat, Gouraud) MIP mapping

;Dithering Rastering

/Graphics primitives (points, lines, triangles)

Key

y = yes.

## API Strengths and Weaknesses

OpenGL

* + Supports Mac, PC, and Unix developers.

& + Quickly draws 2-D and 3-D objects.

6 + Offers an impressive array of rendering functions.

- Not object-oriented.

QuickDraw 3D

$ + Supports the Mac OS and Windows.

+ Fully object-oriented.

4 + Lets you drag and drop objects into a 3-D scene.

> + An interactive renderer manipulates objects during design.

Direct3D

1 + A member of the DirectX family of interfaces.

= + Offers a clean, object-oriented, extensible architecture.

N - Not as versatile as QuickDraw 3D, because it lacks some basic 3-D objects.

- For Windows only.

## 3-D Anatomy

## The Highs and Lows of 3-D

3-D processing, whether it's implemented in hardware or software, has three stages:

The tessallation phase creates a description of an object and converts it into a set of polygons.

The geometry stage includes transformation, lighting, and setup. Transformation scales the scene and establishes perspective. Lighting determines color and reflections. Setup decides each polygon's shape.

Rendering manipulates the 2-D coordinates (x and y) and the z coordinate for the depth value (the z value determines whether each pixel is visible or obscured by other polygons). Next, a variety of shading and texture-mapping algorithms establish the polygon's color and texture. High-end graphics engines for professional workstations often rely on shading, which is adequate for CAD applications. Low-cost 3-D cards, however, use texture mapping for more realism.

mailto:"flohr@dfn.de"

Udo Flohr is a BYTE contributing editor based in Hannover, Germany. You can reach him at

flohr@dfn.de

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Cover Story

## Cover Story

## 3-D Evolution

In the past, spreadsheets used

visual tricks

Y to simulate the 3-D experience. But you actually saw and manipulated data in 2-D space.

Competition is prompting

games developers

j to actively devote resources to 3-D and to wade through problems caused by still-evolving API standards.

This

hyperbolic view

of a Web site, created at Xerox PARC, lets you browse a graphical map. It could be adapted for the 3-D browsing of hierarchical data structures.

## 2D Tricks Do Not 3D Make

## 3D Games Development

## A Hyperbolic Perspective

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Cover Story

## Cover Story

## MMX Accelerates the x86

To improve multimedia and 3-D processing, Intel's new MMX technology can pack multiple pixels into one register and manipulate them with a single instruction. In effect, MMX brings a new level of parallelism to x86 processors.

Instead of adding new physical registers to the x86 architecture (which would slow MMX's adoption), Intel reuses the existing floating-point (FP) stack as logical MMX registers. MMX instructions use only the 64-bit mantissa portion of the 80-bit FP registers, ignoring the 16-bit exponent portion. This yields eight 64-bit logical registers without significantly altering the x86 architecture.

MMX instructions can pack several data types into these 64-bit registers: packed bytes (eight per register), packed words (four per register), packed doublewords (two per register), and a quadword (one 64-bit value per register). These data types are useful because multimedia programs typically work on small units of data. For example, a color pixel in TrueColor mode, the highest commonly used color resolution, uses 24 bits: 1 byte for each RGB color. This mode allows up to 16.7 million colors, more than the human eye can discern. In HiColor mode, only 16 bits are needed for a pixel. For many graphics applications, 16 bits is more than enough.

New x86 processors that support MMX will address the new registers as MM0 through MM7. Instead of treating the registers as a stack -- as FP instructions do -- MMX instructions can access the registers directly. When switching back and forth between FP and MMX instructions, the existing FSAV instruction saves the state of the registers, and the usual FRSTR instruction restores the values. This keeps MMX technology compatible with existing OSes, which frequently must save and restore the registers when context-switching between multitasking applications.

The downside is that programmers can't mix FP and MMX instructions together because they need the same registers. But this is not as significant as it sounds, since multimedia programs typically perform their FP operations before displaying the data. (Rendering relies more heavily on integer instructions.)

MMX introduces a set of general-purpose integer instructions that use the single instruction/multiple data (SIMD) paradigm. One instruction processes the multiple data in the packed registers. This parallelism

increases performance

. Incidentally, this concept is not new at Intel. Years ago, the now-obsolete i860 RISC family featured a similar technology, called Pixel Addressing Extension (PAX).

Another feature of the new instruction set, parallel-compare operations, could improve performance by eliminating branches. (Modern processors try to predict branches, but a misprediction means a penalty of several processor cycles.) Combined with packed data features, parallel-compare operations are useful when, for example, you want to combine or overlay two images.

The MMX instructions are similar to those in Sun's Visual Instruction Set (VIS) for the UltraSparc. VIS also packs registers and uses the FP registers. But it has a lot more to offer than MMX: 32 new registers (compared to Intel's eight), accelerated video decompression with discrete cosine transformations, more-powerful addressing modes, pixel masking, and a highly specialized set of operations that greatly accelerates motion estimation when compressing MPEG video streams.

MMX isn't Intel's only new approach to accelerating 3-D. Another new extension for 3-D accelerators is the Advanced Graphics Port (AGP). To evenly distribute main-processor tasks and graphics-chip tasks, the AGP creates a new data path for data transfers between main memory and the graphics card's frame buffer. By skipping the PCI bus altogether, AGP can theoretically allow read and write transfers at speeds up to 400 MBps, according to Intel.

## Parallelism Speeds Performance

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Cover Story

## Cover Story

## 3-D Glossary

Alpha blending: Support for true object transparency in hardware. An alpha value defines the transparency of each pixel. The accelerator takes this transparency value into account when drawing objects, perhaps by blurring an object when it passes behind a transparent object or changing the color of a transparent foreground object to match that of a background object.

Antialiasing: An antialiasing algorithm will slightly blur diagonal lines and other effects to better simulate a smooth line.

Atmospheric effects (fogging and depth cueing): Fogging creates a haze over a scene. Depth cueing changes the color and hue of an object in accordance with the object's distance from the viewer.

Bilinear versus point-sampled filtering: To interpolate pixels, some low-end 3-D algorithms take the nearest adjacent pixel (i.e., the nearest neighbor sampling) and replicate its color. Small on-screen movements can cause full pixels to change color, causing aliasing and unwanted screen artifacts. Bilinear filtering averages the 4 nearest texels (textured pixels) to interpolate a pixel, producing a higher-quality image.

MIP mapping: When a texture is applied to an object, it often has to be resized or stretched to fit. This process degrades the texture image. MIP mapping creates three or more copies (called MIP levels) of the texture, each of a different size, so that the best-fitting copy can be used.

Perspective-correct texture mapping: Texture maps that continually change to match the perspective of the viewer.

Subpixel positioning: If a line does not run directly through a pixel, it must be moved to the nearest one, which introduces positional error. Pixels can be broken down into smaller subpixels in memory so that the line can be drawn to the nearest subpixel.

2-D and GUI acceleration: If your 3-D accelerator also acts as your primary graphics card, make sure that it supports 2-D and GUI acceleration. Otherwise, the performance of your standard Windows applications will degrade noticeably.

Video acceleration: If your applications include motion video, look for an accelerator that supports hardware video acceleration. Video acceleration performs color-space conversion and scaling in hardware, removing that chore from the host CPU and improving the quality of video clips.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Cover Story

## Cover Story

## Why Memory Matters

Memory and memory speed play pivotal roles in how realistic 3-D looks on our screens. It's important for the CPU to write pixel data to the image buffer quickly, but it's much more critical for the graphics-board circuitry to get data out to the screen.

The old VGA standard of 640- by 480-pixel resolution required a total of 307,200 pixels; at 16 colors, these pixels fit into 153,600 bytes of memory. A reasonably fast graphics driver would fill that memory in about a tenth of a second using a memory bandwidth of 1.5 MBps. Because VGA uses a vertical-refresh rate of 60 Hz, 150 KB of image memory had to be output to the screen 60 times per second, resulting in a memory bandwidth of just of over 9 MBps on the video side.

The situation heats up considerably for the modern resolutions of SVGA and better. To accommodate a moderate 1024 by 768 pixels at 65,536 colors (16 bits per pixel), the image buffer has to hold about 1.6 MB of data. Thus, the CPU needs a bandwidth of 16 MBps to write data to the graphics board. This is no big deal on the PCI bus, which can handle up to 60 MBps. But to get the image out to the screen at an ergonomically correct 75 times per second, the board must read from its image memory at 120 MBps. For 1280 by 1024 resolution, you need a sustained throughput rate of 196 MBps.

How memory delivers this performance depends on the bus width used in the graphics card's design. Basically, more memory bandwidth can be achieved either with faster memory chips or by using several chips in parallel. ISA-bus graphics boards and their chips were generally designed for a data-bus width of 16 bits; to support high screen resolutions, you need fast video RAM (VRAM).

VRAM chips are dual-ported: To the graphics chip, they look like standard DRAMs, but a second port is used for output. Thus, data can be read and written simultaneously; screen updates do not result in lost cycles. A recent development, Window RAM (WRAM), is basically faster VRAM enhanced with special graphics features, such as accelerated, aligned fills and moves.

Given that memory comes in a fixed bus width, watch out for boards that support a bus width of 64 or 128 bits but are sold in economy versions where only half the memory is fitted. For example, a 128-bit board might be designed for 4 MB of RAM, needing eight memory chips, each with a bus width of 16 bits. If only 2 MB is installed, which degrades the bus width to 64 bits, you effectively end up with a lower-performance, 64-bit board. Of course, you can install the missing memory later.

Modern boards, which transfer data at 64 or even 128 bits in parallel, can actually use slower, less expensive memory. For example, board designers can combine standard extended data out (EDO) RAM with a 64-bit bus to achieve a throughput of 240 MBps. Burst EDO RAM delivers about 400 MBps.

Memory manufacturers have come up with a variety of special designs for even-faster throughput, needed for larger color palettes. Some designers put several chips in a single housing and combine them with logic circuitry that allows overlapping access. Each unit works at the speed of standard DRAM, but parallelism increases throughput. All the variations of DRAM described below are single-ported.

Synchronous DRAM (SDRAM) and synchronous graphics RAM (SGRAM) are available from several sources and have already found a flock of followers in the graphics-controller industry. While DRAM needs several special strobe signals, synchronous RAM can handle the memory clock directly. At a bus width of 64 bits, SDRAM can support bandwidths up to 640 MBps. SGRAM adds features that accelerate graphics performance, such as block write (which is useful for video).

Multibank DRAM (MDRAM) combines eight 32-KB banks into blocks of 256 KB. It supports 500-MBps throughput. Tseng Labs' ET6000 graphics chip sports a special 128-bit MDRAM interface, yielding up to 1000 MBps.

Rambus DRAM (RDRAM), a general-purpose memory design, has a bus width of only 8 bits and therefore needs a very high memory clock of 250 MHz. Transfers reach 500 MBps.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## State Of The Art

## State Of The Art

## How to Tame Big Networks

Whether you're designing, simulating, or maintaining extra-large networks, smart software tools can help.

Edmund X. DeJesus

Quantity has a quality all its own. While running a 10-node network might be challenging, and handling a 100-node network might be absorbing, designing and maintaining a 1000-plus-node network are harrowing tasks. The larger the network, the more likely it is to contain a variety of hardware platforms, OSes, connection schemes, and protocols that span countries and continents. In short, bringing order to this potential chaos is more than a single, mortal administrator can handle.

The mega-network administrator's primary concern, of course, is how to foist off this crushing burden. The good news here is that tools exist just for this purpose.

For example, designing a large network or adding onto your existing behemoth can be taxing, since you have to consider so many parameters, including throughput, location, compatibility, size, and budget. New graphical tools let you assemble big networks from databases of components as if you're piecing together Tinkertoys -- and smart Tinkertoys at that, since some of these tools can tell you if you're making blunders such as using an underpowered server for an engineering workgroup.

If instead of designing a network from scratch you must integrate two existing networks, modeling tools can give you the big communications picture. Some products make you get your hands dirty and fill in all the details about the components yourself, while others, using "automatic discovery," quiz the myriad components and construct a model for you.

With so many interconnected components to watch over, maintenance might be your biggest headache. Most network-administration centers look like NASA Mission Control, with all their flickering monitors, each tuned to specific hardware components. Enterprise management systems can reduce the number of monitors you have to stare at each day, and they also consolidate information that logically belongs together. Event-correlation capabilities can even figure out automatically that, yes, it was that iffy router on the thirteenth floor that just triggered the 42 irate calls the help desk just fielded.

The harried system administrator is no longer alone in the battle to keep a company's information electrons flowing efficiently. And that can bring some quality to the business of handling all that quantity.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## State Of The Art

## State Of The Art

## Design and Conquer

Forget pencil and paper: Today's intelligent tools do the design work for you.

Nathan J. Muller

Experience tells us that a properly designed network can help an organization improve customer service, pursue new business opportunities, and respond faster to market forces. But large networks, often supporting tens of thousands of users worldwide, present special design challenges. Typically, such behemoths consist of a dizzying array of transmission facilities, LAN technologies, protocols, and standards -- all cobbled together to meet the differing needs of workgroups, departments, branch offices, divisions, subsidiaries, and, increasingly, strategic partners, suppliers, and customers.

As if this complexity were not enough, big networks are usually in a state of flux. Corporate requirements, technologies, and standards change over time. Carriers introduce new services. Vendors offer new and better products. With continual moves, adds, and changes, a company's traffic patterns begin to shift. Before you know it, applications are gasping for bandwidth, response time slows to a crawl, and frustrated users start looking steely-eyed at the network administrator.

Hidden costs associated with poor network designs include overspending on equipment and WAN links to ensure sufficient capacity, trouble reports, poor response to network problems, unpredictable delays in meeting work schedules, and high labor costs for frequent rush jobs.

Fortunately, automated tools are available to help you head off these sorts of problems at the pass. With built-in intelligence, these tools take an active part in the design process (see

"Design's Four Stages"

). With the type of software we'll discuss in this article, you can build a computerized model of a network; validate its design and gauge its performance; quantify equipment requirements; and explore reliability and security issues before you purchase a single network component. Some of these tools may even identify faulty equipment configurations, design flaws, and standards violations.

Network Designer Tools

Because of the size of the network designs they handle, these tools typically run on Windows NT, Unix, and SunOS. There are two notable exceptions: Supporting Windows 95 (as well as Windows 3.1) are

Network Design

and Analysis's AutoNet, a program for designing T-carrier networks, and American Hytech's NetGuru, for designing LANs and networks of unlimited size.

At the low end, prices for design tools begin at $495 (for NetGuru). At the high end, prices range from $5000 for Image-Net's CANE (Computer Aided Network Engineering) to $15,000 or more for MIL 3's OpNet and Make Systems' NetMaker XA, depending on the type and number of optional plug-in modules. For companies that do not have the time or expertise to learn and use these tools themselves, some vendors, such as Make Systems, offer outsourcing services based on their software; cost of such services starts at $1750 a day.

When working with these tools, you begin the build-a-network process by opening a blank drawing window, into which you can drag various vendor-specific devices -- workstations, servers, hubs, routers -- from a product library and drop them into place (

see the screen

). You can further define the devices by component type, software, and protocols, as appropriate. Lines link the devices to form a network, and each link gets assigned physical and logical attributes. Rapid prototyping provides the ability to copy objects -- devices, LAN segments, network nodes, and subnets -- from one drawing to the next, editing as necessary, until you have built the entire network. Along the way, you can run various simulations to test virtually any aspect of the design.

With the

right tools

, modules, and device libraries, you can design every conceivable type of network, including legacy networks such as Systems Network Architecture (SNA) and DECnet; voice networks including ISDN; and T1, X.25, asynchronous transfer mode (ATM) , and TCP/IP nets. Some tools, such as MIL 3's OpNet, let you incorporate satellite, microwave, and other kinds of wireless technologies.

## Starting from Scratch

Designing a large, complex network requires a multifaceted tool, preferably one that is graphical, object-oriented, and interactive. It should support the entire network life cycle, from the definition of user requirements and conceptual design to the detailed vendor-specific configuration of network devices, their protocols, and the various links between them. At each phase, the tool should be able to test design alternatives for cost, performance, and validity. When the design checks out, the tool should spew out network diagrams and a bill of materials. All this happens before you contact a single equipment vendor or carrier sales rep or write an RFP.

For administrators embroiled in the complexities of network design, this kind of tool represents a dream come true. ImageNet's prerelease version of CANE, an integrated set of Windows NT applications, comes close to meeting this ideal. Designers can take a top-down or a bottom-up approach to network construction. In the top-down approach, the designer starts by sketching out the overall network, then adds increasing levels of detail until every aspect of the network is eventually fleshed out. The bottom-up approach might start with a LAN in a specific department to which you link subsequent drawings to create the overall network structure.

As the drawing window populates, you can further define devices by component type -- such as chassis, interface cards, and daughterboards. You can even specify the operating system, such as "NetWare 3.12 client for a Compaq Presario 660 PC." You can add attributes (like protocol functionality) to each device taken from a library. Once you've configured the devices, each device gets a profile that specifies its traffic characteristics for simulating the network's load and capacity.

Having defined each device's configuration, lines between them form the network. CANE then validates the links, testing for common protocols and network functions. This prevents obvious mistakes, such as NetWare clients connecting to other clients instead of servers, for example. This on-line analysis feature also alerts the designer to undefined links, unconnected devices, insufficient available ports in a device, and incorrect addresses in IP networks. An off-line analysis tool reports violations of network integrity and proper network design practices. The designer can analyze the network's structure, its IP completeness, or both at once.

CANE simulates the completed network, using a database that describes how actual network devices behave under various real-world conditions. The simulator generates network events over time, based on the device and traffic pattern recorded in the simulation profile. The designer can test the network's capacity under various "what if" scenarios and fine-tune the network for optimal cost and performance. Simulation in the prerelease version of CANE operates on one LAN segment at a time. By the time you read this, the commercial version of CANE will support fully integrated enterprisewide LAN and WAN simulation.

Better Designs, the "Primitive" Way

The Make Systems design package focuses on building WANs. Among the company's set of six core tools in NetMaker XA is the Designer module. Designer allows you to build cost-effective topology and clocking designs -- from the ground up or incrementally -- using a library of building-block "primitives."

With the time-division multiplexing (TDM) primitives library, for example, you can build an entire T1 network within your specified parameters and constraints. You can strive for the lowest transmission cost that supports all traffic, for instance, or for line redundancy between all the TDM nodes. Each primitive addresses a different aspect of the design. You can run tail circuit design, hub selection, or redundancy primitives as needed. You can combine them to address the overall design objectives. You can pause the design process after each design primitive executes to study the results and adjust network parameters if necessary.

Designer uses Planner (another NetMaker tool) to run device-specific simulations to ensure that the network design is feasible and will route all traffic successfully. Since the simulation is vendor-specific (via plug-ins) there is less chance that the network will be overbuilt just to guarantee the handling of all traffic. A tariff database can price transmission links and determine the most economical network design.

The Modeling Approach

Sometimes it's best to approach unfamiliar territory by scoping out the terrain before committing time and resources to development; this strategy is especially helpful with large networks. Perhaps you want only to assess the feasibility of implementing a certain type of network by playing with a model's various design issues and evaluating the consequences for your organization. MIL 3's OpNet provides standards-based protocol models against which simulations can run within its multilevel development environment. Its model libraries let you do this with a variety of network technologies including frame relay and ATM.

Frame relay, with efficient statistical multiplexing of data and low overhead, has gained broad acceptance in large networks. As frame relay supplements -- and replaces -- legacy technologies such as X.25 and TDM, important issues arise. These issues include the benefits of frame relay versus the benefits of existing network technology, its use with other emerging technologies such as ATM, and its interoperability with higher-level protocols such as TCP/IP.

OpNet's frame relay models let you build entire networks -- complete with configurable objects such as routers, switches, and access devices -- so you can study their behavior in great detail. The switch model, for instance, supports the creation of routing tables, switching rate, and buffer capacity for each outgoing link. Among the parameters that can be applied to the permanent virtual circuits (PVCs) are the committed information rate (CIR), committed burst size (Bc), and excess burst size (Be). Incorporating such details into the design allows you to study a variety of network alternatives and assess the impact of new features such as switched virtual circuits (SVCs).

Despite their embedded intelligence, CANE, NetMaker, OpNet, and other stand-alone design products lack the comprehensive automatic discovery capabilities found in heavy-duty management platforms. Hewlett-Packard's OpenView, IBM's NetView/6000, and Sun's Solstice SunNet Manager automatically detect various network elements and represent them with icons on a topology map. Stand-alone products are better suited for creating new large-scale networks than for changing existing ones, at least for now.

Still, the shape of things to come is apparent in Make System's NetMaker XA 2.5, which can automatically discover frame relay PVCs. Expect autodiscovery to be the next development focus of independent tool makers in the coming year. Meanwhile, high-end stand-alone products still offer more advanced design capabilities. They incorporate a broader range of network technologies and equipment makes and models than the design tools that come with network management systems.

Bargain Power Tool

Developing a large-scale network does not always require high-priced design tools. To plan a large network that has thousands of PCs, workstations, and servers attached to hubs -- interconnected via bridges or routers over IP networks -- you could, for example, use American Hytech's NetGuru, a $495 package that runs under Windows 3.x.

NetGuru allows network professionals to design, validate, and document LANs of any size, including ARCnets (

see the screen

). It validates a network design based on standards -- or de facto standards -- with an internal rule-checking knowledge base that you can invoke at any time. The validation ensures that all network components are accounted for -- including network interface cards, converters, terminators, transceivers, multistation access units (MAUs), bridges, repeaters, routers, hubs, and different cable types -- before you start building a network or making additions to one. If a device is misconfigured or a 10Base-T wire exceeds the IEEE standard length, for example, NetGuru alerts you. For the truly adventurous, the program has an expert mode that allows experienced designers to override standards and push the envelope.

NetGuru can be used to design only LANs and large-scale IP networks -- not WANs that include TDM, frame relay, ATM, or wireless technologies. Nevertheless, the program has many features of higher-priced packages, including object orientation and device libraries, drag-and-drop component assembly, simulation capabilities, network documentation, and bill of materials support. An advanced Boolean search engine helps you locate any database element.

Web-Accessible Tools

The Web, besides extending help desk support, configuring and monitoring network devices, accessing network performance data, and enabling and disabling device operations, can also assist with network design.

NetSuite development tools help network professionals design and draw a mammoth network and publish their designs on the corporate intranet or the public Internet. Any authorized user can view them with a Web browser. NetSuite DesignView converts network designs and device details developed in NetSuite Professional Design into hyperlinked Hypertext Markup Language (HTML) documents with device configurations, port usage, and even device photographs. Users can easily navigate from device to device to trace connectivity and review device configurations. Besides supporting fault identification, the hyperlinked documents can be useful when you have to plan design changes.

Achieving specific design objectives requires properly configured equipment at each node. Calico Technology provides a product configurator that interconnect vendors can use to help their systems engineers, value-added resellers, and large customers accurately configure complex, built-to-order products such as routers and hubs.

Cabletron and Cisco are two of the companies that use the Calico Configurator. For example, authorized users can access Cisco's Configurator Agent page on the Web, search for configurable products, choose a particular model, and configure it. A Cisco 7000 backbone router, for example, can be configured for software options, power supply, power cables, memory, route and switch processors, and interface modules. Error messages flash on screen to indicate if you've picked a particular equipment configuration that's invalid, and suggestions help you pick the best configuration. The controls on the page allow you to then send the order to Cisco.

Not Quite Rome in a Day

In simpler days, network gurus kept information systems and networks operating smoothly with all configuration details tucked away in their gray matter. Today, systems are distributed and networks are going global. With intelligent hubs, switched LANs, sprawling router networks, broadband facilities, and advanced services like frame relay and ATM in the mix, large-scale networks are beyond mere human comprehension.

A new generation of intelligent design tools with built-in error detection, simulation and analysis, and plug-in function modules, has finally arrived. Managers and planners needn't be intimately familiar with every aspect of their networks. You can retrieve essential information instantly -- often with point-and-click ease -- then analyze, query, manipulate, and reanalyze that information if necessary. You can display the results in easy-to-understand graphics or export it for further study. Since products differ in the type and scope of data they provide, tools from different vendors may be necessary. Ultimately, the quality and completeness of the data determine the optimal network design.

With these powerful and intelligent new network design tools, you still may not be able to build Rome in a day. But you at least have a chance to build a solid foundation.

## Where To Find

American Hytech

Pittsburgh, PA

Phone: (412) 826-3333

Fax: (412) 826-3335

http://www.fyi.net/~netguru

Internet:

http://www.fyi.net/~netguru

Calico Technology

San Jose, CA

Phone: (408) 975-7400

Fax: (408) 975-7410

http://www.calicotech.com

Internet:

http://www.calicotech.com

ImageNet

Wellesley, MA

Phone: (617) 239-8197

Fax: (617) 239-8198

http://www.imagenet-cane.com

Internet:

http://www.imagenet-cane.com

Make Systems

Mountain View, CA

Phone: (415) 941-9800

Fax: (415) 941-5856

http://www.makesys.com

Internet:

http://www.makesys.com

MIL 3

Washington, DC

Phone: (202) 364-4700

Fax: (202) 364-8554

http://www.mil3.com

Internet:

http://www.mil3.com

NetSuite

Wayland, MA

Phone: (508) 647-3100

Fax: (508) 647-3112

http://www.netsuite.com

Internet:

http://www.netsuite.com

Network Design and Analysis

Markham, Ontario, Canada

Phone: (905) 477-9534

Fax: (905) 477-9572

http://www.ndacorp.com

Internet:

http://www.ndacorp.com

5"Intelligent" Icons Add a Dose of Reality to Designs

With some network design tools, hardware icons contain configuration information about the components they represent.

## Design's Four Stages

Large-network design tools can improve and simplify every stage of the design process.

## Smart Management

Each item drawn in NetGuru is an intelligent icon that references information for network design, validation, and simulation.

## Tis A Gift to Be Simple

Network Design and Analysis's AutoNet/Performance-3 offers simple graphical design tools and analysis functions.

mailto:"nmuller@ddx.com"

Nathan J. Muller, based in Huntsville, Alabama, writes extensively about computers, communications, and management. Among his latest books is Network Planning, Procurement & Management, published by McGraw-Hill. You can reach him by sending e-mail to

nmuller@ddx.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## State Of The Art

## State Of The Art

## Building the Model Network

Commercial tools help system administrators manage traffic jams and avoid downtime.

Charles D. Knutson

How do you efficiently design, build, grow, and manage huge networks without being able to automatically model and simulate them? Answer: not very easily.

Modeling is based on the existing large network. A good model can show you nooks and crannies, and their technical features, where you never even knew you had nooks and crannies. Modeling captures the network in a static or a dynamic snapshot for further analysis. What kind of analysis? Let's say you're considering new topologies. You might want one clear diagram of your until-now ad hoc accretion of network segments. You will probably also want to test aspects of network capabilities: Testing exercises network components to find their limits.

Simulation uses the network as a base, then goes off into the

what-if world

that's essential for planning. Naturally, designing large networks (see the article "Design and Conquer") involves simulation, and maintaining networks (see the article "See the Big Picture") involves testing. System administrators are in the tricky position of trying to satisfy everyone on their big network. Here are some automation tools that can help administrators deliver satisfaction.

Good Models Make Good Networks

To manage a complex network and avoid system degradation and downtime, it's critical to have a view -- a model -- of what the network looks like. When big nets go down or slow down, companies lose big money. That's where a good model comes in. Like a road map when you're hopelessly lost and late, a detailed network model can simplify and speed solving network hang-ups. Without a detailed network model? You could be hosed before you know what hit you. As Bob Ross, president of LAN Utilities (Pleasant Grove, UT), developers of LAN test tools, says, "The self-perception of administrators is that they deal with problems within 20 minutes, but that's only after they find out about them."

Luckily, there are tools that can help create detailed and useful models of even the most arcane and far-flung nets. PinPoint Software continues to improve ClickNet, its network-diagramming product that allows administrators to customize graphic views of a network. It interfaces with network management packages (including Seagate's LAN Directory for Windows and McAfee's Saber LAN Workstation), can download information (about cable configurations; types of workstations, servers, hubs, and routers; and mission-critical software packages), and can automatically generate a graphic model of the network.

While Visio's Visio Technical 4.0 and Visio Shapes for Network Equipment may provide more powerful drawing capabilities -- drag-and-drop diagramming, clean interface, and ease in aligning and moving objects without breaking connections -- they can't directly import information from network management packages. One of the more impressive and intelligent network-diagramming tools is Quyen Systems' netViz. Besides powerful drawing capabilities, netViz automatically discovers and displays information about nodes on a Novell network, identifying servers, workstations, and volumes. Automatic discovery does not rely on some earlier (and possibly out-of-date) database of network information. The larger the network, the more critical automatic discovery is for developing an accurate and useful model of that network for testing or simulation.

These diagramming tools ultimately deliver a static model of a system, which can help an administrator design and implement a network, understand the complexity of an existing one, and suggest areas that might become problematic. But nothing beats real-time information displayed graphically. Novell's ManageWise 2.1 allows administrators to model (and also manage) a network from a central location (the console runs under Windows 95 or Windows 3.1). ManageWise can

discover and map

all network devices and inventory the current hardware and software of workstations and servers, creating a dynamic model of the network. And not just for Novell's NetWare. ManageWise can also integrate with enterprise consoles such as IBM's System View for AIX, HP's OpenView, and Sun's Net Manager. The result is the ability to see at a glance when printers, servers, hubs, and routers die. Just as important, ManageWise tracks and displays network performance and

warns when

system behavior might suggest impending problems. ManageWise supports many snap-in applications, such as DenMac's Alert Pager, which immediately informs net supervisors of problems. That means an administrator on the golf course can receive a pager message with the news that a key server has died -- unpleasant as golf rounds go but essential for limiting network downtime.

Good Simulation Means Better Testing

A network simulation builds on a model, then brings it to life. Like a model train layout, a network simulation gets all the make-believe traffic moving, all the imitation lights blinking, and all the artificial crack-ups resulting. This is especially crucial with large networks, since no mere mortal can keep the whole conglomeration straight in his or her mind. With a good simulation, you can spot bottlenecks, buildups, and backups. Simulation is also a valuable basis for testing, since you can try things out on the simulator before flying the real fighter jet.

Unleashing new applications or new changes on an unsuspecting large-scale network can be disastrous. Developers especially face this problem. "That's one thing I've definitely found," says Ross. "In a development environment, usually you're fairly sequestered. It's usually not that busy of a network. So the engineers typically are developing on this quiet net, and then you throw the software onto a production environment and it goes berserk." New applications may also face mysterious and temperamental real-time problems -- sneaky bugs that appear only at certain times of the day or under certain kinds of traffic loads. The hardest part of crushing these bugs is recreating them. To do that, the system administrator has to be able to replicate not just traffic volume but particular kinds of traffic.

So how do you adequately test a client/server application product that has never seen a really ugly network? Build your own ugly network! Chariot, from Ganymede Software, is a tool that can simulate the traffic of client/server applications. Using Chariot, you can force a server to handle many concurrent requests from "clients" artificially made by the simulator -- for a fraction of the cost of doing it live on multiple hardware platforms. CenterLine Software's QC/Sim has other nifty features for creating ugly environments in which to test distributed software. Operating as an add-on to QC/Coverage, a code-testing product, QC/Sim can fake scenarios that are difficult to replicate in practice, like network failures, limited disk capacity, and other real-life horror stories.

Bringing It All Together

In an ideal world, you would buy your whole network from a single vendor, with one perfect modeling and simulation product. But in reality, your huge network has probably snowballed until it seems to have a life of its own. "Larger organizations with multiple deployed offices don't go to Ford and buy," observes Bill Gillman, vice president of operations at Gentner Communications Corp. (Salt Lake City, UT), a manufacturer of telecommunications equipment. "They go to the store and pick some NAPA parts and some GM parts and some Ford parts, and they build their own custom car." As a result, the average system administrator has a nearly impossible task. You need a product that can, first, create a model of your patchwork network and, second, let you simulate what-ifs to that network. So what do you do?

You must zealously identify the tools that can grasp your network's complexities, then assemble those tools into a system that works. Large networks are built out of disparate hardware platforms, operating systems, and applications, and managing them is a daunting adventure. Without the right tools, it's downright impossible.

## Where To Find

CenterLine Software

Cambridge, MA

+Phone: (800) 669-2687 or (617) 498-3000

Fax: (617) 868-6655

http://www.centerline.com

Internet:

http://www.centerline.com

DenMac

Northbrook, IL

+Phone: (800) 315-0952 or (847) 291-7760

Fax: (847) 562-0013

http://www.denmac.com

Internet:

http://www.denmac.com

Ganymede Software

Research Triangle Park, NC

Phone: (919) 558-1138

http://www.ganymede.nctda.org

Internet:

http://www.ganymede.nctda.org

## Novell

Orem, UT

+Phone: (800) 453-1267 or (801) 222-6000

http://www.novell.com

Internet:

http://www.novell.com

PinPoint Software

San Jose, CA

+Phone: (800) 599-3200 or (408) 997-6900

http://www.pinpt.com

Internet:

http://www.pinpt.com

Quyen Systems

Rockville, MD

Phone: (301) 258-5087

Fax: (301) 258-5088

http://www.quyen.com

Internet:

http://www.quyen.com

Visio

Seattle, WA

+Phone: (800) 446-3335 or (206) 521-4500

http://www.visio.com

Internet:

http://www.visio.com

-Find Solutions Through "What If" Simulations

One of the most valuable things about simulation tools is they let you try out different "what if" solutions to network problems.

## Novell Helps You Manage Wisely

Novell's ManageWise 2.1 dynamically discovers and graphically displays all network devices for modeling and managing.

'Summaries and Alarms Keep You Informed

ManageWise also summarizes network configurations and sounds the alarm when system behavior goes awry.

mailto:"cknutson@csconsult.com"

Charles D. Knutson owns ComSoft Consulting in Corvallis, Oregon. In a previous life he was a system test manager for NetWare Client Products at Novell. You can e-mail him at

cknutson@csconsult.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## State Of The Art

## State Of The Art

## See the Big Picture

Tracking thousands of users -- and the related troubleshooting -- can be made simpler with the right tools.

Tim Wilson

If you manage a large network, your job description is simple: Keep your organization's network up and running 24 hours a day, seven days a week, preferably at peak performance. Do a good job, and no one even knows you're there. But if the network crashes, it could cost your organization thousands, even millions, of dollars in lost business and productivity. And you could lose your job. (Gulp!) The task is much like piloting an airplane: hours of boredom punctuated by moments of sheer terror.

You can boil down your job description to a simple axiom: Uptime good, crash bad. That sounds simple enough. It's actually not too much different from managing a 10-node LAN, except that you can't use Norton Administrator to troubleshoot a 20,000-node network that spans 15 countries and includes everything from IBM mainframes to laptops and from multiprotocol routers to T1 multiplexers. For this job you need software with a little bit more power -- what has now become known as an enterprise management system.

IBM, in the mainframe-oriented heyday of the 1980s, was the first company to develop an enterprise management system capable of monitoring and controlling networks consisting of thousands -- even tens of thousands -- of hosts and terminals. That software package, called NetView, opened up a new range of applications that ranks today as one of the data communications industry's hottest markets, which includes competitors from powerhouses such as Computer Associates, Digital Equipment, Hewlett-Packard, and Sun Microsystems.

This emerging range of enterprise management applications has changed significantly over the past decade, creating new capabilities that enable network administrators to monitor and control remote computers and other devices. But many managers of mega-networks, whose jobs are on the line, say the technology has not evolved rapidly enough for their liking.

Setting the Standard

The problem, MIS executives say, is that most so-called network management tools -- such as Cisco's CiscoWorks and Novell's ManageWise -- are designed to manage only particular devices or systems, such as routers and LANs, in the enterprise, not the entire network. These applications (collectively known as element management systems), which include modem, hub, and multiplexer management systems, gather data about the operating status of specific types of network devices (e.g., LAN servers, routers, and hubs) and display it on a Unix workstation or PC monitored by the network administrator.

Element management systems typically are included with network devices, which means that the corporate network administrator who manages equipment purchased from many different vendors might have as many as 100 different consoles to monitor. This has created a need for "swivel-chair network management": the act of swiveling or rolling one's chair among many different consoles in an effort to locate the genesis of a network failure (see the figure

"Swivel-Chair Management"

). It's kind of like walking around with binoculars strapped to your head; you can see one focused area, but you can't step back and look at the whole picture.

Enter the enterprise management platform, usually a high-powered Unix-based workstation that can run many element management system applications simultaneously. The goal of the enterprise management platform is to provide a single workstation (or group of workstations) that can run many different element management applications and, ultimately, integrate the data from these applications to provide a "big picture" view of the entire enterprise network.

A good idea? Definitely. The problem is that not all element management systems speak the same language or report their status information in the same format. A standard protocol for transmitting and handling network management information is required. Most network devices today use SNMP, a standard published in 1992 by the Internet Engineering Task Force (IETF), the same body that sets guidelines for the Internet.

SNMP defines a method for collecting and formatting information about the devices to be managed through a small piece of software known as an agent. An SNMP agent can be installed on any intelligent device. Non-SNMP devices can be managed through proxy agents that translate any kind of status information sent to an intelligent agent.

Today, most network devices come with built-in SNMP agents that let them transmit status information to an SNMP-based management system. An administrator sitting at the console of one of the more popular SNMP-based enterprise management platforms, such as HP's OpenView and Sun's SunNet Manager, can gather and correlate data from a variety of SNMP-compliant devices and systems. This provides a broader view of the topology and status of the entire network (

see the figure

). Most smaller networks do not require SNMP because they don't have the wide variety of hardware and software required in big networks.

## Under Construction

Over the past several years, SNMP agents have been added to many network devices, and enterprise management platform vendors have been improving their products as they fight a pitched battle for industry leadership. Yet despite these steps forward, many corporate network administrators say they're still far from their goal of developing a common set of tools for enterprise management.

One problem is that many network elements still cannot be managed by SNMP. For example, most firms haven't scrapped their mainframes, which generally employ IBM's Systems Network Architecture (SNA) protocols. These SNA networks cannot be fully monitored via SNMP, which leaves huge blind spots in the network administrator's view of the enterprise. Similar problems occur at the LAN level, where companies such as Microsoft and Novell have only recently begun to deploy SNMP in their server products.

To complicate matters, many network administrators now find themselves responsible for managing not only the corporate network but also the hardware and software at the end of each link. Increasingly, systems and applications management are tied to network management, but only network devices typically have built-in SNMP agents.

In addition, many administrators have been disappointed thus far with the lackluster performance of SNMP-based enterprise management platforms. One of the most important problems is a lack of scalability. Initial releases of several SNMP platforms -- including offerings from HP, IBM, and Sun -- were based on a single Unix server that couldn't share information with other management servers.

"In that world, you could see the entire environment, but only if it was small," explains Andy Vanagunas, product manager for HP OpenView. "In the larger environments, it was a little like driving with your windshield half-covered."

Under these limitations, the so-called enterprise management platforms could realistically manage only around 1000 nodes -- only a slight improvement over some higher-powered LAN management systems. Although some vendors -- notably Cabletron Systems, Groupe Bull, and HP -- have fixed this problem to provide high scalability in current releases, many potential buyers are still stinging from the failure of those early releases to meet their high expectations.

Another deficiency in many currently available enterprise management platforms is the absence of communication between element management applications running on the same platform. While administrators may have reduced the number of consoles to be monitored, they still must correlate in their heads the data gathered by multiple applications.

For example, a router failure on a network might terminate communications with 100 systems attached downstream from that router. Sitting at the SNMP enterprise management console, the network administrator is suddenly swamped with 101 alarms that indicate a system failure. Yet only one is the cause of the problem; the other 100 are only symptoms. In many cases, it's left to the network administrator to determine which is which.

This problem has created a niche market for management software that can correlate network events and present the administrator with root-cause information. This correlation can take place in one of two ways: through filtering, which eliminates event data that's downstream from the root problem; or through true correlation, in which data from several different applications is intelligently reviewed and processed to determine the interrelationship between separate network events.

Although event correlation is still a fairly new idea, a number of related products have been on the market for several years. Seagate, for example, offers a package called NerveCenter that correlates SNMP events; other suppliers, such as Boole & Babbage, Maxm, and Objective Systems Integrators, sell products that focus on the correlation of events in non-SNMP legacy environments as well.

Sometimes the lack of data integration between management applications creates difficulties in pinpointing the origin of a network problem. For instance, the router might indicate that a problem is caused by an overflow of data from a particular server; meanwhile, the server may indicate that the problem is in the router. This situation, sometimes called finger-pointing, is a common complaint of enterprise management platform users.

Many enterprise management platform vendors hope to solve the finger-pointing problem by rebuilding their network management applications using object-oriented technology. This capability, which is already in development at companies such as Groupe Bull and IBM/Tivoli, will let users share data across multiple applications, in much the same way that users of the Microsoft Office suite can share information across Word, Excel, and PowerPoint via OLE.

User Approaches

Besides dealing with the deficiencies of technology and tools, corporate network managers must also face the grim reality that no two organizations, or their networks, are alike. Therefore, the method of implementing enterprise network management platforms might differ significantly from company to company.

Some firms, particularly long-established IBM mainframe shops, have a central data center that controls most of the data network management functions in the enterprise. These organizations prefer a central point of control for monitoring all network activity, such as what the mainframe-based NetView provided in past years. This allows all troubleshooting, as well as other administrative tasks, to be handled by a centralized group of people and software.

In today's client/server multivendor environment, this centralized method of control can even be applied to the use of SNMP-based enterprise management systems. The network manager might divide the enterprise into multiple management domains -- based on geography, applications, or traffic type -- each managed by local SNMP platforms. These local platforms would all be connected to a single, central platform that collects filtered data to create a high-level view of the entire enterprise.

However, the proliferation of client/server technology, as well as the decentralization of many large businesses, is making centralized management increasingly difficult. In many large enterprises, network management and administration decisions are made at a departmental or business-unit level. The central MIS manager is responsible for coordinating these distributed activities -- as well as distributed multivendor tools and personnel -- across the enterprise.

Unfortunately, there are no universal truths as to whether centralized or distributed approaches work best in the very largest networks. The decision to use centralized or distributed network management is much like the decision between centralized and distributed personnel management; how you do it depends largely on how the organization operates.

SNMP-based enterprise management platforms were designed to function in distributed environments, collecting data in many different formats across many different domains (

see the figure

). But, as previously mentioned, the lack of server-to-server communications capability in many SNMP platforms has made this approach hard to implement, since this capability is a prerequisite for scalability in very large network environments.

Whether centralized or distributed, it seems that today's enterprise management platforms have barely scratched the surface of the data they will eventually have to manage. In large organizations, the network management system is rapidly becoming the point at which the pulse is taken for the entire IS environment.

For example, many enterprise management platform vendors are adding systems management capabilities to their network management platforms. These capabilities let an administrator monitor hardware parameters, such as I/O performance, response times, and storage utilization, as well as the performance of the network. In fact, some products, such as HP's IT/OperationsCenter and IBM's SystemView, actually subordinate the network management function to a higher-level system management function.

Large organizations have recently taken this evolution a step further by focusing on enterprise applications management. Administrators employ systems and network management tools only to support the end game of ensuring that specific mission-critical applications are available and are performing well. This approach makes sense to CEOs and end users, who seldom have a great deal of knowledge of network or systems management but know when their applications are not performing as they should.

The addition of systems and applications management functions threatens to completely overwhelm today's enterprise management platforms, which have already proven to be deficient in handling network-specific data alone. How will these platforms be able to keep up?

One development that will help is the recent improvement in SNMP platform scalability. Several of the industry's leading platforms, including HP's OpenView and Cabletron's Spectrum, are now delivering server-to-server distribution capabilities that should enable them to scale to infinitely large networks. The ability of these systems to handle network and systems information -- even in environments of 10,000 nodes or more -- is improving significantly.

Object-oriented technology may make it easier for applications running on the same platform to share data. Companies such as IBM/Tivoli are advancing new object-oriented frameworks for building management tools; this should result in improved integration. Vendors are also integrating event correlation, rules-based reasoning, and even AI into network management systems to reduce reliance on human operation and make network administrators more productive.

Will tomorrow's enterprise management systems replace the human network administrator? Not in our lifetimes. But with new technology, administrators may be treated to a little more boredom and a lot less terror.

## Swivel-Chair Management

## Centralized SNMP Management

## Distributed SNMP Management

mailto:"twilson@decisys.com"

Tim Wilson is a senior consultant at Decisys, Inc., an enterprise network consulting firm based in Sterling, Virginia. You can reach him at

twilson@decisys.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## State Of The Art

## State Of The Art

## Tornado Touches Down

The oldest and best-known Unix-based enterprise manager on the market today is Hewlett-Packard's OpenView, which was introduced in 1990. OpenView uses the industry-standard SNMP protocol to gather data from multiple network elements via many different network management applications that run on a common workstation.

In 1993, HP began working on a new version of OpenView that was designed to manage very large networks through the distributed interconnection of multiple OpenView servers. This new version, code-named Tornado, was HP's answer to OpenView's limitations. At that time, the software could manage a maximum of only about 1000 nodes.

Development problems caused the delivery of Tornado to be delayed more than a year, but last year HP shipped an initial release that expanded the system's ability to process management data as well as increase the number of operators that could work from one OpenView server. However, Tornado 1 didn't provide the distributed capabilities required in the largest corporate networks.

In March, HP unveiled the Tornado 2 release of OpenView, which offers much-expanded distributed management capabilities. Tornado 2, officially designated HP OpenView Network Node Manager 4.1, lets managers use multiple Unix workstations to gather information about networks of 10,000 nodes or more. In the fall, HP will deliver the same software on a Windows NT platform.

The new release of OpenView also includes a new management tool, called OpenView Workgroup Node Manager, which is designed to manage smaller workgroups or departmental networks. The workgroup management tool, which also runs on Unix or NT, can interface with Network Node Manager 4.1, enabling users to handle some management tasks locally without giving up the ability to pass some management information to an enterprise management platform in the central network-control center.

## Monitor the Hordes

~HP OpenView Network Node Manager 4.1 lets multiple Unix and Windows NT workstations monitor networks with thousands of nodes.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## BYTE Hardware Lab Report

## BYTE Hardware Lab Report

$19 Pentium Portables Do Multimedia

With Pentium processors, gigabytes of drive space, large screens, and CD-ROM drives, these notebooks are more than ready for prime time.

+Maggi Bender, Jim Kane, and John McDonough

When it comes to work, today's multimedia notebooks certainly let you take it with you. Running Pentium processors at rates of up to 166 MHz, today's multimedia notebooks might not be as fast as the top Pentium and Pentium Pro desktop systems, but they make good business computers, both on the road and in the office. These high-end Pentium notebooks are also expensive, being almost twice the cost of comparably configured desktop systems. However, with accelerated graphics, large active-matrix color displays, CD-ROM drives, and 810-MB or larger hard drives, they provide

full-throttle computing

for on-the-go professionals.

We tested 18 Pentium portables that range in price from $3000 to almost $7000 and employ 100-, 133-, or 166-MHz CPUs. We also included Canon's AMD 5x86-powered Innova Book 360CD (see the article "AMD Inside"), which provides Pentium performance. You can buy a more economical 486DX4-based notebook, but you'll want a Pentium to handle graphics-intensive multimedia tasks under Windows 95 or OS/2 Warp -- and to delay your next upgrade cycle.

Modular components have become a hot notebook feature. Many high-end notebooks we test here provide an all-purpose bay that can hold a CD-ROM player, a floppy drive, or an additional battery. You swap them in and out depending on what you need. You can't use floppy and CD-ROM drives simultaneously, but the modular design saves space, weight, and battery power while maintaining desktop functionality. We included two ultrathin systems -- Digital Equipment's HiNote Ultra II and the Impulse Duonote -- because they have attachable multimedia bases for CD-ROM and stereo-sound functionality, another form of modularity.

Most of the portables we tested have removable hard drives, a feature that ensures upgradability. Even the 2.1-GB hard drive in Micro-International's Mint 5200 may seem small in a year or two. Most notebooks have two Type II PC Card slots and infrared ports for cableless file transfers. The Toshiba and NEC units implement the new 4-Mbps IrDA 1.1 infrared standard.

All test notebooks came with active-matrix screens that display graphics with crisp details and deeply saturated colors. With three 10.4-inch exceptions, the high-end notebooks we reviewed have either 11.3- or 12.1-inch SVGA displays. All can display at 800- by 600-pixel resolution, which is great for Windows 95, but you'll want a big display and one with a wide horizontal viewing angle if you routinely use your notebook with a handful of people sitting around a table. The 12.1-inch panels provide roughly the same viewable screen real estate as a 14-inch desktop monitor.

Less expensive passive-matrix displays are still an option with most of these products, but the trend is toward the bigger, brighter, more responsive active-matrix displays. IBM, for instance, dropped its ThinkPad 550 with the pop-open butterfly keyboard so it could add more screen real estate, and Toshiba's cutting-edge Tecra 730CDT supports an unusual 1024- by 768-pixel resolution on its 12.1-inch screen (we reviewed the Tecra 500CDT).

Those notebooks costing more than $5000 are from big-name vendors such as Compaq, Gateway 2000, IBM, and NEC Technologies. Compared to less expensive units, they come with more software and longer warranties. A unit such as IBM's ThinkPad 760ED, for instance, has multimedia luxuries: a 64-bit graphics chip with 2 MB of dual-ported video memory, hardware-assisted MPEG playback, an internal 28.8-Kbps data/fax/telephony modem, and lithium-ion batteries that outlast nickel-metal-hydride (NiMH) batteries in our battery run-down tests.

Such feature-laden portables use battery power quickly. We suggest that you get a notebook that can hold multiple lithium-ion batteries if you want to work throughout a cross-country plane flight.

The two 166-MHz notebooks we tested turned out not to be the fastest. In spite of 256-KB Level 2 caches, the Chem Book 5580 and the Micro-International Mint 5200 didn't perform as well as the 133-MHz NEC Versa 6030H. Typically, a 166-MHz Pentium system should perform 10 percent faster than a 133-MHz system. The Mint 5200 suffered from below-average memory performance and slow hard drive and CD-ROM drive speed.The Chem Book 5580 was hurt by poor memory and hard drive performance.

For multimedia, software development, or just to load large applications, a notebook must have a built-in CD-ROM drive. We recommend that you get one with a four- or six-speed CD-ROM drive for faster read and seek times. Multimedia notebooks must also have integrated stereo speakers, though a small speaker size limits sound quality.

Notebooks that come with hardware-assisted MPEG -- the Compaq LTE 5300, NEC Versa 6030H, Nimantics Quanta 6x 133, Impulse Duonote, and IBM ThinkPad 760ED -- can effectively zoom video clips to full-screen without the dropped frames and blocky pixellation associated with software-only MPEG. Having 1 or 2 MB of dedicated video memory and a PCI-bus architecture also helps to enhance graphics I/O performance.

Toshiba's Tecra 500CDT has a Zoomed Port Video (ZPV) PC Card slot. The proposed ZPV standard establishes direct communication between the PC Card controller and the audio and video controllers, so that large amounts of multimedia data don't require processing through the CPU or system bus. When ZPV cards become widely available, the Tecra 500CDT will provide a fast connection for full-motion video playback. The Tecra 500CDT and NEC's Versa 6030H also support CardBus, another proposed standard. This standard provides for 32-bit PC Card peripherals such as Fast Ethernet and Fast SCSI adapters.

Contributors

Jim Kane, Project Manager/NSTL

John McDonough, Technical Writer/NSTL

Maggi Bender, Senior Tester/NSTL

Dave Rowell, Senior Technical Editor/BYTE

## Portable Multimedia

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## BYTE Hardware Lab Report

## BYTE Hardware Lab Report

## Pentium Portables

Almost every desktop maker now has a portable for sale, and the market is stratifying with notebooks at different price/performance levels. Higher-priced Pentium notebooks are heavy on cutting-edge components, while value systems are capable but lack such advanced features as hardware-assisted MPEG playback. For this reason, we rated the notebooks in three categories: best-overall portable, best desktop replacement, and best low-cost notebook (under $4000).

## BEST OVERALL

We chose the well-rounded NEC Versa 6030H as the best-overall notebook. It has fast performance, a multitude of portability features, and a high ease-of-use rating. While the Versa 6030H is a hot multimedia notebook, several other models weren't far behind in our best-overall ranking.

Shadowing the Versa 6030H was the WinBook FX (our pick for best low-cost system; see below). Toshiba's 8.2-pound Tecra 500CDT also did well. The $4999 unit provides many leading-edge features, including Zoomed Port Video (ZPV) and CardBus support, as well as 4-Mbps IrDA capability. With a 120-MHz Pentium, it performed better than many units with 133-MHz processors, and it placed in the top five for battery life.

Impulse Computer may not be familiar to many users, but its Duonote made a big splash in our Lab Report. It's a moderately priced multimedia notebook ($4699) with a nice modular design. Compaq's $6398 LTE 5300 is a 7.4-pound lightweight that also placed in the top five. The highly modular system scores high in features (right behind the IBM ThinkPad 760ED and Hewlett-Packard's OmniBook 5500 CTS) and also in usability, because Compaq supplies a three-year warranty and 24-hour, toll-free technical support. (An even more modular model that wasn't ready in time for this roundup is the Compaq Armada 4100; see the article "Notebook Under Construction" in the Reviews section.)

Best Desktop Replacement

Several notebooks in this roundup beg the question: "Do I really need that desk-stealing power hog back in my cubicle?" Not only do these systems provide excellent docking options, the best desktop-replacement systems run fast and furious in our performance benchmarks, providing desktop-level performance. NEC's Versa 6030H, our best-overall pick, is again the winner, but some strong runners-up are Toshiba's Tecra 550CDT and Compaq's LTE 5300.

The 7.5-pound Nimantics Quanta 6x 133 is an affordably priced ($3999) multimedia notebook with high-end functionality. It has a 12.1-inch SVGA display, a voluminous 2.1-GB hard drive, and an efficient lithium-ion battery that lasts 2 hours and 37 minutes in our tests.

HP's OmniBook 5500 CTS ($6120) costs much more than the Quanta 6x 133, but it's a premium notebook for making presentations with its wide-angle 12.1-inch SVGA display.

Best Low Cost

It's quite a stretch to call any multimedia notebook a low-cost product, but some are easier on the credit card than others. We drew a low-budget line in the sand at $4000, which left us with nine notebooks. The WinBook FX is our low-cost winner. It had high all-around scores and did particularly well in usability. Nimantics' Quanta 6x 133 took the number-two spot, followed closely by Texas Instruments' 100-MHz Extensa 570 CDT.

Dell's Latitude LM P-133ST had the best battery life of all the test units. Its lithium-ion battery and effective power management scheme kept it going for 3 hours and 41 minutes in our battery run-down test. We must also give battery-life honorable mentions to the Gateway Solo S5-133 (3:31) and IBM's ThinkPad 760ED (3:24), which both also use lithium-ion batteries (but aren't low-cost portables).

The 6.1-pound TravelPro 1900 ($3695), from AMS Tech, is a top-quality multimedia portable with a 133-MHz Pentium, a 12.1-inch SVGA display, a 1.3-GB hard drive, and a three-year warranty -- components and support you would expect from a higher-priced notebook.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## BYTE Hardware Lab Report

## BYTE Hardware Lab Report

## Taking the Heat

Heat is the limiting factor in getting high-end desktop performance out of a portable computer. The more heat a notebook design can dissipate, the faster you can reliably run the CPU or the more memory you can hold. Fan-induced convection cools most desktop systems, but fans are unacceptable in notebooks -- they're noisy, power-consuming, and a potential failure point. Convection also needs space for air to move, something compact notebook designs lack.

Good notebook designs rely instead on passive conduction. Heat is conducted away from the CPU, hard drive, and the graphics subsystem to exterior surfaces capable of radiating heat. The keyboard, the I/O port area, and (if it's not a docking unit) the bottom surface of the notebook (that isn't blocked by the battery) are all good surfaces for dissipating heat.

An aluminum heat sink will quickly draw heat away from the CPU, but the heat must then be conducted to the outside. Typically, metal sheets or frame elements, often made of a lightweight, conductive magnesium alloy, serve this purpose. Compaq's Armada 4100 series, for example, has a magnesium chassis that provides structural stiffness to the notebook, a path for outward heat conduction, and external radiation surfaces. Tadpole's notebooks can handle the latest desktop processors because they have a magnesium-alloy case that is thermally connected to the CPU.

Some designs use heat pipes to beef up thermal conduction by metal plates. These small-diameter sealed metal tubes contain a liquid that wicks from one end of the tube to the other, driven by a thermally induced fluid-to-vapor cycle. The pipe serves as a passive but effective heat pump.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## BYTE Hardware Lab Report

## BYTE Hardware Lab Report

## Pentium Portables Ratings

Best Overall:

## NEC Technologies Versa 6030H

The Versa 6030H ($5799) is our best-overall portable Pentium because

Fit is fast, feature-packed, and easy to use. The 9.5-pound unit races

Cthrough our benchmarks with a 133-MHz Pentium processor, 256 KB of

@synchronous pipeline cache memory, a PCI bus, and 2 MB of video

<memory. The Versa 6030H is a strong multimedia machine with

=hardware-accelerated MPEG for full-motion, full-screen video

@playback; a six-speed CD-ROM drive for fast data transfers; and

Dexcellent 16-bit stereo sound. The system also has a healthy bundle

Eof applications and telephony features for those who need to keep in

touch with the office.

Weighting:

Technology 10%

Performance 35%

Implementation 55%

Features 23%

Usability 23%

Battery 5%

Price 4%

Ratings:

O Price Tech- Imple- Perfor- Fea- Usa- Battery OVERALL

N nology menta- mance tures bility RATING

& tion

MNEC Versa 6030H $5799 **** **** ***** **** ***** *** ****

WinBook FX $3999 **** **** **** **** ***** *** ****

Toshiba Tecra $4999 **** **** **** **** ***** **** ****

500CDT

Impulse Duonote $4699 **** **** **** **** **** *** ****

Compaq LTE 5300 $6398 **** **** **** **** **** ** ****

Key

***** Outstanding

**** Very Good

*** Good

** Fair

* Poor

Best Desktop Replacement:

## NEC Technologies Versa 6030H

With its strong performance score, the Versa 6030H is also our choice

Dfor best desktop replacement. It is not only efficient but flexible

@with its easily accessible Versabay II, which supports a floppy

Cdrive, an extra hard drive, an extra battery, or the CD-ROM drive.

For an extra $799, NEC offers even more desktop functionality with

Fits Docking Station 6000, which has three expansion-card slots, three

Ddrive bays, built-in speakers, four audio ports, and an RJ-11 phone

jack.

Weighting:

Battery 10%

Usability 40%

Features 40%

Price 10%

Ratings:

P Price Tech- Imple- Perfor- Fea- Usa- Battery OVERALL

O nology menta- mance tures bility RATING

& tion

MNEC Versa 6030H $5799 **** **** ***** **** ***** *** ****

Toshiba Tecra $4999 **** **** **** **** ***** **** ****

500CDT

Compaq LTE 5300 $6398 **** **** **** **** **** ** ****

Nimantics $3999 **** *** **** **** *** *** ****

Quanta 6x 133

MHP OmniBook $6120 **** **** *** ***** **** ** ****

5500 CTS

Key

***** Outstanding

**** Very Good

*** Good

** Fair

* Poor

Low Cost:

## WinBook FX

You don't have to pay $6000 for a multimedia notebook. The WinBook FX

Dgoes for $3999 and sacrifices little. With a 133-MHz Pentium, 16 MB

Cof RAM, and 1 MB of video memory, the WinBook FX does admirably in

Cour performance benchmarks. The 6.8-pound laptop has an 11.3-inch

@SVGA display, Sound Blaster Pro-compatible sound, a 1.3-GB hard

Fdrive, and a lithium-ion battery that lasts 2 hours and 38 minutes in

our Thumper II run-down test.

Weighting:*

Technology 10%

Performance 35%

Implementation 55%

Features 23%

Usability 23%

Battery 5%

Price 4%

*Sub-$4000 notebooks only

Ratings:

P Price Tech- Imple- Perfor- Fea- Usa- Battery OVERALL

O nology menta- mance tures bility RATING

& tion

WinBook FX $3999 **** **** **** **** ***** *** ****

Nimantics $3999 **** *** **** **** *** *** ***

Quanta 6x 133

MTI Extensa $2999 **** **** *** **** **** ** ***

570 CDT

Dell Latitude $2999 **** **** ** **** **** ***** ***

LM P-133ST

MAMS Tech $3695 **** **** *** **** **** *** ***

TravelPro 1900

Key

***** Outstanding

**** Very Good

*** Good

** Fair

* Poor

## NEC Technologies Versa 6030H

## NEC Technologies Versa 6030H

## WinBook FX

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## BYTE Hardware Lab Report

## BYTE Hardware Lab Report

## Details

If you find most notebook designs boringly similar, check out Digital Equipment's HiNote Ultra II. Its sleek,

angled chassis

should turn the head of any individualist. The HiNote Ultra II has a lithium-ion battery that clips onto the rear and two attachable base modules: One is a thin wedge with a floppy drive, while the larger multimedia base provides speakers and a CD-ROM drive. Do you think Compaq found inspiration here for its new Armada 4100?

Users can often choose from many different peripherals when buying a notebook, but the

pointing device

usually isn't one of them. The WinBook FX comes standard with a pointing stick between the G, H, and B keys. For an extra $80, however, you can opt for a dual-button touchpad.

NEC's Versa 6030H has two hot-loaded McAfee antivirus software packages -- VirusScan and WebScan -- that

guard the system

t from known viruses and provide virus protection for the most popular Internet services, Web browsers, and e-mail.

## Ultracool Design

## Making Your Point

## NEC's Bug Barrier

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## BYTE Hardware Lab Report

## BYTE Hardware Lab Report

## Up Against the Wall

John McDonough

Hooking a 17-inch monitor to a notebook is a cost-effective way to make a presentation to a small group of people sitting around a table. For larger groups, however, you need projection. You can buy an LCD panel that sits on an overhead projector or a self-contained projection unit. In either case, your notebook drives the display. Wedge Technology's ShowBiz 5000P ($4799) provides another option.

The

ShowBiz 5000P

is a Pentium notebook with an LCD that converts into an overhead projection panel. Like a few projection notebooks before it (see "Presentation Quality," September 1995 BYTE), the ShowBiz 5000P lets you make large-room presentations at any office with an overhead projector. While the ShowBiz 5000P is best for software demonstrations, Wedge also offers optional MPEG playback and TV cards, so you can project videos 6 feet high on a screen.

We found the LCD projection panel easy to set up. After removing a protective back panel from behind the ShowBiz 5000P's 10.4-inch active-matrix display, you place the LCD panel on an overhead projector. A support tray for the notebook itself attaches to the projector. The display supports 800- by 600-pixel resolutions at 65,536 colors. The unit comes with a cooling fan that connects to the LCD panel to dissipate the heat from the projector's lamp.

Though the projected images are not as bright as on some desktop projectors (see the review "Road-Show Romance"), we found the images to be clear and well defined when shown in a fairly dark room. It takes some adjustment of the LCD projection panel to eliminate ambient light from the overhead projector, but that should not be a problem after you get used to setting it up.

The notebook sits directly in the path of the overhead projector, so Wedge supplies an infrared-attached remote-control device so the presenter can control the PC. Mind Path's Presentation F/X software lets you move the mouse around the display and zoom in on different areas of the screen.

## Product Information

ShowBiz 5000P..................$4799 (fully loaded system}

Wedge Technology, Inc.

Milpitas, CA

Phone: (408) 263-9888

http://www.wedgetech.com

Internet:

http://www.wedgetech.com

Circle 1080 on Inquiry Card.

$Effective Overheads from a Notebook

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## BYTE Hardware Lab Report

## BYTE Hardware Lab Report

## Test Specs

We picked the best portable Pentiums by running low-level and application benchmarks under Windows 95, as well as battery tests under real-world conditions. We also weighted important notebook features and how easy a system is to set up and use.

## Performance

For the Windows 95 application benchmarks, we ran scripts with 32-bit versions of Microsoft Word (7.0) and Excel (7.0) plus a 16-bit version of FoxPro (2.6). NSTL's low-level InterMark Multimedia PC tests exercise specific components of the notebook: CPU, hard drive, CD-ROM drive, and sound (percentage of CPU utilization). InterMark video benchmarks test how well a system can produce multiple Windows draws, bit-mapped images, and display screens generated by applications like PowerPoint and CorelDraw.

Battery Life

We measured battery life with our Thumper II battery run-down tester. Thumper II emulates a typical word processing session. It uses robotic arms and an optical screen sensor to detect and control each system's power management function. Before testing, we completely drained and recharged each notebook's battery twice, according to the vendors' instructions. People use their notebooks in different ways, so you will probably get different battery life with a given portable.

Features/Usability

We reward features that differentiate the notebooks. For instance, AMS, Compaq, Dell, Digital Equipment, Hewlett-Packard, IBM, Impulse, NEC, and Toshiba back their systems with impressive three-year warranties, as opposed to one-year warranties with the other vendors. We asked the vendors to fill out a lengthy features questionnaire, and we verified the features in the labs. For usability, technicians worked extensively with each notebook to assess the quality of the keyboard, status indicators, and pointing device. We also evaluated the user's manuals and checked how easy it was to install modular components and upgrade the systems with memory.

Evaluations in this report represent the judgment of BYTE editors, based on tests conducted by NSTL, Inc., as documented in a recent issue of its monthly PC Digest. To purchase a copy of the full report, contact NSTL at 625 Ridge Pike, Conshohocken, PA 19428; (610) 941-9600; fax (610) 941-9950; on the Internet, editors@nstl.com. For a subscription, call (800) 257-9402. BYTE Magazine and NSTL are both operating units of the McGraw-Hill Companies, Inc.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## BYTE Hardware Lab Report

## BYTE Hardware Lab Report

## AMD Inside

Not every road warrior can afford to fork over $3000 or more for a Pentium-powered multimedia notebook. Fortunately, Canon Computer Systems' Innova Book 360CD provides Pentium performance without the Pentium price. It's a full-fledged multimedia notebook with a price of only $2599, but it uses the Pentium-compatible 133-MHz 5x86 processor from AMD.

The Innova Book 360CD doesn't compare favorably with Pentium systems when tested with NSTL's InterMark test of low-level functions. In particular, it was dead last in memory performance. However, these factors don't appear to matter with Windows application performance. With our application tests, the Canon portable outshone all other test systems.

What's the price trade-off then, if not performance? For one thing, Canon cut costs on components by using a 10.4-inch dual-scan VGA display instead of an active-matrix screen and a nickel-metal-hydride (NiMH) battery instead of a longer-lasting lithium-ion battery. The battery lasted 2 hours and 18 minutes in our battery run-down tests, while lithium-ion-equipped models averaged 2:48.

The 6.7-pound (with battery) Canon notebook is light for a multimedia notebook, and it has a modular design with a four-speed CD-ROM drive on the right side that you can swap with a floppy drive. The laptop has an IrDA infrared port in the back, and a Type III PC Card slot and an external monitor port on the left side. It has a 32-bit VL-Bus architecture and 1 MB of video memory to boost its graphics performance.

The unit is ready to hit the road right out of the box with applications such as Sidekick for Windows 95 and FaxWorks 3.0. It also has on-line user documents for each of the bundled applications, so you don't have to drag manuals with you on business trips. Canon backs the Innova Book 360CD with a one-year warranty for parts and labor.

## Product Information

Innova Book 360CD....................$2599

Canon Computer Systems, Inc.

Costa Mesa, CA

Phone: (800) 848-4123

http://www.ccsi.canon.com

Internet:

http://www.ccsi.canon.com

Circle 1064 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## BYTE Software Lab Report

## BYTE Software Lab Report

## Running on NT

Is Microsoft's Windows NT 4.0 the answer to our OS prayers or just a set of incremental improvements?

Robert L. Hummel

A new (Windows 95) interface, Internet support, and distributed object technology make NT 4.0 worth buying, despite the installation hassles caused by its numerous hardware and software incompatibilities.

Without any fanfare, Microsoft has released the long-awaited upgrade to its high-end workstation and server OS products: Windows NT 4.0 Workstation and Server. In contrast to the pop-rock launch for the consumer-oriented Windows 95, Microsoft is aiming NT 4.0 squarely at business users. And with an impressive list of features and performance improvements, NT appears to hit its target.

NT 4.0 seems to promise something for everyone. For Windows 3.x users who want more reason to upgrade than just the pretty face of Win 95, NT 4.0 adds an alluring combination of stability and security. Users get a performance boost, a wide range of new and better features, and enhanced Internet connectivity.

The sweeping changes made to NT 4.0 touch nearly every service and aspect of the OS. It's easy to see signs of upgrades in the interface, management tools, Internet and networking capabilities, programming interfaces, and performance.

## Performance

We've had beta versions of the new NT in the BYTE lab for a while. However, it wasn't until Microsoft handed us the final release code -- barely in time to make this issue -- and we did some real-world testing with the actual OS that we could determine how well NT's performance matches its promotion.

The

features table

and

performance charts

summarize our findings. Except where noted, performance results are for NT 4.0 Workstation. We focused more heavily on Workstation because, to users of Windows 3.x, the target audience for the upgrade, it's unfamiliar. In contrast, those users interested in NT Server are likely already familiar with NT's capabilities from their experience with version 3.51.

We configured three mainstream systems for testing: a Gateway Pentium-133 with 64 MB of RAM, a Gateway Pentium Pro-150 with 64 MB, and a Cyrix 6x86-P200 with 32 MB. The hard disks in the Gateway systems were connected to the system boards' IDE interface. The Cyrix system used an Adaptec AHA-2940 SCSI adapter and a SCSI hard drive.

Each system was equipped with a PCI-based Matrox Millennium video adapter configured for 1024- by 768-pixel resolution with 256 colors. Matrox supplied video drivers for Win 95 and NT 3.51, and we used the Microsoft video driver that comes with NT 4.0.

To evaluate performance, we used the new SYSmark/32 1.0 benchmark for Win 95 and NT platforms. This test measures performance in six categories by executing scripts that run eight real-world applications: Adobe PageMaker 6.0, CorelDraw 6.0, Lotus Freelance 96, Lotus WordPro 96, Microsoft Excel 7.0, PowerPoint 7.0, Word 7.0, and Paradox 7.0.

The results of this first round of tests (see

"NT 4.0 SYSmark/32 Performance"

) show a clear trend: NT Workstation 4.0 outperforms both NT 3.51 and Win 95. On the Cyrix system, however, we discovered that a change made to the NT code just before final release produced some surprising results (see the sidebar "NT 4.0 Bogs Down on Cyrix 6x86" for more information).

On the Pentium system, NT 4.0 bested Win 95 in all categories, delivering an average 12 percent performance increase. NT 4.0 showed a stunning improvement of 49 percent in the graphics test and 33 percent in desktop publishing. Microsoft's decision to move the display and print drivers into the kernel (see the sidebar "Getting to the Kernel: Is NT Still Safe?") and its attention to optimization have clearly paid off.

The improvement over NT 3.51 averaged 30 percent. We attribute this seemingly high score to a 45 percent increase in word processing scores and a 40 percent increase in spreadsheet scores, results that are due to the poor performance of 3.51, which fell below that of Win 95 in those categories.

The performance differential between NT 4.0 and Win 95 is much more dramatic on the Pentium Pro system. The Pentium Pro's CPU core is optimized for 32-bit operation at the expense of 16-bit instructions, so it naturally favors NT over Win 95, which is still built around 16-bit DOS code. Improvements in the graphics architecture also contributed to the 68 percent increase in the graphics benchmark.

Again, NT 3.51's lackluster word processing and spreadsheet performance are obvious, allowing Win 95 to turn in better scores, even on the Pentium Pro. In the same tests, NT 4.0 shows increases of 40 percent and 29 percent, respectively. Increases in the other graphics-based tests range from 12 percent to 22 percent.

Windows NT Server 4.0 is also faster than NT 3.51 Server. We compared old and new Server versions of NT using a SQL server benchmark developed by NSTL (see "Powerhouse Pentium Pro Servers," September BYTE, for test details). Running Microsoft SQL Server 6.5 under both versions of NT Server on a four-processor, 200-MHz ALR Revolution Quad6, we noted a 5 percent overall performance increase under NT 4.0 Server when testing with up to 16 users. The test is CPU- and memory-intensive and doesn't measure I/O performance.

Interface and Management

Surely the most prominent change to NT 4.0 is the addition of the Win 95 user interface. Present are the familiar Start button, Taskbar, Shortcuts, Network Neighborhood, and My Computer. Also included is Windows NT Explorer, which provides a hierarchical view of each drive and folder, including network drives.

Desktop management should get easier for system administrators as well. NT's User Profiles and System Policies provide a convenient means to control access to network and desktop resources. System policies help administrators to standardize desktop configurations and enforce behavior. And you can store roaming users' profiles on an NT server so that users always receive the same desktop, regardless of their location.

Internet Operability

If Internet immersion is the name of the game, then Microsoft is playing for keeps. NT 4.0 includes Internet Explorer (IE) 2.0, Microsoft's Web browser. (Unfortunately, Microsoft released a much-improved version, IE 3.0, shortly after NT 4.0 shipped -- too late to make it onto the NT 4.0 CD-ROM.) IE supports existing Hypertext Markup Language (HTML) standards, such as tables, while also incorporating extensions for in-line sound and video, background Secure Sockets Layer (SSL) support, and support for Internet shopping applications.

On NT Server, Internet Information Server (IIS) has been upgraded to version 2.0. Features include easier setup, administration from a Web browser, and support for Systems Management Server (SMS) as well as SNMP administration tools. Microsoft claims that IIS 2.0 is 40 percent faster than the previous version.

Peer Web Services (PWS), a subset of IIS Workstation, enables any user to publish personal Web pages over a corporate intranet. PWS also offers a platform on which to develop and test Web applications. While much more modest than IIS in resource requirements, PWS provides all ISAPI extensions and filters and is integrated into the NT security model.

Networking Enhancements

NT Workstation now has an improved version of Client Services for NetWare that supports NetWare Directory Service (NDS). This enables NT users to log in to NetWare 4.x servers running NDS and access files and print resources. It's integrated into NT and offers NDS authentication, browsing and print capability, and full support for NetWare log-in scripts, property pages, and NDS passwords.

The Point-to-Point Tunneling Protocol (PPTP) is an open standard that allows you to use the Internet, or other public carriers, to provide secure connectivity between remote clients and public networks. It also provides the basis for Microsoft's Virtual Private Network (VPN) technology.

Using PPTP, remote users can dial into a local Internet provider and tunnel into their corporate network, seeing the same security and features found on their private network. From the user's perspective, the physical connection path is irrelevant; the VPN tunnel encapsulates all data in IP packets. VPN supports all the major network protocols, including TCP/IP, IPX/SPX, and NetBEUI.

The updated version of Dial-Up Networking now provides channel aggregation, the ability to combine the bandwidth of all available dial-up lines to achieve higher transfer speeds. For example, you can combine two PPP-compliant ISDN B channels or two standard modem lines to double the effective bandwidth. You can also mix ISDN lines with standard analog modem lines.

Two NT server services, Windows Internet Name Service (WINS) and Domain Name System (DNS), have been combined to provide a form of dynamic DNS. Users can enter fully qualified DNS domain names, making it easier to connect to system resources.

NT now supports the Windows Messaging Client, a universal e-mail inbox that includes drivers for Internet and Microsoft mail. Internet support includes the ability to exchange mail over any network with SMTP or Post Office Protocol 3 (POP3) services. Messaging Client includes full MAPI 1.0 support, allowing you to send, receive, organize, and store e-mail and file-system objects.

Network OLE, which is now dubbed Distributed Component Object Model (DCOM), is a step closer to reality in this release. DCOM, a system of software objects designed to be reusable and replaceable, in theory allows you to distribute processes across multiple computers by providing the object-based communications infrastructure. NT 4.0 supports DCOM by hiding the details of application pointers from both the application and the object.

New APIs

NT 4.0 now supports several new or updated APIs. For example, a set of encryption APIs lets developers create applications that work securely over nonsecure networks, such as the Internet.

For instance, Telephony API (TAPI) provides a platform for developing end-user computer telephony and communications applications. TAPI abstracts a wide array of telephone hardware and services, providing a standard programming interface. TAPI hides the actual details of a phone connection from an application in the same way that a network relieves an application from knowing the physical location of a printer.

NT 4.0 now supports the multimedia APIs introduced in Win 95. DirectDraw provides a device-independent way to access display-dependent features, such as memory, bit block transfer, and color decompression. It also enables digital video playback by taking advantage of the various types of hardware support available on video adapters, such as video stretching.

DirectInput offers joystick support and control. The DirectPlay API provides simplified access to communications protocols and on-line services for games. The DirectSound API provides direct control of audio hardware and is designed to enable 3-D audio support in games. Under NT 4.0, however, DirectSound is emulated, and calls get translated to existing Win32 API calls at run time.

Support for these multimedia APIs will enable developers to create games and other applications for NT that were previously limited to Win 95. In addition, the Compact Disk File System (CDFS) has been upgraded to support Auto-Run and CD-XA, the format for video CDs that contain MPEG movies.

Shortcomings

The Plug and Play (PnP) philosophy states that your computer, add-in hardware, and software should work together without user intervention to configure themselves and resolve any conflicts. It's a noble goal, but it's one that NT doesn't yet reach in this release.

As partial compensation, NT supports hardware profiles, allowing users to select from a list of known configurations (e.g., docked and undocked configurations for a notebook computer). Profile variables might include video resolution, network cards, and client services.

Other aspects of PnP can cause problems when you're installing NT 4.0. Interrupt-request (IRQ) and I/O-address conflicts between hardware components that Win 95 resolved, for instance, often stopped our NT installation in its tracks. Whether or not you're using PnP peripherals, make sure that you know the I/O-address and IRQ requirements for your hardware and have your jumper settings or configuration software and driver disks handy before you begin installation.

Caching disk controllers can also be a problem under NT because a reboot or a power failure could occur before the cache is flushed. Support for caching is limited to the DPT or IBM SCSI adapters for which drivers exist. However, you can use other controllers in write-through mode or with caching disabled.

http://www.microsoft.com/hwdev

It's reasonable to expect that some older, obsolete hardware won't be supported in a new OS release. However, NT 4.0 lacks support for wave-table sound on current Sound Blaster PnP sound cards. Support for the ATAPI CD-ROM interfaces on these cards is also nonexistent. Before you plunge into an upgrade, be sure to check out the latest hardware compatibility list at Microsoft's Web site (

http://www.microsoft.com/hwdev

In general, applications that attempt to access hardware directly won't work. This includes software to control sound cards, video cards, scanners, and so on. In addition, NT doesn't support virtual device drivers (VxDs), so a lot of multimedia applications, games, and memory management utilities won't work. Other applications may fail due to poor programming practices; for instance, they may refuse to install under NT instead of checking whether the required services are available.

http://www.microsoft.com/ntworkstation/95tontw.htm

Users of Win 95 might be disappointed that there is no automatic upgrade path to NT 4.0. Microsoft attributes this to differences in registry architectures between the two products and assigns partial blame to applications that store files in different places on the two systems. Installing NT 4.0 on a Win 95 system requires that you install to a new directory and then reinstall all your applications. For advice on the issues and procedures involved, check Microsoft's upgrade paper at

2http://www.microsoft.com/ntworkstation/95tontw.htm

e. For an overview of the upgrade process, along with the possible paths and pitfalls, see the figure

"Upgrade: The Roads to NT 4.0"

Windows' perennial lack of driver support continues to plague this release of NT (by comparison, Win 95 supports approximately 1000 more drivers than NT does). Categories in which NT falls short include video, audio, and PC Card subsystems. The Win32 Driver Model (WDM) is being advanced to address this problem by providing a common set of I/O services and binary-compatible device drivers for future versions of NT and 95.

Finally, if you have been running NT on a 386-based system, Microsoft has a message for you: It's time for you to stop. Performance considerations aside, NT 4.0 is now coded to require a 486 or higher processor to run on x86-based systems.

Within the limits of the NT architecture, Microsoft has done a good job of supporting hardware peripherals. NT 4.0 recognizes and configures itself automatically for a greater variety of hardware during installation than version 3.51 does. And Microsoft has provided new NT 4.0-style drivers for a wide range of printers and video systems.

There's no doubt that NT 4.0 has a slick interface, powerful features, and raw performance. The more important question is whether it will work with your hardware and software. You'll have to answer those questions yourself, mainly through trial and error. But all in all, NT 4.0's better performance and greater feature set are adequate compensation for any upgrade troubles.

## Product Information

Windows NT 4.0

Workstation.....................$319

................................$149 upgrade

Server..........................$809 five-user license

...............................$1129 10-user license

................................$409 upgrade from 3.x (for first 90 days).

@(Requires 486 (or higher), Alpha, or other supported RISC chip)

Microsoft Corp.

Redmond, WA

Phone: (206) 882-8080

Fax: (206) 936-7329

http://www.microsoft.com

Internet:

http://www.microsoft.com

Circle 1081 on Inquiry Card.

## Ratings

Technology ***

Implementation ****

Performance ****

KEY

***** Outstanding

**** Very Good

*** Good

** Fair

* Poor

## Features

Win 95 NT 4.0 NT 3.51

Minimum/recommended RAM 8/16 16/32 12/16

Typical disk space required (MB) 40 120 90

Minimum x86 processor 386 486 386

Runs on PowerPC-, Mips-, and Y Y Y

" DEC Alpha AXP-based RISC systems

9486 emulator for RISC machines N/A Y

Scalable: supports multiprocessor Y Y

configurations

Automatic upgrade path to NT 4.0 N/A Y

9Windows 95-style GUI Y Y

9Windows Explorer file browser Y Y

?Plug and Play dynamic configuration Y (Can use

< hardware

= profiles)

(Dynamic PC Card support Y

(Power management Y

9System policies to provide Y Y

centralized control over

desktop configuration

9DCOM support Y

FNTFS support Y Y

File compression VFAT NTFS NTFS

Peer-to-peer networking Y Y Y

7Peer Web Services Y

7Windows Internet Name Service Y

7Client-side NDS support Y Y

7PPTP support Y

7Multilink PPP connections with Y

channel aggregation

9Multimedia API support (DirectPlay, Y Y

DirectDraw, DirectSound,

DirectInput)

OpenGL 3-D graphics libraries Y Y Y

(Direct3D Y

7Telephony APIs Y Y

> (version 1.4) (version 2.0)

7Cryptography APIs Y

Key

Y = yes

N/A = not applicable.

## Upgrade: the Roads to 4.0

Upgrading to NT 4.0 from other versions of Windows can be a low-cost, easy job or an expensive nightmare requiring you to replace much of your hardware and software.

## NT 4.0 SYSmark/32 Performance

mailto:"rhummel@monad.net"

mailto:"editors@bix.com"

Robert L. Hummel is a computer programmer, consultant, and author. You can reach him at

rhummel@monad.net

or at

editors@bix.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## BYTE Software Lab Report

## BYTE Software Lab Report

## NT 4.0 Bogs Down on Cyrix 6x86

Dave Andrews

In testing the final-release candidate of NT Workstation 4.0, BYTE discovered a performance discrepancy when running the software on a Cyrix 6x86-based PC. While running the BAPCo SYSmark/32 suite of 32-bit Windows applications, we noticed a slowdown of 31 percent in the final version of NT 4.0 that was released to manufacturing, compared to the previous release candidate. In both cases, BYTE tested NT on the same PC, which uses the Cyrix 6x86-P200+ running at 150 MHz (

see the charts

Intel-based PCs running the same NT beta software did not exhibit such a performance decrease from one NT beta to the next. Additionally, NT 4.0 running on the same Pentium system ran the SYSmark/32 applications suite an average of 30 percent faster than NT 3.51, and 12 percent faster than Windows 95. Pentium Pros ran NT 4.0 26 percent faster than NT 3.51, and 28 percent faster than Win 95. The Cyrix 6x86, on the other hand, ran NT 4.0 16 percent slower than NT 3.51, and 24 percent slower than Win 95.

Microsoft added code to NT to change the way it runs on Cyrix-based PCs. Phil Holden, a product manager in Microsoft's Desktop & Business Systems Division, confirmed these changes were made to make NT more stable on the Cyrix platform. This may be the source of the application's performance slowdown. BYTE will have a full report next month.

## NT 4.0 SYSmark/32 Performance

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## BYTE Software Lab Report

## BYTE Software Lab Report

*Getting to the Kernel: Is NT Still Safe?

To improve NT 4.0's performance, Microsoft moved some of the OS's most critical processes closer to the unprotected code of the microprocessor. Now NT's Graphical Device Interface (GDI) -- which handles all writing to the screen -- is in the NT Executive; this gives it Ring 0 status and potential access to important system-data structures. Ring 0 is one of the Intel processors' four protection modes, in which OSes typically run trusted or performance-sensitive kernel-level processes, such as file management and keyboard input.

This move raised concern that NT would be less stable and more likely to crash. We seriously considered trying to prove or disprove the point by trying to "break" NT 4.0 with older video cards and drivers. But we quickly realized that such tests would take a lot of work to prove what we already know from analysis: NT 4.0's stability will not be substantially affected by the Ring 0 change.

The real issue is -- and always has been -- unruly or buggy device drivers. Essentially, they have always been part of the OS and have had low-level control of the CPU. Bad ones will crash NT 4.0, just as they've brought all its predecessors to their knees. Microsoft is trying to steer people away from risky behavior by telling them to use only hardware that's on a Microsoft-approved list. A product's placement on the list means that Microsoft has written and debugged its device driver.

Admittedly, this smacks of a smug solution that serves to place the onus on users while requiring them, in some cases, to buy new hardware when they upgrade to NT 4.0. But again, the same was true with previous versions of NT. We think most corporate buyers of NT are not likely to stumble blindly into hardware conflicts, especially with their mission-critical servers.

It's true that when NT's GDI wasn't in the kernel's memory space, a crash theoretically was more likely to freeze only the screen, leaving background processes intact. We haven't heard of this ever happening, however. Besides, rebooting would be inevitable, since at some point the user would need access to screen output.

Finally, some nervousness about the GDI move to the NT kernel derives from a misunderstanding about what Ring 0 status means. It does not mean that a process has carte blanche to write anywhere in memory that it pleases. Rules exist, but poorly written or malicious drivers have always been able to ignore them.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Web Project

## Web Project

## Web Surveys

@Helpful techniques for Web-based data collection and analysis.

Jon Udell

http://www.byte.com/art/9510/sec9/art1.htm

The BYTE Site is, among other things, a giant survey application. Each of its 6000+ archive pages presents a link to a feedback form. Or rather, as I explained last October (

*http://www.byte.com/art/9510/sec9/art1.htm

), to a script that generates a form that's customized for each article. Recently, I began harvesting this data to answer questions like "How highly do site visitors rate State of the Art articles?" and "How often do site visitors say they read BYTE magazine?" We've also run Web surveys to ask visitors about their experiences with ISDN, assessment of uninterruptible power supplies (UPSes), and OS preferences.

Along the way, I've refined the techniques and tools I use to capture, store, and analyze survey data. I hope you'll find them useful for surveys and other kinds of Web-based data collection and analysis.

The Form

I tend to bail out when confronted by a sprawling multipart Web form, and I assume you do, too. So I try to make my own forms as concise as possible -- ideally, just a single screen. The most effective space-saving device is the Hypertext Markup Language (HTML) tag. The drop-down lists that it creates ask multiple-choice questions far more compactly than arrays of radio buttons or checkboxes can. Forms built with drop-down lists render more quickly. Browsers tend to struggle when given too many discrete form elements.

While I prefer the drop-down list, two circumstances militate against its use: multiple selection and no sensible default. The tag does, of course, support multiple selection. You simply add the attribute multiple="yes." However, a multiselect drop-down list looks the same as a single-select one. No visual cues tell you that multiple selection is available or that Ctrl-click is the way to operate it. Explaining these things chews up screen space. If the number of choices is not too large, you may be better off with a self-explanatory set of checkboxes.

Without a sensible default choice, there's a similar trade-off between a drop-down list and checkboxes. A drop-down list always returns a value; a checkbox set may not. To differentiate a passive "no reply" choice from a drop-down list's active choices, you have to encode it explicitly as the default choice. You can use that item to document the drop-down list (e.g., "multiselect from below"). Still, I'm never quite comfortable with the semantic inconsistency of this approach. Again, you need to weigh the compactness of the drop-down list against the elegance of a checkbox set.

To lay out your forms, you can use an HTML editor, or you can just clone an existing form and tweak it with a text editor. I do the latter; HTML widgets are really quite simple. To simplify layout, I enclose elements between a <pre>...</pre> tag pair that specifies monospacing and hard newlines. Within this preformatted region, you can still use <strong> (bold), <em> (italic), or even Netscape <font size> tags to clarify the organization of the form.

The Database

For surveys and other data-collection applications, there's no reason to wire the form directly to a database unless you need the information available in real time. Dumping records into structured text files is a simple, low-overhead, and highly effective solution. For example, the BYTE on-line archive logs feedback as a set of files, each containing a single ASCII-delimited record. The concatenation of this set of files forms a database import file.

When I began harvesting this data, though, I ran into a few limitations. The import records weren't self-descriptive -- that is, they didn't carry field names along with values. Lacking names, an import tool must rely on an ordering of fields defined elsewhere. Many import tools allow a special first row of field names. But including such a row in each record wouldn't solve another problem -- poor handling of multiline text data.

The surveys I run usually ask both quantitative questions ("How much did your ISDN installation cost?") and qualitative ones ("What was your ISDN experience like?"). No one tool is best suited to analysis of these two very different types of data. You want a relational database or statistics package for the quantitative data and a text database (possibly a searchable HTML archive) for the qualitative data. How can you store information destined for either or both of these repositories? I've settled on a text representation of a Perl associative array:

%record = ('name1',"val1",'name2',"val2");

http://www.bio.cam.ac.uk/cgi-lib/

If you process the form data with a Perl Common Gateway Interface (CGI) script that uses cgi-lib (

!http://www.bio.cam.ac.uk/cgi-lib/

) or an equivalent library, you're given an in-memory structure of this type. Unfortunately, Perl lacks a primitive function to ASCII-ize such structures, but it's not difficult:

foreach $f (keys %record) {

s/\"/\\"/g;

print RECORD

!"'".$f."\',\"".$in{$f}."\",\n";}

As long as you take care to convert double-quote to backslash-double-quote, as shown here, this technique handles multiline text fields nicely.

If the file handle RECORD maps to the file 0001.REC, a subsequent Perl script can parse and reconstitute the %record array with the single statement

do '0001.REC';

http://www.byte.com/art/download/sqlload.pl

What's the point of all this? It's now trivial to write Perl scripts that transform collections of such files into a variety of database import formats or directly to an HTML textbase. For relational analysis, sqlload.pl (

+http://www.byte.com/art/download/sqlload.pl

) produces a SQL load file containing a bunch of INSERT INTO statements. For textual analysis, I use variants of another script that builds a simple, navigable Web archive.

The Tool

Tools that marry Web forms to databases tend to assume, reasonably enough, that you're acquiring data directly into a database. They typically use templatized HTML forms containing triggers that read or write database fields. For a survey, however, it's convenient to separate data collection from database import -- particularly when you're building both relational and textual databases from a common data set. Thus, there's no reason to use a template-oriented tool such as Cold Fusion or the Microsoft Internet Information Server (IIS) Internet Database Connector (IDC).

http://www.byte.com/art/download/form2db.pl

What's more, I've found that these products don't simplify database bookkeeping to the degree I'd like. They assume that you'll build both an HTML template and a corresponding database schema. You end up with two sets of field names that you have to maintain in sync. It's not a big deal, but life's short and I'm lazy, so I wrote form2db.pl (

+http://www.byte.com/art/download/form2db.pl

) to generate a database schema automatically from an HTML form. This Perl script relies on the fact that browsers will quite happily ignore user-defined HTML attributes. For example, browsers render the input text box described by the following code:

<input type="text" name="email" dbtype="char (50)">

which is the same as

<input type="text" name="email">

The dbtype attribute, which I simply invented, means nothing to browsers. However, when I write forms using this attribute, they can double as database schemata. Form2db.pl parses these enhance forms and emits a SQL CREATE statement. Do you have to abandon your HTML editor if you go this route? Not if it's a smart one that knows how to preserve user-defined HTML. Adobe, for example, says PageMill 2.0 will do this.

There's still more mileage to be gotten out of form2db.pl. I've said that I store each record initially as an ASCII-ized Perl associative array. That implies a CGI script, wired to the form, that writes the ASCII file. It's a simple CGI script -- so simple, in fact, that form2db.pl can create it automatically. When I wrote the form for our OS survey, for example, I pretended that the script os.pl already existed:

<form action="os.pl">

When form2db.pl reads this form, it makes the imaginary script real. The single occurrence of the name os in the form tag drives several related processes. It becomes the name of the table created by form2db.pl's SQL CREATE output, the name of the file containing that output, and the name of the subdirectory in which os.pl deposits records. The figure

"One Form, Many Uses"

summarizes these interactions.

The Analysis

ftp://ftp.digex.net/pub/access/psii/iodbc.zip

In July's ToolWatch, I mentioned iodbc (

-ftp://ftp.digex.net/pub/access/psii/iodbc.zip

), a command-line interface to the Open Database Connectivity (ODBC) subsystem on Windows 95 and NT. It's the thinnest-imaginable ODBC wrapper, and therein lies its strength. To load the OS survey data into a database, I used ODBC Administrator to create a new data source called OS. (The driver was MS Jet 3.0 and the format was .mdb, but I could have used any database supported by ODBC.) I then issued one command to execute the SQL CREATE code written by form2db.pl:

iodbc -S OS < os.sql

and another to execute the SQL INSERT INTO code written by sqlload.pl:

iodbc -S OS < os.lod

Then I launched iodbc in interactive mode to begin exploring the data set:

iodbc -S os

1> select count(*) from os

This approach makes me a knuckle-scraping Neanderthal or an avant-garde minimalist, depending on your perspective. I see it the latter way, because I find that operating a full-blown wizard-equipped GUI database can take more time and effort than just typing the small bits of SQL you need. What's more, as you write those SQL statements, you discover patterns -- that is, opportunities to parameterize and automate SQL queries.

Perl coupled with iodbc is one way to exploit those opportunities, but it's awkward. Perl has to write SQL statements to a file, invoke iodbc on that file, and then parse iodbc's output. A better solution is odbc.pm, a

Perl 5 module

that makes ODBC SqlExecute and SqlFetch calls directly available to Perl programs. This has two major advantages: The SQL code doesn't have to take a trip through the file system, and its output comes back neatly chunked by row and column.

http://www.bunyip.com/

These two methods are complementary. I use iodbc when first exploring a data set and odbc.pm to codify the repeatable patterns that emerge from that exploration. Today, all this happens on my NT systems only because, while ODBC itself is available for Unix, iodbc and odbc.pm are not yet available. But the Perl scripts I'm distributing with this article will work fine on Unix, as will the generic SQL code they produce. If you're in need of a lightweight Unix SQL engine to use in conjunction with these, try msql (

http://www.bunyip.com/

The Methodology

What did our OS survey reveal? Nothing of value, I'm afraid. I got so absorbed in the mechanics of Web-based data collection and analysis that I ignored the most fundamental survey precept. BYTE senior editor Tom R. Halfhill puts it succinctly: "You can't let the studied population select itself." Team OS/2, an international band of OS/2 enthusiasts, drove that point home with a vengeance.

Two days into the survey, analysis showed that usage of the Mac OS, OS/2, Unix, and various Windows flavors -- on desktops and servers -- was comparable to what many other sources have reported. A few days later, Team OS/2 struck, and OS/2's numbers soared. An Alta Vista search of the Usenet uncovered one cause of the surge -- a posting to comp.os.os2.advocacy, which contained the uniform resource locator (URL) of the survey page.

We reported the results in last month's Bits section on page 32. However, please don't quote the three pie charts, which show OS/2's dominance, without also quoting the portion of text showing that an OS survey response was 12 times more likely to come from the Internet domains ibm.com and ibm.net than was a typical BYTE Site visit.

We'll continue to run surveys on The BYTE Site. The anecdotal information we've gathered, for example from the ISDN survey, seems valuable as an indicator of trends and opinions. Quantitative data may have some limited value as well, on subjects charged with less religious fervor. However, we won't put much stock in the numbers until we can invite true random samples of participants, probably from a (yet-to-be-developed) site-registration database. For that valuable lesson learned, we have Team OS/2 to thank.

## Toolwatch

ftp://ftp.cygnus.com/pub/gnu-win32/latest

gnu-win32 (free at:

)ftp://ftp.cygnus.com/pub/gnu-win32/latest

Cygnus Support

Mountain View, CA

http://www.cygnus.com

Internet:

http://www.cygnus.com

The gnu tools and libraries -- gcc, bash, grep, bison, the lot -- for NT (x86 and PowerPC).

## Booknote

2World Wide Web Database Programming for Windows NT

by Brian Jepson

John Wiley and Sons

http://www.wiley.com/compbooks/

Internet:

http://www.wiley.com/compbooks/

Price: $39.95

A great Perl-oriented tutorial for NT-based Web developers.

## Using the Perl 5 ODBC Module

use NT::ODBC; $o = new NT::ODBC("DSN=os");

c@use_cli = ('use_cli_mac','use_cli_os2','use_cli_w95', 'use_cli_nt','use_cli_unix','use_cli_w3x');

!foreach $s (@use_cli,@use_srv) {

B if ($o->sql("select $s, count(*) from $view group by $s") != 0)

{ die; };

print "\n"; &printData

sub printData {

local ($data);

7 while ($o->fetchrow) {foreach $f ($o->field names) {

@ $data = $o->data($f); print $data . "\t"; } print "\n"; } }

## One Form, Many Uses

3World Wide Web Database Programming for Windows NT

mailto:"jon_u@dev5.byte.com"

Jon Udell is BYTE's executive editor for new media. You can contact him at

jon_u@dev5.byte.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Features

## Features

## NT in Real Time

Clever modifications of Windows NT make it a compelling OS choice for some mebedded applications.

Rick Grehan

Pity the embedded-systems developer when it comes time to choose a real-time OS (RTOS). The approximately 40 RTOSes now on the market present an embarrassment of riches; each one offers slightly different capabilities and development tools. So, for a developer on a deadline, he or she may spend a lot of valuable time searching for the right tools -- time that would be better spent developing the actual program.

Life would be easier if embedded-systems developers needed only to choose among a handful of general-purpose OSes, such as Windows NT, that have been customized into embedded, real-time versions. Phar Lap Software and Venturcom are doing just this kind of customization: Both are offering real-time variations of NT. The approaches these two organizations take with their products are quite different, but both of them count on catching some of NT's wake.

NT's Coattails

The potential rewards of using Phar Lap's TNT Embedded ToolSuite, Realtime Edition, version 8.0 (ETS), and Venturcom's Real-Time Extension (RTX) are manifold. First, if you're already familiar with programming to NT's API, you don't have to go to the trouble of learning a new API to use them. All the programming knowledge that you've gained while working with NT in the desktop realm becomes applicable for real-time applications.

Second, programmers can choose from a wide range of development systems. Custom real-time OSes often require the purchase of equally custom and expensive development tools. By contrast, developers using ETS or RTX have the option of using standbys, such as Microsoft's Visual C++ and Borland C++. Along with these tried-and-true development tools come some substantial piles of documentation and various other educational materials that are often missing in some custom OSes.

Third -- and most important -- both the host-development and target systems can run the same OS. This means that a great deal of the software development work can be completed before the target hardware is even available to the software engineers. (Venturcom's RTX runs on any Intel hardware that supports NT. Phar Lap's ETS supports standard AT architectures, starting with the 386SX.)

The Challenge

Embedded-systems developers have a short list of "must have" features for any RTOS, whether it's a custom design or one built from a general-purpose OS. For example, a multithreaded RTOS with a moderately sophisticated memory management system must be able to safeguard against the memory-manager thread's waking up and preempting a time-critical interrupt service routine. (The memory-manager thread operates at a high priority to maintain system consistency.)

Such safeguards are critical to providing determinism. An RTOS is said to be deterministic if a designer is able to figure out precisely how the system will behave given any set of inputs and the current state of the system at the time the inputs arrive. Most of the time, this boils down to a known and guaranteed task-scheduling protocol.

Because embedded applications usually offer limited memory resources, another important characteristic of an RTOS is the ability to tolerate small living quarters. Some embedded systems must endure size and power restrictions; both translate directly to limits on the amount of silicon a developer can throw at the application. If the real-time system won't fit, no amount of shoehorning will fix the problem. Finally, an RTOS must provide adequate development tools.

Both ETS and RTX need to solve these problems and work compatibly with NT, even though NT doesn't natively provide the deterministic task-scheduling necessary for RTOSes. In addition, NT typically runs with applications that offer 32 to 64 MB of memory -- which is hardly a small footprint. While development tools for NT are common, developers using the Phar Lap and Venturcom products need to use those tools in a specialized way.

Inside ETS

Phar Lap's ETS owes a great deal of its heritage to the company's venerable TNT DOS Extender. TNT brings a subset of the Win32 API into a DOS extender to provide developers with access to NT-style multithreading and all the NT-synchronization objects (e.g., events, critical sections, mutexes, and semaphores). Most important, however, is the fact that TNT is a 32-bit flat-memory-model environment. It's about as close to NT without the Windows as you can get. To produce ETS, Phar Lap took the basic TNT technology and added a context-switching and memory-managing heart to produce a stand-alone kernel.

Note that ETS is a single-process, multithreaded environment. It's important to remember that ETS is not true NT; it's based on a subset of the Win32 API. The context-switching component provides determinism via the following easy-to-remember principle: The highest-priority runnable thread will run. This means that a thread will run until it becomes blocked (e.g., while waiting for completion of an I/O operation) or its time slice expires and a thread of equal or higher priority is ready to run.

By contrast, task scheduling in Windows NT is not deterministic. Because ETS is basically a real-time kernel rather than a full-blown OS with its own development tools and supporting applications, it's aimed primarily at the embedded developer working in C and C++. Fortunately, ETS allows a development tool to be selected from among several of the standard NT C/C++ compilers. ETS applications can be constructed using Microsoft's Visual C++, Borland C++, or MetaWare High C/C++.

Well-Timed Interrupts

To understand Venturcom's RTX, you must first understand how NT's hardware abstraction layer (HAL) handles system timing. The HAL intercepts timer interrupts produced by a system's hardware clock. NT's designers programmed these interrupts to occur once per millisecond; the HAL essentially passes the interrupts "up" to the NT kernel. This once-per-millisecond interrupt, which forms the smallest resolution of the NT system, is used to manage device drivers that request timer services.

Every 10 ms, the NT kernel nudges the NT scheduler, which performs whatever process and thread scheduling needs to be done. Hence, 10 ms represents NT's fundamental process/thread time slice. RTX's real-time extensions depend on a cleverly modified HAL that programs the hardware so that interrupts occur once every 100 microseconds.

This modified HAL delivers interrupt notification in two directions. First, the new HAL continues to inform the NT kernel of interrupts once every 10 ms. In this respect, the NT kernel is unaware that the HAL is acting in a different manner. The second notification sequence, however, sends an interrupt every 100 ms to Venturcom's RTX. RTX is a sort of real-time kernel that appears to the remainder of NT as a device driver, so it's simultaneously a part of and separate from NT. Tasks running in RTX run at priorities higher than those of NT interrupt handlers. Consequently, RTX tasks cannot be preempted by NT tasks.

Thus, NT's normal functions run unimpaired so that real-time software can execute on an NT system side-by-side with standard, off-the-shelf software. Also, because tasks in the real-time extension execute at a higher priority than NT processes and threads, NT tasks won't destroy the determinism of the real-time extension. Finally, developers can use RTX for SMP (symmetric multiprocessing). On a dual-processor system, one processor can run the real-time extension, and the other one can run NT with no degradation in performance.

Build Your Own Kernel

Both ETS and RTX address the resource limitations of embedded systems via associated products that let you custom-construct a kernel. Phar Lap's Visual System Builder, which comes bundled with ETS, lets you identify

what pieces

you want in your kernel (e.g., keyboard driver or timer driver). Operating Visual System Builder is straightforward: You simply click on check boxes that correspond to the desired components, and the Builder automatically assembles the proper modules. When you compile and link your application's executable image, ETS pulls in the selected modules.

RTX's optional Component Integrator is more elaborate because it helps you assemble a

customized version

of a full-blown NT system. The modules that the Component Integrator must cope with are more complex than keyboard drivers and serial drivers, and these modules are also interdependent. The ultimate goal, however, is the same for both ETS and RTX. Each one allows you to construct a tuned OS core that has only the pieces your application needs.

How do the two products compare in scalability? That depends on your perspective. Developers who measure ETS by its ability to bear the burden of increasing numbers of tasks find that the product fares well. For example, Ark Degtiarov, principal software engineer for Nova Biomedical, a Boston-based biomedical instrumentation manufacturer, says that his company's blood-analyzing system runs about 40 simultaneous tasks using ETS. He adds that he has never seen a problem with system stability.

Developers might measure scalability with Venturcom's RTX by the number of NT services that are available in conjunction with RTX. Given that, the Component Integrator provides all the scalability necessary at the upper end of the spectrum; there's no reason why a full-blown NT kernel can't be run in conjunction with RTX.

For a deeply embedded application, however, there's a lower end to the spectrum. A minimum embedded NT system with RTX requires about 8 MB of memory (5 to 6 MB for NT, and the rest for the embedded application). ETS fares much better in tight spaces; depending on how the kernel is carved up, it can take as little as 27 KB of memory.

The Dark Side

Before you think that these products offer perfect solutions, consider some of their drawbacks. For starters, Venturcom's RTX is in an early incarnation and currently supports only soft real-time. In other words, RTX's high-performance, deterministic characteristics have not yet been implemented -- and this is not expected until later this year or early 1997. (A "hard" real-time system guarantees an immediate response to a given stimulus regardless of the system state. In contrast, a "soft" real-time system can tolerate an occasional fraction-of-a-second delay. For example, microwave ovens are soft real-time systems; you wouldn't notice if the oven responded in 2/10 second, rather than 1/10 second, after you pressed the Start button.) In defense of the product, the company claims soft real-time satisfies 95 percent of the real-time marketplace.

Then there's the aforementioned RTX footprint of about 8 MB. On one hand, this excessive memory requirement exists because RTX runs full-blown NT, not some subset of the Win32 API. On the other hand, this is likely to eliminate RTX from consideration for many deeply embedded applications.

Phar Lap's ETS tackles the real-time embedded market at a lower level than RTS does. This means you'll need to program in C or C++ if you choose to work with it. This isn't completely a fault of ETS; it's intrinsic to hard real-time development. However, this means that the ETS environment is more primitive than what RTX offers. With ETS, you can't currently run an off-the-shelf database package alongside your real-time data-acquisition system.

Note that this primitiveness does not imply higher performance on the part of ETS. (It's often the case that the lower an application's level, the higher its raw performance.) On the contrary, one complaint about ETS is its poor latency (i.e., the time it takes the system to respond to an interrupt). Additionally, the minimum time slice for threads running under ETS is 10 ms (the same as for a "regular" NT thread). Compare that to RTX, which can schedule real-time threads in 100-ms time slices.

The Choices

These two products take fundamental-ly different approaches to handling NT. Therefore, you shouldn't have much trouble distinguishing when it's best to use one rather than the other.

Venturcom's RTX and Component Integrator target the high end of the embedded marketplace. These tools benefit applications that incorporate a mixture of real-time and desktop software.

Imagine, for example, a system that controls a complex manufacturing process and perhaps runs a factory's automated assembly line. The shop-floor manager -- who's already familiar with the NT interface on the desktop in the office -- can go to the shop floor and use the same graphical interface to reprogram the assembly line. If this reprogramming task requires that a set of device-control parameters be called up from a database, this could be done with an Access database that communicates directly with the real-time extension tasks that control the devices on the assembly line.

Meanwhile, Phar Lap's ETS works efficiently with deeply embedded applications where resources (available memory, for example) are scarce. Small, application-specific devices that don't require graphical interfaces or a great deal of mass storage are perfect candidates for ETS applications.

In addition, both of these products face some stiff competition from Unix-based RTOSes, such as QNX and Lynx. Still, NT is one big rolling snowball. And although NT is just now entering the embedded world, developers may feel safer working behind the snowball rather than in front of it.

## Where To Find

Phar Lap Software, Inc.

Cambridge, MA

Phone: (617) 661-1510

Fax: (617) 876-2972

E-Mail: info@pharlap.com

Venturcom, Inc.

Cambridge, MA

+Phone: (800) 334-8649 or (617) 661-1230

Fax: (617) 577-1607

http://www.vci.com

Internet:

http://www.vci.com

## Inside Phar Lap's Real-Time Kernel

The ETS kernel lets you add or delete services and hardware device drivers to match the needs of each application.

## A Custom HAL

PRTX relies on a customized HAL that lets NT operate in real-time applications.

mailto:"rick_g@bix.com"

Rick Grehan is a BYTE senior technical editor who frequently writes articles about embedded-systems programming. You can reach him at

rick_g@bix.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Features

## Features

Ds for the Gigabyte Era

Next-generation optical disks, due this year, offer capacities that are 25 times higher than a CD-ROM's.

Tom R. Halfhill

DVD is Goliath. Variously defined as digital versatile disc, digital videodisc, or simply a generic trade name, DVD is the next-generation optical disk standard that will bring gigabytes to your desktop. DVDs are the same physical size as today's CDs, but in terms of storage capacity, they're giants: 4.7 to 17 GB per disc, depending on the format. These sizes are up to 25 times the maximum capacity of conventional CDs, whose 682-MB size seemed unimaginably vast only a few years ago.

Like the biblical Goliath, however, DVD has some vulnerabilities. Last summer, unresolved differences over standards and copyright-protection issues were delaying its launch. It was supposed to make a big splash this fall, but don't expect to see significant numbers of drives or discs until next year. That means DVD will compete with the new CD Erasable (CD-E) format, which will also debut in 1997. Many users will prefer a rewritable CD drive to a read-only DVD drive. DVD-RAM is still a few years away.

Still, the insatiable demand of computer users for gigabyte-size storage media will eventually win out. The long-term success of DVD-ROM, DVD Recordable (DVD-R), and DVD-RAM seems virtually guaranteed.

Never Enough

The extra space won't go to waste. Multimedia software eats megabytes for breakfast, and growing numbers of companies are distributing documents, databases, and software on CD-ROMs. A higher-density disc will let them consolidate multivolume sets of CD-ROMs on a single DVD-ROM. Moreover, DVD is fast: The first DVD-ROM drives (which should sell for about $500-$600) will be roughly equivalent to a 9X CD-ROM drive, and DVD's greater capacity reduces the need to swap discs.

For example, the popular PhoneDisc PowerFinder USA from Digital Directory Assistance requires six CD-ROMs to store 112 million phone listings. Even with a CD-ROM changer, disc-swapping is slow. In June, the company demonstrated its new DVD version. The entire 3.7-GB database, with the same number of listings, fits on a single DVD-ROM, with room to spare.

Entertainment software will get a boost, too. Multimedia developers are running out of space on CD-ROMs for their increasingly realistic graphics, video clips, and stereo soundtracks. Games such as Sierra's Phantasmagoria -- which fills seven CD-ROMs -- could easily fit on one DVD-ROM.

DVD isn't just for computers. Hollywood movie studios want to replace VHS videocassettes with DVD video in the rental and retail markets. The discs are much cheaper to manufacture than VHS tapes (about 80 cents compared to $2.20), occupy less shelf space, never need rewinding, deliver higher-quality video, and can accommodate multiple-language soundtracks and subtitles.

The music industry is also expressing some interest in the evolving DVD standard. More data means higher sampling rates and longer playing times, so DVDs could surpass the fidelity and convenience of regular CDs.

To ensure the success of this new medium, the computer and entertainment industries are hammering out a worldwide standard. DVDs won't work with existing equipment, of course, but new DVD-ROM drives will read several variations of the DVD format. Optionally, the DVD drives will be designed to also support some future formats that are still evolving, such as write-once DVD-R and rewritable DVD-RAM.

Even though the DVD standard does not mandate backward compatibility, it's highly likely that DVD-ROM drives will read existing CD-ROM and CD Recordable (CD-R) discs. Likewise, the DVD video and audio players sold to consumers will almost certainly play audio CDs and maybe other CD-based formats, such as CD Interactive (CD-I) and CD Video. There's even talk about a hybrid disc that stores data at CD and DVD densities in separate layers on a single platter.

Despite its storage capacity and the array of format choices, DVD faces some serious challenges in the consumer market. For DVD video to catch on, the studios must release enough movies in this format to make the players a worthwhile purchase. Also, it may possibly be several years before recordable DVD video decks appear. They will need real-time MPEG-2 compression to fit 2 hours of video on a disc, and implementing real-time MPEG-2 currently costs tens of thousands of dollars.

Even if you care about DVD only to store corporate data or distribute sales presentations, what happens in the consumer market is quite important. DVD-ROM prices will remain high if there is no consumer market to drive down the manufacturing costs.

The Many Sides of DVD

The most amazing (and confusing) thing about DVD is its plethora of physical formats. There are more than a dozen possible variations, though only a few will likely be popular (see the table

"DVD Physical Formats"

s). Fortunately, most DVD drives will automatically recognize all formats, so DVDs should be as easy to use as CDs.

The

multitude of formats

is a radical departure from the CD standard. CDs always store data at the same density on a single-sided disc. The capacity varies only by how closely the outward-bound spiral data track approaches the disc's outer rim. Most CD-ROMs settle for a conservative 553 MB. Some discs stretch it to 682 MB by living close to the edge. It's risky because the outer region of a disc is more susceptible to defects, and some drives have trouble reading the longer track.

DVD achieves its greater capacity in four ways. The first two methods take advantage of improved manufacturing techniques and shorter-wavelength lasers. CDs and DVDs store data in the form of microscopic pits that represent binary ones and zeros. On a CD, the minimum length of a pit is 0.834 micron; on a DVD, it's reduced to 0.4 micron. This lets the disc-mastering machinery squeeze the pits more closely together.

In addition, the data track that spirals outward from the center of the disc is spaced only 0.74 micron apart on a DVD; the track pitch on a CD is 1.6 microns. To read these smaller pits and tighter tracks, DVD drives use a red laser at a wavelength of 635 to 650 nanometers; CD-ROM drives use an infrared laser at 780 nanometers. The red-laser diodes in DVD drives are identical to those in bar code readers (see the table

"Comparing CD-ROM and DVD-ROM"

Reducing both the pit size and the track pitch increases the disc's capacity about sevenfold: 4.7 GB for DVD compared to 682 MB for CD. Mindful of the unquenchable demand for mass storage, however, DVD designers (Philips, Sony, Toshiba, and Matsushita deserve most of the credit) adopted two additional strategies: dual layers and double sides. Each enhancement is optional.

Dual layering is the most impressive technology. All CDs and DVDs have a layer of reflective material (which is usually aluminum) immediately behind the pitted polycarbonate substrate. The reflective layer bounces the laser back to the photodetector. Dual-layer DVDs have a semireflective layer on top of the fully reflective layer, and the lasers in DVD drives can read each layer separately.

This technique almost, but not quite, doubles the capacity of a disc. The lower reflectivity of the second data layer limits it to about 3.8 GB, compared to 4.7 GB in the fully reflective layer. That's why dual layering yields 8.5 GB per side instead of 9.4 GB.

If that's not enough for you, DVDs can also store data on both sides. Double-sided discs have two polycarbonate substrates bonded back-to-back, and each substrate may contain one or two layers of data. It's even possible to bond a single-layer substrate with a dual-layer substrate. Therefore, the total capacity of a double-sided DVD-ROM can range from 9.4 to 17 GB.

Double-sided DVDs have some drawbacks, however. Ordinary disc labels are opaque to lasers, so double-sided discs require a special holographic label that's difficult to see in dim light. Also, double-sided DVDs are more vulnerable to surface damage, because both sides contain data and the substrates are thinner.

Wait, There's More

The options for single- or double-sided discs and single- or dual-layer sides raise the possibility of at least five physical formats -- but DVD doesn't stop there. Another variation is DVD-R, expected to debut late next year. This is a write-once format similar to CD-R that replaces the read-only polycarbonate data layer with an organic dye. DVD-R drives can record data by burning spots in the dye. However, due to the limitations of this material, single-layer DVD-R discs will have somewhat less capacity than single-layer DVD-ROMs (about 4 GB compared to 4.7 GB). Also, this material is not as suitable for making dual-layer discs.

DVD-RAM, expected to debut in 1998, encodes the data on a rewritable phase-change material. It will have even less capacity than DVD-R, probably topping out at 2.6 GB per side. According to Arjen Bouwman, DVD marketing director at Philips, DVD-RAM shows more promise for dual layering than DVD-R, but the first DVD-RAMs will almost certainly be single-layered.

The DVD standard also provides for discs that are 80 mm in diameter instead of 120 mm. Although they have about 70 percent less capacity, the smaller discs may find a home in mobile devices. Like their 120-mm cousins, they can be single- or dual-layered, single- or double-sided, and recordable or rewritable.

Just to keep things interesting, the industry is also talking about DVD drives that could read discs at a constant angular velocity (CAV) as well as a constant linear velocity (CLV). Currently, the CD and DVD standards use CLV to maintain a constant bit rate; rpm gradually increase as the drive reads the inner (shorter) tracks.

In a CAV drive, however, rpm would remain constant, no matter which part of the disc the laser is reading. Throughput would decrease when reading sequential data from the inner tracks, but the trade-off would be faster access times, because the drive wouldn't have to speed up or slow down when it's switching tracks. CAV drives would be better for applications that rely on random access, such as databases.

Yet another possible format is the hybrid CD/DVD. This disc would overlay a semireflective DVD layer on top of the fully reflective CD layer. The shallower DVD layer (0.6 mm) would be effectively transparent to existing CD-ROM drives and CD audio players, whose infrared lasers would focus on the deeper-layered CD data (1.2 mm). Thus, a hybrid disc could work on both types of drives.

Hybrid drives that read both CD and DVD discs are another possibility, though they're not required by the DVD standard. To avoid the cost of two laser diodes (red and infrared), Mitsubishi has designed a mechanism that swings two different lenses into the path of the laser beam, changing its wavelength from 635 to 780 nanometers. Another clever solution, devised by Matsushita, beams the laser through an aspheric molded-glass lens that has a special holographic pattern on its surface. The holographic pattern modifies the laser's wavelength for either CD or DVD by diffracting the beam.

At this writing, it was too early for us to test DVD-ROM drives and discs for multiformat compatibility. This will obviously be an important consideration when choosing a DVD-ROM drive.

Pair Bonding

Why are there so many DVD formats? Blame the industry's long-running battle over DVD. Two alliances tried to unilaterally establish the new standard. One group, led by Sony and Philips, favored a single-sided/dual-layer disc. The other group, led by Toshiba and Time Warner, favored a double-sided disc. To avoid a format war reminiscent of the Beta-versus-VHS debacle of the 1980s, the computer industry worked with Hollywood to reach a compromise. As a result, the DVD standard inevitably bears some marks of a technology that was designed by committee.

For example, if you closely examine a single-sided DVD, you'll notice it has two polycarbonate substrates bonded back-to-back, just like a double-sided DVD. The only difference is that one substrate is a blank dummy.

This happened because the Toshiba/Time Warner alliance insisted on a double-sided option, which requires back-to-back bonding. Each substrate is 0.6 mm thick; after bonding, the total thickness is 1.2 mm. To be compatible, a single-sided DVD must also be 1.2 mm thick. However, it can't use a 1.2-mm substrate, because the laser expects to find the data at a depth of 0.6 mm. Thus, a single-sided disc must have two 0.6-mm substrates, even though only one substrate stores data.

Sony and Philips argued that bonded discs are more expensive to manufacture, and users have to manually flip over a double-sided disc to read the other side. (Conceivably, a DVD drive could have a separate laser for each side, but this would nearly double the cost and complexity of the drive. Moreover, it would make it too bulky to fit in a standard drive bay.) Toshiba and Time Warner argued that disc bonding is a mature technology (it's been done for years with 12-inch video laserdiscs) and that double-sided DVDs have more capacity. Ultimately, the latter argument won.

Fortunately, one thing that everybody involved agreed on is a standard logical format. Up to now, I've been talking about physical formats: the methods of physically storing data on the disc. The logical format is the disc's file structure. All DVDs will obey a standard that's called the Universal Disk Format (UDF), which is a subset of the ISO-13346 standard for data interchange.

With UDF, it should be easier to create a single disc that works on multiple OS platforms, including DOS, Windows, Windows NT, OS/2, the Mac OS, and Unix. When these OSes add support for UDF -- in the form of a new driver or extension -- they will be able to recognize any DVD. UDF essentially abstracts OS-specific features like filename conventions, extended file attributes, byte ordering, and Mac resource forks. Executable programs are still platform-specific, of course, but at least the data is portable.

To help bring developers up to speed on UDF, the Optical Storage Technology Association publishes a technical white paper on its Web site (see the

"Where to Find"

information).

Just in case some OSes don't immediately support UDF, some early DVD-ROMs may be "bridge discs": They will have both UDF and ISO-9660 file structures pointing to the same data. (ISO-9660 is the CD-ROM standard.) DVD video players, however, will recognize only a special subset of UDF known as Micro UDF. It's basically the same as full UDF, except the video player looks for files in one particular subdirectory. This lets developers mix video and computer data on one DVD that's playable on either a consumer video deck or a DVD-ROM drive. For example, Disney could release The Hunchback of Notre Dame and a computer game based on the movie on a single disc.

With so many possibilities, DVD deserves its nickname digital versatile disc. But its versatility could also be a vulnerability. Can the numerous companies that are pulling DVD in so many directions settle their remaining differences and produce drives that are as versatile as the discs? Achieving full compatibility with all of DVD's physical formats won't be trivial, and most users will want backward compatibility with their CDs, too. That will be the real test.

If vendors can deliver on their promises, DVD seems like a no-brainer for computer users and developers who are eager to make the transition from megabytes to gigabytes.

## Where To Find

General DVD Information

http://www.unik.no/%7Erobert/hifi/dvd/

Internet:

&http://www.unik.no/%7Erobert/hifi/dvd/

Philips DVD

http://www-us.philips.com/pkm/laseroptics/dvd/brochure/index_en.htm

Internet:

Chttp://www-us.philips.com/pkm/laseroptics/dvd/brochure/index_en.htm

Sony DVD

http://www.sel.sony.com/SEL/consumer/dvd/

Internet:

)http://www.sel.sony.com/SEL/consumer/dvd/

Toshiba DVD

http://www.toshiba.com/tacp/SD/

Internet:

http://www.toshiba.com/tacp/SD/

Universal Disk Format

'Optical Storage Technology Association

Santa Barbara, CA

http://www.osta.org/html/ostatech.html

Internet:

&http://www.osta.org/html/ostatech.html

## DVD Physical Formats

DVD format Capacity (120-mm disc) Capacity (80-mm disc)

HDVD-ROM: one side, one layer 4.7 GB 1.4 GB

HDVD-ROM: one side, two layers 8.5 GB 2.6 GB

HDVD-ROM: two sides, one layer 9.4 GB 2.9 GB

HDVD-ROM: two sides, two layers 17 GB 5.3 GB

IDVD-R: one side, one layer 3.9 GB* 1.2 GB*

IDVD-R: two sides, one layer 7.8 GB* 2.4 GB*

IDVD-RAM: one side, one layer 2.6 GB* 0.7 GB*

IDVD-RAM: two sides, one layer 5.2 GB* 1.5 GB*

:*BYTE estimate; industry standards are not yet finalized.

## Comparing CD-ROM and DVD-ROM

CD-ROM DVD-ROM

Disc diameter 120 mm (4.7 inches) 120 mm(1)

Disc thickness 1.2 mm (0.6 mm X 2) 1.2 mm

Track pitch 1.6 microns 0.74 micron

Minimum pit length 0.834 micron 0.4 micron

Laser wavelength 780-790 nanometers 635-650 nanometers

O (infrared) (red-laser diode)

Data layers One One or two

Data sides One One or two

Data capacity (per layer)(2) 682 MB 4.7 GB(3)

Data capacity (per side)(2) 682 MB 4.7 to 8.5 GB

Total data capacity(2) 682 MB 17 GB

Reference speed (1X) 1.2 meters per 3.49 meters per

M second CLV(4) second CLV(5)

Reference data rate (1X) 153.6 KBps 1.385 MBps

Key

0(1) The DVD standard includes an 80-mm version.

I(2) Read-only. Recordable and rewritable DVD formats have less capacity.

B(3) Dual-layer DVD-ROMs have a semireflective layer that has less

+ capacity than a fully reflective layer.

(4) Constant linear velocity.

D(5) Industry groups are also discussing a constant-angular-velocity

(CAV) version.

## CD-ROM vs. DVD-ROM

mailto:"thalfhill@bix.com"

Tom R. Halfhill is a BYTE senior editor based in San Mateo, California. You can reach him on the Internet at

thalfhill@bix.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Reviews

## Reviews

## Notes Opens Up to the Web

The eagerly awaited Lotus Domino serves up a goodly dose of Notes functionality to Web clients.

Steve Gillmor

Domino, a.k.a. HTTP Services for Lotus Notes, gives Notes developers a powerful jump-start in creating dynamic Web sites, and it offers unique interactive tools not yet available from other major players. Domino extends Notes' proprietary architecture onto the Web, serving Notes databases to browsers on-the-fly. It loads as a Notes 4.x server task, delivering both a traditional HTTP server and the Domino engine that interacts with the Notes document and object store.

While not eliminating the need for Notes clients, Domino does give Web browsers a great deal of Notes' functionality. Users can browse multiple views; create, edit, and delete documents; perform full-text searches; download binary files; read and send Notes mail; and post documents that trigger work-flow agents.

Installing Domino on our Windows NT server required updating the Notes Release 4.1 Public Address Book and registering Web users, adding them to a special Domino Users group. You can give group members access to databases at a variety of Notes security levels. You can also create an Anonymous entry in the Notes Access Control List to give access to unregistered users.

Domino allows Web developers to leverage Notes tools such as input validation and translation formulas, hiding and revealing information based on time-sensitive and user-identity criteria, and displaying threaded discussions that are automatically indexed for querying. The "gold" release we tested supplied several sample databases, including a registration application with several agents.

With Domino, you can detect the type of client and optimize the look of a database according to whether a Web browser or a Notes client is viewing it. Domino supports the insertion of Hypertext Markup Language (HTML) code, combining HTML and Notes data and passing it to the browser. You can use HTML pass-through code to process graphics, run Common Gateway Interface (CGI) scripts, and add URL links. Browsers don't support the same rich server connections as Notes clients, so only server-based agents can use LotusScript scripting.

Domino will evolve as Web browsers acquire more capabilities. But even in its first release, this HTTP server add-in propels Notes to the head of its class.

## Product Information

Lotus Domino

http://domino.lotus.com

Free download from

http://domino.lotus.com

(requires Notes 4.x Server)

Lotus Development Corp.

Cambridge, MA

+Phone: (800) 343-5414 or (617) 577-8500

http://www.lotus.com

Internet:

http://www.lotus.com

Circle 1049 on Inquiry Card.

## Ratings

Technology *****

Implementation ****

Performance ****

Key

***** Outstanding

**** Very Good

*** Good

** Fair

* Poor

## Now Serving Interactive HTTP

_Domino lets you customize Notes templates, databases, and forms for interactive HTTP serving.

mailto:"sgillmor@aol.com"

Steve Gillmor, of Southern Digital, Inc. (Charleston, SC), has extensive experience using and installing Notes. You can reach him at

sgillmor@aol.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Reviews

## Reviews

## Who's on Guard?

Domino creates new security exposures. Even with optional Secure Sockets Layer encryption, there's somewhat less security when accessing the Notes environment via a Web browser. With a standard Notes client, authentication requires an authorized Notes ID in addition to a password.

Domino globally exposes all Notes databases, requiring you to manually disable confidential databases from the Open Database dialog and Catalog lists. For now, Lotus suggests putting Domino databases on a separate server, using Notes replication to update and maintain communication between Internet and intranet.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Reviews

## Reviews

&X Terminal + Browser + Java = Web PC

QHDS's @workStation is a low-cost box for Web access, Java applets, and Windows.

Peter Wayner

Many people are fascinated by the concept of a "network computer" that provides a low-cost way to get on the Net, browse the Web, and run Java applets. One of the first such machines to reach the market comes from HDS, which is selling an enhanced version of its X Window terminal called the @workStation. The system offers a surprisingly versatile way to give many users access to both the Web and Windows applications for as little as $750 per seat.

HDS could jump into this new market so quickly because smart terminals that run X Window are a fixture in the Unix community. These are often diskless systems with a small amount of memory that simply display whatever the workstation tells them to. HDS took these functions and added three crucial ROM-based components: a Web browser, a Java virtual machine to run applets, and

NTRIGUE client

software from Insignia Solutions (Santa Clara, CA) that lets you fire up Windows applications remotely. The @workStation provides excellent browsing and Java applet speed because these operations run locally on an Intel i960 embedded RISC machine.

We tested the @workStation Prima, the 25-MHz model. The basic unit ($749) comes with 8 MB of RAM, no hard disk, and a 17-inch grayscale monitor. A system with a 15-inch color monitor costs $1199, while 17-inch color costs $1499. Our test unit -- with 36 MB of RAM (128 MB is tops) and a 15-inch color display -- priced out at $1899.

The browser firmware, licensed from Spyglass (Champaign, IL), loads documents directly from the Web if you let the @workStation have its own IP address (which can be statically or dynamically assigned). To use Windows applications, however, you must run them remotely on an NT server that's running NTRIGUE ($1995 for five-user license, $195 per additional user). Computation is done on the server machine, but drawing takes place on the @workStation. Sending the drawing information over the network is relatively slow, but not prohibitively so.

We hooked our test unit through its built-in 10Base-T Ethernet connection to an AST Bravo 200-MHz Pentium Pro system running NTRIGUE. Windows performance on the @workStation was respectable, but the user interface could not duplicate the snappy response of the big machine. For example, when I typed in the NT MS-DOS editor (an old 16-bit application), screen output lagged one or two characters behind. Clearly the network limits the ability for the low-end box to compare with a dedicated PC.

If you're building a network of computers for people who occasionally use Windows applications that are not graphics-heavy, then an array of @workStations could save you money. Hooking up a dozen or so terminals to a good high-end server running NT can cut the cost of hardware and dramatically reduce system upkeep because you have to upgrade only the software on the central NT server. In terms of performance, the @workStation is comparable to that of a PC when using basic applications like word processing. It falls short when running graphics applications like games. But who plays games at work anyway?

## Product Information

@workStation Prima........................$1899

7 (as tested, with 25-MHz i960 processor, 36 MB of RAM,

15-inch color display)

HDS Network Systems

King of Prussia, PA

+Phone: (800) 437-1551 or (610) 277-8300

Fax: (610) 275-5739

E-mail: info@hds.com

http://www.hds.com

Internet:

http://www.hds.com

Circle 1059 on Inquiry Card.

## Ratings

Technology ****

Implementation ****

Key

***** Outstanding

**** Very Good

*** Good

** Fair

* Poor

## Office Intrigue

The HDS @workStation uses Insignia Solutions' NTRIGUE to access Windows applications on an NT server.

mailto:"pcw@access.digex.net"

Peter Wayner is a BYTE consulting editor who lives in Baltimore. You can reach him at

pcw@access.digex.net

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Reviews

## Reviews

## Road-Show Romance

Innovative optics and integrated Adobe Player firmware make Proxima's new projector a presentation stunner.

G. Armour Van Horn

By combining Texas Instruments' Digital Light Processor (DLP) optics and Adobe Acrobat technology into its Desktop

Projector 4100Z

, Proxima has set a new standard for direct digital projection systems. The $7750 DP4100Z uses DLP optics to project bright, sharp, 24-bit, 640- by 480-pixel color images through its 1.5-to-1 zoom lens. With the optional Media Express package ($1495), you can present slides in

Acrobat .PDF

+ file format without an attached computer.

After carrying the unit through several airports on a speaking engagement, I have only one complaint: its 27-pound weight. That said, the projector's brightness (350 ANSI lumens), clarity, and flexibility impressed fellow speakers.

The DP4100Z's DLP display engine uses an active semiconductor reflective surface that modulates red, green, and blue images in turn as a tricolor filter rotates through the illumination source (see "Micromirrors Project Better Images," July BYTE). The filter absorbs less light than polarizers, so the image is brighter than images from LCD-based projectors. Because the same addressable matrix forms the three component images, there is no color misregistration.

The DP4100Z accepts 24-bit video from two computers, has RCA jacks and S-Video inputs for two video sources, and accepts stereo sound from all four. Other connections include a microphone jack, a serial-mouse connector, and outputs for VGA and stereo sound. Its 3-W stereo speakers face backward.

The Media Express option includes Acrobat Exchange PDF editing software (five-user Windows and Mac licenses; Unix is optional), an internal floppy drive to hold PDF presentations, and a plug-in cartridge with a Motorola 68EC040 processor and Acrobat Player firmware to present the slides. Exchange lets you rotate images (a crucial feature), establish transitions between slides (e.g., wipes, window blinds, zooms, and dissolves), crop, set display intervals, and combine different presentations. The cartridge firmware includes limited Exchange capabilities: deleting and sorting slides, adding some transitions, and setting intervals.

The optional Optimizer plug-in compresses PDF presentations. You can fit 1000 slides on a floppy disk. An optional 540-MB hard drive increases capacity.

Equipped with Media Express, the DP4100Z is both a sophisticated presentation system and an "appliance" that requires only the remote control to advance from slide to slide -- you can leave your notebook home. Either way, the DLP optical system is superb.

## Product Information

Desktop Projector 4100Z............................$9745

2(with Media Express option and 540-MB hard drive)

Proxima Corp.

San Diego, CA

+Phone: (800) 447-7692 or (619) 457-5500

Fax: (619) 457-9647

http://www.prxm.com

Internet:

http://www.prxm.com

Circle 976 on Inquiry Card.

## Ratings

Technology *****

Implementation ****

Key

***** Outstanding

**** Very Good

*** Good

** Fair

* Poor

## Many Routes to PDF

## Acrobat Turns Options Around

Adobe Acrobat technology turns the DP4100Z into a presentation appliance. DLP optics provide big, bright, razor-sharp images.

mailto:"vanhorn@bix.com"

rG. Armour Van Horn is a production artist and consultant in electronic imaging and prepress. You can reach him at

vanhorn@bix.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Reviews

## Reviews

## Alpha Learns to Do Windows

Digital's FX!32 is the key to running Win32 software on Alpha/Windows NT.

Selinda Chiquoine

Executing code written for one CPU on another has always been like the talking dog: Though she didn't speak very well, the wonder was that she could do it at all. A new application from Digital Semiconductor has changed the way we think about emulators and what they can do. FX!32 lets you run 32-bit x86 Windows programs on Alpha/NT systems at surprising speeds. Depending on the applications and how they are used, they might run faster on an Alpha system than on a high-end Intel machine, though never as fast as native Alpha programs. In our tests,

FX!32 1.0

b achieved about 40 percent to 50 percent of the performance of the same code compiled for Alpha.

BYTE editors gave FX!32 the Best Technology award at Comdex last fall because it breaks the emulator mold. It looks at the instructions you're using and translates some of them into native Alpha code, saving the result in a separate DLL. It intercepts system calls and directs them to a native Alpha library. FX!32 thus combines both translation and interpretation, saving execution profiles and analyzing them heuristically (see "An Alpha in PC Clothing," February BYTE).

I tested FX!32 on a 466-MHz Alpha system with 128 MB of RAM running a beta version of Windows NT 4.0. The BYTEmark test results are summarized

in the chart

. The FX!32 translations ran at 47 percent (integer) and 32 percent (floating point) of native speeds. Straight emulation clocked at 2 percent to 3 percent.

I also ran scripts using Microsoft Visual Test 4.0, Word 7.0a, Excel 7.0a, Bentley Systems' MicroStation 95, and Maple V release 4. Because FX!32 translates only those parts of an application that you execute, scripts and users that use different commands and system calls will produce different results. Most applications will have a relatively slow first run and increasingly fast second or third run. After that, performance gains taper off.

You can set a maximum disk space allotment for translations, delay optimization, optimize now, delete translated code, or set optimization profile sizes. FX!32 itself takes up 10 MB. Its translations are between one and two times the size of the original code.

The real value of FX!32 is that Alpha users no longer need an Intel system to use Win32 applications. For 16-bit Windows applications, however, you'll need Insignia Solutions' SoftWindows, a traditional (slow) emulator.

Digital will offer FX!32 free to Alpha customers and bundle it with all Alpha systems. FX!32 should end Alpha critics' cries of, "Where's the software?"

## Product Information

FX!32 1.0............................free

(requires Windows NT 4.0)

Digital Semiconductor

Hudson, MA

;Phone: (508) 628-4724 ext. 32 or (800) 332-2717 ext. 32

Fax: (508) 626-0547

http://www.digital.com/info/semiconductor

Internet:

)http://www.digital.com/info/semiconductor

Circle 1050 on Inquiry Card.

## Ratings

Technology *****

Implementation ****

Key

***** Outstanding

**** Very Good

*** Good

** Fair

* Poor

## FX!32 Performance

## FX!32 Reports for Duty

^The FX!32 Manager reports the status of Win32 applications and background code optimization.

mailto:"selinda@bix.com"

Selinda Chiquoine is a former BYTE technical editor. You can reach her at

selinda@bix.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Reviews

## Reviews

## Net Saviors

]Replica and ArcServe take vastly different approaches to meet the network-backup challenge.

Steven J. Vaughn-Nichols

Somewhere in the fog of your memory, along with 1980s rock bands and single-server networks, you probably remember when you could back up a network onto 250-MB quarter-inch-cartridge (QIC) tapes. Perhaps you even recall the days when you could bring down your NetWare or Windows NT network during the middle of the night for backup.

Today, if your storage media can't handle at least a gigabyte per tape, you're wasting time swapping out tapes. As for bringing down the network for back-up, fat chance. In today's office, workers are just as likely to be running applications from Hong Kong hotel rooms at 2:00 a.m. local time as they are during business hours. A good enterprise network never goes down.

As you can see, backup is different today, and it needs different software. Heterogeneous networks are the norm, and intranets are taking over the LAN world. With a large LAN , you may very likely have several different servers providing backup services with just as many backup media devices. Thus, you need backup software that can not only speak different computer dialects but also cope with different tape formats. Last, but far from least, the software must be able to catalog and track them all in a centralized database. If you have a NetWare-based LAN , you need client agents -- small programs that enable "foreign" systems (running anything from the Mac OS to Unix to Windows 95) to hook up with the backup program.

BYTE has tested a couple of products that satisfy these massive requirements: Cheyenne Software's ArcServe 6.0 and Stac Electronics' Replica 2.1. Both programs are primarily NetWare oriented; however, each is also available in an NT-server version.

These two programs take vastly different approaches to network backup. ArcServe, honed by years of experience, employs a standard file-by-file backup and recovery system, while relative newcomer Replica mirrors entire NetWare volumes. Besides this major difference, there are a number of other small dissimilarities between the programs. Each approach has its advantages for particular situations.

Although ArcServe has been around in some form for nearly as long as NetWare, version 6.0 isn't your father's ArcServe. This new version comes with a host of new features, the most important being what Cheyenne calls Push Agents.

Unlike agents that supply you with data from non-Novell sources, ArcServe's Push Agents manage multiple

system-file access

. These agents allow multiple data streams, so ArcServe can back up data from multiple servers across the network simultaneously. This, in turn, produces faster throughput. In short, ArcServe works as an honest-to-goodness multitasking, multiprocessing backup system; it's not like the old-fashioned, one-job-at-a-time, batch routine that we all know and hate.

You may wonder whether the existence of multiple Push Agents makes much of a difference when they're all writing to the same storage device. Indeed it does, because ArcServe uses another technique, called media pooling, to maximize backup speeds by writing to multiple backup devices at once. The result is the fastest file-to-tape backups we've ever seen.

ArcServe has even more tricks up its sleeve. It can use multiple backup devices as RAID Level 5 devices, so even if you lose one tape out of a backup set, you won't lose any data. RAID 5 takes up more tape space, but it ensures that not one byte of data is lost without ArcServe's noticing it and making the appropriate on-the-fly repairs. The RAID 5 implementation, a technology that is mainly used with secure servers, raises this program far above the common herd of file-by-file backup programs. If you want utmost reliability, then choose this option.

Replica, on the other hand, roars by ArcServe when it comes to backing up and restoring an entire NetWare volume or directory tree. By mirroring only the data in active file systems, and not simply

replicating a disk image

sector by sector, Replica leaves older image-backup technology eating its dust. System administrators get a faster system-mirroring solution that needs far fewer tapes.

How fast is Replica? On our 120-MHz Pentium Windows NT server with a Travan TR-4 tape drive, we saw 5 GB per hour go whipping by like mile markers on the highway at 80 mph. And that was with a Travan drive, which doesn't come close to the raw throughput of a digital audiotape (DAT) or 8-mm tape drive.

Interestingly, although Replica works best at the volume/directory-tree level, it can also copy non-volume-specific information, such as an MS-DOS partition, without a hitch. At a time when you need a scorecard to keep track of which machines are using which file systems, it's a true pleasure to have a backup system that doesn't care whether the file system being used is file allocation table (FAT), High Performance File System (HPFS), NT File System (NTFS), or whatever. Replica instantly recognizes the format.

Stac's Object Replication Technology (ORT) also adds flexibility, enabling you to store entire file systems on other servers, tape drives, or even completely different types of storage devices, such as magneto-optical (MO) drives. Better still, Replica can recognize most available storage options, and it automatically presents them to you as possibilities; you don't have to fiddle with configuration files to ensure the program knows about the MO drive here or the 8-mm library over there.

Restoring files is almost fun with Replica. With NetWare, for instance, you use the program to see the backup media as a volume, assign it a drive letter, and use the usual file-copy and move commands.

When you combine this feature with Replica's imaging capacity, you can even perform such miracles as restoring a dead NetWare server with just two disaster-recovery floppies and a copy of your backup media. This is distinctly reminiscent of Unix, where you can run the OS straight off the tape if you're desperate.

Which One Is Best?

These programs are intended for two different audiences. If you want to clearly see the granularity of file systems -- such as when you're in desperate need of one particular file -- then ArcServe is for you. Its file-searching and restore speeds are great. And its RAID 5 option makes it potentially the safest backup system currently on the planet. Still, you pay a hefty price, both in total backup time and in the $1995 cost of the software.

If you're more likely to want to back up and restore entire systems, even from the brink of server failure, then Replica is what you want. Its major weakness is that, whether you're backing up or restoring, the program will bring other network activity to its knees. Moreover, the program is simply not in the same ballpark as ArcServe for finding and restoring individual files. Still, with its $995 price, you may be able to forgive these sins.

Thus, picking between these two products is both simple and complex; there is no clear editor's choice here. Both are great, but they do somewhat different jobs. You need to analyze your network use carefully to see what your users and your network need most. Only then can you make a reasonable choice between these very different products. But no matter which one you choose, you're going to have a first-rate backup system that should see you through to the end of the century.

## Where To Find

ArcServe 6.0.................$1995

Cheyenne Software

Roslyn Heights, NY

Phone: (800) 243-9462

http://www.cheyenne.com

Internet:

http://www.cheyenne.com

Circle 1047 on Inquiry Card.

Replica 2.1...................$995

Stac Electronics

San Diego, CA

Phone: (619) 794-4300

http://www.stac.com

Internet:

http://www.stac.com

Circle 1048 on Inquiry Card.

## Cheyenne ArcServe 6.0

## ADVANTAGES

+ Fastest file-based backups

+ Multithreaded backup agents

+ Can do RAID 5 backup

Disadvantages

- Expensive

## Ratings

Technology ***

Implementation ****

Performance ***

## Stac Replica 2.1

## ADVANTAGES

#+ Data-mirroring needs fewer tapes

3+ Great for mirroring and restoring server volumes

/+ Can copy non-DOS data, files, and partitions

Disadvantages

)- Network is crippled while program runs

3- Better at restoring images than individual files

## Ratings

Technology ****

Implementation ****

Performance ***

## ArcServe

## Replica

mailto:"sjvn@vna1.com"

Steven J. Vaughan-Nichols is a freelance writer and consultant in Lanham, Maryland. You can reach him at

sjvn@vna1.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Reviews

## Reviews

## Mirror, Mirror, on the Tape...

Still confused about what Stac's Replica does that's different from what Cheyenne's ArcServe does...or from what other backup systems do? Here's a quick guide to popular backup options.

File by file: With traditional file-by-file backup, each file is copied as a single, named entity, regardless of whether it's compressed. This approach makes finding individual files quick and easy, but creating thousands of individual files on a tape in the first place can be time consuming. An analogy can be drawn to a word processing file containing many individual words that can be found and copied without any problem.

Disk mirroring: Traditionally, mirroring software makes an exact copy of a disk, sector by sector. This is easy and fast to do on the backup end. But when it comes to restoring a file, it's almost impossible to find any individual item inside that image quickly. In terms of our word processing analogy, this is like sending a fax. Instead of having a document that's easy to search, you end up with one huge image file that's nearly impossible to search automatically. Worse, the document includes large amounts of white space that you have to transmit and navigate around to get to the words you need. Like image backup, it's easy to handle, but it's almost impossible to find anything within it quickly.

Data mirroring: What Stac does with Replica, in effect, is to combine the best elements of both approaches. Replica makes disk images that don't include the time-wasting white space of ordinary mirroring. Getting to an individual file still isn't as fast as when working with a file-by-file copy, but it's far faster than dealing with an ordinary mirror-style backup. And note, too, that when we say "data mirroring," "data" includes application code.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Reviews

## Reviews

$Enterprise Visual Basic? Almost...

Siemens Nixdorf's ComUnity aims to turn Visual Basic 4.0 into a client/server environment but falls short.

%Volker Weber and Hans-Jochen Schmitt

Although Microsoft markets the Enterprise Edition of Visual Basic 4.0 (VB 4) as an enterprise-level client/server tool, the product still lacks the high-level business-logic tools of such client/server mainstays as PowerBuilder.

Now, along comes Siemens Nixdorf, the German computer company, with a major effort to provide an overarching framework for client/server development that exploits VB 4's open programmable objects. Called ComUnity, the framework prescribes how to build distributed client/server applications. The related development environment is called the Open Technology (OT) Framework, which in its first incarnation works with VB 4. Siemens Nixdorf plans to port it to other languages, including C++. Our examination of a beta version revealed an ambitious product that nonetheless falls well short of its goals.

Members of the ComUnity

ComUnity consists of a three-layer application model that comprises a Presentation Layer, a Business Logic Layer, and a Database Layer (

see the figure

). This model, like other three-tier architectures, offers advantages in scalability, usability, maintenance, and performance compared to monolithic applications. You can distribute the layers across a network, with the Presentation Layer on users' desktop computers, the Business Logic Layer on an applications server, and the Database Layer on a database server.

To implement ComUnity's architecture in VB, Siemens Nixdorf had to employ Microsoft's standard development tools, including VB 4 itself, Microsoft Visual C++ 2.2, and OLE components. But because these tools are best suited for small-scale software projects, Siemens Nixdorf added more tools to improve support for large projects.

Inside the OT Framework

Central to OT Framework's Database Layer is a relational data dictionary that serves as a central repository where all the tables, attributes, and relations are managed. From the data dictionary, OT Framework generates Open Database Connectivity (ODBC) data sources, migrates databases, generates SQL statements for data access, and even produces simple entry forms for the user interface.

Unfortunately, even though you can manage the data dictionary with a simple data-entry and maintenance tool, OT Framework provides no graphical representation of the data-dictionary information. It does, however, import data models produced with CASE tools, such as Microtool's CASE 4.0 and IBM's Mood.

The data dictionary becomes part of the run-time environment repository that's distributed with OT Framework applications. Because the data dictionary contains information on the relationships between tables, applications can provide for relational integrity even if the underlying database has no such provisions.

The Presentation Layer, which establishes the user interface (UI), is built around VB 4. A forms generator uses the data-dictionary information to generate default VB 4.0 data-entry forms. You can customize these forms, but they also work with real data right out of the box.

OLE Automation acts as the glue between the Presentation Layer UI and the Business Layer. Perl scripts link code and single UI controls, but the program generates them automatically, so users don't have to deal directly with Perl. A cross-checker monitors the UI forms against any modifications in the data dictionary.

The forms are stored in the run-time repository, and you can use OT Framework tools to further customize the UI by working on the forms data. Users can use the Tailoring Tool (

see the screen

) to customize the UI: data-entry fields can be switched off, changed, or moved, even in the delivered version of an application. Developers who are skittish about giving users this much control over the UI can turn the tailoring tool off. Regardless of whether a site contains some highly individualized UIs, centralized program updates can merge with them seamlessly.

## Putting It All Together

the figure

indicates, the glue between the UI and the database is the Business Logic Layer. OT Framework implements this layer in VB 4 code using the new VB 4 class concept. This pseudo-object-oriented feature allows you to define reusable classes and instances, but it doesn't support inheritance or polymorphism. OT Framework comes with predefined classes for UI handling and general-purpose business applications, such as order entry.

The application framework itself is a template-based VB data dictionary called Code Wizards. Regrettably, except for a run-time debugger, there are no tools in the Business Logic Layer -- you're on your own as far as business processes are concerned. Thus, any higher-level knowledge must go from paper directly into VB code.

An Incomplete Toolkit

If you're not familiar with the VB environment, ODBC data sources, or tool-based software development environments in general, installing ComUnity can be a bit daunting. The beta version of the setup routine had some rough edges; the ODBC data sources for the data dictionary and the target applications are not added automatically. You must also add the VB Code Wizards and Form Wizards manually to the VB environment.

From a lone developer's point of view, OT Framework's major advantage is its vast library of reusable VB code for business applications software. The tool is rather loosely integrated with the VB environment. For small-scale projects, it does not go much beyond VB 4 or other add-ins and components that are on the market.

ComUnity also lacks an integrated version-control and project management tool. It relies on Microsoft Visual Source Safe, which comes bundled with the VB 4 Professional Edition, for version control. But Siemens Nixdorf says it's working to integrate Microsoft Project into a future version of ComUnity OT Framework.

Missing from this first implementation of the ComUnity architecture are integrated Upper-CASE tools, such as data modelers and object-oriented modeling tools. Sinking the whole business logic into pure VB code is asking for trouble, especially if users ask for changes in the application.

As long as you equate cross-platform development with Windows 95 and NT on Intel platforms, you'll have no problems with OT Framework. Its VB-centric approach restricts you to those platforms.

In the final analysis, ComUnity OT Framework caters to very specific needs. If you're a VB developer building large-scale business applications and are willing to learn a new application framework, give version 1.0 of ComUnity OT Framework a closer look. Everyone else should take a pass on it for now.

## Product Information

ComUnity OT Framework.......................$1000 per seat

J (quantity discount available)

Siemens Nixdorf

Information Systems, Inc.

Burlington, MA

Phone: (800) 225-1484

Circle 983 on Inquiry Card.

'Siemens Nixdorf Informationssysteme AG

Munich, Germany

Circle 984 on Inquiry Card.

## Ratings

Technology ****

Implementation ***

Key

***** Outstanding

**** Very Good

*** Good

** Fair

* Poor

## Three Tiers for ComUnity

Implementing ComUnity applications as OLE servers lets them communicate over a network.

## Tailor Your UI with ComUnity

ComUnity OT Framework's Tailoring Tool lets users modify a custom application's UI.

mailto:"100120.577@compuserve.com"

}Volker Weber and Hans-Jochen Schmitt are principals at ifos, a consulting firm in Darmstadt, Germany. They can be reached at

100120.577@compuserve.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Reviews

## Reviews

## Linking Tiers with Remote OLE

Divide et impera (divide and rule) -- splitting applications into

three parts

-- is the state of the art in client/server technology. Modern client/server applications, such as SAP's R/3, use a Presentation Layer (for realizing the user interface) and a Database Layer (for storing persistent data), which are held together by a Business Logic Layer. For performance or maintenance reasons, the different layers can be implemented on distributed systems in a network.

To a programmer, the problem is not whether to split the application, but to choose a distribution technology that allows the parts to communicate over a wide range of networks and OSes. Remote procedure calls (RPCs), Common Object Request Broker Architecture (CORBA), and IBM's Distributed System Object Model (DSOM) are possible solutions. With Visual Basic 4.0 (VB 4) Professional Edition, Microsoft has offered yet another option: Remote OLE.

Remote OLE allows OLE servers and clients to be distributed over a Windows-based network. Instead of invoking OLE server methods on a local machine, the OLE client sends OLE requests over the network to a remote OLE server. Siemens Nixdorf chose Microsoft's Remote OLE as the primary communications technology for distributed, three-tier, client/server applications. Therefore, applications built with ComUnity OT Framework are implemented as VB 4 OLE servers, and thus they can be distributed fairly easily via Remote OLE.

The only catch to this elegant Remote OLE solution is its incompatibility with non-Windows environments.

## Three Tiers for ComUnity

Implementing ComUnity applications as OLE servers lets them communicate over a network.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Reviews

## Reviews

## A C++ Tool that Cures VB Envy

Powersoft's Optima++ makes C++ client/server development a drag-and-drop dream.

Rick Grehan

In spite of all the complaints about Visual Basic (it's slow, it's only somewhat object-oriented), you have to love how easy it makes building user interfaces (UIs). Wouldn't you like to have the same building-block-style environment in a C++ package?

Powersoft's Optima++ is about as close as you'll get...for now. It is a rapid application development (RAD) system for Windows 95 and NT that incorporates the best of current Windows development systems. Look at who's contributed genetic material to its conception: Watcom, producer of one of the best C/C++ compilers for Intel platforms; Sybase, a database organization of considerable repute; and Powersoft, creator of the PowerBuilder fourth-generation language (4GL) development system. The result is a combination UI builder, client/server database construction kit, and general-purpose C/C++ compiler that will probably have Delphi and VB developers sneaking peeks over the shoulders of Optima++ users.

Cultured Drag and Drop

Optima++'s most elegant feature is without doubt its drag-and-drop programming. The designers have turned on-line help into a reference card, a kind of souped-up hierarchical help system structured in outline form. The upper-level branches of the outline consist of the object categories understood by Optima++: database objects, graphics objects, menu objects, and so forth. The leaves are the object methods.

The reference card is much more than a static help mechanism. For example, associated with any visual object (say, a button) on a form is source code for handling events that the object receives. Open a window to that source code, grab any other visual object (say, a listbox), and drag that object into the source code window. This will cause Optima++ to open the reference card, properly positioned to the methods associated with that listbox. With just a few more mouse-clicks, Optima++ will automatically write the source to invoke the selected method for you.

Components and C++

Drag-and-drop programming is only part of Optima++'s allure. Because it uses a construction-by-components paradigm, you'll find nonvisual components as well as visual ones (e.g., database query components and transaction components). Optima++ can also incorporate OLE Controls (OCXes) into its component toolbars, which means it also creates entries in the

reference card

s for each OCX. Consequently, you manipulate OCXes in the same way as the native components supplied with Optima++.

Finally, because Optima++ is, after all, a C++ development system, it wraps a number of system services in easy-to-handle classes (e.g., thread objects). Its debugger is as full-featured as any I've seen, going so far as to include a memory tracker, which can locate a number of memory-related bugs. The memory tracker's coverage ranges from simple leaks to more elaborate validity checks on objects such as strings and Graphical Device Interface (GDI) handles.

What's Ahead

At the time of this writing, only Optima++'s Developer Edition was in release. Professional and Enterprise Editions will appear soon (see the table

"Just Up the Road"

). If the upcoming editions are as well done as the Developer Edition, they could well be the stepladders that many VB developers need to begin their ascent to the otherwise frightful altitudes of C++ programming.

## Product Information

Optima++..........................$199 Developer Edition

Powersoft Corp., Concord, MA

+Phone: (800) 395-3525 or (508) 287-1500

Fax: (508) 369-4695

http://www.powersoft.com

Internet:

http://www.powersoft.com

Circle 985 on Inquiry Card.

## Just Up the Road

Soon-to-be-released editions of Optima++ will include:

) Sybase SQL Anywhere (four-user version)

Internet components

Integrated support for Java

Team programming

Native database drivers

## Ratings

Technology ****

Implementation *****

Key

***** Outstanding

**** Very Good

*** Good

** Fair

* Poor

## Optimize Client/Server Development

mailto:"rick_g@bix.com"

]Rick Grehan is senior technical editor of BYTE reviews. You can reach him on the Internet at

rick_g@bix.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Reviews

## Reviews

## Notebook Under Construction

With Compaq's Armada 4100 family, you build the notebook you need.

Dave Rowell

I love Compaq's new Armada 4100 notebooks for many reasons, but particularly for their configurability. Compaq has taken the concept behind Digital Equipment's HiNote Ultra II notebooks and run with it.

The standard 6-pound, 1.5-inch-thick configuration has an internal floppy drive, but the battery is in the sturdy handle, which can prop up the rear 10 degrees or fold up to protect the I/O ports in transit. Remove the handle and replace the modular floppy drive with a $199 battery module, and you have a 5-pound slim-line notebook. Two screws with D-ring loops make the handle attachment easy and secure.

Going the other way, you can attach the optional $399 CD-ROM base and have an 8.2-pound multimedia notebook. The base holds a 4X CD-ROM drive, two more (larger) stereo speakers, and a bay for another battery. Remove the floppy drive, and the notebook can hold three lithium-ion batteries for a really long flight.

In any configuration, an Armada 4100 is bulkier than a HiNote Ultra II, but it's also more functional, holding floppy and CD-ROM drives simultaneously, for example. The Armada's magnesium-alloy frame gives it strength and conducts heat from the processor. Compared to Compaq's larger LTE 5000 series, the Armada 4100 notebooks lack the option of a full docking station with drive bays. They can, however, attach to a port-replication base (with or without the CD expansion unit) that has an Ethernet port.

Pricing is competitive, starting at $2599. I tested the high-end

Armada 4130T

, which costs $4599 and includes a 133-MHz Pentium, 16 MB of RAM on the system board, an 11.8-inch active-matrix color display, and a 1.08-MB hard drive (the current maximum). With the CD-ROM expansion base and an extra battery, I was up to $5197. You can add up to 32 MB of additional RAM using two dual in-line memory module (DIMM) sockets. All models come with 256 KB of 9-nanosecond static RAM (SRAM) cache, a PCI bus, full video and audio ports, speakers and a microphone, an infrared port, and zoomed-video-enabled PC Card slots.

Displays are upgradable. Compaq designed the 4130T's 11.8-inch, 800- by 600-pixel active-matrix color display with a limited horizontal viewing angle, which is better for plane flights than conference rooms. Less expensive models can have 10.4- or 11.3-inch dual-scan displays. You get your choice of pointing devices. Armada 4100 notebooks come standard with a Cirque-type touchpad, but you can order it with a trackball and swap out one for the other.

The four programmable keys along the top left of the keyboard are surprisingly useful. A Compaq extension to the keyboard control panel lets you assign a program to each key, choosing from a list of all runnable programs. You can press a key to launch Explorer, for example.

Compaq adds some nice touches to the Windows 95 environment. A slick power management control panel offers many sensible options, like AC power management, that are easy to figure out and modify. Compaq's diagnostics program tells you more things about your computer than you'll ever want to know.

In performance

, the Armada 4130T ties the NEC Versa 6030H, the performance winner in this month's NSTL Hardware Lab Report. In design, Compaq has really hit a sweet spot. I expect the Armada to be both admired and copied.

## Product Information

Armada 4130T...............................$5197 (estimated street price with

L a mobile CD base with an

A extra battery)

Compaq Computer Corp.

Houston, TX

+Phone: (800) 345-1518 or (713) 370-0670

Fax: (713) 514-1740

http://www.compaq.com

Internet:

http://www.compaq.com

Circle 1060 on Inquiry Card.

## Ratings

Technology ****

Implementation *****

Performance *****

Key

***** Outstanding

**** Very Good

*** Good

** Fair

* Poor

## Application Score

## Have an Armada Your Way

mailto:"drowell@bix.com"

Dave Rowell is a BYTE senior technical editor who handles hardware reviews. You can reach him at

drowell@bix.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Pournelle

## Pournelle

## Of Zip and Spam and NT 4.0

Jerry finds new uses for removable drives -- once he gets SCSI drive assignments under control.

Jerry Pournelle

The worst prediction I ever made was that using spinning metal for mass storage would go away. "Silicon is cheaper than iron," I said. That hasn't happened. Mass storage, like memory, has become so cheap that anyone who loses work because it wasn't backed up deserves what happened.

You can add mass storage by getting a big hard drive and adding it to your system. That's worth doing, but there's an easier way.

The Iomega parallel Zip drive has become something between a standard and a necessity. Attach it to the parallel port of any PC, run one "guest" program from a floppy disk or your hard disk, and you have a 100-MB removable-cartridge drive to use for backup and file transfer. It's extremely well behaved, attaching itself as the next unused drive letter, and it leaves no residual problems when you disconnect it.

The last time I talked about the parallel Zip drive, I casually said "alas, no Mac." Since a Mac has no parallel port, that seemed obvious enough. I have since got a ton of e-mail, some polite, reminding me that the SCSI version of Iomega's Zip drive works just fine with Macs.

Some of the mail was nasty. I know a columnist who swears he will never again mention Macs because he's weary of the hate mail he gets whenever he writes anything but fulsome praise about the Mac. Although I guess I have a bit thicker skin, really, people, you do your cause no good this way. Save your hate mail for your enemies, or better yet, for archiving before you send it.

Anyway, I have a SCSI Zip drive, and, indeed, it works with Macs. With System 7.5's PC Exchange (or a similar utility), the Mac can read DOS-formatted Iomega disks, so you can use the Zip drive as a convenient sneakernet with backup for transferring data files between Macs and PCs.

The SCSI drive is a lot faster than the parallel drive. It took 6 minutes to transfer 44 MB (some big files, lots of small ones, a complex subdirectory structure) from a hard drive to the parallel Zip drive; doing the same operation with the SCSI Zip drive took just under 2 minutes. Writing that 44-MB directory from the parallel Zip drive to a hard drive took about 5 minutes, as opposed to about 1-1/2 minutes with the SCSI Zip drive. If you're after speed, or you want to transfer from a PC to a Mac and back, clearly you'll want the SCSI version. On the other hand, if what you want is backup and convenient file transfer among PCs, the parallel version is preferable.

The SCSI Zip drive will run off any standard SCSI controller, or you can buy Iomega's SCSI controller card, which appears to be a standard Adaptec SCSI-1 card. Installation for using it with the Zip drive is well documented. My advice is to get an Adaptec SCSI-2 card, but the Iomega card will certainly work. Installation of a SCSI card is simple provided you have a free interrupt request (IRQ). DOS-only systems don't need an IRQ.

For my first test, I connected the SCSI Zip drive to the SCSI outlet of the Distributed Processing Technology caching drive controller on Pentafluge, the Pentium 60 system we built a couple of years ago. This is an older controller that requires a jumper setting to activate the external SCSI port. I long ago set it to make the external port active and keep a Granite Digital SCSIVue Active Diagnostic Terminator on the port when no other device is attached, so I don't have to go inside Pentafluge to install a SCSI string.

It would have been a lot simpler if I'd had the right cable; alas, the SCSI output on Pentafluge's controller is a standard 50-pin SCSI-2 connector, while the Zip drive wants a DB-25 cable. The cable that comes with the SCSI Zip drive is a male-to-male DB-25 that looks exactly like a heavy-duty parallel-port cable.

Of course, the potential for accidentally plugging the SCSI Zip drive into a parallel port, or the parallel Zip drive into a SCSI port, is pretty high. I don't know what would happen, but I sure wouldn't want to try it.

Pournelle's first law of making SCSI work: start with Granite Digital SCSIVue Gold Diagnostic Cables and don't change to anything else until you have everything working properly. Granite Digital makes the High Density MicroD 50/DB-25 Cable, a SCSI-2-to-DB-25 cable, but I didn't have one and didn't want to wait. Thus, I connected the Pioneer DRM-624X six-disc CD-ROM changer to Pentafluge with one Granite Digital cable and used a Granite Digital 50 Centronics/DB-25 Cable to daisy chain the SCSI Zip drive to that. The SCSI Zip drive has a switch on the back to set termination: it was the last drive in the SCSI string, so I set it to "on."

The Zip drive also has a switch that sets it as SCSI ID 5 or 6; I set it to 6. Then I brought up the system with no cartridge in the drive and with the DRM-624X turned off and thus inactive.

Windows 95 (Win 95) came up fine, ignoring the DRM-624X as it should. There was one hitch. Pentafluge has logical hard drives C and D, a Maxoptix T3-1300 optical drive as E, and the CD-ROM drive as F. The SCSI Zip drive had taken over the F slot, moving the CD-ROM drive to G. I described a similar experience with the Syquest EZ135 SCSI hard drive in the June column. I got quite a bit of e-mail from people telling me, with various degrees of politeness, that SCSI drives take over in the order of their SCSI ID number, so I'd hoped that setting the SCSI Zip drive to ID 6 would prevent that shift. Alas, that turned out not to be the case.

Once I had the SCSI Zip drive operating, I timed some massive file transfers across the network and then shut down the system.

I got the "Please Wait" message. After about 5 minutes, it was pretty obvious that nothing else would happen, so I cut the main power. When I turned it back on, Pentafluge trundled for a while and then Win 95 announced there were problems with the Registry. It offered to restore the Registry from backup and try again, warning me that I might lose something in the process. There didn't seem to be much of an alternative, so I told it to go ahead.

I got the same message once more, and once more told it to go ahead. Recall that the first time I brought up the SCSI Zip drive, I did so with no cartridge in the drive. I had forgotten that, and there was a cartridge in the drive this time.

The system came up on the third try, and Lo!, the drives were really out of order. The D drive, which is merely a logical partition of a single physical drive, had been moved and the SCSI Zip drive had taken over D. E was still the Maxoptix T3-1300, F was now the D drive, and the CD-ROM drive that normally lives at F was now G. All those drives worked in the sense that I could access them, but any software that expected the D drive to be D was hosed.

Shut down once more. This time, it shut down with no problem, and I have been unable to duplicate the shutdown problem on any machine since that first time. I've no idea what happened. Anyway, I removed the cartridge from the SCSI Zip drive and fired up once more. It came up fine. The D drive was once again D.

Of course, the Zip drive had shoved the CD-ROM drive aside and taken over F in its usual high-handed fashion, but otherwise I had no problems. This time it shut down properly, and from that moment on, I have had no problems other than the displacement of the F CD-ROM drive.

The moral of this story is that SCSI has a mind of its own, and if you intend to use a SCSI Zip drive, plan your drive-lettering scheme accordingly. Do not imagine that you can have a CD-ROM drive with a lower drive letter than the SCSI Zip drive; and if you plan to boot up your system with a cartridge in the drive, be prepared for some other oddities in drive lettering.

You will, however, have a perfectly good drive. You can even boot from it, which means that you can have a series of OSes on different Zip cartridges and boot the one you like. I've tested it with Win 95 and Windows 3.11. I haven't yet tried it with Unix, Windows NT, or any flavor of OS/2, and I probably won't; but I'm told it will work just fine with those, too, since you can set up your computer to believe that the SCSI Zip drive is just another Winchester hard drive. Incidentally, that's also true of the Syquest EZ135.

One possible configuration is to have a hard drive as the data drive. Set it as a nonprimary drive and then set a Zip drive as the C boot drive. Then you can boot any OS you like by changing cartridges.

Once I was sure the SCSI Zip drive worked on Pentafluge, I transferred it to Cyrus, my Cyrix 6x86-P166 system. Cyrix claims their P166 is completely compatible with, and faster than, a Pentium running at 190 MHz. I've used the Cyrix system for a couple of months now, and I have no reason to dispute that claim. It is fast, compatible, and reliable.

Cyrus has a PCI-bus Adaptec SCSI card with an external SCSI-2 connector port, so I moved the DRM-624X and SCSI Zip drive string over to it, and booted up with the DRM-624X turned off and no cartridge in the Zip drive. It came up fine. Cyrus does not have a Maxoptix optical drive, so the CD-ROM drive is E. As expected, the SCSI Zip drive displaced it, taking over the E slot for itself and moving the CD-ROM drive to F.

Unlike Pentafluge, Cyrus had a network drive mapped to F, but that didn't matter. The SCSI Zip drive became E, the CD-ROM drive became F, and the F network connection vanished. Actually, it didn't quite vanish. While I could read the CD-ROM drive as F, when I went into My Computer and looked at network drive connections, the pull-down menu still showed F as a network connection.

Shutdown was normal, and booting up with a cartridge in the Zip drive produced no different result from when there wasn't a cartridge. That is, while booting with a cartridge displaces the D partition on Pentafluge, it doesn't do that on Cyrus. No one I've spoken to can tell me why.

The next step was to connect both Zip drives to Cyrus. They worked fine, with the parallel drive taking the next empty drive letter (G), while the SCSI drive displaced the CD-ROM drive as usual. Finally, I turned on the DRM-624X, leaving both Zip drives attached to Cyrus. Everything worked. The SCSI Zip drive took over E; the internal CD-ROM drive became F; the DRM-624X took over G, H, I, J, K, and L; and the parallel Zip drive took the lowest unused drive letter after L.

The interesting thing about this is that several of the drive letters between F and L had been mapped to other network drives. Those network connections simply vanished -- except that their ghosts remained in the network setup, and booting up with the DRM-624X turned off restored them.

The bottom line here is that both parallel and SCSI Zip drives work quite well. They read each other's disks just fine. The parallel Zip drive installs simply and works unobtrusively, finding an unused drive letter for itself.

The SCSI Zip drive installs easily if you already have SCSI devices; otherwise, you will have to install a SCSI card and drivers. This isn't particularly difficult, but it's certainly harder than just connecting a cable to the printer port. The SCSI Zip drive is more aggressive and will certainly displace a CD-ROM drive if brought up with a cartridge in the drive, and it may even displace a hard disk partition. You are unlikely to prevent this no matter how hard you try. Otherwise, no damage is done.

The SCSI drive is about three times as fast as the parallel drive and perhaps half as fast as your average hard drive. Either can be a good way to add storage capacity to your system. I particularly like the parallel Zip drive as a backup-and-sneakernet system, but, of course, unlike the SCSI Zip drive, you can't use it with a Mac. The SCSI drive works well with both Macs and PCs. If you need storage space and a backup system, either is pretty hard to beat. Recommended.

Having said all that, I have to point out that I have for about a year had a Fujitsu DynaMO 230 magneto-optical (MO) system attached to a SCSI port on an ancient Cheetah 386. I've used it across an Ethernet, and it's about as fast as the SCSI Zip drive. It has always been reliable. Nothing in the Fujitsu literature mentions using this on a Mac, but SCSI is SCSI, and I'd be astonished if you couldn't connect the DynaMO 230 to a Mac. What you won't do is read the DynaMO cartridges on a parallel-port device. Still, the DynaMO 230 works. The drive and cartridges are smaller than the Iomega Zip drives and their cartridges, and each DynaMO cartridge holds a bit more than 200 MB compared to the Zip drive's 100 MB.

We installed the beta version of NT 4.0 on the Doubleshot 133, which had previously been running NT 3.51. At one time, it ran OS/2, and I had hoped that Merlin, the newest version of Warp, would be able to make use of the Doubleshot 133's dual processors, but IBM didn't put that feature in Merlin. IBM is beta-testing SMP for Warp Server. For now, to run OS/2 with symmetric multiprocessing (SMP), you are stuck with clunky OS/2 2.11. While I rather like OS/2 Warp Connect, and I think I like Merlin, I refuse to go back and relearn version 2.11.

Installation of NT 4.0 was really simple on the Doubleshot 133. I haven't yet tried installing it on a machine running Windows 3.1 or Win 95; I'm told that's a bit more difficult, but nothing excessive. One thing, though: be sure you know the IRQ and port address settings for all your hardware. Unlike Win 95, NT doesn't even try to be Plug and Play. On the other hand, it won't change your settings for you once you have them the way you like.

We haven't done a lot of work with NT 4.0, but what I've seen I like a lot. It's much more like Win 95 than 3.11. In fact, you can use NT 4.0 quite a while before you notice it isn't Win 95. It's also faster. Although few current applications have threaded code able to take advantage of the Doubleshot 133's dual processors, ordinary single-threaded jobs are still faster because NT 4.0 is able to trade off between processors, putting all the background stuff like network and disk operations, monitoring the uninterruptible power supply (UPS) status, etc., on one processor while the other runs your task.

In practice, it's not quite that simple. NT 4.0 has a utility that shows a graph of processor-use history. There are two such graphs for a dual-processor system, and it's interesting to watch how NT switches loads between processors as you load it down by networking to the server.

There was a time when OS/2 was a technically more elegant OS than NT, and OS/2 Server was about the best server software around. I don't think that is true any longer; IBM long ago lost the marketing edge and may now have lost the technical edge as well. NT 3.51 is very stable and makes for a good server system; while NT 4.0, even in the beta version, is fast, easy to use, simple to install, and looks like Windows to most of your network. Moreover, IBM is rapidly adapting its server software to run just fine on NT systems. If you have a large computer network system and the resources to manage it, you may have a need for OS/2; but NT 4.0 seems to be the NT for the rest of us. More when I know more, but my first impressions of NT 4.0 are very positive.

Meanwhile, the little Doubleshot 133 remains the quietest system in the house. It's very stable, and running NT 4.0, it may be the fastest networked system we have here. Those dual processors really speed things up. Just now, it is the NT experimental machine, but once I'm sure NT is stable, I think I'll put the Micropolis external 4-GB drive on the Doubleshoot 133 and make it the main Chaos Manor server.

Visioneer's PaperPort Vx is a blooming little miracle.

This is a gadget about 4 inches tall, 3 inches deep, and a foot wide. It sits anywhere you like and connects to a serial port with a normal cable. Once installed, you activate it by feeding it a sheet of paper. It reads your papers, one sheet at a time, into image files, one file per sheet.

Installation was simple: I plugged the PaperPort Vx into the COM1 serial port, connected its power supply, and ran the installation program. The software seems to have scanned my system, because when it was done, the PaperPort "desktop" had icons for Microsoft Word and WinFax, as well as "printer," Exchange, Excel, WordPad, and Paint.

I fed in a printout of some e-mail I'd received on BIX. The PaperPort Vx pulled it through and quickly made an image file of the document. Then I dragged the image onto the WinFax icon and sent it to my fax machine downstairs. It came out quite readable, as good as any fax comes out on my old thermal fax machine.

Then I dragged the image onto the Microsoft Word icon. That automatically activated the OCR to produce a Word document. It made one mistake: the original said "pc." The OCR read that as "pe."

I've also fooled around with other stuff. There are a bunch of settings to get different qualities of OCR performance and image quality. It's all quite intuitive, and now I've got electronic versions of some newspaper articles I've been saving, meaning I can find them by electronic search now. I think I'll do a lot more of that.

I had one major glitch. Once when I fed in a sheet of paper, the electric fan blew it about as it emerged, and the program said the read had failed, although examination of the document image didn't show any problems. After that, though, the PaperPort Vx wouldn't feed paper at all, and the software kept telling me there was no PaperPort device on COM1. I even tried turning off the computer and bringing it back up, and still the Visioneer software insisted there was no PaperPort on COM1. Finally, I turned off the PaperPort itself by pulling its power cord. That worked: it processed the next sheet of paper I fed it just fine. Apparently that "reset" it.

Visioneer also makes a keyboard with a PaperPort built into it, called the PaperPort ix. It has a separate power supply, so presumably you can "reset" it the same as with the stand-alone version. I'm fairly picky about keyboards, so I haven't tried it yet, but I'll have one of the interns install it at his station. I'm sure it will work; my only question is whether I'd like the PaperPort ix as a keyboard. More another time.

Disk space keeps getting cheaper. You can put a lot of documents on a 100-MB Zip cartridge; and that's a lot of paper you don't have to keep around. My son Richard uses a PaperPort to keep his paper files small, and it sounds like a good habit to get into. I expect I'll be writing about this again.

You'll have noted that my primary e-mail address remains jerryp@bix.com. BIX began as the BYTE Information Exchange and was eventually sold by McGraw-Hill to Delphi, which was later bought by News Corp. Recently, a group of Delphi/BIX employees with some outside backing bought both BIX and Delphi and are making a going concern of both.

BIX isn't for everyone. It's small, and the interface is text-based and command-line-driven. It looks old and clunky. The appeal of BIX is the information density. BIX never exploded the way the Internet did, and as a consequence, there are intelligent technical conversations and very little spam. When you ask a question on BIX, you get a reliable answer.

My usual access to BIX is through a shareware program called Galahad. This is a Windows/Win 95 program that goes out to BIX, logs on, downloads all my e-mail and all the message traffic in the conferences I belong to, and then logs off, letting me deal with everything off-line with reasonable text editors. It's one of the main reasons I stay with BIX.

The main problem with Galahad has been using it on multiple machines. Galahad keeps all kinds of reference files, archives, and databases, and transferring all that when I want to use a different machine is a major pain. Then, just today, on BIX, BYTE technical editor Russell Kay suggested the solution: put Galahad -- program, logs, files, and all -- on a Zip cartridge. Carry the Iomega parallel Zip drive in checked luggage -- a good idea for a backup system since I do a lot of work on the road -- and access BIX that way. When I get back home, I attach the Zip drive to the parallel port of the system I'm using.

I haven't tried this, but I will. I'll probably go even further: since I have five Internet accounts and three e-mail boxes, I'll put all that Internet stuff on a Zip cartridge. Working out a backup system shouldn't be too difficult. Yet one more use for the parallel Zip drive.

Meanwhile, BYTE readers weary of the bickering and nonsense in much of the Internet might think about BIX, where all conferences are moderated and most of the participants really do know what they're talking about.

Two vital books for computer pros: The Hard Disk Data Base and The BIOS Companion, both by Phil Croucher, and both exactly what their titles imply. If you work with odd computers, particularly older ones, these are invaluable: page after page of technical data, all in one place.

The game of the month is the Strategic Studies Group's The Complete Carriers at War. All the older Carriers at War games and construction tools, plus new scenarios, including the North Atlantic and Mediterranean. Suppose the Germans had gotten control of the entire French navy: could the British have beaten the combination? Plus the entire Pacific carrier war. Lots of realism and no arcade action.

The CD-ROM of the month is The 1996 Grolier Multimedia Encyclopedia. It's well balanced between details and brevity. Philip Jose Farmer defined a dullard as a person who can go to the encyclopedia, look up one item, read it, and close the book. It's fun to browse Grolier.

The book of the month is by Cicely Veronica Wedgwood, The Thirty Years War (Routledge). I thought I knew all I wanted to about the Defenestration of Prague, Friedrich the Winter King, Father Tilly, Cardinal Richelieu and Father Joseph "the gray eminence," and Wallenstein, but once I opened this wonderful book, I found a wealth of details more fascinating than any novel. Part of Hitler's popularity came from his promise to upset the Peace of Westphalia that ended the Thirty Years War.

The computer book of the month is by Gary Frerking, Nathan Wallace, and Wayne Niddery, Borland Delphi How-To (The Waite Group). I've neglected Borland Delphi in my language discussions, and I shouldn't: it's a practical language every bit as useful as Visual Basic, and, being rooted in Pascal, it has a more logical structure. The book teaches through examples and includes a CD-ROM with hundreds of subroutines that are useful in themselves as well as worth studying.

A computer book I overlooked when it first came out is Susan A. Kitchens' The KPT Bryce Book (Addison-Wesley). Bryce is the landscape-generator software portion of the Kai's Power Tools series; Kai's Power Tools are one of the reasons Mac computers are so much fun. Kitchens starts with basics and explains how to build structures, from castles to planets, with examples, including the inevitable CD-ROM of routines and pictures. If you use a Mac, you'll like this.

http://www.earthlink.net/discontinuity

As usual, I've written more than will appear in the magazine. You can find it on BYTE's Web site. You might also want to check out

&http://www.earthlink.net/discontinuity

4, where John C. Dvorak and I argue critical issues.

## Where To Find

The Complete Carriers at War............................$69.95

Strategic Studies Group

Pensacola, FL

Phone: (904) 469-8880

Fax: (904) 469-8885

Circle 977 on Inquiry Card.

Cyrix 6x86-P166.......................................$3939

......................................................$3389 without monitor

Cyrix Corp.

Richardson, TX

+Phone: (800) 340-7501 or (214) 968-8388

Fax: (800) 340-7532

http://www.cyrix.com

Internet:

http://www.cyrix.com

Circle 978 on Inquiry Card.

Doubleshot 133 (with OS/2 SMP 2.11)

or Landmarq P133 VPM Doubleshot (with Windows NT).....$2599

Diamond Flower, Inc.

Sacramento, CA

+Phone: (800) 808-4334 or (916) 568-1234

Fax: (916) 568-1233

http://www.dfiusa.com

Internet:

http://www.dfiusa.com

Circle 979 on Inquiry Card.

?The 1996 Grolier Multimedia Encyclopedia................$59.99

Grolier Interactive, Inc.

Danbury, CT

+Phone: (800) 285-4534 or (203) 797-3530

Fax: (203) 797-3130

http://www.grolier.com

Internet:

http://www.grolier.com

Circle 980 on Inquiry Card.

PaperPort Vx.....................................about $299

PaperPort ix.....................................about $349

Visioneer, Inc.

Palo Alto, CA

+Phone: (800) 787-7007 or (415) 812-6400

+Fax: (800) 505-0175 or (415) 855-9750

http://www.visioneer.com

Internet:

http://www.visioneer.com

Circle 981 on Inquiry Card.

Zip 100-MB Removable Disk Drive........................$199.95 SCSI or parallel version

Iomega Corp.

Roy, UT

+Phone: (800) 697-8833 or (801) 778-1000

Fax: (801) 778-5763

http://www.iomega.com

Internet:

http://www.iomega.com

Circle 982 on Inquiry Card.

mailto:"jerryp@bix.com"

Jerry Pournelle is a science fiction writer and BYTE's senior contributing editor. You can write to Jerry c/o BYTE, One Phoenix Mill Lane, Peterborough, NH 03458. Please include a self-addressed, stamped envelope and put your address on the letter as well as on the envelope. Due to the high volume of letters, Jerry cannot guarantee a personal reply. You can also contact him on the Internet or BIX at

jerryp@bix.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Pournelle

## Pournelle

$WEB EXCLUSIVE: Speed, At Any Cost

Chaos Manor is once again the scene of a battle over IRQs -- this time under Plug and Play. Jerry finally upgrades his fax system and offers thoughts on security as well a word of advice for game developers. And don't forget to check the October issue of BYTE: Jerry finds plenty of uses for Iomega's Zip drives, but not before a tussle with SCSI drive-letter assignments.

Jerry Pournelle

[EDITOR'S NOTE: This bonus section is a web exclusive.]

I don't think Plug and Play is ready for prime time.

My Cyrix 6x86-P166 system is full up: every interrupt request (IRQ) but one was used for something. I needed to add a network card. The one I chose was Applied Creative Technology's Ultimate PCI-3000 Ethernet Card, which is Plug and Play-ready. It has the advantage that in addition to the normal 10Base-T outlet, there's an "EZ" Ethernet connector, which you can daisy chain to another Ultimate PCI-3000. I went into the Cyrix BIOS, enabled Plug and Play, installed the network card, and brought up the system.

The network card worked fine, but Plug and Play moved the Creative Labs Sound Blaster ISA-bus sound card from IRQ 5 -- where it belongs (many DOS games in particular expect it to be there) -- to IRQ 10 and put the modem at IRQ 5. That's no good. The Sound Blaster will work at IRQ 10 for Windows stuff, but DOS programs won't be able to find it.

Back to the BIOS. I set the PCI slot where the network card lives to IRQ 9, the Adaptec SCSI controller board's slot to IRQ 10, and the Matrox MGA Millennium video board's slot to IRQ 11. Doing that is simple; learning how to do it is tedious, involving poking about with BIOS settings. The important thing about spelunking your BIOS is that you keep a really good log of what you're doing so you can recover when you muck something up. One of Pournelle's laws is that the relentless application of logic will solve most problems; it proved to be the case this time, too.

Once I learned how to work on the Cyrix BIOS settings, I took the internal modem card out and started over. This time, Plug and Play put the Sound Blaster card at IRQ 5. I disabled a COM port, freeing up that IRQ slot, and put the modem back in. That worked, and the modem card took over the disabled COM2 port's IRQ and now works as COM2. Then I quickly disabled Plug and Play before anything could change its mind. The system is now stable.

I've had to do much the same thing with our Gateway 2000 Pentium systems, which also tend to come full up with equipment and features. Once again, spelunking the BIOS is largely a matter of keeping good records and exercising patience.

Gateway 2000 systems work well: Roberta's new machine is a Gateway 2000 P5-200XL, and she loves it. More on that next month.

In theory, Windows 95 lets you set IRQ assignments. In practice, however, if you enable PCI Plug and Play and Win 95 Plug and Play, they will fight it out, and the results may not be what you want. With patience and luck, you can get things working -- both the Cyrix and Gateway 2000 systems are working wonderfully now -- but it can be a struggle. Your best weapon in that fight is a good logbook. Get in the habit of keeping good notes, and don't make them on an old envelope, which you will inevitably lose. Buy a hardbound composition book and keep your records in that. If you do record something on an old envelope, tape the envelope into the permanent log. I guarantee you'll be glad you did.

We have Windows NT running on two machines now. Version 3.51, which looks and feels a lot like Windows 3.11, is running on Spirit, a dual-Pentium 120. Spirit boasts a Micropolis external 4-GB drive as well as a Digital Equipment 4-GB internal drive. It's the main network server for Chaos Manor. It has been running NT for months now and has never been shut down.

When we set up Spirit, we attached it to an American Power Conversion Smart-UPS (uninterruptible power supply) 700, but we didn't have the cable and software to make it smart. There weren't any problems. APC was supposed to send the cable and software, but instead they sent an entire new unit. We thought about that for a minute, took the cable and PowerChute Plus software, and installed them on the existing Smart-UPS 700. Installation was simple; you don't need to shut down or restart. Then we tested the system by yanking the plug. I also did rapid on-off flicks on the power-strip switch the Smart-UPS 700 is plugged into. Everything works fine.

PowerChute Plus will also run diagnostics on the UPS and log the results, or you can run them on command. We deliberately set the date a day ahead and ran some tests. Naturally, the log showed the test date as a day ahead of reality. Then I reset the date properly. The log didn't change, but when I ran the diagnostics again, it updated the "latest event" to the correct date. The log also shows the "blackout" events from our tests.

The software will run tests as scheduled events in the background, and if there's any indication that the batteries need servicing or the system needs any other attention, it will signal you. All told, this is the simplest and most painless UPS installation I've seen.

There's only one problem. The Smart-UPS 700 causes the server to broadcast messages to all the workstations announcing that the server is now under battery power. It sent the messages loud and clear to a Diamond Flower Doubleshot 133 running a beta version of NT 4.0. They went just fine to a Cheetah 486DX2/25 running NT 3.51 and to a Pentium 90 running OS/2 Warp Connect. Whatever you're doing, including in a DOS program, up pops the message that "Spirit is running on battery power and will shut down in 4 minutes and 50 seconds." When you plug the UPS back in, the message goes out that normal power has been restored. This is as it should be.

Unfortunately, that message does not go to workstations running Windows 3.11 or Win 95, even if they're logged in to Spirit. They remain in total ignorance of the impending failure of the server. We weren't sure why this was or if anything could be done about it. I now find that Win 95 doesn't have any mechanism for receiving the broadcast messages.

Otherwise, the Smart-UPS 700 with PowerChute Plus is the easiest server protection I know of. There are many UPSes out there, and I have no way of knowing which are best. I do have experience with Clary and APC UPSes, and I can say with confidence that both companies' products are good enough, and the APC software is the best I've seen. If your work is at all valuable and you're not using a UPS, you are taking needless risks. Get one.

I wish people would stop improving things.

I don't do a lot of fancy stuff with faxes. I have an old-fashioned curly fax machine downstairs. It's connected to its own phone line and nothing else. Most of the time when we want to send a fax, we take a sheet of paper, put it in the machine, dial the number, press Start, and walk away. It does the job. It also receives on horrible curly paper, which drives me nuts, but most of the faxes I get aren't anything I want anyway.

Sometimes I need something different. When I finish my column, I try to send an advance copy to anyone I've written about, with the invitation to correct me if I'm wrong. My cover letter says I'll correct errors of fact, I'll listen to arguments about errors of judgment, and I reserve the right to decide which is which. For years, I did that mostly by mail, but that seems a bit silly. After all, the documents exist in my computer, the computer has a fax modem, and most companies have a fax number. Then for a while, I got involved in testimony to Congress on space policy, and that turned out to be easier done by fax than by mail.

The result was that I installed Symantec's WinFax and ran the macro program to add it to my File menu in Microsoft Word. That version of WinFax wasn't written for Win 95, but it worked pretty well until one day I had to reinstall Win 95. After that, WinFax didn't work very well. Finally, one night when I had to send a fax to NASA headquarters, it wouldn't work at all.

I printed the document and sent it with the old fax machine, but I did miss the convenience of sending faxes directly from my computer. Thus, I got WinFax Pro 7.0, which is supposed to run with Win 95. Then I made the mistake of trying to do an upgrade installation. That is, I didn't remove the old (and somewhat broken) WinFax, I just installed the new version over it.

The result was a complete failure, remedied only by doing an uninstall from the Add/Remove Programs icon in the Control Panel, and even that didn't get it all. I had to use FirstAid 95 Deluxe and go in with fire and sword to get rid of the last components. Even then, I had to do some modification of the Microsoft Word Normal template.

That's the bad news. The good news is that once I did that, I was able to install WinFax Pro 7.0 with a minimum of trouble. Then I ran the Word macro -- there are two, one for Word 6, the other for Word 7 -- and now I can write a document in Word, invoke WinFax from the File menu, and send the fax. There's a new "improved" notebook that for reasons I don't understand requires me to insert the 1 in any long-distance number I dial -- the old version understood I was in area code 818 and acted accordingly -- and it all seems more complicated than it used to be, but actually it works quite well. I've sent about a dozen faxes, including a couple to my downstairs machine, and everything has worked smoothly.

Moreover, WinFax will do a good job of answering the phone and receiving faxes. The OCR reader works quite well to take an incoming document and turn it into Microsoft Word text. I don't use that feature very much just now, but I will in the future when I have my firewall protection set up.

I'll be glad to be rid of curly faxes. With WinFax on the job, I can look at faxes on-screen, file the useful ones, and print only the very few that need to go in a paper file. It's about time I rationalized that part of my business, and it looks like WinFax is going to let me do it.

WinFax Pro 7.0 goes back on my recommended list, provided you understand that you take your chances trying to do an upgrade installation. Symantec says it ought to have worked, and they don't understand why it didn't. Neither do I, and I'm prepared to believe I had my system messed up worse than most people have theirs, but I still don't recommend upgrade installations. Go into Control Panel and remove your old version. Then do the new installation.

Otherwise, recommended.

I have two reasons to be concerned about security here. First, given my readership, there are a lot of people out there capable of remarkable feats with computers; and some will think it a great joke if they can get into my system and leave me a message in, say, the draft of my current novel.

Perhaps that's not too likely, but then neither is what happened at PC Expo. The editorial staff had met to decide the winners of the BYTE Best of PC Expo Awards. The meeting ran until about 2:00 a.m.: we take those awards seriously. Eventually, we had chosen all the winners, and it was time to write them up. My own part was done quickly, and I bugged out just as I heard some complaints about lost files.

The next morning, I found I'd escaped just in time: all four of the BYTE laptops had become infected with the Word Macro Concept virus. This virus has the effect of saving documents as Template files, and if you don't know how to deal with it, the result can be quite frustrating. It's also a cross-platform virus -- it can spread to Macs, too -- and worse, it can infect your system through a downloaded file despite a number of precautions. It's not all that vicious. Dr. Solomon's Anti-Virus Toolkit, Norton AntiVirus, and other antivirus tools will get rid of it for you, and the versions I've seen do no permanent damage provided you don't panic and erase something yourself. Still, the notion of the BYTE editors -- who collectively know ever so much more about this stuff than I do -- getting burned with a virus is a little frightening.

I've never had one of my machines infected, although I have been given infected disks. This is largely because we run most new programs on a machine not connected to the network, nothing I have answers the telephone, and we run Dr. Solomon's Anti-Virus Toolkit every time there's a new edition and sometimes more often.

If you don't have a good antivirus program, you probably ought to get one. Alan Solomon no longer runs S&S Software International, the company that publishes Dr. Solomon's, and he was the main reason for my high confidence in that product. It's still good. So is Norton. Get something reliable, though. It's time.

One of these days, game designers are going to understand that converting strategy games to arcade games does no good and a lot of harm. Warcraft: Orcs and Humans and Warcraft II: Tides of Darkness are really enjoyable medieval fantasy games; but when Blizzard Entertainment decided to add extensions to the games, instead of making them more interesting, they made them nearly impossible.

The scenarios in Warcraft II: Beyond the Dark Portal are not only difficult because you don't have enough force, but the game has become Whack-A-Mole. You can't give orders when the real-time action is paused, and even at the slowest setting, you cannot possibly pay attention to two fronts at once. Meanwhile, the enemies become both numerous and powerful, the frustration level rises, and eventually it's no fun at all. Finishing becomes a matter of grim determination and teeth grinding, with no time to stop and look over the situation, no way to play a strategy, and nothing for it but to save, get lucky, save, get unlucky, restore and try again, save, etc. All semblance of role playing is gone at this point. So is all the fun.

I did win, of course. I used Norton Disk Editor to increase the amount of gold and lumber I start with, thus taking one of the vulnerabilities out of the game: with lots of resources, you can build cannon towers to hide behind until you get a decent-size army. Take that, game designers!

But I do wish game designers would understand that some of us don't have the reflexes of teenage fanatics, and if we'd wanted to play arcade games, we'd have gotten an arcade game. Meanwhile, arcade players find hyped-up strategy games boring. I have no doubt they'll sell a lot of the Warcraft II: Beyond the Dark Portal extensions simply because Warcraft: Orcs and Humans and Warcraft II: Tides of Darkness were so enjoyable, but my advice on the extension set is to buy Strategic Simulations' Fantasy General. When that one gets difficult, it's because you made a bad decision, not because you're trying to fight what in the real world would be an all-day battle, but in the game world is about 3 minutes flat.

## Product Information

Fantasy General...........................$40

Strategic Simulations, Inc.

Sunnyvale, CA

+Phone: (800) 601-7529 or (408) 737-6800

Fax: (408) 737-6814

http://www.ssionline.com

Internet:

http://www.ssionline.com

.Smart-UPS 700 with PowerChute Plus.......$588

American Power Conversion Corp.

West Kingston, RI

+Phone: (800) 877-4080 or (401) 789-5735

Fax: (401) 789-3710

http://www.apcc.com

Internet:

http://www.apcc.com

.Ultimate PCI-3000 Ethernet Card...........$79

"Applied Creative Technology, Inc.

Dallas, TX

+Phone: (800) 433-5373 or (214) 358-4800

Fax: (214) 351-6741

\Warcraft: Orcs and Humans...........about $45

Warcraft II: Tides of Darkness......about $50

Blizzard Entertainment, Inc.

Irvine, CA

+Phone: (800) 953-7669 or (714) 955-1380

Fax: (714) 955-1381

http://www.blizzard.com

Internet:

http://www.blizzard.com

.WinFax Pro 7.0...........................$129

Symantec Corp.

Cupertino, CA

+Phone: (800) 441-7234 or (541) 334-6054

http://www.symantec.com

Internet:

http://www.symantec.com

mailto:"jerryp@bix.com"

Jerry Pournelle is a science fiction writer and BYTE's senior contributing editor. You can write to Jerry c/o BYTE, One Phoenix Mill Lane, Peterborough, NH 03458. Please include a self-addressed, stamped envelope and put your address on the letter as well as on the envelope. Due to the high volume of letters, Jerry cannot guarantee a personal reply. You can also contact him on the Internet or BIX at

jerryp@bix.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

.E-Mail Meets Personal Information Management

Dave Andrews

There's good news for those of you who spend a good portion of your day creating and responding to e-mail: Microsoft's Outlook 97 integrates e-mail with common business applications such as scheduling, PIMs, and word processing. Slated to ship by the end of the year, Outlook 97 lets you juggle tasks such as scheduling, basic contact management, and task delegation in one place, under one consistent interface (

see the screen

Outlook 97 offers an immense number of new features. The primary benefit is that unlike Schedule+ (which this new program replaces), Outlook 97 provides a single store for e-mail and other information. For example, you can create an appointment in Outlook 97's calendar module by simply dragging an e-mail message into the calendar. Another timesaving feature, auto-preview, helps you prioritize e-mail reading by displaying only the first few lines of a message. Remote users can download just the header and subject of a message before downloading all its contents.

Outlook 97 includes several form templates to let you automate expense reports, vacation requests, and other activities; you can also create forms. The intuitive rules-creation module, slated to ship shortly after Outlook 97, lets you automate message responses. Based on my experience with Outlook 97, it is a fine implementation of the next step in the evolution of e-mail.

## Where To Find

Outlook 97.............................Call for price

Microsoft Corp.

Redmond, WA

+Phone: (800) 429-9400 or (206) 882-8080

Fax: (800) 727-3351

http://www.microsoft.com

Internet:

http://www.microsoft.com

Circle 1013 on Inquiry Card.

## The Outlook is Good

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## Enterprise-Wide Business Planning

Two integrated products for Windows help you manage and control groups, departments, divisions, and entire companies. Business Maestro ($995; Enterprise model, $3995) provides tools for formal business and strategic planning, financial modeling and control, and managing the budget process. Business Maestro has data import and export facilities supporting a number of popular formats. Designed for cost centers, Budget Maestro ($495; Enterprise model, $1995) assists companies in bottom-up and top-down budgeting, and you can use it with Business Maestro.

Contact: Planet Corp., Worcester, MA

+Phone: (800) 366-5111 or (508) 757-2840

!E-Mail: planet@planet-corp.com

Circle 1014 on Inquiry Card.

*Maestro Orchestrates Effective Management

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## Manage Documents Over the Web

Available for Unix and Windows NT, the Basis Intranet Solution lets you integrate enterprise-wide document management applications with Web technology to develop intranets. The package includes links to business-critical applications, including policies and procedures, research information management, and competitive analysis; monitoring of security controls and operating logs; full-text search and retrieval; thesaurus-based search assistance; cross-repository queries; and the ordering of search results.

Contact: Information Dimensions, Inc., Dublin, OH

+Phone: (800) 328-2648 or (614) 761-8083

http://www.idi.oclc.org

Internet:

http://www.idi.oclc.org

Circle 1015 on Inquiry Card.

## Wide-Ranging Solution

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

*Client/Server Project-Collaboration Tool

A client/server application that supports TCP/IP- and NetWare-based IPX/SPX networking, TeamWay (per server, $1000; per client, $350) delivers timely status information to individual team members and their managers. The product helps team members track personal responsibilities across projects, as well as manage nonproject obligations. The program schedules a project's component tasks based on each team member's constraints and updates everyone as changes occur in the project.

Contact: Island Way Corp., Wellesley, MA

Phone: (617) 235-6740

http://www.islandway.com

Internet:

http://www.islandway.com

Circle 1016 on Inquiry Card.

## Timely Tool

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## Build Business Models

A stand-alone Windows application for creative business thinking, Advance 1.0 ($695) helps you build business models and analyze multidimensional business data contained in corporate databases.

Contact: Lighten, Inc., Berkeley, CA

+Phone: (800) 398-4545 or (510) 528-4376

http://www.lighten.com

Internet:

http://www.lighten.com

Circle 1017 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## Dynamic Database Management

A suite of software tools, Total Performance Management (tools, from $2995; TPM Premium Package, $25,000) proactively manages client/server database environments. You can use the product with Oracle, Sybase, or Microsoft SQL Server databases that use SQL*Net, SNMP, or Open Client.

Contact: The Database Solutions Co., Richmond, VA

+Phone: (800) 933-7668 or (804) 794-0354

http://www.dbsol.com

Internet:

http://www.dbsol.com

Circle 1018 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## Engineering Series on CD-ROM

McGraw-Hill's Interactive Engineering Calculations Series includes Civil Engineer's Solutions Suite ($79.95), Chemical Engineer's Solutions Suite ($89.95), and Architectural Engineer's Solutions Suite ($69.95). The CD-ROMs include the text, tables, graphs, and diagrams from corresponding sections of the original handbooks.

Contact: McGraw-Hill Professional Book Group, New York, NY

+Phone: (800) 722-4726 or (212) 337-4097

http://www.books.mcgraw-hill.com

Internet:

http://www.books.mcgraw-hill.com

Circle 1019 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

!Scanning OS for Desktop Imaging

By providing a link between a TWAIN- or Adobe Plug-In-compliant scanner and desktop applications, the Presto PageManager Suite lets you drag and drop a scanned image to a printer, fax application, e-mail, filing system, OCR software, or word processor for further processing. Available for Windows and the Mac, the Presto PageManager Suite (about $199) includes the scanning OS, an electronic filing system, OCR software, a color-image editor, business-card scanning software, forms, and a color-image-transmission system.

Contact: NewSoft, Inc., Fremont, CA

+Phone: (800) 214-7059 or (510) 252-0267

http://www.tophat.com

Internet:

http://www.tophat.com

Circle 1021 on Inquiry Card.

## Now the TWAIN Shall Meet

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## Share Images Over a Network

Now, users on Novell NetWare 3.12 or higher LANs can store, manage, search, and share document images. Recollect LAN (server, $2000; client, $299 each) consists of Recollect Server, an NLM that provides centralized image storage and retrieval; the Recollect Scan and Search client module, which allows users to capture, retrieve, view, and organize documents on the server or their own PCs; and the Recollect Search client module, which allows users to retrieve, view, and organize Recollect documents.

Contact: MindWorks Corp., Sunnyvale, CA

+Phone: (800) 683-8005 or (408) 730-2100

Circle 1020 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## Windows 95 Backup Software

SmartStor's ($65) Installable File System feature uses a 32-bit VxD to establish a tape drive as a logical, mounted storage device, making it easier to view, back up, and restore data. Once you mount the system, you can access the tape drive just as you would any other on-line storage device. SmartStor also lets you back up data to hard drives and optical drives anywhere on the network.

Contact: McAfee, Santa Clara, CA

Phone: (408) 988-3832

http://www.mcafee.com

Internet:

http://www.mcafee.com

Circle 1022 on Inquiry Card.

## Logical Backup

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## Internet Firewall Security

Designed to provide computer network security for medium- to large-size organizations with Internet or intranet exposure, On Guard screens IP and IPX packets and rapidly compares the "state" of each packet against the firewall's rules base. If the traffic is not permissible or is unexpected, such as a hacker's attempt to spoof the firewall, On Guard drops the packets and issues an alert to the On Guard Manager workstation.

Contact: On Technology Corp., Cambridge, MA

+Phone: (800) 767-6683 or (617) 374-1400

http://www.on.com

Internet:

http://www.on.com

Circle 1023 on Inquiry Card.

)On Guard Ready to Fence with Interlopers

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## Make Space on Your Crowded Hard Disk

DiskMapper ($49.95) shows you the size of every file and subdirectory on your hard disk, as well as the filename, path, size, date, and extension type, so you can delete or compress files you don't need or rarely use. The utility for Windows 3.x and 95 also lets you launch programs or data files from DiskMapper.

Contact: Micro Logic Corp., Hackensack, NJ

+Phone: (800) 342-5930 or (201) 342-6518

http://www.miclog.com

Internet:

http://www.miclog.com

Circle 1024 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## Render Molecules, Calculate Symmetry

Designed for desktop visualization and publishing, SymApps ($499) is a 3-D molecular rendering program for Windows 95 and NT that can calculate symmetry point groups and display the symmetry elements on-screen. You can calculate point groups over a range of tolerances to identify distortions in molecular coordinates and calculate character tables for symmetry point groups.

Contact: SoftShell International, Grand Junction, CO

Phone: (970) 242-7502

http://www.softshell.com

Internet:

http://www.softshell.com

Circle 1025 on Inquiry Card.

## 3-D Symmetry

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## Notebook Surge Protector

The SurgeArrest notebook protector ($29.95) offers three telephone jacks -- one phone in and two modem/fax lines -- and a 6-foot telephone cord. A thermal fuse disconnects the AC line if there is a sustained overvoltage.

Contact: American Power Conversion, West Kingston, RI

+Phone: (800) 877-4080 or (401) 789-5735

http://www.apcc.com

Internet:

http://www.apcc.com

Circle 1031 on Inquiry Card.

## SurgeArrest Stops Spikes Cold

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## Net Link Internet Device

Sega Saturn Net Link ($199.99), a 28.8-Kbps modem and browser peripheral for the Sega Saturn, brings the Internet to your TV for networked gaming, e-mail, on-line chats, and Web connections. The modem plugs into the cartridge slot on the Sega Saturn, and the package has CD-ROM-based HTML 2.0-compatible Web-browser software developed specifically for the NTSC display standard.

Contact: Sega of America, Inc., Redwood City, CA

+Phone: (800) 872-7342 or (415) 508-2800

http://www.sega.com

Internet:

http://www.sega.com

Circle 1032 on Inquiry Card.

## Sega Saturn Net Link

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## Digital-Only PCI Frame Grabber

Designed for digital cameras, the DT3157 Mach frame grabber ($1495) can transfer images in real time to system memory or the display. Compatible with single- and dual-channel digital cameras with image size outputs as high as 4 MB and data transfer rates of up to 40 MBps, the board accepts 8-, 10-, 12-, 14-, and 16-bit digital images.

Contact: Data Translation, Marlboro, MA

+Phone: (800) 525-8528 or (508) 481-3700

http://www.datx.com

Internet:

http://www.datx.com

Circle 1033 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

.PCI-Format SCSI Adapter for PC and Power Mac

Using only a simple jumper to select PC or Power Mac capability, the AdvanSCSI ABP970 PCI Bus Host Adapter ($199) includes a dedicated 50-MHz RISC processor chip with on-board SRAM that relieves the host CPU of I/O tasks through bus-mastering technology. The adapter can obtain data transfer rates of 133 MBps. It comes with Charismac's Anubis Power Mac drivers for hard disk and removable media, and Charismac's CD-ROM and recordable CD device drivers.

Contact: AdvanSys, Inc., San Jose, CA

+Phone: (800) 525-7443 or (408) 383-9400

http://www.advansys.com

Internet:

http://www.advansys.com

Circle 1034 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## Improve Processor Speeds

Three motherboards improve the processor speeds and performance of desktop systems in CAD/CAM and multimedia applications. Compatible with Intel Pentium and Cyrix CPUs, the P55TU ($479) can support system speeds of up to 200 MHz and features Intel's 430HX chip set and the Adaptec Ultra Wide SCSI controller. The P55TU is also SCSI RAID bus slot-ready, so you can add RAID functionality to your system, supporting RAID levels 0, 1, and 5. The P55TV ($369) and P55TVS ($399) provide most of the same features as the P55TU, but, instead, they are equipped with the Intel 430VX chip set and an Ultra SCSI controller.

Contact: Quick Technology Corp., Tustin, CA

Phone: (714) 258-4500

E-Mail: quick8@ix.netcom

Circle 1035 on Inquiry Card.

## Three Mothers Perform

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## Champagne Graphics at Beer Prices

Mark Schlack

PC graphics are entering a new era. For the price of almost any of yesterday's vanilla PCI graphics boards, today you can get swift 2-D graphics, impressive 3-D effects, and smooth video.

Engineers, stay calm. The Mystique won't fit the bill for a lot of CAD-type work, since it stops at a resolution of 1280 by 1024 pixels. Similarly, if you're a graphic artist who needs 3-D graphics with 32-bit color at the highest resolutions, look elsewhere.

However, more mainstream computer users will benefit from this 64-bit board's MGA-1064SG processor and fast memory. MPEG software decoding performance is very smooth. I ran the Mystique, with late beta drivers, through NSTL's Imark video suite, and it dropped no frames in any of the video tests. As for 3-D, whether the application is a game, training, or a simulation, results will be impressive. A peek at upcoming games based on Microsoft's Direct3D reveals that features such as perspective-correct texture mapping and shading add a great deal of realism to animated scenes.

While beta drivers prevented me from making accurate comparisons with Matrox's older MGA Millennium line, I expect the Mystique to outperform it and most other midpriced graphics boards (including some 128-bit ones) with previous-generation chips.

## Product Information

Mystique..............................$199 with 2 MB of SGRAM

......................................$279 with 4 MB

Matrox Graphics, Inc.

Dorval, Quebec, Canada

+Phone: (800) 810-2550 or (514) 969-6300

Fax: (514) 969-6363

http://www.matrox.com/mga

Internet:

http://www.matrox.com/mga

Circle 1030 on Inquiry Card.

## Graphics Mystique

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## Wireless Infrared Token Ring Adapter

Now, you can connect your portable PC to Token Ring networks using JetEye Net Plus ($719). The adapter supports IrDA data transfer standards of up to 4 Mbps; supports IPX, TCP/IP, and NetBEUI; and allows you to roam between Token Ring and Ethernet networks without reconfiguring your portable.

Contact: Extended Systems, Boise, ID

+Phone: (800) 235-7576 or (208) 322-7800

http://www.extendsys.com

Internet:

http://www.extendsys.com

Circle 1036 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## 100Base-TX LAN PC Card

Meeting the 32-bit CardBus PC Card standard, the Network Flyer 100 ($329) is eight times faster than 10Base-T mode. The Ethernet PC Card offers 10Base-T and 100Base-TX LAN solutions and is optimized for low power consumption. The LAN Adapter PC Card comes with ODI and NDIS drivers, allowing for fast connections to popular NOSes.

Contact: TDK Systems, Nevada City, CA

+Phone: (800) 999-4835 or (916) 478-8421

E-Mail: tdkpr@tsd.ssi1.com

Circle 1038 on Inquiry Card.

## Meet the Bus

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

"10Base-T-to-100Base-T LAN Bridge

Single-port bridge users can connect their 10Base-T-only devices to Fast Ethernet LANs. The BlueStreak Fast EtherPrint 10/100 (about $395) offers plug-and-play functionality requiring no software setup or hardware configuration, protocol-independent bridging from 10- to 100-Mbps Ethernet, an RJ-45 jack for 100Base-T and 10Base-T connections, a reset switch, and diagnostic LEDs for link, transmit, and receive.

Contact: Dayna Communications, Inc., Salt Lake City, UT

+Phone: (800) 531-0600 or (801) 269-7200

http://www.dayna.com

Internet:

http://www.dayna.com

Circle 1037 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## Personal Fax Server

Consisting of an external fax/modem card and a memory chip set, which comes with 512 KB of RAM (expandable to 4.2 MB), 3D FaxPal ($169) captures faxes from a telephone line and stores them (up to 20 faxed pages) for later retrieval from a PC. You can transmit faxes at 14.4 Kbps and receive them at 9.6 Kbps. You can convert a fax machine into a printer and scanner.

Contact: InfoImaging Technologies, Inc., Palo Alto, CA

+Phone: (800) 966-1140 or (415) 960-0100

http://www.infoimaging.com

Internet:

http://www.infoimaging.com

Circle 1039 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## Power Protection for Workstations

Now, you can combat hardware damage caused by surges and data loss from brownouts and blackouts. The Back-UPS Office ($179) multipath power device offers six outlets with multistage surge suppression and EMI/RFI filtering, phone-line protection for Internet users, network data-line protection for workstations, and battery backup for CPUs.

Contact: American Power Conversion, West Kingston, RI

+Phone: (800) 800-4272 or (401) 789-5735

http://www.apcc.com

Internet:

http://www.apcc.com

Circle 1040 on Inquiry Card.

!Back-UPS Office Belongs Up Front

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## 19.2-Kbps Wireless Modem

Designed with direct-sequence spread-spectrum technology, the Hopper DS wireless modem (from $980) can transmit and receive data at speeds of up to 19.2 Kbps at distances exceeding 6 miles. You can connect the modem to most PCs, programmable logic controllers, or remote terminal units. You can also use the Hopper DS for point-to-multipoint applications.

Contact: Wi-LAN, Inc., Calgary, Alberta, Canada

Phone: (403) 273-9133

http://www.wi-lan.com/wilan

Internet:

http://www.wi-lan.com/wilan

Circle 1041 on Inquiry Card.

## Cover the Miles Quickly with a Hopper

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

)Windows 3.1-Based Multiuser File Server

A combination of hardware and software, Centralan (including four monitors, under $7000) lets up to 16 users share a single PC with a 166-MHz Pentium processor, 32 MB of EDO memory (expandable to 192 MB), a multi-VGA adapter, a 2-GB Fast/Wide SCSI-2 hard drive, an eight-speed IDE CD-ROM drive, three internal and four external drive bays, and two 32-bit PCI and five 16-bit ISA expansion slots. Each user needs only a keyboard, mouse, and SVGA monitor at their desktops, which plug into a junction box. Centralan's four-user base system comes installed with a LAN-ready Intel EtherExpress 10/100B network adapter and a 33.6-Kbps modem. With a separate PC, remote users can access data and run applications the same way they would while in the office.

Contact: AST Research, Inc., Irvine, CA

+Phone: (800) 876-4278 or (714) 727-4141

http://www.ast.com

Internet:

http://www.ast.com

Circle 1042 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## 230-MB MO Drive

A battery-powered 3-1/2-inch 230-MB MO drive, Fujitsu's DynaMO 230 Portable PC Card Drive (from $499) comes with a Type II connector that provides a data transfer rate of up to 1.6 MBps. Compatible with PCs and Macs, the drive has a seek time of less than 65 ms, a rotational speed of 2700 rpm, and a 128-KB cache.

Contact: Fujitsu Computer Products of America, Inc., San Jose, CA

+Phone: (800) 626-4686 or (708) 432-6333

http://www.fcpa.com

Internet:

http://www.fcpa.com

Circle 1043 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## DLT Libraries

The entry-level, scalable Q2*15 DLT system can store more than 1 TB of data with 15 cartridges per library storage module. Available in rack-mount, desktop, and deskside configurations, the Q2*15 (with two DLT 4000 drives, $22,000) features one or two DLT 2000XT, 4000, or 7000 drives; an integrated bar code reader; and a removable 10-cartridge magazine. The system supports leading software backup and HSM applications running under Novell NetWare, Windows NT, and Unix.

Contact: Breece Hill Technologies, Inc., Boulder, CO

+Phone: (800) 941-0550 or (303) 449-2673

http://www.breecehill.com

Internet:

http://www.breecehill.com

Circle 1044 on Inquiry Card.

!An Upwardly Scalable DLT Library

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## 120-/133-MHz Pentium Notebooks

The TravelMate 6020 (about $4199) and 6030 (about $4999) incorporate Intel 120- and 133-MHz Pentium processors, 256 KB of L2 cache memory, 8 and 16 MB of EDO memory, ZPV technology, a six-speed CD-ROM drive, 16-bit full-duplex audio, a 28.8-Kbps modem, and a removable hard drive (1.08 GB on the 6020 and 1.35 GB on the 6030). The TravelMate 6020 comes with an 11.3-inch TFT display, and the TravelMate 6030 comes with a 12.1-inch 800- by 600-pixel active-matrix SVGA TFT display.

Contact: Texas Instruments, Inc., Temple, TX

+Phone: (800) 848-3927 or (817) 774-6001

http://www.ti.com

Internet:

http://www.ti.com

Circle 1045 on Inquiry Card.

## A Great Traveling Companion

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

(Multimedia Notebook Goes 5 to 10 Hours

Weighing 7 pounds, the AcerNote Nuovo (about $3499 to $3999) features an Intel 133-MHz Pentium processor; 16 MB of EDO memory, upgradable to 64 MB; 256 KB of second-level cache memory; 2 MB of EDO video memory; a 1.2-GB EIDE hard drive; a 128-bit NeoMagic graphics accelerator, which provides 16-million-color, full-motion video playback and full-color MPEG at 32 fps; an Ethernet controller with an RJ-45 jack; an 11.8-inch active-matrix or 11.3-inch dual-scan screen; a microphone; a 16-bit stereo audio system; a 28.8-Kbps fax/data modem with DSVD; a touchpad; and a palm rest. The Nuovo also offers two Type II/one Type III PC Card slots and a module bay for a six-speed CD-ROM drive or floppy drive. When you combine it with the AcerDock III, the notebook offers warm-docking connectivity to peripherals.

Contact: Acer America Corp., San Jose, CA

+Phone: (800) 733-2237 or (408) 432-6200

http://www.acer.com/acc/

Internet:

http://www.acer.com/acc/

Circle 1051 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## Three Pentium Notebooks

The Monte Carlo (about $3199 to $5199) comes with a 100-, 120-, or 133-MHz Pentium processor; a 12.1- or 11.3-inch SVGA active-matrix color display with a resolution of 800 by 600 pixels; 8 or 16 MB of RAM, expandable to 40 or 48 MB; an 810-MB or 1-GB hard drive; a removable 3-1/2-inch floppy drive; a six-speed CD-ROM drive; stereo speakers and a microphone; MPEG-1 video-acceleration support; and an ErgoTrac pointing device. Besides bridge-battery technology for warm-swapping of batteries, the Milan (about $2199 to $4599) features the same Pentium options, RAM, and hard drive as the Monte Carlo, with a 10.4-inch SVGA active-matrix or dual-scan color display or an 11.3-inch SVGA active-matrix color display. The Montego ($3199) offers a removable 3-1/2-inch floppy drive, plus a 100-MHz Pentium processor; a 10.4-inch SVGA active-matrix color display; 8 MB of RAM, expandable to 40 MB; and a 1-GB hard drive.

Contact: Fujitsu PC Corp., Milpitas, CA

+Phone: (888) 466-8434 or (408) 935-8800

http://www.fujitsu-pc.com

Internet:

http://www.fujitsu-pc.com

Circle 1046 on Inquiry Card.

## Three Pentium Notebooks Are We

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

#RADical Advancements from Clarion

A RAD environment, Clarion for Windows 2.0 includes OOP enhancements to the Clarion 4GL language, OLE/OCX support, and new options for customizing application appearance. Professional Edition, $599; Enterprise Edition, $1499; Standard Edition, $199.

Contact: TopSpeed Corp., Pompano Beach, FL

+Phone: (800) 354-5444 or (954) 785-4555

http://www.topspeed.com

Internet:

http://www.topspeed.com

Circle 1026 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## HiJaak Gets More Professional

HiJaak Pro 4.0 supports common 3-D graphics, PostScript, and CAD formats; supports graphics file operations, such as viewing, printing, and converting, from the shortcut menu; and integrates with the Windows 95 shell to expand graphics handling in the OS. About $279.

Contact: Quarterdeck Corp., Marina del Rey, CA

+Phone: (800) 282-0866 or (310) 309-3700

http://www.quarterdeck.com/

Internet:

http://www.quarterdeck.com/

Circle 1027 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

'BeyondMail Eases Information Handling

BeyondMail 3.0 Internet Edition introduces directory services via a four-tier address book: personal, workgroup, enterprise, and global; multimedia messaging; information handling with configurable folders; remote-access enhancements; and messaging-administration enhancements. Call for prices.

Contact: Coordinate.com, Waltham, MA

+Phone: (800) 567-8818 or (617) 398-7900

http://www.coordinate.com

Internet:

http://www.coordinate.com

Circle 1028 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## What's New

## What's New

## FireWall-1 2.1 Enhancements

Enhancements in FireWall-1 2.1 include Internet and intranet gateway support for Windows NT, management console support for NT and 95, integrated support for FireWall-1 SecuRemote client-encryption software on Windows 95 laptops and desktops, and extended application support for RealAudio, VDOLive, Internet Phone, and Oracle SQL*Net. For up to 50 nodes, $4990; for up to 250 nodes, $9990; for unlimited nodes, $18,900.

Contact: CheckPoint Software Technologies, Ltd., Redwood City, CA

+Phone: (800) 429-4391 or (415) 562-0400

http://www.checkpoint.com

Internet:

http://www.checkpoint.com

Circle 1029 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## Codetalk

## Codetalk

## Beyond the Bouncing Heads

5Use JFactory to quickly assemble Java applications.

Rick Grehan

The quantity of new Java products that arrives daily at BYTE is unnerving. The number of new Java books alone is such that I'm pretty sure the delivery people will soon be unloading them with snow shovels.

Consequently, the Java signal-to-noise ratio is very low; the job of sifting wheat from chaff is difficult. Many of us are still working through the source code for the bouncing-heads demo. There's nothing wrong with that; I'm guilty of it myself. You have to start somewhere.

http://www.roguewave.com

But once you've got those heads figured out, you should turn your attention to a pair of seriously good Java program jump-starters from Rogue Wave Software. A purveyor of C++ class libraries, Rogue Wave now also offers JFactory, a user-interface development environment for Java. (At the time of this writing, a beta version of JFactory with a 30-day usage limit was available for downloading from

http://www.roguewave.com

.. Be warned, however; the file is over 3 MB.)

Factory looks with longing eyes toward Visual Basic (VB). The act of creating an application (or applet) within JFactory proceeds along the same lines as building a VB program. You start out guided by what amounts to a wizard, which builds for you an empty window (or form, or frame, whichever term you feel comfortable using). A tool palette appears, and, by selecting items from that palette, you populate the window with scroll bars, text boxes, buttons, and other elements. When you click on a visual object, the object-manager window opens, revealing that object's associated properties and events. Sound familiar? If you're a VB programmer, it should.

All the while, JFactory is conjuring source code, waiting for you to pick the Generate menu selection so that it can pour that source into a file for you. And in the resourceless world of Java, the amount of source code that must be produced (and ultimately executed) to create those visual objects will amaze you. Hence, JFactory does you a big favor.

Iterative development is particularly important in user-interface design. You want to be able to add a toolbar and see immediately what it looks like in the final application or be able to associate a series of buttons with the opening of various dialog boxes and quickly confirm that each button leads to the intended dialog box. JFactory permits code-and-test work with its Test Interface capability. Once you've got a rudimentary user interface clicked-and-dragged together, you then select Test Interface from the Project menu, and JFactory simulates the action of the interface.

This simulation goes quite far. For example, JFactory's image-loop visual object accepts as properties the path name to a starting GIF file and the number of images in the loop. If the first GIF file's name is PICT1.GIF, and if the number of images selected is four, then the image-loop object knows to load the series of files PICT1.GIF, PICT2.GIF, PICT3.GIF, and PICT4.GIF. Once the image-loop object is instantiated and added as a member of a window's or dialog box's components, it immediately begins playing those images as frames in a moving picture. JFactory's Test Interface selection provides full image-loop automation.

Ironically, the simulation of an image loop goes faster than the actual execution of that same loop in Java. And thus another little dark cloud forms over the Java-performance landscape.

Also available from Rogue Wave is a suite of three Java packages: Jtools, Jwidgets, and Jmoney. Collectively, these packages are called JLibraries. (A subset of Jwidgets is included with JFactory.) Jtools is a collection of well-reasoned interfaces and classes. These include container classes for objects such as binary trees, B-trees, bags, collections, and the like. It also includes a regular-expression-handling class, as well as a set of classes that format text and numerics for output. (The latter is a real blessing if you have grown weary of coping with the paucity of System.out.println().)

http://www.javasoft.com

Factory is available for Windows NT and 95. Both JFactory and Jtools need at least the version 1.0.2 release of the Java developer's kit (available from

http://www.javasoft.com

). JLibraries and a single-user license for JFactory each cost $195. The individual packages within JLibraries cost $99 each. Rogue Wave also provides annual support and upgrade contracts, as well as site licenses.

## Where To Find

Rogue Wave Software

Phone: (541) 754-3010

http://www.roguewave.com

Internet:

http://www.roguewave.com

mailto:"rick_g@bix.com"

Rick Grehan is a senior technical editor for BYTE reviews. You can reach him by sending e-mail to

rick_g@bix.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International Bits

## International Bits

## Your Complete Inbox

The latest versions of fax software integrate with corporate messaging systems.

Rainer Mauth

A new round of fax-server software, from several European vendors, features inbound routing via ISDN, scheduling, least-cost routing, and advanced cost management. The programs can also integrate with standard messaging systems or provide a comprehensive communications platform by themselves.

Products include Equisys's (London) Zetafax, Fenestrae's (Leidschendam, The Netherlands) Faxination, and Digitronic's (Hamburg, Germany) Faxit. The latest versions of all these programs are tightly integrated with Microsoft Exchange. Thus, a user of any of these systems can send and receive faxes by using his or her familiar e-mail client and address list. A key feature of these systems is drag-and-drop support of attachments. With Faxination, for example, you can attach Word, Excel, and RTF files, while Faxit supports a list of 40 file formats as attachments.

However, "a fax gateway for Exchange is only the first step," says Wim de Koning, the president and CEO of Fenestrae. "We're also currently working on a consistent gateway architecture for Electronic Data Interchange [EDI], X.400, GSM Short Message Service [SMS], and Telex." Koning says that the company's Interpersonal Messaging Server will extend the Faxination kernel and also include end-to-end addressing; access security, such as logging, tracking, and support for firewalls; and connectivity to major business applications, such as SAP's R/3.

Tobit

(Ahaus, Germany) is taking another approach: turning its NetWare-based fax server, FaxWare, into a universal communications platform. Code-named David, the system has a central multimedia archive for incoming faxes, e-mail, and other documents that can be accessed via LAN, fax, phone, or Web. This concept lets a company's employees access all kinds of personal documents with a variety of media from anywhere in the world. Tobit also plans to support paging services, SMS, and text-to-speech output. Says Dieter van Acken, marketing manager at Tobit: "Universal inboxes like David will soon be the core of many virtual offices."

## Fax or E-Mail?

Four-fifths of the U.K. businesses polled would rather give up their

?e-mail than their fax systems. The reason: the ubiquity of fax

Fmachines. Only 42 percent of the small companies surveyed use e-mail,

=while 79 percent of large ones do, says market-research firm

International Data Corp. (IDC).

## Public-In-Box

Tobit's fax-server technology is turning into a universal message inbox.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International Bits

## International Bits

## Witness for the Prosecution

Computers are serious business tools, but sometimes they also support business delinquency. So, how do you go about questioning a computer? Authentec, a U.K. data-recovery company, now has an answer: Do it at the sector level of the BIOS, and don't change a single bit.

Authentec has developed a portable file server that allows investigating authorities to make a replica, or image, of a target computer system at the site of an alleged crime. Called

FlightServer

, the system runs NetWare 3.12 and copies a hard disk, sector by sector, without interfering with the target system. Once this image has been taken, it can then be investigated at the prosecutor's office using Authentec's forensic software package, which indexes all a hard disk's sectors, including lost chains, and automatically sets up libraries of words relevant to the case.

The company says that the biggest problem for prosecutors of computer crime is not the technical reliability of the FlightServer system but the computer ignorance of most judges. Despite today's sophisticated digital image-manipulation techniques, judges still trust a photo more than a sector-by-sector image of a hard disk.

## The Inspector at Work

Inspector FlightServer at work.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International Bits

## International Bits

## Demand Soars for Big Screens

Asian firms predict a huge demand for wall-mounted plasma displays.

Mark LaPedus

The demand for large-screen color plasma display panels (PDPs) is now heating up in Asia. Japan's

Fujitsu

, NEC, Sharp, and others are introducing large-screen PDPs, while Korea's Samsung is reportedly making large investments in the arena.

NEC is building a new PDP factory in Kagoshima, with production slated to begin in April 1998. Production quantities are expected to reach 30,000 units per month, NEC says. The company has already completed the development of 33- and 42-inch PDPs and has plans to ship these products in August and December, respectively.

PDPs are one of the key display types for next-generation multimedia applications, such as wall-mounted TV screens. PDP technology has been around for a while, but recent advances in the technology have made the products more cost-effective to produce, NEC officials say. The company estimates that the PDP market will grow from 3 million units, or $2.4 billion, in the year 2000 to 11 million units, or about $7 billion, by 2002.

## Displays Go Wall-Size

1Fujitsu's new 42-inch-wide color-plasma display.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International Bits

## International Bits

(Korea to Install New CDMA Phone System

Mark LaPedus

During the next two years, Korea will deploy its initial Personal Communication Services (PCS), a wireless cellular system that provides greater capacities than traditional analog phones. But Korea is not going with the de facto standard in digital cellular -- Global System for Mobile Communications, or GSM. Instead, the country will deploy the code division multiple access (

CDMA

[) system, a technology that operates at a frequency of 1.9 GHz. (GSM operates at 900 MHz.)

CDMA modulates the signal from each user by using a digital code that spreads the spectrum across a wide bandwidth. CDMA proponents, such as Qualcomm (San Diego, CA), claim the technology offers better voice quality and less multipath resistance than competitive digital cellular systems.

In Korea, Shinsegi Telecom last spring began providing PCS services based on CDMA technology in Seoul and Taejon, joining Korea Mobile Telecom in the business. Meanwhile, the Korean government recently issued similar licenses to LG Telecom, Hansol Paper, and the state-run Korea Telecom.

As Korea moves from analog to digital cellular services, the demand for CDMA-based phones in the country will jump from 402,000 units in 1996 to 1.247 million in 1998, according to figures from Korea Mobile Telecom. Meanwhile, in the U.S., the demand for CDMA-based telephones is expected to increase from 400,000 units to 2.245 million, according to market-research firm BIS.

To support CDMA-based technology, Korea will deploy land-based base-station transceivers. Samsung recently began mass production of CDMA-based hand-held phones in Korea. Samsung, which will reach an annual production of 1.5 million units by 1997, will sell its CDMA phones in the local market, in the U.S., and in other nations that are backing the technology.

## Korean CDMA Phones

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International Bits

## International Bits

## Psion Clones Coming

-Pegasus-based PDAs are also on the horizon.

Jim Nagel

Psion, the U.K.-based computer company that holds a third of the world market for palmtop devices, is currently licensing its ROM-based OS and applications to other manufacturers. Psion hopes that the move will grow the market and foster the development of new smart phones, mobile Web browsers, and intelligent terminals that will capitalize on the convergence of computer and telecommunications technologies.

The first licensees and products based on Psion's EPOC platform will be announced next year. Company officials say that there will be no reference design, like the one discussed for the Web PC, because the target systems can differ so widely (e.g., a feature phone versus a complete PDA).

Psion's decision to license its OS may be partially motivated by the slew of new PDAs expected to be released later this year. These new systems will be built around Pegasus, a new Windows-compatible OS for PDAs from Microsoft. But Stephen Randall, Psion's vice president of licensing, says Pegasus-based products are not a threat because "through our licensing, the Psion platform will move into many highly customized solutions." He adds that the desktop companion products that Pegasus is intended for are not the target market of Psion licensees.

The first new Psion model to be made available to palmtop manufacturers will succeed the popular Psion 3a series. It will be constructed around the highly integrated ARM7100 processor (fabricated by Cirrus Logic [Fremont, CA]), which is basically a complete PDA on a chip. Other systems will also deploy the powerful StrongARM chip, which has the ability to bring speech recognition to the next generation of Psion computers.

## Psion's A-Comin'

Psion's popular 3a model.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International Features

## International Features

## You Said What?

Machine translation tools are far from perfect, but they can save you serious money.

Peter Jaapaniemi and Peter Hofland

Think globally, act locally. That's a mantra international organizations chant constantly. But at a price. In large corporations, the total costs of translating things such as marketing materials and documentation can add up to several million dollars a year. IBM, for example, spent more than $100 million last year to translate manuals from English into 25 other languages.

The problem is especially acute for European corporations, which generally provide documents in at least three or four of the European Union's nine official languages. What these companies are looking for are sophisticated, multilingual translation tools that can help reduce these costs.

Machine translation (MT), the use of computers to automate translation, is one of the computer industry's oldest areas of interest -- and one of its most frustrating. Computer scientists and linguists have been working on MT techniques for decades. The results are disappointing: Perfect translation without human intervention is still a dream that will not be realized for the next 10 years or so.

MT has come a long way from simple word-to-word translation. Products can now deduce subtle contextual differences in languages. But even the most sophisticated systems on the market are far from automatic. They are, however, useful support tools for professional human translators. Some systems are based on huge dictionaries that translators use to more efficiently look up words and phrases. Other systems take a first look at a document and produce a rough draft that is then edited by a human translator. The best of these tools can deliver about 80 percent accuracy, experts reckon.

Real MT breakthroughs are rare and developments are slow because of the complexity and continuous progression of language. To be truly effective, a translation system must take into account the formation and use of words, syntax, and semantics. Furthermore, it must be able to recognize colloquial phrases, acronyms, and contractions -- not to mention incorrect grammar and misspelled words. That's why many vendors of language processing tools are now changing strategy. Rather than trying to keep up with constant additions to their products, they are making them customizable, enabling users to update dictionaries and also extend context sensitivity.

Globalink's new generation of technology, dubbed Barcelona, allows translators -- rather than programmers -- to include their own rules of how words should translate in a certain context. That means the front-line translator can efficiently deal with new word fields and idioms that might occur in a specific project. Globalink says this new technology will soon incorporate a "wizard" that allows nonexperts to implement rules in a comprehensive high-level language. Other Windows programs will be able to access the Barcelona translation service via OLE Automation or an API.

Another example of a tool that lets users fine-tune the translation process with an expandable context-sensitive dictionary is Logos' Semantha. According to Mark Andrews, a Logos product marketing manager, this new generation of customizable translation tools enables users who systematically track new phrases and idioms to get to a point where they can push a button and generate close-enough translations for internal company documents and other communications.

So how do you keep up with ever-changing contexts and the variety of technical terms that occur in new projects? One answer comes from the Rank Xerox Research Center (RXRC) in Grenoble, France. RXRC's Terminology Extraction Project aims at facilitating the building of dictionaries. It compares translated documents in both the original and the target language and aligns the text sentence by sentence. Then it extracts the multiword expressions and produces a list of paired terms that can be incorporated in a dictionary. In other words, the system automatically detects multiword expressions in the original and the translated documents and puts them in a dictionary. The technology currently works in Dutch, English, German, French, Italian, Spanish, and Portuguese.

A dictionary of 20,000 terms can take 1000 hours to build and cost up to $600,000, RXRC researchers say. With well-bred extraction tools, such costs can to a large extent be eliminated, they say.

The Terminology Extraction Project is part of the Xerox Lexical Development Architecture (XeLDA). This translation framework includes tools that can detect phrases. For example, if you click on the word "sweep" in the phrase "to sweep it under the rug," you don't get the translation of "to sweep,"; you get the translation of the complete phrase. This happens even if the idiom is split up, as in "to sweep that crime under the nearest rug," because the system is designed to detect basic idioms.

Although the XeLDA services are prototypes, RXRC is planning to make these kinds of services commercially available in corporate LAN environments or over the Internet. "In the long term," says Monica Beltrametti, director of the Grenoble RXRC, "we aim to provide our Translation Aid Network Services as general-purpose translation tools to any networked computer user faced with multiple languages at work."

Personal MT

The market for MT tools has traditionally been professional translators in large corporations, international organizations, or governments. However, a new, more casual market for translation tools is emerging. Much of the information being passed around the globe doesn't require the precise translation that a novel or a technical manual might. "There is an increasing need for quick multilingual information scanning," says Ann-Marie Derouault, IBM's worldwide speech and translation marketing executive. "No one would pay a professional translator to translate an e-mail message because a quick translation that gives you a rough idea of its content is all that's required."

New products in this area are nevertheless

context-aware

, and some also use sophisticated syntactical analysis. They integrate with standard word processors and are priced at less than DM 500. Here are some examples:

IBM Europe now offers Windows and OS/2 versions of its host-based translation technology, Personal Translator. This program comes in a basic package with a vocabulary of 160,000 words and 440,000 phrases and in an advanced version with approximately 200,000 words and 550,000 phrases. In Italy this technology is used in Synthema's PeTra English/Italian translation product, which runs under OS/2. And in Germany, IBM has worked with v.Rheinbaben & Busch Electronic Publishing to create a Windows-based German/English version of the Personal Translator technology.

Accent Software offers Accent Duo with Translation, which integrates translation with word processing capabilities. This Windows system is available in English to Spanish, German, French, or Italian versions (it works bidirectionally). The program features a spelling checker and a thesaurus in both languages and lets users translate documents automatically or work interactively.

Logos' Remote Client is a Windows application that lets users dial into a Unix-based translation server. You can choose a multitude of dictionaries for several subjects, then send the job to the server, which returns a translated version. Users can maintain their own translation server or call the Logos corporate server, which costs $.04 per translated word. Logos' goal is to make machine translation available to smaller businesses and freelance translators who can't afford a high-end system.

Another force driving translation technology is on-line chat and communication in newsgroups. CompuServe, for example, offers English/French and English/German translation in some of its help forums. These translations are often very meager, but their value is immediacy, because in the context of a support forum messages can lose their relevance if they are delayed. As a CompuServe manager puts it, "The purpose is to quickly provide translations that otherwise would take hours to understand."

Multilingual translation is also reaching the World Wide Web. Globalink, for example, provides an add-on to Netscape Navigator 2.0 that translates Web sites in Spanish, French, or German into English, and vice versa, at the click of a button. Called Web Translator, the software allows users to translate on-line, or to save pages to be translated off-line, while maintaining the original page's hot links, graphics, and formatting.

The development of multilingual translation tools is key for most companies. Many of these systems support at least three of the main European languages -- English, French, German, and Spanish. However, there is no such thing as a one-size-fits-many translation technology. The experience of developing a translation system that works from language A to language B is in most cases of little help when developing a system for languages C and D. Merely replacing dictionaries is not enough because it does not reflect the grammatical structure or different semantic classes of words.

This famous example illustrates the difficulties of MT. Use any standard translation system to translate the old saying "The spirit is willing but the flesh is weak" to French and then back to English and you will get something like "The alcohol is strong but the meat is weak.

## Where To Find

Accent

Jerusalem, Israel

Phone: +972 2 793 723 243

Fax: +972 2 793 731

E-Mail: normank@accent.co.il

http://www.accentsoft.com

Internet:

http://www.accentsoft.com

Globalink Europe

Bracknell, Berkshire, U.K.

Phone: +44 1344 382111

Fax: +44 1344 382112

http://www.globalink.com

Internet:

http://www.globalink.com

IBM Europe

Paris, France

Phone: +33 16 38 55 77 77

E-Mail: ibmrep@fr.ibm.com

Logos

Eschborn /Ts., Germany

Phone: + 49-61 96-59 03 0

Fax: + 49-61 96-59 03 15

http://www.logos-ca.com

Internet:

http://www.logos-ca.com

$Rank Xerox Research Centre Grenoble

Meylan, France

Phone: +33 76 61 50 76

Fax: +31 76 61 50 99

+v.Rheinbaben & Busch Electronic Publishing

Munich, Germany

Phone: +49 89 723 77 77

Fax: +49 89 723 87 58

## A Subtle Differential

Detecting subtle contextual differences requires fine-tuning of dictionaries and syntactical analysis.

mailto:"100544.307@compuserve.com"

Peter Haapaniemi and Peter Hofland are technology journalists at The Visual Consultancy Corp. in Amsterdam. You can contact them at

100544.307@compuserve.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International Features

## International Features

%Direct Speech-to-Speech Translation

Direct speech-to-speech translation aims to provide translation in real time for applications such as videoconferencing or automatic translation over the telephone. Although this seems like the next step in machine translation, the technology is still not mature enough for commercial products. But researchers persist. Organizations working in this field include the C-Star Consortium and the Interactive Systems Laboratory (ISL), a cooperative venture of the University of Karlsruhe in Germany and Carnegie Mellon University in the U.S.

C-Star includes companies and academic institutions from France, Germany, Italy, Japan, India, Korea, the U.K., and the U.S. In 1993, C-Star demonstrated automatic interpretation over the phone in a series of bilingual experiments. That system required the speaker to talk very clearly and be grammatically correct, which humans normally don't do. C-Star II research aims to reduce such restrictions and create more robust interpreting systems that can recognize ordinary spontaneous speech, translate it, and turn it into synthesized speech. C-Star's goal is "multilingual speech-to-speech translation" in real applications by 1999.

The ISL's Janus speech-to-speech project deals with learning and handling new vocabularies in predefined situations, such as scheduling of appointments. It supports English, German, Spanish, Japanese, and Korean. The collaboration has developed a laptop-based speech translator that handles spontaneous, continuous, speaker-independent translation in limited domains. Translation output can be presented as synthesized speech or as text on screen or transparent goggles.

ISL has also developed a translating videophone station that allows one person to hear another's original voice and receive translations as subtitles or synthesized speech. When the speaker on one end makes a statement, the system returns a paraphrased version for verification. As soon as the speaker has verified it, the system translates the message and sends it to the recipient. Although the translation is not instantaneous, it allows for adequate straightforward communication.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International Features

## International Features

"Europe's Internet Infrastructure

The service you get from European ISPs depends on more than bandwidth.

Valerie Thompson

The key to good response times on today's Internet is your Internet service provider's IP experience and the line capacity and throughput rates the ISP offers you. But capacity is not all. When traffic moves out of the local hop into the Internet backbone, it's the ISP's connectivity to the backbone that counts.

Today more than 600 ISPs rival for customers in Europe. Half of these providers have been on the scene for less than a year. To the home or small-office user, retail ISPs may more or less look the same and differ just by pricing structure. However, for corporate users, the quality of service and the overall data throughput vary greatly.

Don't think that just because an ISP is small it cannot offer good performance. One of the neat things about the Net is that a small ISP with a 64-Kbps line to the Internet can still provide speedy response because most of its subscribers are "low-power" users. A big ISP might have a 2-Mbps line to the Internet, but it may also have a lot of subscribers plus a few real power users who clog the link to the backbone. That's why you should look beyond just the links.

At its most basic level an ISP is nothing more than a rack of modems or ISDN boards, a server, a router, and some communications and billing software. The ISP typically connects all this equipment to the Internet with a leased line. That link into the Internet is crucial to the service the ISP's customers are going to get.

http://www.marktplatz.ch/eurointernet

The connection to the Internet might involve a hop (routing point) to a regional IS wholesaler. From that point the ISP links to one of the European Internet backbones. Knowing how ISPs are connected gives you an idea of the performance you can expect. That's where CyberRoadMaps, such as the one provided by market researcher EuroInternet, can help (for more information, see

%http://www.marktplatz.ch/eurointernet

). These maps show how more than 2000 ISPs in various countries in Europe, as well as providers in North America, Japan, and Australia, connect to Internet backbones.

World Wide Wait

The ad hoc nature of the Internet more than often converts the World Wide Web into the World Wide Wait. Data packets sometimes travel around the world once or twice before they find their destination. This may even be the case if the server you need to locate is in a neighboring city.

This situation is prevalent on both sides of the Atlantic; however, the European Internet backbone is by far not as efficient as the North American. "Europe has 20 to 30 percent of the Internet's traffic, but it produces 80 percent of people's [Internet] nightmares," as a manager of a European ISP recently put it.

The main bottlenecks in the European portion of the Net, according to a recent analysis done by EuroInternet, occur at three points: country-to-country, backbone-to-backbone, and Europe-to-U.S. links. At these key points, insufficient bandwidth slows down the traffic. One reason for this unfortunate situation is the high cost of international and transatlantic leased lines in Europe, further aggravated by fluctuating and unfair prices between the U.S. and Europe. In many cases, European backbone providers have to pay an additional fee to connect to the States, whereas U.S. providers can link to the European backbone for free.

Unlike the U.S. portion of the Internet, where tariffs are based only on distance, European backbone providers have to deal with prohibitive international tariffs whenever the network crosses the border from one country to another. Steep prices of leased lines supplied by Europe's PTTs are the main culprit. "We remain heavily penalized by monopoly tariffs for leased lines as well as ATM [asynchronous transfer mode] connections," says Brian Carpenter, group leader of Communications Systems at the CERN research center in Geneva, Switzerland, and chair of the Internet Architecture board.

Backbone Bottlenecks

After 1998, tariffs for leased lines will drop as a result of increased competition fostered by a more liberalized European telecommunications market. But one Internet analyst says the transatlantic and cross-border links are not being used optimally. "International backbone providers are often reluctant to interconnect because of competitive pressures," says Jim Romaguera, principal consultant at EuroInternet. "They fear that smaller ISPs could be able to offer better services for lower prices to their customer base."

It is the nature of today's Internet that two ISPs in the same country often are not connected to each other. The result: Data sent from one ISP to another in the same region travels via the U.S. These expensive Europe/U.S. links carry traffic that actually should remain in Europe.

http://www.isi.edu:80/div7/ra/eu.html

What is required is that more ISPs connect via commercial Internet exchanges (CIXes) to relieve the intercontinental traffic jams. CIXes were originally set up to free commercial service providers from the policies that were restricting use of the Internet to educational and research purposes only. The development of CIX points is crucial to the European Internet infrastructure because it will avoid routing data over the already congested and expensive transatlantic links. The six major European CIX points today are in Helsinki, Paris, Amsterdam, Geneva (CERN), London, and Stockholm (see

%http://www.isi.edu:80/div7/ra/eu.html

The original idea behind CIXes was simple: Commercial ISPs would agree to route traffic over each other's networks without restriction or additional charges. However, because CIXes deploy sophisticated communications protocols and global guidelines, some CIXes don't accept interconnection with smaller commercial ISPs.

Another way to release pressure on the transatlantic links is as old as the Internet itself: caching of popular sites locally to relieve traffic on the remote server and the network. This method was fine when research and cooperation were the spirit of the Net, but now that business is being done there, it creates a new set of problems. Is copyright being violated by ISPs who choose to cache sites locally? What about all the user information the site owner gets when people visit the site? If pages are stored elsewhere, those valuable statistics will not be available to owners of the site.

Trace the Route

For its report "The Global Internet -- Featuring CyberRoadMaps," EuroInternet surveyed data packets traveling on the Internet and calculated the number of different ISP subnetworks they visited on their odyssey. EuroInternet consultant Romaguera says this is the best way to locate bottlenecks and measure the performance of ISPs.

The most recent analysis from EuroInternet identifies nine Pan-European backbone providers and another nine organizations for the U.S. backbone. The regional and national providers connect to the backbone and act as Internet wholesalers. Some also offer retail services. Local or retail ISPs connect with one or two lines to the regional providers.

An example of an Internet wholesaler is the

SWITCH network

in Zurich. It connects more than 100 sites consisting of universities, engineering schools, R&D institutions, companies, and regional ISPs. A leased-line network links all organizations to other providers (EUnet, Unisource Business Networks) and to backbone networks (EuropaNET, EBONE). Two T1 links connect directly to the ANS network in New York.

http://www.switch.ch/switch/lan/SWITCHlan-map.html

SWITCH publishes statistics that show the link utilization at the three key points of the network (see

2http://www.switch.ch/switch/lan/SWITCHlan-map.html

v). For the customer this is an excellent service because it shows exactly the performance the ISP is able to provide.

To cope with the increasing demand for bandwidth, many backbone providers are developing a new infrastructure. Unisource Internet Access Services, one of the European backbone providers, for example, confirmed the establishment of a premium service network with hubs in Amsterdam, Stockholm, London, Zurich, and Madrid, and with interconnections at all the CIX points in Europe. IBM and EUnet are currently at work on similar projects.

As the Internet continues to expand, peer-to-peer networks are expanding as well. These private networks offer added value such as roaming agreements or data-interchange services to large businesses. But it's important to remember that the public access an ISP can offer is directly tied to its amount of bandwidth and type of connectivity to the global backbone. When it comes to these factors, Europe's local ISPs are far from equal.

## Where To Find

EuroInternet

Bern, Switzerland

Phone: +41 31 998 4331

Fax: +41 31 998 4103

!E-Mail: eurointernet@thenet.ch

http://www.marktplatz.ch/eurointernet

Internet:

%http://www.marktplatz.ch/eurointernet

## How to Choose an ISP in Europe

It's not just price that makes for a quality Internet service

,provider. To help find the appropriate ISP:

# Ask for network utilization data.

3 Check the ISP's connectivity to the backbone and

+ watch the number of hops to the backbone.

- Ask for the number of users per modem line.

0 Evaluate the competence of the help-desk staff

and the cost of support.

0 Look for roaming services in other regions and

countries.

## The SWITCH Network

|Valerie Thompson, based in Zurich, tracks telecommunications developments. You can reach her at 100271.257 @compuserve.com.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International Features

## International Features

## Types of ISPs in Europe

Backbone providers offer international, intracontinental, and intercontinental networks to other ISPs. Typically they have high-speed links and hubbed networks. In Europe these backbone providers are:

http://www.eu.net

Unet (

http://www.eu.net

http://www.EBONE.net

EBONE (

http://www.EBONE.net

http://www.pipex.net

Pipex-UUNET (

http://www.pipex.net

http://www.dante.net

EuropaNET (

http://www.dante.net

http://www.global_one.net

Sprint (

http://www.global_one.net

http://www.nordu.net

NORDunet (

http://www.nordu.net

http://www.inet.fi/telecom

http://www.tele.fi/

Telecom Finland (

http://www.inet.fi/telecom

http://www.tele.fi/

http://www.unisource.nl

Unisource (

http://www.unisource.nl

http://www.francetelecom.fr

France Telecom (

http://www.francetelecom.fr

National or regional ISPs resell Internet connectivity to local ISPs and act as retail ISPs themselves. They often have multiple links to the Internet.

Local or retail ISPs are small companies with one or two lines to the Internet. This category includes proprietary on-line service providers with Internet gateways, such as CompuServe or AOL/Bertelsmann Online.

Commercial Internet exchanges (CIXes) occur at the backbone or wholesale level. They are neutral interconnection points that in some countries connect only to the backbone; in others they also link up with regional and local services.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International Features

## International Features

## Internet Access Prices Vary

ISP rates for PPP connections (dial-up connections) differ dramatically. For example, an ISP in the U.K. offers unlimited time and data volumes for about $15 a month. This is one of the lowest rates in the U.K. The rates in Germany are in general the highest in the European Union. In Switzerland, an ISP offers unlimited use for $10 a month.

One ISP in Switzerland has apparently decided it doesn't want to attract dial-up users and has made its monthly fee about $40 (plus usage charges). But because this provider has such a good reputation for service and response times, Swiss subscribers who know the importance of performance are willing to dig deeper to pay.

More demanding needs of the corporate Internet subscriber have resulted in the development of value-added services. Prices vary and are, in fact, negotiable. Fees in general are much higher for Internet access when offered by the international and global providers, many of whom manage bigger networks that tend to be more reliable and available -- thus the higher price. Basically, say industry insiders, the old unwritten rule applies to the Infobahn: "You get what you pay for."

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International Features

## International Features

## Infrastructure Improvements

While many national Internet backbones already have 34-Mbps links, and there are some 34-Mbps links between one or two European countries, a pan-European 34-Mbps highway does not exist -- yet. Unisource has announced plans to link Spain, Sweden, Switzerland, the Netherlands, and the U.S. at this speed. EuropaNET is developing a new pan-European 34-Mbps backbone that is primarily for research but will pave the way for development of higher-speed services across the Union. To make for better throughput to the United States, EUnet, Pipex/UUNET, and EBONE are adding a 34-Mbps link.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International Features

## International Features

## Set-Top Madness

Asian manufacturers are rushing to market a new generation of set-top boxes.

Mark LaPedus

Asia, like other regions of the world, is testing the delivery of interactive digital TV services. Phone carriers and computer companies are paving the way for Asian consumers to have a range of services -- Internet connections, video on demand (VOD), pay-per-view, interactive shopping, electronic commerce, and more -- delivered through their TVs, enabled by a so-called set-top box.

The initial demand for VOD services has been slower than expected. The high cost of these services and disparate networking infrastructures present major problems. Another important issue is that the worldwide standards for set-top-box design have been a moving target, according to Steven Chao, the director of digital/video technology for Taiwan's Computer & Communication Research Laboratories (CCL), a government-backed R&D organization that is part of a major consortium developing set-top boxes. "It's also a business issue," notes Chao, adding, "How much are customers willing to pay for them?"

What's in the Box

But most analysts concur that, when it finally develops, the market for set-top boxes and related services will be tremendous. Companies are beginning to rush their products to market, at prices ranging from $200 to $300. Today's first- generation set-top boxes offer more than a multitude of TV channels; they're flexible platforms that connect to various networking architectures and consumer-electronics gear. Follow-up products will contain a slot for a smart card, which will give users a secure way to conduct transactions over cable networks.

Standard set-tops are stand-alone units that connect directly to a TV. Other models will support wireless transmissions; direct broadcast satellite (DBS) services, such as DirecTV; and the Multichannel Multiport Distribution System (MMDS), which uses multiple local terrestrial microwave transmitters located in metropolitan areas to get a signal to homes. Other box vendors are taking different approaches. For instance, aside from their standard set-top lines, NEC and Samsung are integrating set-top-box functions into some of their PC lines.

In what appears to be a collision -- or conversion -- course between PCs and TVs, some set-tops also run real-time OSes and Java applets, which allows the boxes to double as TV Internet surfers if they're connected to the Web. Since some cable companies offer broadband data connections on their networks, some set-tops also feature Ethernet connectors that allow you to download information from the Net.

Asian countries are expected to embrace a combination of standard and wireless set-top boxes that will connect to current and future consumer-electronics devices as the home moves from analog to digital. Future set-tops will support the emerging IEEE-1394 digital interface standard, which specifies the way PCs and consumer-electronics devices exchange data.

The Network Connection

According to analysts, the major issue in Asia is how to link a set-top box to disparate (and sometimes poor) networking infrastructures. Future set-tops will incorporate so-called network interface modules (NIMs), which will allow them to support a bevy of protocols: Asymmetric Digital Subscriber Line (ADSL), hybrid-fiber-coaxial (HFC), and Fiber to the Curb (FTTC, also known as switch digital video). Wireless boxes will support DBS and MMDS.

Basically, ADSL uses specialized modems to transmit signals over an existing twisted-pair telephone wire. A typical ADSL system supports a downstream rate of 6 Mbps and an upstream rate of 64 Kbps. Meanwhile, HFC uses an existing cable-TV network; however, this bandwidth must be shared among several hundred subscribers using interactive services.

Switch digital video calls for fiber-optic cable to be strung to a neighborhood, with a portion connected by coaxial or twisted-pair wire. Such a network might require the use of asynchronous transfer mode (ATM), a cell-switching technology with data rates starting at 1544 Kbps. For interactive-TV services, a set-top box requires several components: a CPU, an NIM, an MPEG-2 audio/video decoder, a real-time OS, main and graphics memory for use in displaying menus and/or bit-mapped images, modulation/demodulation chips, and forward-error-correction ICs.

According to the Interactive Multimedia Association, there are six types of set-top boxes. Below are some details about these six types.

Class 1 and 2 boxes are low-end, analog-based units built around a CISC microprocessor unit (MPU), usually a 386 or a 68020/30. These boxes have little or no capacity for transmitting, but they support cable channels and pay-per-view TV.

Class 3 and 4 boxes also employ CISC MPUs. They provide more functionality by retaining some return-channel bandwidth capabilities while splitting the download channel between analog and encoded video. Class 4 units offer more digital interactive services.

Class 5 and 6 boxes are all-digital units that support a full range of interactive-TV services. Class 5 units have a downstream path that's wider than the upstream path, while Class 6 units have equal bandwidth for sending and receiving. Class 5 and 6 boxes use embedded RISC CPUs, such as the PowerPC, from Motorola and IBM; R4000 variants, from LSI Logic or others; and the MicroSparc, from Sun.

Many RISC MPUs integrate the CPU core, analog descrambler, and network-security interface. Like Class 3 and 4 units, the high-end boxes use MPEG-2 for audio/video compression. Many MPEG-2 chips enable PAL-format video, with a full-screen, 16-color on-screen display and only 16 Mb of DRAM.

Set-tops will also support one or more real-time OSes, including Integrated Systems' pSOS, Microware's OS-9, and the Thomson-Sun Interactive Alliance's OpenTV. These boxes must also support several international standards, which are being devised by a new consortium, the Digital Audio/Visual Council (DAVIC).

A Special OS

Set-top OSes are generally

kernel-based

, scalable software platforms that offer support for CISC and RISC processors as well as provide multitasking functions in real time. This is important for embedded applications, explains Doug Lewis, manager of Asian business development for Microware Systems (Des Moines, IA).

Microware's OS-9 is bundled with Spyglass's Web Technology Kit. This allows Microware's OS-9 to support Internet-access capabilities for several types of electronic appliances: Web-enabled TVs, network computers, pagers, digital cameras, cellular phones, and others. Microware's OS is also bundled with the Java programming environment, enabling the use of Java applets on OS-9.

One of the first VOD trials in Japan is a collaboration between Nippon Telegraph and Telephone (NTT) and cable-TV operators in Tokyo, Chiba, and Kanagawa. The trial, which started in July 1995 and runs through March 1997, calls for 300 households to use a set-top box via NTT's fiber-optic network. Telephone services use a 64-Kbps ISDN network.

A separate VOD trial now taking place near Tokyo, which will also run through March 1997, is being conducted by NTT and Silicon Graphics, Inc. (SGI). This trial uses SGI's set-top box, a custom unit built around a Mips R4000 RISC CPU. Last spring, NTT, CATV Yokosuka, and Microsoft launched a similar program.

NEC, Pioneer, and Toshiba are among the major set-top-box vendors in Japan. NEC's new box, the Broadband Access System-2000, is based on a PowerPC chip that runs OS-9 and supports switch digital video, ADSL, MMDS, DBS, and HFC. It handles NTSC/PAL video signals, while decoding is done via MPEG-2 over a 15-Mbps transport stream.

NEC's box can support narrowband services, such as plain old telephone service (POTS), narrowband ISDN, and Internet access. The optical network unit can support narrowband signals via T1 or E1 interfaces. NEC's ADSL system can transport signals via ATM cells using the ADSL format. The downstream bit rate is 6 Mbps; the upstream rate is 64 Kbps. A typical price for a set-top box in Japan runs from 20,000 to 30,000 yen.

Karaoke on Demand

Late last year, NEC was picked as the set-top-box vendor for a major VOD contract in Hong Kong. NEC's box is built around IBM's PowerPC. Hong Kong's VOD provider, Hongkong Telecom-IMS, has delayed its VOD trials until 1997, when it will offer VOD, karaoke on demand, electronic commerce, home shopping, and pay-per-view TV.

Hongkong Telecom-IMS will carry its interactive-TV services via an ATM or broadband ISDN network. Applications servers will supply Java over dial-up connections across the ATM network. Two-way communications will take place across this ATM connection via TCP/IP protocols. Video content sent out from the server will be in MPEG-2 form. It will then be decoded by a hardware chip in the set-top box and turned into an analog signal for transmission to the TV, according to William Lo, president of Hongkong Telecom-IMS.

Meanwhile, Taiwan is also endorsing the PowerPC in a set-top-box/VOD pilot program. This set-top box comes from a newly formed consortium led by Acer, CCL, and Tatung. Taiwan's Interactive TV consortium consists of some of the island's other PC and consumer-electronics vendors: ADI, First International Computer, Mitac, and Sampo, as well as some multinational corporations, including Philips and Matsushita.

Acer's box, the AcerStar, will ship early next year. It's built around IBM's 403 version of the embedded PowerPC, and it runs OS-9. Once it hits mass production in 1997, the Acer box will sell for about $300. It includes an MPEG-2 chip and 3 MB of memory, and it supports the European Digital Video Broadcast (DVB) standard. "DVB, which is getting support in the U.S., has a good descrambler system for encryption and decryption purposes," says Carlie Wang, R&D director for Acer's set-top-box project.

Tatung, one of Taiwan's largest consumer-electronics companies, also has a new set-top box, the TDS-403D. Like the AcerStar, the TDS-403D is based on the PowerPC and uses an MPEG-2 chip for compression/decompression.

Samsung is playing a major role in Korea Telecom's (KT's) VOD pilot project, which is taking place in Seoul. Fifty subscribers in the Yoido area have been able to enjoy movies, drama, documentaries, and karaoke by placing an order through a telephone line to KT's VOD server. In the trial, Samsung is developing and providing an ATM switching system, an ATM multiplexer, ADSL, set-top boxes, and other systems. Meanwhile, Digital Equipment provides the video server, consulting, and systems integration.

The set-top box may take yet another form in the future. Like NEC, Samsung, and others, Acer may integrate set-top functions into its PCs. "The PC will likely integrate the set-top, the DVD [digital videodisc] player, and other devices," Acer's Wang says. "But eventually, we see the stand-alone set-top becoming the home server for distributing information to the PC or other appliances in the home. With the set-top, you can receive video information or telephone signals. In a sense, the set-top becomes the cornerstone in the home."

## Where To Find

Acer, Inc.

Taipei, Taiwan, R.O.C.

Phone: +886 2 545 5288

Fax: +886 2 545 5308

http://www.acer.com/

Internet:

http://www.acer.com/

/Computer & Communication Research Laboratories

Hsinchu, Taiwan, R.O.C.

Phone: +886 035 917 743

Fax: +886 035 820 044

&E-Mail: a000@ccloal.ccl.itri.org.tw

Hongkong Telecom-IMS, Ltd.

Hong Kong

Phone: +852 2888 2888

Fax: +852 2877 8877

E-Mail: wlo@hkt.com.hk

http://www.netvigator.com

Internet:

http://www.netvigator.com

NEC Corp.

Kanagawa, Japan

Phone: +81 44 435 5260

Fax: +81 44 435 5425

http://nec.co.jp/index_e.html

Internet:

http://nec.co.jp/index_e.html

%Nippon Telegraph and Telephone Corp.

Tokyo, Japan

Phone: +81 3 5200 9136

Fax: +81 3 5200 9135

http://www.ntt.jp/

Internet:

http://www.ntt.jp/

Samsung Electronics Co., Ltd.

Seoul, Korea

Phone: +82 2 727 7833

Fax: +82 2 727 7985

Tatung Co.

Taipei, Taiwan, R.O.C.

Phone: +886 2 592 5252

Fax: +886 2 591 6443

WebTV Networks, Inc.

Palo Alto, CA

Phone: (415) 326-3240

Fax: (415) 326-5277

## David 2.1 Software Architecture

More than 2 set-top-box manufacturers chose the David API becuase of its compact, modular architecture.

mailto:"5916955@mcimail.com"

Mark LaPedus is a BYTE contributing editor based in Taipei. You can reach him by sending e-mail to

5916955@mcimail.com

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International Features

## International Features

## Web-Browsing from Your TV

The set-top box will appear in many forms. Philips and Sony recently licensed a hybrid set-top/network-computer technology from WebTV Networks (Palo Alto, CA). They won't release the final specs of their boxes until this fall, but they claim their systems will connect to a TV and a phone line.

Such boxes allow you, via remote control, to change TV channels, surf the Internet, get e-mail, and access WebTV's own on-line service without the hassles and delays of going through an on-line provider on a PC.

The feature-rich Sony and Philips set-top boxes will sell for $200 to $400. The companies licensed two components from WebTV: WebTV Reference Design and WebTV Network, the on-line service. The Reference Kit includes software and hardware guidelines for making a set-top. Built around Integrated Device Technology's 112-MHz R4640 RISC chip, the WebTV-based box comes with a 33.6-Kbps V.34bis modem, memory, 16-bit stereo, and an on-the-fly decompression technology.

The box's patented Worldscan technology allows Web content to appear on all TV formats. Company officials would not disclose what OS the box will run. But it comes with its own WebTV browser, which is compatible with HTTP, Multipurpose Internet Mail Extensions (MIME), and Hypertext Markup Language (HTML) 3.0; virtually all extensions of Netscape Navigator 3.0; and Microsoft's Internet Explorer.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

## ISDN-Based Total Comm Package

Rainer Mauth

View is a comprehensive ISDN communications solution. It features videoconferencing software, a digital camera, an answering machine, and application-sharing capability, plus it supports MPEG playback in hardware. IView includes an external handset that performs like an ISDN phone and contains a sound card.

The ISDN PCI card offers standard H.320 videoconferencing, deploying two B channels transmitting at 15 frames per second. The system can also operate with ISDN videoconferencing systems that use only one B channel. In conference with another IView board, you not only can share applications but can also simultaneously transfer files. In this situation the system uses one B channel for audio transmission and the other one for video and data. It is also possible to connect a camcorder or a video recorder via a second camera socket.

The system supports Eurofile transfer, fax group 3 and 4 protocols, V.110-compliant bit rate adaptation, as well as CAPI version 1.1. Support for CAPI 2.0., Siemens says, will come later in the year.

## Product Information

View.........................DM 1990

Siemens

Munich, Germany

Phone: +49 722 35305

Fax: +49 722 33668

Circle 986 on Inquiry Card.

View

## ISDN PCI card

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

(Upgrade Processor for Compaq Notebooks

With the H&P 586 upgrade module users can upgrade their Compaq Elite and Contura notebooks to Pentium performance by replacing the processor and socket on the main board. The H&P 586 upgrades 486 processors to 100-MHz or 133-MHz clock speeds.

Price: DM 598.

1Company: Hantz & Partner, Gundelfingen, Germany

Phone: +49 761 592100

Fax: +49 761 585228

%E-mail: 100431.2606@compuserve.com

Circle 987 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

## Add Floppy Drive to Psion

Cyclone is an external 3-1/2-inch floppy drive for the Psion Series 3a and Workabout computers. It appears as drive C to all Psion applications, works with all software that adheres to Psion standards, and includes the File Manager software. The drive is powered by 5 AA cells or mains power.

Price: 170 Pounds UK.

"Company: Purple Software, London

Phone: +44 171 387 7777

)E-Mail: purplesoft@cix.compulink.co.uk

Circle 988 on Inquiry Card.

## Psion C's All Apps

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

## German Pilot 5000

A German version of the Pilot 5000, a pocket-size hand-held computer, comes with 512 KB of memory and can be upgraded to 1 MB to hold 10,000 address entries. An information management system communicates with your Windows PC via a docking station and HotSync software.

Price: DM 780.

Company: US Robotics, Paris-la-Defense, France

Phone: +33 14 197 4600

Fax: +33 14 907 0303

http://www.usr.com/palm

Internet:

http://www.usr.com/palm

Circle 989 on Inquiry Card.

## Pilot 5000

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

## Image Acquisition Board

Elf, a PCI-based image acquisition system, can capture data from RGB, S-video, composite, or monochrome video sources. The board supports trigger input, strobe control, and other external devices. It also incorporates real-time scaling, panning, scrolling, and zooming. Elf comes either as a bus-mastering DMA board that works with any PCI graphics card or as a combined VGA graphics and image acquisition board.

Price: Call company.

+Company: Active Imaging, Maidenhead, U.K.

Phone: +44 1628 415444

Fax: +44 1628 415400

E-Mail: info@datacell.co.uk

http://www.imaging.co.uk

Internet:

http://www.imaging.co.uk

Circle 990 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

## 200-MHz Pentium PCs

Siemens' Scenic Pro C5 and Pro M5 series of desktop and mini-tower PCs now comes with 200-MHz Pentium processors. These faster models are aimed at people running professional multimedia applications as well as at SOHO users. All the systems deploy SNI's Quickfax software, which enables users to receive faxes without the PC being on.

Price: Starts at DM 3950.

-Company: Siemens Nixdorf, Augsburg, Germany

Phone: +49 821 804 3680

http://www.sni.de

Internet:

http://www.sni.de

Circle 996 on Inquiry Card.

## Scenic Pros from Siemens

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

## Fiber Modem

FOM-E1/T1, a fiber modem, converts electrical E1 or T1 signals into optical signals. With FOM-E1/T1 you can deploy E1/T1 equipment while you switch your cabling to fiber optics. The system works over a distance of 50 kilometers. It comes as a standard E1 add-in board.

Price: Call company.

4Company: RAD Data Communications, Tel Aviv, Israel

Phone: +972 3 645 8107

Fax: +972 3 649 8250

!E-Mail: ilan@radmail.rad.co.il

http://www.rad.co.il

Internet:

http://www.rad.co.il

Circle 991 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

$SmartView Controls Several Servers

SmartView lets a pool of servers share keyboard, video, and mouse. The device supports any mix of AT and PS/2 keyboards and PS/2 and RS-232 mice. An autoboot function reboots shut-down servers automatically. The devices support two or four servers and can be cascaded to form a video-switching network. Additional features include a security function (password for access), screen-saver mode, and variable scan rates between active ports.

Price: Starts at 295 Pounds UK.

,Company: Adder Technology, Cambridge, U.K.

Phone: +44 1223 420 912

Fax: +44 1223 423 495

Circle 993 on Inquiry Card.

## Pool Your Server Resources

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

$Remote Access Router Supports CAPI

The BIANCA/BRICK remote access routers now come with a dual-mode interface that supports CAPI 1.1 and CAPI 2.0. The CAPI drivers run under all flavors of Windows, OS/2, and Unix and can access all CAPI-compliant applications.

Price: Call company.

3Company: BinTec Communications, N

rnberg, Germany

Phone: +49 911 9673 162

Fax: +49 911 9673 195

E-Mail: awild@bintec.de

http://www.bintec.com

Internet:

http://www.bintec.com

Circle 992 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

"10Base-T Hubs with Video Display

D-Link's DE-1824 series of stackable 10Base-T hubs offers video display of statistics, diagnostic information, and segmentation of a network from a management station. Up to eight hubs can be linked, with seven client hubs sharing an SNMP management agent of a master hub. Each hub comes with 24 twisted-pair ports in one low-profile, rack-mountable case. The RJ-45 ports support both UTP and STP cable, while a recessed AUI slot is provided for flexible connection to the thin coax, thick coax, and fiber cable through any standard-size transceiver.

Price: Call company.

'Company: D-Link Corp., Taipei, Taiwan

Phone: +886 2 916 1600

Fax: +886 2 914 6299

Circle 994 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

## ATM Upgrade for LANs

Fibronics' XM501 ATM Access Card is a simple way to upgrade your current LAN to asynchronous transfer mode via the Fibronics GigaHub. The XM501 connects the GigaHub backplane to ATM networks, forming large backbone systems. It features a bridge/switch engine that provides a backplane-to-ATM gateway using a 155-Mbps OC3 connection. The XM501 preserves all network investments and, Fibronics says, ensures interoperability between switched Ethernet and Fast Ethernet stations over an ATM backbone. The Access Card features LAN Emulation Server service, allowing it to operate in ATM networks with an ATM switch that does not provide such service. The XM501 supports permanent virtual circuits, switched virtual circuits, and UNI V3.1 signaling.

Price: Call company.

(Company: Fibronics Ltd., Haifa, Israel

Phone: +972 4 8313 313

Fax: +972 4 8550 550

E-Mail: sales@fibronics.co.il

http://www.fibronics.co.il

Internet:

http://www.fibronics.co.il

Circle 995 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

## Industrial 486 Board

The PCA-6144V is a 486DX2/DX4 CPU card for industrial use. It has a local-bus VGA controller with Windows accelerator and 1 MB of display memory, an enhanced IDE interface, a floppy controller, two high-speed buffered serial ports, and a 63-level watchdog timer.

Price: Call company.

Company: Integrated Measurement Systems Ltd., Southampton, U.K.

Phone: +44 1703 771143

Circle 997 on Inquiry Card.

## PCA-6144V CPU Card

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

## A Dozen Gigabytes

The N3000 series of network file servers can store up to 12.9 GB. They support RAID functionality, and you can daisy chain two devices via SCSI. You can attach them to any Ethernet LAN without shutting down the network.

Price: Starts at DM 14,000.

'Company: Xyratex, Havant, Hants, U.K.

Phone: +44 1705 486363

http://www.xyratex.co.uk

Internet:

http://www.xyratex.co.uk

Circle 1001 on Inquiry Card.

## N3000 File Server Selection

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

.New Version of RAPID Visual Programming Tool

Tania Hershman

Emultek's 32-bit RAPID 3.5 is the latest version of the company's tool that enables nonprogrammers to quickly create interactive simulations of systems ranging from cellular telephones to airplane cockpits. No knowledge of computer code is needed to create simulations. Just use the Object Editor to pick objects from a library that includes switches, dials, displays, buttons, and a host of other options. The Logic Editor then links the objects to create a working simulation.

Version 3.5 has several innovative features, including the capability to make the RAPID application you've created into a user-defined object, which can then be encapsulated in other simulations. If you want to develop training tools, it's easy to link RAPID simulations to multimedia applications built with all leading authoring tools. An Internet plug-in will be released shortly, Emultek says.

## Product Information

RAPID 3.5.....................$6000

Emultek

Jerusalem, Israel

Phone: +972 2 870 770

Fax: +972 2 870 773

%E-Mail: 100274.2054@compuserve.com

http://www.emultek.com

Internet:

http://www.emultek.com

Circle 1002 on Inquiry Card.

## RAPID 3.5

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

.Magic System Releases Win 95 and NT Versions

Magic Software Enterprises has launched the first Windows 95 and NT version of its Magic rapid application development tool. The faster 32-bit version 7 of the table-driven, code-free programming tool has several new features, including a built-in Web link for creating Internet applications. Magic 7 has an increased emphasis on component reusability and also supports OLE 2.0. There are improved GUI functions and performance enhancements for the Magic client and server architecture. Form templates can be saved as Magic Form Templates and reused. Support for multilingual applications has also been enhanced.

Price: $6000.

8Company: Magic Software Enterprises, Or-Yehuda, Israel

Phone: +972-3 538-9400

Fax: +972-3 538-9402

&E-Mail: beni@mse.mhs.compuserve.com

http://www.magic.co.il

Internet:

http://www.magic.co.il

Circle 1003 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

## Repository-Based CASE Tool

The Intelligent Software Factory (ISF), an integrated suite of object-oriented CASE tools, is built on a shared repository and allows for complete life-cycle management of development projects. It includes event tracing, modeling of nested states and events, and documentation and diagnosis features. With ISF, programmers can capitalize on multiple CASE methods and iterative development.

Price: Call company.

2Company: Reich Technologies, Paris Cedex, France

Phone: +33 98 46 61 32

Fax: +33 98 44 77 72

%E-Mail: 101473.1573@compuserve.com

Circle 1004 on Inquiry Card.

## Integrated CASE Suite

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

-DeCaf Protects Against Foreign Java Applets

DeCaf is an HTTP proxy server that sits between a corporate LAN and the Internet and acts as a special relay that scrutinizes all inbound and outbound Web traffic. The software provides an extra measure of security. When it receives a request from a Java applet, it blocks this request and warns the network manager about what's happening. The program also logs all requests and builds audit trails.

Price: Call company.

Company: LeReseau Netwerksystemen, Middlesturm, The Netherlands

Phone: +31 595 552431

Fax: +31 595 551279

E-Mail: info@reseau.nl

http://www.reseau.nl

Internet:

http://www.reseau.nl

Circle 1006 on Inquiry Card.

## DeCaf Just As High-Powered

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

2Now You Can Put PowerPoint Shows on the Internet

PointPlus, from Net-Scene, enables PowerPoint users with no HTML skills to publish PowerPoint presentations on the Internet. Net-Scene's compression technology converts existing PowerPoint presentations, from bullet-point slides to presentations with sound, for on-line viewing. The PointPlus plug-in viewer lets you see the presentation within the Netscape Navigator or Chameleon Websurfer window. PointPlus is the first in a series of low-end and midrange Internet-based presentation tools for other graphics-authoring programs. You can download a free copy of PointPlus's viewer and sample presentations from the Net-Scene Web site. PointPlus requires Windows 95 or Windows NT 3.51 and PowerPoint 4.0 or higher. The plug-in works under Windows 3.1 or higher, Windows 95, and Windows NT 3.51.

Price: Call company.

Company: Net-Scene, Herzliya, Israel

Phone: +972 9 558 260

Fax: +972 9 558 262

E-Mail: info@net-scene.co.il

http://www.net-scene.co.il

Internet:

http://www.net-scene.co.il

Circle 1078 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

## Software-License Control

Integra-SLM distributes and controls software licenses in heterogeneous networks. In case all licensed copies of an application are in use, the program puts further requests for that software on hold and then assigns the next free license. The program also includes virus detection and utilization statistics. Integra-SLM runs on NetWare, Windows NT, Sinix, Unix, Banyan Vines, or LAN Manager servers.

Price: DM 20 per client.

+Company: CSD Software, Starnberg, Germany

Phone: +49 8151 3690

Fax: +49 8151 36988

E-Mail: StephanH@csdsoft.de

Circle 1010 on Inquiry Card.

!License Control with Integra-SLM

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

## Event Log Manager for NT

Enabling Windows NT network administrators to detect network, system, and application issues as they occur, SeNTry Event Log Manager 1.6 monitors server status, network traffic, and unauthorized access attempts. The system collects events in an ODBC-compliant database and integrates with HP's OpenView and NetView network management platforms.

Price: 149 Pounds UK per server.

Company: Serverware Group, London

Phone: +44 171 419 2020

Fax: +44 171 419 2030

Circle 1011 on Inquiry Card.

## SeNTry Log Manager

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

2Easier Access to E-mail While You're on the Road

With HT Mail, checking e-mail from a remote site becomes easier and cheaper because this mailbox server software provides access to the post office of your LAN over the Internet. You launch a standard Web browser, tap in the corporate URL, and key in a password to access the e-mail system in your office. You get full access to personal and shared folders as well as the complete LAN address book.

HT Mail keeps your mail in sync while you're on the road. It doesn't matter if you download e-mail or read it on-line; when you are back in the office, you will find the complete e-mail conversation filed on your LAN. HT Mail links to an external Web server on your LAN but it can be used within your corporate intranet. The software works with Microsoft Exchange, MS Mail, cc:Mail, and other SMTP or MAPI messaging systems. Via MAPI you can even access Lotus Notes 4.0. Supported server platforms are Windows NT and Unix.

Price: Starts at 195 Pounds UK (10-user license).

Company: Elonex, London

Phone: +44 181 452 4444

Fax: +44 181 452 6422

http://www.elonex.co.uk

Internet:

http://www.elonex.co.uk

Circle 1012 on Inquiry Card.

## High Tech Mail

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

## Accounting System Supports Multiple Currencies

Exchequer Enterprise is a new 32-bit accounting system for Windows 95 and Windows NT that supports multiple currencies and uses an Explorer-style tree to group and subgroup general ledger accounts. The system also handles open period accounting, which makes it possible to retrieve accounting balances and transactions from any previous period. A drill-down approach lets the user interrogate top-level as well as single stock information. The software supports multiuser environments.

Price: Call company.

-Company: SBS Financial Systems, Derby, U.K.

Phone: +44 1202 298008

Fax: +44 1202 298001

Circle 1009 on Inquiry Card.

## Exchequer Enterprise

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

+Archiving System with Full-Text Searching

Easy Archive 2000, an archiving system for Windows 3.1 and Windows 95, offers direct access to 20 archives with up to 2000 documents each. It provides version numbering and document history and automatically assigns alteration dates. Additionally, the system automatically inserts text into any archiving field, thus allowing full-text searching and editing.

Price: Call company.

(Company: Easy, Muehlhein/Ruhr, Germany

Phone: +49 208 450160

Fax: +49 208 4501690

"E-Mail: easygmbh@pop.du.gmd.com

http://www.easy.de

Internet:

http://www.easy.de

Circle 1008 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

## CD-ROM Mastering for the Mac

Toast CD-ROM Pro 3 is mastering software for the Macintosh that creates Mac or ISO 9660 volumes on-the-fly from files and folders. With this program, Mac volumes can be optimized and defragmented during recording.

Price: $360.

Company: Astarte, Karlsruhe, Germany

Phone: +49 721 9855412

Fax: +49 721 853862

%E-Mail: 102404.3564@compuserve.com

http://www.astarte.com

Internet:

http://www.astarte.com

Circle 1005 on Inquiry Card.

Copyright

1994-1997 BYTE

BYTE Magazine, October 1996

## International What's New

## International What's New

## OCR for Arabic

OmniPage for Arabic, an OCR program, turns printed Arabic pages into editable documents. This Windows 3.1 or 3.11 software recognizes all Arabic fonts regardless of style, size, or column format, Caere says. It also provides a bilingual interface of Arabic or English and comes bundled with the international version of 12 Western and European languages.

Price: Call company.

Company: Caere, London

Phone: +44 171 222 3200

Fax: +44 171 222 3202

Circle 1007 on Inquiry Card.

## OmniPage for Arabic

## Images

![image-0210.gif](../images/image-0210.gif)

![image-0211.gif](../images/image-0211.gif)

![image-0212.gif](../images/image-0212.gif)

![image-0213.gif](../images/image-0213.gif)

![image-0214.gif](../images/image-0214.gif)

![image-0215.gif](../images/image-0215.gif)

![image-0216.gif](../images/image-0216.gif)

![image-0217.gif](../images/image-0217.gif)

![image-0218.gif](../images/image-0218.gif)

![image-0219.gif](../images/image-0219.gif)

![image-0220.gif](../images/image-0220.gif)

![image-0221.gif](../images/image-0221.gif)

![image-0222.gif](../images/image-0222.gif)

![image-0223.gif](../images/image-0223.gif)

![image-0224.gif](../images/image-0224.gif)

![image-0225.gif](../images/image-0225.gif)

![image-0226.gif](../images/image-0226.gif)

![image-0227.gif](../images/image-0227.gif)

![image-0228.gif](../images/image-0228.gif)

![image-0229.gif](../images/image-0229.gif)

![image-0230.gif](../images/image-0230.gif)

![image-0231.gif](../images/image-0231.gif)

![image-0232.gif](../images/image-0232.gif)

![image-0233.gif](../images/image-0233.gif)

![image-0234.gif](../images/image-0234.gif)

![image-0235.gif](../images/image-0235.gif)

![image-0236.gif](../images/image-0236.gif)

![image-0237.gif](../images/image-0237.gif)

![image-0238.gif](../images/image-0238.gif)

![image-0239.gif](../images/image-0239.gif)

![image-0240.gif](../images/image-0240.gif)

![image-0241.gif](../images/image-0241.gif)

![image-0242.gif](../images/image-0242.gif)

![image-0243.gif](../images/image-0243.gif)

![image-0244.gif](../images/image-0244.gif)

![image-0245.gif](../images/image-0245.gif)

![image-0246.gif](../images/image-0246.gif)

![image-0247.gif](../images/image-0247.gif)

![image-0248.gif](../images/image-0248.gif)

![image-0249.gif](../images/image-0249.gif)

![image-0250.gif](../images/image-0250.gif)

![image-0251.gif](../images/image-0251.gif)

![image-0252.gif](../images/image-0252.gif)

![image-0253.gif](../images/image-0253.gif)

![image-0254.gif](../images/image-0254.gif)

![image-0255.gif](../images/image-0255.gif)

![image-0256.gif](../images/image-0256.gif)

![image-0257.gif](../images/image-0257.gif)

![image-0258.gif](../images/image-0258.gif)

![image-0259.gif](../images/image-0259.gif)

![image-0260.gif](../images/image-0260.gif)

![image-0261.gif](../images/image-0261.gif)

![image-0262.gif](../images/image-0262.gif)

![image-0263.gif](../images/image-0263.gif)

![image-0264.gif](../images/image-0264.gif)

![image-0265.gif](../images/image-0265.gif)

![image-0266.gif](../images/image-0266.gif)

![image-0267.gif](../images/image-0267.gif)

![image-0268.gif](../images/image-0268.gif)

![image-0269.gif](../images/image-0269.gif)

![image-0270.gif](../images/image-0270.gif)

![image-0271.gif](../images/image-0271.gif)

![image-0272.gif](../images/image-0272.gif)

![image-0273.gif](../images/image-0273.gif)

![image-0274.gif](../images/image-0274.gif)

![image-0275.gif](../images/image-0275.gif)

![image-0276.gif](../images/image-0276.gif)

![image-0277.gif](../images/image-0277.gif)

![image-0278.gif](../images/image-0278.gif)

![image-0279.gif](../images/image-0279.gif)

![image-0280.gif](../images/image-0280.gif)

![image-0281.gif](../images/image-0281.gif)

![image-0282.gif](../images/image-0282.gif)

![image-0283.gif](../images/image-0283.gif)

![image-0284.gif](../images/image-0284.gif)

![image-0285.gif](../images/image-0285.gif)

![image-0286.gif](../images/image-0286.gif)

![image-0287.gif](../images/image-0287.gif)

![image-0288.gif](../images/image-0288.gif)

![image-0289.gif](../images/image-0289.gif)

![image-0290.gif](../images/image-0290.gif)

![image-0291.gif](../images/image-0291.gif)

![image-0292.gif](../images/image-0292.gif)

![image-0293.gif](../images/image-0293.gif)

![image-0294.gif](../images/image-0294.gif)

![image-0295.gif](../images/image-0295.gif)

![image-0296.gif](../images/image-0296.gif)

![image-0297.gif](../images/image-0297.gif)

![image-0298.gif](../images/image-0298.gif)

![image-0299.gif](../images/image-0299.gif)

![image-0300.gif](../images/image-0300.gif)

![image-0301.gif](../images/image-0301.gif)

![image-0302.gif](../images/image-0302.gif)

![image-0303.gif](../images/image-0303.gif)

![image-0304.gif](../images/image-0304.gif)

![image-0305.gif](../images/image-0305.gif)

![image-0306.gif](../images/image-0306.gif)

![image-0307.gif](../images/image-0307.gif)

![image-0308.gif](../images/image-0308.gif)

![image-0309.gif](../images/image-0309.gif)

![image-0310.gif](../images/image-0310.gif)

![image-0311.gif](../images/image-0311.gif)

![image-0312.gif](../images/image-0312.gif)

![image-0313.gif](../images/image-0313.gif)

![image-0314.gif](../images/image-0314.gif)

![image-0315.gif](../images/image-0315.gif)

![image-0316.gif](../images/image-0316.gif)
