---
title: "Running C in a Java World"
publication: "BYTE Magazine"
issue: "November 1996"
section: "State Of The Art"
source_file: "BYTE.DAT"
source_offset: "0x00764a11"
---

# Running C in a Java World

*State Of The Art*

The picoJava design team knew it had to overcome one major hurdle: the Java language has no instructions for manipulating a computer's main memory. Most computers use memory locations to handle all input and output. For example, getting input from a mouse or a keyboard requires reading directly from memory. For security and safety reasons, Java won't allow this, which is why many system designers believe Java is unusable as a general system language.

But picoJava designers had a trick up their sleeves. They simply added new bytecode instructions for reading and writing memory. These instructions won't work on a Java-ready browser, but they will work for Java chips. Someone could even write an entire OS in Java. You also could compile C for Java-only chips and convert memory references. In fact, C is similar enough to Java that a Java chip running C might be faster than a C chip emulating Java.

Copyright

1994-1997 BYTE

}Jv

4Jv

4Jv

4Jv

^Kv

4Jv

Mv

4Jv

8Ov

4Jv

4Jv
