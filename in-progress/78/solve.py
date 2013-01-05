#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://ru.wikipedia.org/wiki/%D0%A0%D0%B0%D0%B7%D0%B1%D0%B8%D0%B5%D0%BD%D0%B8%D0%B5_%D1%87%D0%B8%D1%81%D0%BB%D0%B0#.D0.A0.D0.B5.D0.BA.D1.83.D1.80.D1.80.D0.B5.D0.BD.D1.82.D0.BD.D1.8B.D0.B5_.D1.84.D0.BE.D1.80.D0.BC.D1.83.D0.BB.D1.8B
"""

import math

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

for i in range(1, 101):
    print i, partitions(i)
