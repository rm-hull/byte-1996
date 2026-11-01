---
title: "Programming with BSP"
publication: "BYTE Magazine"
issue: "November 1996"
section: "Core Technologies"
copyright: "1994-1997 BYTE"
source_file: "BYTE.DAT"
source_offset: "0x0073921f"
---

# Programming with BSP

*Core Technologies*

BSP doesn't require the invention of any new programming languages. You can write BSP programs in conventional sequential languages such as C or FORTRAN 90. You then link the program to a library that implements a few primitive BSP operations.

The simplest primitives are bsp_put and bsp_get, which are requests for nonlocal data access, and bsp_sync, which marks a barrier for synchronization. Put and get are both one-sided operations, and you don't need to pair them: You either put a value into a remote process or get a value from it, but not both. They do, however, require variables to have the same names in different physical address spaces, so they are most suited for Single Program Multiple Data (SPMD) algorithms.

Other BSP primitives are better suited for different types of parallelism. Put and get are nonblocking, so the process that calls them can proceed immediately. Issuing a put or get guarantees only that the requested data operation will be completed by the end of the superstep or next barrier synchronization.

The C function, bsp_allsums(), hints at the flavor of BSP programming. It calculates the running sums of p integers stored on p processors. Put another way, if integer xi is stored on processor i, the result on processor i is x0 + x1 + ... + xi.

You use the primitives bsp_pushregister and bsp_popregister to register the name of the destination variable left across all the processors. The cost of this algorithm is log(p)x(g + l + 1) + l, as there are log(p) + 1 supersteps (including one for the registration), and the addition operation costs 1 FLOP.

## BSP Code Fragment

#include "bsp.h"

#include

#include

int bsp_allsums(int x) {

int i, left, right;

& bsp_pushregister(&left,sizeof(int));

bsp_sync();

right = x;

- for(i=1;i if (bsp_pid()+i < bsp_nprocs())

4 bsp_put(bsp_pid()+i,&right,&left,0,sizeof(int));

bsp_sync();

* if (bsp_pid()>=i) right = left + right;

bsp_popregister(&left)

return right;
