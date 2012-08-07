#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

factorials=map(lambda e: math.factorial(e), range(0, 10))

def factorialSum(number):
    return reduce(lambda a, b: a+b, map(lambda e: factorials[int(e)], str(number)))

numbers=[]
for i in range(1, factorials[9]*7):
    if i==factorialSum(i):
        if 1!=i and 2!=i:
            numbers.append(i)

print sum(numbers)
