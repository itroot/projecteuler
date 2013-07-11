#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
see: http://en.wikipedia.org/wiki/Fibonacci_number
Iterate trough suffix (JFYI, they are cyclic)
For each pandigital suffix, calculate fibonacci number.
Need to precalculate math.sqrt(5) with great accutacy, and multiply it
phi = (sqrt(5)+1)/2
"""

import sys
sys.path.append("../lib")
from Fibonacci import Fibonacci

def isPandigitalString(s):
    pattern = tuple(range(1, 10))
    digits = tuple(sorted(map(int, list(s))))
    #print digits, pattern
    return digits == pattern

f = Fibonacci()
for i in range(0, 1000000):
    stringNumber = str(f.GetNumberAtPosition(i))
    prefix = stringNumber[-9:]
    suffix = stringNumber[:9]
    if isPandigitalString(prefix) and isPandigitalString(suffix):
        print  i
