---
title: "Making the Data Connection"
publication: "BYTE Magazine"
issue: "November 1996"
section: "BYTE Software Lab Report"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x0080f153"
---

# Making the Data Connection

*BYTE Software Lab Report*

Many types of multimedia applications -- encyclopedias, kiosks, even some games -- depend on sophisticated databases. For these applications, a tool that supports database access is a necessity. All the products we tested offer some form of database support, but they vary drastically in how easy these functions are to use.

ToolBook II Instructor was by far the easiest for adding a database to our kiosk application. ToolBook has a database utility that parses database files and automatically creates a database front end with fields, labels, and browsing buttons. Unfortunately, what ToolBook gains in ease it loses in flexibility because dBase and Paradox are the only two file formats it supports. The other three programs are all compliant with Open Database Connectivity (ODBC) and support many database formats through the Microsoft ODBC driver.

Of these three, Innovus Multimedia was the easiest to use to add the database to the kiosk. It aids in formatting the screen by adding the field placeholders and record navigation buttons. In both Authorware and IconAuthor, the application designer has to add the proper field placeholders, labels, and record navigation buttons manually and individually. The process lacks the automation found in Innovus Multimedia.

Authorware's tutorial material for creating a kiosk application is less than satisfactory. The program comes with a sample application describing how to set up connections to various database formats and a booklet on connecting to databases using Microsoft's ODBC driver. But to succeed in using a database with an Authorware-constructed project, you will need a working knowledge of database structures and SQL statements. There are no automated tools to help here.
