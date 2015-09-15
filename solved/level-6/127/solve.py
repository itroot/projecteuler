#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from fractions import gcd
from Factorize import factorize

known_f = {
    1: (set(), []),
}

def rad_factorize(n):
    result = known_f.get(n)
    if result is None:
        f = factorize(n)
        result = (set(f), f)
        known_f[n] = result
        return result
    else:
        return result

def is_rad_gcd(a, b):
    #return gcd(a, b) != 1
    a_f = rad_factorize(a)[0]
    b_f = rad_factorize(b)[0]
    return len(a_f & b_f) != 0

def rad(a, b, c):
    rad_set = rad_factorize(a)[0] | rad_factorize(b)[0] | rad_factorize(c)[0]
    return reduce(lambda e, f: e*f, rad_set, 1)

c_list = []

def has_repeated_fractions(n):
    (s, d) = rad_factorize(c)
    prev = 0
    ok = False
    if len(d) == 0:
        return True
    for a in d:
        if prev == a:
            ok = True
        prev = a
    return ok

#upper_limit = 1000
upper_limit = 120000
for c in range(1, upper_limit):
    if not has_repeated_fractions(c):
        continue
    for a in range(1, c/2):
        b = c - a
        if not has_repeated_fractions(a):
            continue
        if not has_repeated_fractions(b):
            continue
        #print a, b, c
        if is_rad_gcd(a, b):
            continue
        if is_rad_gcd(a, c):
            continue
        if is_rad_gcd(b, c):
            continue
        rad_value = rad(a, b, c)
        if rad_value < c:
            print a, rad_factorize(a)
            print b, rad_factorize(b)
            print c, rad_factorize(c)
            print rad_value, rad_factorize(rad_value)
            print "====="
            print 
            c_list.append(c)

print sum(c_list)
