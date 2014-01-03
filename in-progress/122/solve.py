#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple

#upperLimit = 15
upperLimit = 200

T = namedtuple("T", ["first", "second", "steps"])
t = {1 : [T(None, None, 0)]}

def dijest(number):
    #print number
    result = []
    for s1 in range(1, number/2+1):
        s2 = number - s1
        # FIX this
        if s2 % s1 != 0:
            dumb_steps = t[s1][0].steps + t[s2][0].steps + 1
        else:
            dumb_steps = t[s2][0].steps + 1
        result.append(T(s2, s1, dumb_steps))
    t[number] = sorted(result, key=lambda e: e.steps)
    #print t[number]
    return t[number][0].steps

result = 0
for i in range(1, upperLimit):
    number = i + 1
    multiplications = dijest(number)
    print number, multiplications
    result += multiplications
print result
