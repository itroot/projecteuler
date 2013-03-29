#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Let a, b, c - a dimensions of a cuboid.
Suppose that M>=a>=b>=c . Then a shortest cuboid route will be:
(a**2+(b+c)**2)**.5 , i.e. a hypo of triangle catetes: (a)<=M, (b+c)<=2*M.
"""

import sys
sys.path.append("../lib"    )
from IsSquare import isSquare

M=100

result=0
for c in range(1, M+1):
    for b in range(c, M+1):
        for a in range(b, M+1):
            if (isSquare(a**2+(b+c)**2)):
                result+=1

print result

