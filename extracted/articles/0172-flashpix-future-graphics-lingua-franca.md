---
title: "FlashPix: Future Graphics Lingua Franca?"
publication: "BYTE Magazine"
issue: "November 1996"
section: "Bits"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x005fa777"
---

# FlashPix: Future Graphics Lingua Franca?

*Bits*

Jon Pepper

It isn't often that a file format generates much excitement or offers much to end users, but the new FlashPix architecture may be the exception. Kodak created FlashPix, in collaboration with Hewlett-Packard, Live Picture, and Microsoft, to provide a better way for people to work with digital images. One important design goal of the FlashPix file format, which should now be available, is to let you work with large photographic images without requiring high-end computing power or bandwidth.

FlashPix meets this challenge in an ingenious way, based on the premise that most people don't need to work with all parts of an image at once. Images saved in the FlashPix format are automatically stored in a tiled format of 64 pixels per square. In this way, you can save images of any size, and when a FlashPix-optimized software program asks for data, only the specific tile or tiles requested are loaded into memory. The benefits of this approach: Photo editing is much faster because only the affected area is loaded into memory, and the changes are available almost instantly for the same reason.

FlashPix stores single images at multiple resolutions and enables applications to automatically choose the best resolution for a particular activity. You can thus access a smaller low-resolution image for an on-line preview and then download a bigger high-resolution copy of the image. This should eliminate the long waits currently associated with viewing high-quality graphics on the Web.

Another big plus is FlashPix's ability to save edits as a linked file, which can reduce storage requirements, especially for graphic artists who often save multiple versions of the same image. You can link edits to an original file but store the edits separately, thus eliminating the need to store multiple versions of the entire file.

At press time, there was only one program, Microsoft's Picture It, an image-editing application, that supported FlashPix. Software Development Kits (SDKs) for writing Windows and Mac FlashPix applications should now be available. Several vendors may incorporate FlashPix into scanners, printers, and digital cameras. Microsoft says that it will incorporate FlashPix into its Internet Explorer Web browser.

However, not everyone has endorsed FlashPix. One notable company that had not committed to the format as of press time was Adobe. Kodak officials say they will continue to discuss FlashPix with Adobe and others. If the standard is successful, FlashPix could make digital imaging easier, faster, and more fun.
