#!/usr/bin/env python
# -*- coding: utf-8 -*-

def generate1to6Multiplies(number):
    return list(number*i for i in range(1, 7))
#print generate1to6Multiplies(125874)

def assureEqualDigitsSet(numberList):
    sortedDigitsSet=set(map(lambda e: "".join(sorted(list(str(e)))), numberList))
    return 1==len(sortedDigitsSet)
#print assureEqualDigitsSet([12, 22])

upperBound=1000000
for i in range(1, upperBound):
    multiplies=generate1to6Multiplies(i)
    if (assureEqualDigitsSet(multiplies)):
        print i
        break
