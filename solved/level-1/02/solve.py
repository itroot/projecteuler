#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from Fibonacci import *

MAX_FIBONACCI=4000000
fibonacci=Fibonacci()
position=0
result=0

while True:
    fibonacciNumber=fibonacci.GetNumberAtPosition(position)
    if (fibonacciNumber>MAX_FIBONACCI):
        break
    if (0==fibonacciNumber%2):
        result+=fibonacciNumber
    position+=1

print result
