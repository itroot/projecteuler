#!/usr/bin/env python
# -*- coding: utf-8 -*-

upperLimit=100

maxSum=0

for a in range(1, upperLimit+1):
    for b in range(1, upperLimit+1):
        number=a**b
        sumOfDigits=sum(map(lambda e: int(e), str(number)))
        maxSum=max(maxSum, sumOfDigits)
        
print maxSum
