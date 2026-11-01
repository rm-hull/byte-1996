---
title: "Getting Along with Alta Vista"
publication: "BYTE Magazine"
issue: "November 1996"
section: "Web Project"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x008482be"
---

# Getting Along with Alta Vista

*Web Project*

Web-component interactions run back and forth along a two-way street. The BYTE Site now uses AltaVista as a component of Metasearch. But conversely, Alta-Vista uses The BYTE Site as a content-providing component. We're the source of about 5000 of the nearly 20 million pages in AltaVista's vast index. The API that AltaVista (or any robotic indexer) uses to access The BYTE Site (or any Web site) is the same as the one that humans use: uniform resource locators (URLs). Thus, you don't need to do anything special to make your site a pluggable AltaVista component.

Some Webmasters worry -- with reason -- that a robotic indexer will fetch too many pages too quickly and render a site unresponsive to normal users. That isn't a problem with AltaVista, which adapts dynamically to your site's ability to pump out pages. When I first heard about AltaVista last winter, I was amazed to learn it had already indexed our site.

Why the surprise? After a few other robots had applied heavy suction to our server, I added a "pig report" to my daily log processing. It highlights visitors who pull more than 1 percent of any day's pages. These high-volume customers are invariably Web crawlers. I like to keep track of who they are and how they use the data they vacuum out of my server.

But AltaVista never showed up on the pig report. Its inventor, Louis Monier, later explained why. Scooter, the AltaVista spider, measures the time it takes to fetch a page from each of the hundred-odd sites it visits concurrently. It multiplies that interval by what Monier calls a "good-guy factor" and waits that long between fetches. Thus, Scooter can concurrently fetch once per second from a major site on a T3 link, and once every 5 minutes from a minor site on a 28.8-Kbps dial-up link.

The Robot-Exclusion Standard

There's an API that can govern site/Web-crawler interaction. It's called the robot-exclusion standard, and your site implements it by placing directives into a file called robots.txt at the Web-server root. Here is the robots.txt file that I use on several BYTE Site development servers to lock out robots completely:

User-agent: *

Disallow: /

Why? A few months back, I did an AltaVista search and turned up URLs pointing not only to www.byte.com, but also to a backup archive on one of my development servers. I checked its log and found that about 5 percent of the official site's traffic had diverted to the backup server. Worse, the archive was several months out of date.

How did this happen? I'd let a page on the official site include a pointer to an unrestricted subtree on the backup server. Scooter found the hole and jumped through. Yikes!

To prevent Inktomi and WebCrawler and the rest from following suit, I plugged the hole using access controls and (for good measure) robots.txt. But AltaVista to this day remembers these unofficial URLs, and there's no way I can make it forget them.

An ambitious fix would be to regenerate the archive on the backup server, substituting redirection headers for documents. My less ambitious fix was to lock down the backup server and rig it to tell people to look instead on www.byte.com. If you're one of those people, I apologize for allowing the sorcerer's apprentice to run amok. Learn from my mistakes and use robots.txt (along with regular access controls) to protect what you don't want to publish.

## AltaVista's Altruism

Problem: Robotic indexers can clog your Web site by trying to fetch

& too many pages too quickly.

Solution: AltaVista's indexer, called Scooter, multiplies the time it

F takes to fetch a page by a "good-guy factor." Thus, Scooter

C dynamically adapts itself to each site's ability to send

out pages.

Result: Scooter may call upon a major site with a T3 link to pump

B pages at a rate of one per second, while the rate for a

A site with a 28.8-Kbps link may be one every 5 minutes.
