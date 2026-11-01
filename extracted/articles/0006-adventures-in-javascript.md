---
title: "Adventures in JavaScript"
publication: "BYTE Magazine"
issue: "December 1996"
section: "Inbox"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x000039cb"
---

# Adventures in JavaScript

*Inbox*

"JavaScript Adventures" (August) offered a refreshingly real-world approach, but it contained some minor discrepancies, and I found it a bit too critical of Java-Script. First, author Rex Baldazo is correct that the document.clear() method doesn't work consistently in any version of Netscape. However, there is a simple work-around: Use document.open(), which also clears the window, then write the new window's content, then use document.close() to finish the display. He also overlooked a much larger issue, though: Once you use document.open() (or document.clear(), if it worked), the current document -- and hence the currently running script -- disappears. Thus it would not be appropriate for the first example, although it is very useful when dealing with multiple windows or frames. Finally, JavaScript's documentation is incomplete and does include some errors, as does the language itself. However, JavaScript is a young language that was still officially beta at the time of your article, so this can be expected to improve. In the meantime, there are Java books that are comprehensive and address the problems.

Michael Moncur

Author, Web Workshop: JavaScript (Sams.net)

mgm@pair.com

The document.open()/document.write()/document.close() work-around is well known. As you point out, though, it overwrites a page and will erase your script unless the script is in one frame and writing to another. If it worked as advertised, document.clear() would let a script manipulate its own page without the risk of destroying itself. While JavaScript may be a young language, Netscape and others have been pushing it as a way to develop real-world Internet and intranet applications. With JavaScript moving to Netscape servers as well, it is vitally important that it be well documented and, more important, that it work as advertised. Sadly, your last observation is also correct: Third-party documentation has often been more useful than Netscape's own. -- Rex Baldazo
