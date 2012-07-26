#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

upperLimit=2

digits=range(0, upperLimit+1)

# 0 012 -> 0 12
# 1 021 -> 1 21
# 2 102
# 3 120
# 4 201
# 5 210


def nth_permutation(digits, number):
    length=len(digits)
    factorial=math.factorial(length)
    if (number<0 or number>=factorial):
        raise Exception("Incorrect parameters, digits: %s, number: %d" % (str(digits), number))
    if (0==number):
        return digits
    if (number<=factorial):
        return [digits[0]]+nth_permutation(digits[1:], number)
    else:
        divide_result=number//(length)
        reminder=number%(length)

for i in range(0, math.factorial(upperLimit+1)):
    print nth_permutation(digits, i)
