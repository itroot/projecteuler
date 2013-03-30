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

print "test"
"""
Idea: we can generate all P-triplets under M, then calculate all
possible cuboid dimensions
"""
tripletList=[]
M=100
for m in range(1, M):
    for n in range(1, m):
        triplet=(m**2-n**2, 2*m*n) #, m**2+n**2)
        if not all(map(lambda e: e<=M, triplet)):
            break
        else:
            tripletList.append(triplet)
print tripletList
import sys
sys.exit()
print "test"

def getSpecialCuboidsUnder(M):
    result=0
    for c in range(1, M+1):
        for b in range(c, M+1):
            for a in range(b, M+1):
                if (isSquare(a**2+(b+c)**2)):
                    result+=1
    return result

upperLimit=100
print getSpecialCuboidsUnder(upperLimit)

print map(getSpecialCuboidsUnder, range(2, 80))
