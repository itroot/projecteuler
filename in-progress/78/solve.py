#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://en.wikipedia.org/wiki/Partition_(number_theory)#Intermediate_function
"""

import math

cache={}

def p(k, n):
    if k>n:
        return 0
    elif k==n:
        return 1
    else:
        nk=str(n)+"/"+str(k)
        if nk in cache:
            return cache[nk]
        else:
            result=p(k+1, n)+p(k, n-k)
            cache[nk]=result
            return result

def partitions(n):
    return 1+sum(map(lambda k: p(k, n-k), range(1, int(math.floor(n/2)))))

for i in range(1, 100):
    print partitions(i)
