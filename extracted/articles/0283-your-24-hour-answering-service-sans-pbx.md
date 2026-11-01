---
title: "Your 24-Hour Answering Service Sans PBX"
publication: "BYTE Magazine"
issue: "November 1996"
section: "International Features"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x00a058ea"
---

# Your 24-Hour Answering Service Sans PBX

*International Features*

PBXes normally have around three times as many internal extensions as incoming trunks. If you want more trunks than extensions, and if you want to use ISDN's multiple subscriber numbers and have up to 100 numbers per trunk, you have a problem.

Service Centrale Benelux (Oss, The Netherlands), a 24-hour guard and security service, had this requirement when it implemented a smart-call monitoring and answering system to reduce the number of false break-in alarms. "Each of our clients is allocated a dedicated phone number," says Ingo Heijst of Service Centrale Benelux.

"Currently, we have more than 100 incoming phone numbers but only a handful of agents. In the future, there will be more, but they will not need additional agents." So the company deployed a PC-based switch solution on a Windows NT server with an ISDN 30B line-interface card and a station-interface board from VSN Systemen that connects directly to the phones. A Pentium Pro machine runs a call-monitoring application based on VSN's Open Telephony Service middleware that is not limited to the number of incoming calls. A 486 backup server running the same application updated by standard NT replication facilities guarantees 24-hour operation without downtime.
