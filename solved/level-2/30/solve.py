#!/usr/bin/env python
# -*- coding: utf-8 -*-

power=5

def sumOfPowersOfDigits(number, power):
    return reduce(lambda a, b: a+b, map(lambda e: int(e)**power, str(number)))

result=0
for i in range (2, 9**5*6):
    if (i==sumOfPowersOfDigits(i, power)):
        result+=i
print result