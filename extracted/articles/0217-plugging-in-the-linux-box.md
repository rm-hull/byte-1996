---
title: "Plugging in the Linux Box"
publication: "BYTE Magazine"
issue: "November 1996"
section: "Web Project"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x00849c4a"
---

# Plugging in the Linux Box

*Web Project*

A few months back, analysis of the keywords used to search The BYTE Site revealed that Linux ranked fifth. Clearly, a lot of visitors knew something I didn't, and I resolved to find out what.

Today, a P150-based Dell running the Caldera distribution of Linux is an increasingly important pillar of The BYTE Site. All our conferences run there; INND supports newsreaders, and Apache provides an alternate Web-based view. I transfer files between Windows NT servers and Unix servers using Samba, a nifty SMB utility that makes the Linux server look like an NT peer file server.

And when I found that the key component of Metasearch (a Perl 5 module called Wire.pm) didn't like my NT Perl setup, I didn't waste time figuring out why. (A lot of Perl tools, though in principle are portable, in practice work better with Unix.) It was easier to build and run Metasearch over on the Linux box, so I did.

What's delightful about Web development is that the components you build can float effortlessly from one platform to another. NT and Unix offer complementary strengths. Exploit them both. And if you want to deploy a Unix system as part of the mix, Linux is a really useful one.
