#!/usr/bin/env python
# -*- coding: utf-8 -*-

lowerLimit = 3
upperLimit = 1000

def rmax(a):
    isEven = (0 == a%2)
    if isEven:
        return (a-2)*a
    else:
        return (a-1)*a

result = 0

for i in range(lowerLimit, upperLimit + 1):
    result += rmax(i)

print result