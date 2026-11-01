---
title: "Don't Swap: Network!"
publication: "BYTE Magazine"
issue: "November 1996"
section: "Pournelle"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x0094579e"
---

# Don't Swap: Network!

*Pournelle*

Upgrading the Pournelle way means more than trading in one machine for another.

Jerry Pournelle

I've got a new method for writing fiction, and it's been working so far. Every morning, including Saturday, I get up at 8:00, have a leisurely breakfast, and read the papers. By 10:00, I'm upstairs in what used to be Alex's room. There's nothing in it but an elderly (in this business, three years is old) Gateway 2000 486DX2, a steno chair, a portable ice chest I fill with Dr. Pepper and root beer, and Alex's old high school books. There are no distractions. No phone. No modem. No computer games. No interesting books.

I stay there until 12:30. So far, I have averaged more than 1000 words a day plus rewriting the previous day's output. Starswarm, my new juvenile about a boy who grows up with a computer in his head, is taking shape wonderfully, with over 50,000 words done. At more than a thousand words a day, it will be finished in two weeks.

The Gateway 2000 486DX2 was Roberta's computer before we upgraded her to a Gateway Pentium 200. It's a perfectly good machine, and we've never had any trouble with it. It's certainly fast enough for what I'm doing. (Heck, for writing fiction, a 286 with Q&A Write is good enough.) The programs I run are Windows 95 (Win 95), Microsoft Office, Norton Commander (for DOS), and Info Select.

Info Select is a general notes program. It started life as Tornado Notes, which was a far better name than Info Select. When Micro Logic changed it from a DOS pop-up to a Windows utility, they changed names. I find the name ugly, but it's a terrific utility.

I use Info Select to accumulate and organize notes, such as character names, locations, and all the other stuff that goes into my novels. It's easy to copy some text, such as the first scene where I name and describe a character, switch to Info Select, create a note or open an existing one, and stuff the new information into it. It's also great for diaries, keeping track of work in progress, and other stuff. You can learn to use it in about 5 minutes, and I don't see how anyone gets along without it. Micro Logic also makes DiskMapper, a program that graphically maps your hard drive and shows you exactly what's eating up all that disk space. I'll try to get to that soon, too.

I've also installed CyberMedia's First Aid 95 Deluxe on this Gateway machine. I chose it as much for its cleanup capability as anything else. Roberta had a whole bunch of stuff on the computer that I don't need, so after I copied it all to her new machine, I erased almost everything. That freed up a lot of disk space, but it left a whole bunch of Win 95 shortcuts and other junk. First Aid seems to have fixed all that.

I had what I thought were some problems with First Aid on another machine, but I know now that the problems were something else. I've been using First Aid on a number of machines without difficulties. It's good for cleaning up after big deletes, and while I haven't needed the recovery features so far, I might.

On the other hand, the installation program sucks rocks.

Actually, that's not true; the installation program works fine once you get it going. The problem is the serial number. First Aid comes on a CD-ROM. Apparently, CyberMedia caught the serial-number disease from Microsoft, because you can't install First Aid without one. This means keeping paperwork handy, and I don't want to do that, so I use a marking pen to write the serial number on the face (the printed side, not the data side) of the CD-ROM. I do that on all those that need a serial number. Now I can't lose the serial number.

The First Aid CD-ROM is auto-play, so when you put it in the drive, it offers to install the program for you. So far, so good, but now it asks for the serial number. I opened the CD-ROM tray to read the serial number. When I closed it, auto-play brought up another copy of the installation program. Eliminating that blew up the original installation program. There was nothing for it but to close down all attempts to install, copy the serial number on paper, and start over. Once that was done, things went smoothly enough, and First Aid's background programs came up on restart. I fail to understand the point of having serial numbers on CD-ROMs.

I formerly used Norton System Doctor to accomplish the same things that First Aid does, but System Doctor has an ugly feature: when it's running in the background, there's a steady blink-blink-blink of the cursor on the desktop that I find extremely annoying. First Aid does not do that.

What I do on that upstairs machine is important. I back up to floppy disks every day, but I worry about power failures, so I have an American Power Conversion uninterruptible power supply (UPS) on the machine. If First Aid 95 Deluxe has even a small chance of saving the work in progress, it's worth it, and having it there makes me feel better.

There are still plenty of Windows 3.11 systems out there, so we need one here as a test-bed. The machine that got stuck with the job is SuperCow, a Gateway 2000 486DX2 VL-Bus system. When we got that machine, it was the fastest thing in the house. Over the years, this column has featured upgrades to SuperCow: a Western Digital Caviar AC31000 1-GB hard drive, a new BIOS to support that drive, more memory, and new video cards. One of the first upgrades was a Creative Labs Sound Blaster 16 card and a CD-ROM drive. That was at least three years ago.

Since then, I've used SuperCow for nearly everything, including using it as the world's heaviest portable: I used to lug it down to the beach house when I'd go there to write. Whether it was from doing that or something else, eventually the CD-ROM drive began to fail. It might have been the cable, or perhaps the laser needed cleaning -- I'm not sure I ever cleaned it -- but whatever happened, it stopped working. I decided this would be a good opportunity to update the double-speed CD-ROM drive, and as it happened, I had a new Creative Labs Sound Blaster Performance 8&#215

Physical installation was a bit tight. The CD-ROM cable Creative Labs supplied was shorter than the one that came with the original kit. However, because of the local-bus slots, I didn't have any choice where to put the sound card/CD-ROM controller. Eventually, I had to shuffle the drives so that the CD-ROM drive was on top, with the floppy drives beneath it; hardly a big sacrifice -- indeed, it's an improvement -- but just a bit annoying because I was working in close quarters.

When I got it installed, I tested it all under DOS. The sound card worked fine. So did the CD-ROM drive. I went into Windows. As Windows came up, Mr. Spock gave me some information about the confines of this solar system, so the sound was working; but when I accessed the CD-ROM drive, the system locked tighter than a drum. The only way out was the power switch.

That happened twice: the CD-ROM drive worked fine in DOS and locked up in Windows 3.1. Time to do some thinking. It took me longer than it should have to figure it out.

SuperCow is on my local Ethernet. When it comes up, it goes out on the network to connect to whatever machines it can find. Until that happens, though, the network card hasn't been accessed, and, more important, the interrupt request (IRQ) hasn't been used by the network card.

The Sound Blaster Performance 8&#215

The sound card uses a different IRQ for the eight-speed CD-ROM drive, and that is set by default to IRQ 10. Once again, this is no bad thing. Many systems use IRQ 10 for the CD-ROM drive. Unfortunately, that is where I long ago set the Intel EtherExpress card on the grounds that nothing uses IRQ 10 by default -- which was true at the time. At least I'd found the cause of the problem.

I now had two choices: reset the EtherExpress card or the Sound Blaster. Resetting the EtherExpress card is simple, so in keeping with the notion that I go to a lot of trouble to try complex things so you don't have to, I decided to reset the Sound Blaster's CD-ROM drive IRQ.

In theory, that should be simple. Like the EtherExpress card, there are no jumpers on the Sound Blaster. Instead, there is software that automatically configures the card, an attempt at Plug and Play. There's also software that is supposed to let you change the card's configuration. It's not well documented, so I called Creative Labs' technical-support department. The first two people I talked to couldn't make it work. The next day, I got calls from increasingly savvy people. It didn't help. We'd manage to get the card to reset to a different IRQ -- but as soon as I powered down and brought it back up, it seized IRQ 10 with a death grip.

To make the story short, I finally gave up. IRQ 10 belongs to the Sound Blaster to control the CD-ROM card. I used SoftSet to change the IRQ for the EtherExpress card. That's a DOS program. One thing: if you change the IRQ for your network card in Windows 3.11, you must then invoke Windows with the command WIN /n, bringing it up without the network; go into the network settings; and manually change the IRQ to your new setting. If you don't, Windows will either lock up or try to change the card setting back to what it expects, and since Windows for Workgroups originally shipped with EtherExpress cards, Windows knows how to do that. The result is that you'll be back where you started. This is one case where attempts to Plug and Play actually get in the way.

Now that the IRQ conflict is over, SuperCow's CD-ROM, sound, and networking are fine. The CD-ROM drive is screamingly fast, the new speakers that came with the Creative Labs Sound Blaster Performance 8&#215

Note that if you install the Creative Labs Sound Blaster Performance 8&#215

If you need sound -- and most of us now do -- and you want to add a CD-ROM drive to your system, the Creative Labs Sound Blaster Performance 8&#215

You will have noted that we have several Gateway 2000 machines. There's RacingCow, a P5-133XL that Eric uses to cruise the Internet; SuperCow, and its non-VL-Bus counterpart I have upstairs; Joizy, my wife's new P5-200XL; the Liberty laptop; and Alex sometimes uses the old HandBook. We work these machines hard; indeed, SuperCow has undergone some real torture tests, what with frequently being taken apart to accommodate new equipment and every couple of months being carried off to the beach house in the trunk of the car.

Except for an initial problem finding a free IRQ so we could add a SCSI board to RacingCow -- that system came fully equipped with an internal modem and sound card, and my first act was to add an Ethernet card, using the last free IRQ -- we haven't had any problems with these machines. Roberta used the older Gateway machine for years and now has the P5-200XL, which she loves.

These are not special machines. I get them off the factory line, just as you do, and, indeed, the P5-200XL came with evidence of hard shipping since a few of the bezels in the front panel had been displaced. It didn't seem to matter; the machine worked just fine right out of the box.

I say all this because I get a lot of mail asking if it's really safe to buy computers by mail order, and I can only reply that it depends on the mail-order outfit. I know of several good ones, and I can't possibly tell you which is best. I can only say that I can get just about any machine I want, and I've had quite satisfactory experiences with Gateway 2000 systems. I use them, and I rely on them.

Note also that I write only about what I'm familiar with. There was a time when I might try to keep up with the field and know what's best, but that was long ago. Now, all I can guarantee is that I don't write about what I won't use, and I sure won't use anything that's not more than good enough.

If my mail is any indication, a lot of you are concerned about upgrade paths. I've given this a bit of thought.

First, there are now full-featured laptops that are good enough to be your only computer, and people looking to upgrade might keep that in mind. Example: we just acquired a Nimantics Orion 6&#215

The keyboard isn't bad, either: it's full-size, with plenty of keys -- it's not one of those "space-saving" designs that assigns two or even three functions to every other key -- and it includes so-called Windows 95 keys. Of course, keyboards are a personal thing, but I like this one, and I can write with it.

I could write books with this machine, and, in fact, if I didn't already have the Gateway machine installed upstairs in Alex's old room, I'd probably be taking Blue Streak up with me. Be warned: by today's standards, it's a real heavweight -- about 8 pounds -- if you're considering lugging it around airports, but on the other hand, it really is good enough to be your desktop machine. I don't have room here for as full a report as I'd like to give; but check the Pournelle bonus section on BYTE's Web site for much more on the Nimantics Orion 6&#215

In my judgment, the best upgrade route is not to fiddle with your old system; get a new machine and network it to your old one. Ethernet boards are cheap and getting cheaper, and so are Ethernet PC Cards. Win 95, and for that matter Windows 3.11, make networking simple and painless, and you'll soon find plenty to do with both systems. For one thing, you can do instant backups of important work by sending a copy to the other machine. That practice has saved me more than once.

Full-featured laptops -- like the Nimantics Orion 6&#215

Whatever you do, get a PCI-bus system and a PCI-bus Ethernet card for your new system; they're much easier to set up, and when Plug and Play works, it works very well.

On that subject, we've found there are two kinds of Ethernet cards to consider: 3Com and no-name generics. The no-names are cheap and often work, but if the drivers that come with them don't work well, you'll probably never get anything better. The 3Com cards come with good drivers, and when there are updates, you can download them. A PCI-bus 3Com Internet card will cost maybe $30 more than a no-name card; in my judgment, the peace of mind and absence of installation problems are worth the money.

Understand, this is in the context of a low-cost upgrade by networking; those of you with more serious networking requirements should look into other alternatives, such as Applied Creative Technologies' Ultimate PCI-3000 network card. Of course, if you already have Ethernet cards that work, it's hardly worth buying new cards until you're ready for an upgrade to Fast Ethernet. We'll be doing that one of these days, but for the moment, I've found vanilla Ethernet plenty good enough.

Once you've decided to upgrade by networking, the obvious choice is to get the fastest new system you can afford. Less obvious -- but possibly cheaper and better -- is to get a reliable dual-Pentium system. If you go that route, you'll have to use Windows NT; Win 95 can't make use of your second processor, and given IBM's treatment of OS/2, I can't recommend that to anyone not already using it. That's a pity, but there it is. Fair warning: installation of NT isn't all that simple. If you don't know what you're doing, be prepared for headaches or get it preinstalled.

Once it's installed, you probably won't have any problems. We've been using NT 3.51 for a while, and it works well with a dual-processor system. Now there's NT 4.0, which is much like Win 95, so much so that most times you need to look to be sure you're not running Win 95. NT 4.0 is stable and, except for some DOS and Win 95 games, runs all your software.

If you are running multiple programs, especially if at least one is a DOS program, a dual 120 or 133 will likely be faster than one of the screamingly fast single-processor systems. You will almost certainly win with dual processors if you routinely run more than one DOS session simultaneously. DOS programs eat cycles, and handing control to a DOS program and then taking it back involves a deal of overhead. Dual processors let one run the application while the other does the overhead and housekeeping.

Actually, it's not quite that simple. The OS doesn't say "you do housekeeping and I'll do applications"; rather, the OS passes control back and forth as needed. Still, the effect is the same. The applications get the attention they need while the networking and other OS stuff goes on in the background.

A dual-processor system architecture will let you do all your networking and communications without losing speed. We've been experimenting with Diamond Flower's dual-Pentium Doubleshot 133, and for many multiple tasks, it is by far the fastest machine in the house.

The original Pournelle's law was "one user, one CPU," but that was back when CPUs were really expensive. I've since amended it to "one user, at least one CPU." No one deep down inside likes to share CPU cycles with anyone -- including oneself. I believe multiprocessor systems are the wave of the future. So, incidentally, does Intel. Of course, it's self-serving for Intel to recommend multiple processors, but that doesn't mean it's not a good way to go.

I'm still tracking down the hesitations I get in Win 95. A dozen readers have made helpful suggestions; and I think I now know what the problem is.

The symptom is that every few minutes there's a series of hesitations, typically manifesting itself when I am typing: I strike the key, and nothing happens for half a second or so. This goes on for a couple of seconds and then the system returns to normal.

The strange part is that Pentafluge, a Pentium 60 that was the fastest thing in the house when we built it, didn't have this problem under Windows 3.11; but as soon as we changed over to Win 95, the hesitations began, and we see them in Win 95, Windows 3.11, and DOS programs.

We don't see these hesitations on all the machines; the common element among those that do have the problem is that they all have Intel EtherExpress-16 ISA Ethernet cards. I am told by a reader that all I need to do is get the updated Win 95 EtherExpress drivers, and my glitches will go away.

I don't know if that's true. I downloaded what I thought were the proper Intel drivers. However, when I went to install them, Win 95 refused to believe there were any proper drivers in the directory I'd put them in. To make matters even worse, when I decided to reinstall the EtherExpress card with its original drivers, it took me five tries to get my network restored. The problem is that when Win 95 installs the EtherExpress hardware and default software, it does not automatically install NetBEUI. NetBEUI is an elderly protocol whose major -- almost only -- use is Windows 3.11 and other Microsoft peer-to-peer networks, but you must have it for those.

Worse, the Network Troubleshooter wizard in the Win 95 Help system is almost useless. It does not ask if you have installed NetBEUI, so if you don't know you need that protocol, I don't know how you'd ever find out. I had forgotten I needed it, but since I had other systems networking properly, I could go study one that worked and see what I had left out.

In any event, I'm pretty sure the hesitations are caused by Intel EtherExpress cards running the Win 95 default drivers, and that they can be made to go away by either installing a different Ethernet card or getting the proper drivers for the EtherExpress card. I'll try to test that before we go to press next month.

The first book of the month is also the CD-ROM of the month: Erica Sadun's Java Script CD-CookBook (Charles River Media, ISBN 1-886801-35-5). This is a "book" you read with your Web browser. Clearly written, lots of examples, and probably the first of many "books" done this way.

A more traditional computer book of the month is Mark Warhol's The Art of Programming with Visual Basic (John Wiley and Sons, ISBN 0-471-12853-8). The subtitle is Techniques for Writing Solid Code That's Easy to Maintain, and it is all that and more. The chapter on naming conventions is worth the price of the book. If you do large Visual Basic programs, or you supervise people who do, this is nearly indispensable.

The book of the month is Thomas Cahill's How the Irish Saved Civilization: The Untold Story of Ireland's Heroic Role from the Fall of Rome to the Rise of Medieval Europe (Doubleday, ISBN 0-385-41848-5). It's as much a delightful insight into Irish character as a history. Parts of it are serious enough, but even then you'll hear an echo of Irish laughter.

The game of the month is The Pandora Directive from Access Software. This is one of those role-playing movie games, and frankly I wouldn't have fired it up if I hadn't noticed that my old neighbor John Agar is in it.

It's actually a rather interesting plot hinging around what happened in Roswell, New Mexico, on July 6, 1947, involving UFOs. The acting is quite good. I find the pace of this game to be a bit slow, but that's really saying that I am not usually fond of the kind of game where you must poke around, looking in desk drawers and under rugs, and talking to everyone in sight. For those who do like that kind of game, The Pandora Directive is about as good a one as I have seen.

The piles grow higher at Chaos Manor, and even with the longer column -- see BYTE's Web site for the parts of the column that didn't get into the printed edition -- I can't keep up. We now have CD makers, a lot of great new software, so many CD-ROMs I have lost count, and a whole bunch of stuff I wish I had space to tell you about. The computer revolution isn't slowing down at all.

## Product Information

First Aid 95 Deluxe......................about $59.95

CyberMedia

Santa Monica, CA

+Phone: (800) 721-7824 or (310) 581-4700

Fax: (310) 581-4736

http://www.cybermedia.com

Internet:

http://www.cybermedia.com

Circle 1006 on Inquiry Card.

6Info Select...................................$149.95

Micro Logic Corp.

Hackensack, NJ

+Phone: (800) 342-5930 or (201) 342-6518

Fax: (201) 342-0370

http://www.miclog.com

Internet:

http://www.miclog.com

Circle 1007 on Inquiry Card.

Orion 6&#215

Nimantics, Inc.

Tustin, CA

+Phone: (800) 646-5005 or (714) 573-4030

Fax: (714) 573-4025

http://www.nimantics.com/

Internet:

http://www.nimantics.com/

Circle 1008 on Inquiry Card.

6The Pandora Directive..........................$79.95

Access Software, Inc.

Salt Lake City, UT

+Phone: (800) 800-4880 or (801) 359-2900

Fax: (801) 359-2968

http://www.accesssoftware.com

Internet:

http://www.accesssoftware.com

Circle 1009 on Inquiry Card.

!Sound Blaster Performance 8&#215

Creative Labs, Inc.

Milpitas, CA

+Phone: (800) 998-5227 or (408) 428-6600

Fax: (408) 428-6611

http://www.creativelabs.com

Internet:

http://www.creativelabs.com

Circle 1010 on Inquiry Card.

mailto:"jerryp@bix.com"

Jerry Pournelle is a science fiction writer and BYTE's senior contributing editor. You can write to Jerry c/o BYTE, One Phoenix Mill Lane, Peterborough, NH 03458. Please include a self-addressed, stamped envelope and put your address on the letter as well as on the envelope. Due to the high volume of letters, Jerry cannot guarantee a personal reply. You can also contact him on the Internet or BIX at

jerryp@bix.com
