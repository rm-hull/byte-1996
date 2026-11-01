---
title: "What's an Asynchronous System?"
publication: "BYTE Magazine"
issue: "November 1996"
section: "Reviews"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x0093c217"
---

# What's an Asynchronous System?

*Reviews*

ObjectGeode addresses one class of real-time systems: asynchronous systems -- those that service nonperiodic events. An example of an asynchronous system is a telecommunications switching system; there's no way for the system to predict when you'll pick up the phone. It's no surprise, then, to find that many of ObjectGeode's customers are in the telecommunications industry.

The other class of real-time systems -- synchronous -- deals with events or signals that arrive within a known period. (The dichotomy is not rigid. Plenty of real-time systems have both synchronous and asynchronous characteristics.) Synchronous systems also tend to be "hard real time" in nature. That is, not only do the events occur with known regularity, the system must service them in a specified amount of time. An example of a synchronous real-time system is a stepper-motor controller. Signal pulses must be transmitted to the motor at a certain frequency, or the motor simply won't step.

Designing a synchronous real-time system amounts to determining how many events will arrive at the system and at what frequency, and deploying tasks (or threads) to handle each event. The developer then explores worst-case scenarios to determine, for example, whether there would be enough horsepower to service events if they all arrived simultaneously.
