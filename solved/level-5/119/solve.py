#!/usr/bin/env python
# -*- coding: utf-8 -*-

# NB 2**8 == 4**4 -> this case

def digitSum(number):
    return sum(map(int, str(number)))
x = []

for i in range(2, 200):
    for j in range(2, 200):
        number = i**j
        result = digitSum(number)
        if i == result:
            x.append((i, j, number))
x = sorted(x, key=lambda e: e[2])
#import pprint
#pprint.pprint(x)
print x[29]
