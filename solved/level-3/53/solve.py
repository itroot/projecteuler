#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

upperLimit=100
minC=10**6

def C(n, k):
    f=math.factorial
    if n<k:
        raise Exception("n<k")
    return f(n)/(f(k)*f(n-k))

#print C(5, 3)
count=0
for n in range(0, upperLimit+1):
    for k in range(0, n+1):
	if C(n, k)>minC:
            count+=1
print count
