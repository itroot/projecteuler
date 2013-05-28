#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib/")
import Factorize

upperLimit=12000+1

divisorListMap={}

def divisors(number):
    if not number in divisorListMap:
        divisorListMap[number]=Factorize.getAllDivisors(number)[1:]
    return divisorListMap[number]

for number in range(2, 2*upperLimit):
    divisorListMap[number]=divisors(number)
    if number==2000:
        break

from collections import defaultdict

answerMap=defaultdict(list)

def dig(number, divisorList, path):
    if len(divisorList)==0:
        index=number-sum(path)+len(path)
        if index>1:
            answerMap[index].append(number)
        #print number, path, index
    for divisor in divisorList:
        if (len(path)!=0 and divisor>path[-1]):
            continue
        dig(number, divisors(reduce(lambda a, b: a/b, path, number/divisor)), list(path)+[divisor])

for number in range(2, 2*upperLimit):
    dig(number, divisors(number), [])

import pprint

#pprint.pprint(dict(answerMap))

print sum(set(map(lambda e: min(e[1]), filter(lambda e: e[0]<upperLimit, dict(answerMap).iteritems()))))

"""
def product(numberList):
    return reduce(lambda a, b: a*b, numberList, 1)

k7=[1, 1, 1, 1, 1, 2, 7]
k8=[1, 1, 1, 1, 1, 1, 2, 8]
k9=[1, 1, 1, 1, 1, 1, 1, 2, 9]
k10=[1, 1, 1, 1, 1, 1, 1, 1, 2, 10]
# so at least it <=n*2
kn=k8
print "product:", product(kn)
print "sum:", sum(kn)
"""
