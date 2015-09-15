#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from fractions import gcd
from Factorize import factorize

def rad_factorize(n):
    if n == 1:
        return []
    else:
        return factorize(n)

def rad(a, b, c):
    rad_set = set(rad_factorize(a) + rad_factorize(b) + rad_factorize(c))
    return reduce(lambda e, f: e*f, rad_set, 1)

c_list = []

for c in range(1, 1000):
    for a in range(1, c/2):
        b = c - a
        #print a, b, c
        if gcd(a, b) != 1:
            continue
        if gcd(a, c) != 1:
            continue
        if gcd(b, c) != 1:
            continue
        rad_value = rad(a, b, c)
        if rad_value < c:
            print a, b, c, rad_value
            c_list.append(c)

print sum(c_list)
