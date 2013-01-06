#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://ru.wikipedia.org/wiki/%D0%A0%D0%B0%D0%B7%D0%B1%D0%B8%D0%B5%D0%BD%D0%B8%D0%B5_%D1%87%D0%B8%D1%81%D0%BB%D0%B0#.D0.A0.D0.B5.D0.BA.D1.83.D1.80.D1.80.D0.B5.D0.BD.D1.82.D0.BD.D1.8B.D0.B5_.D1.84.D0.BE.D1.80.D0.BC.D1.83.D0.BB.D1.8B
"""

import math

upperLimit=10101
table=[[1]]
for n in range(1, upperLimit):
    table.append([0])
    for k in range(1, n+1):
            currentList=table[n]
            addendFirst=currentList[k-1]
            addendSecond=None
            if (n-k<k):
                addendSecond=table[n-k][n-k]
            else:
                addendSecond=table[n-k][k]
            currentList.append((addendFirst+addendSecond)%10**6)
    number=table[n][n]
    print n
    if number%10**6==0:
        print number
        break

#print map(lambda e: e[-1:], table)

import sys
sys.exit(0)

cache={}

def P(n, k):
    if n==0 and k==0:
        return 1
    elif k==0:
        return 0
    else:
        kn=(k, n)
        if kn in cache:
            return cache[kn]
        if k<=n:
            result=P(n-k, k)+P(n, k-1)
        else:
            result=P(n, n)
        cache[kn]=result
        return result

def partitions(n):
    return P(n, n)

for i in range(1, 10000):
    for k in range(1, i):
        P(i, k)
    result=partitions(i)
    print i, result
    if result%10**6==0:
        break
