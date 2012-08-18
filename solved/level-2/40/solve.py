#!/usr/bin/env python
# -*- coding: utf-8 -*-

upperLimit=10**6

decimalFraction="."
counter=1
while (len(decimalFraction)<=upperLimit):
    decimalFraction+=str(counter)
    counter+=1

result=1
for i in map(lambda e: 10**e, range(0,7)):
    result*=int(decimalFraction[i])
print result
