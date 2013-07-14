#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
see: http://en.wikipedia.org/wiki/Fibonacci_number
Iterate trough suffix (JFYI, they are cyclic)
For each pandigital suffix, calculate fibonacci number.
Need to precalculate math.sqrt(5) with great accutacy, and multiply it
phi = (sqrt(5)+1)/2
F(n) = phi^n/sqrt(5)
"""

import sys
sys.path.append("../lib")
from Fibonacci import Fibonacci

size = 9

def is10PandigitalString(s):
    pattern = tuple(range(1, 10))
    digits = tuple(sorted(map(int, list(s))))
    return digits == pattern

index = 0
number1 = 0
number2 = 1

import math
phi = (math.sqrt(5)+1)/2

def calulcateFirstDigits(index):
    power = index*math.log(phi)
    l10 = math.log(10)
    while power>12*l10:
        power = power - l10 
    f2 = math.exp(power)/math.sqrt(5)
    return f2

print calulcateFirstDigits(1048577)
import sys
sys.exit(0)

while True:
    import time
    index += 1
    number1 = (number1 + number2) % 10**9
    number1, number2 = number2, number1
    strnum = str(number1)
    if (is10PandigitalString(strnum)):
        f2 = calulcateFirstDigits(index)
        f2 = int(f2)
        print index, f2
        if (f2<10**9):
            print "wtf", f2
        if (is10PandigitalString(str(f2)[:9])):
            print index, strnum, f2
            break
