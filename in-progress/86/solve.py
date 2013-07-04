#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Let a, b, c - a dimensions of a cuboid.
Suppose that M>=a>=b>=c . Then a shortest cuboid route will be:
(a**2+(b+c)**2)**.5 , i.e. a hypo of triangle catetes: (a)<=M, (b+c)<=2*M.
Let x=b+c, then , a>=x (?) -> x/2 possibilities, a<x ?
"""

import sys
sys.path.append("../lib"    )
from IsSquare import isSquare

print "test"
"""
Idea: we can generate all P-triplets under M, then calculate all
possible cuboid dimensions
TODO: We can generate primitive triplets only
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
print len(tripletList)

import sys
#sys.exit()
print "test"

def getSpecialCuboidsUnder(M):
    result=0
    for a in range(1, M+1):
        print "# a -> ", a
        for b in range(1, a+1):
            for c in range(1, b+1):
                if (isSquare(a**2+(b+c)**2)):
                    import math
                    print a, b, c, "->", a, b+c, int(math.sqrt(a**2+(b+c)**2))
                    result+=1
    return result

upperLimit=100
print getSpecialCuboidsUnder(10)

#print map(getSpecialCuboidsUnder, range(2, 80))
