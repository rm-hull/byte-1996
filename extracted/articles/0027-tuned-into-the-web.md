---
title: "Tuned Into the Web"
publication: "BYTE Magazine"
issue: "December 1996"
section: "Bits"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x000e3f27"
---

# Tuned Into the Web

*Bits*

Sangam Pant

d, vice president of engineering at Lycos, discusses how best to find sights and sounds on the Web.

BYTE: Lycos recently added sound- and picture-specific searching. How do you do this?

Pant: As we do with regular HTML text searching, our spiders get documents and create abstractions of them. In creating the abstract, it figures out things such as key words. It also looks for some specific fielded information like who is the author of the document and what's the title of the document.

But more important is that it figures out the key words and phrases in the document. We use computer heuristics to determine the importance of these words and phrases within the document. The advantage of creating the abstract is in size. You are not storing the whole document, you're only storing a portion of the document. Another advantage is that you don't violate any copyright law, because you are not storing the document. And last but not least is that it helps us figure out what are the critical pieces of the document. We also compare the number of times a word appears in a document compared to the average number of times the word appears in other documents we've indexed to determine relevance.

BYTE: Does this approach help you screen out pages that have certain words arbitrarily slapped onto them to attract surfers?

Pant: We know that at times people jam words into documents on their Web pages that really don't relate to the document itself. That's one form of what's called spamming. And so our newer versions of our search engines need anti-spam code. We now have spam detectors that can go in and figure out where spam is. Those spam-detection algorithms keep changing. It's basically like cops and robbers. When we add spam detection code, there's always a new variation of spam people introduce into their document to avoid our detectors. So one of the things you may have noticed when you're doing searching for images or sounds using Lycos was the fact that with a certain combination of words you find a certain set of documents. And from two slightly different sets of words in your search, you may find two different clips, but both from the same movie. This is because the importance of the words showing up in a clip was different in one title of a clip versus some other title of another clip.

BYTE: From the abstract, how do you identify images and sounds? I'm assuming that you do more than just look for extensions such as AVI or GIF.

Pant: Anybody can do the extension matching and say this is a GIF versus a WAV versus an AVI file. That's the easiest part of it. We go a step further than that because we treat pictures and sound and documents as similar objects, but we look at the characteristics of these objects. And we look at what describes the picture and sound file itself.

BYTE: So you analyze text that acts as a caption for an image or sound?

Pant: Right. But not only do we look at that, we look at the content of the page itself that contains the embedded object. If the entire page is talking about computers, and a person doing a search wants a picture of the computer, it makes sense that the image in question is a picture of a computer. You can take it a step further and say that if you have 15 links pointing to the .gif and all those links are from computer-oriented sites, your certainty that this is a picture of a computer goes up drastically. In the grand scheme of things, the Web is really a network of documents, and links carry the most important information.

BYTE: What about situations where you've got Web sites where a few sample graphics are available for public viewing for free, but you have to pay for access to view the rest of the images. Is there a way for you guys to handle that?

Pant: Our job is pretty much to catalog the World Wide Web. But if our spider goes to a site with an exclusion tag that says don't spider this document, we are good citizens. If we come across these kinds of exclusions, we don't go any further. If we come across a site that is using a username/password, we have the ability to actually supply the username. We log the fact that we came across a site that has username/passwords and our spiders have the ability to be able to go in with a username password and then index the site. But we do that on a case by case basis.

BYTE: Could those people that are operating Web clip-art sites somehow make information available to your spider without letting people view them for free publicly?

Pant: We can definitely work out something like that.

BYTE: Is there a way they can do that automatically or is it done on a case by case basis?

Pant: We are trying to automate that as much as possible. It's not fully automated yet. My job is to go out and help people find stuff on the Web. And the fact that the site charges or doesn't charge for that piece of information is something that I don't want to get in between. That's a transaction between the person who is trying to get the information and the person who has the information. My job is to make sure that the person who is trying to find the information finds it in the first place.

BYTE: Are you actually doing the equivalent of optical character recognition on the image anywhere in your process? For example, does your engine look at just the bitmap and determine, for example, that it's a girl with a cat?

Pant: Not in the current version, because that is, computationally-based, very extensive. Think of all the little pictures on the Web. Trying to catalog them all and for each picture, basically using some kind of optical character recognition to figure out whether this is of a particular object or not, becomes extremely difficult. I think the technology exists but I don't think it's available to be deployed at the volume that you're talking about. My take on this personally is that we should move the onus to the person who creates the image. What I would really like is a standard that says that when you create the image, a bunch of metatags that describe the image get created along with it. That would make everybody's life a lot easier.

http://www.lycos.com

For more information, see

http://www.lycos.com

## Sangam Pant, VP, Lycos

## Images

![image-0014.gif](../images/image-0014.gif)
