#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from Factorize import *

class AllDivisors:
    def __init__(self, factorization):
        self.__powers=factorization2power(factorization)
        self.__uniqueSortedFactors=sorted(self.__powers)
        self.__divisors=[]
        self.__generate(1, 0)
        self.__divisors=sorted(self.__divisors)
    def __generate(self, value, uniqueFactorNum):
        if (uniqueFactorNum==len(self.__uniqueSortedFactors)):
            self.__divisors.append(value)
            return
        factor=self.__uniqueSortedFactors[uniqueFactorNum]
        power=self.__powers[factor]
        for p in range(0, power+1):
            self.__generate(value*factor**p,uniqueFactorNum+1)
    def divisors(self):
        return self.__divisors

def getAllDivisors(number):
    if (1==number):
        return [1]
    factors=factorize(number)
    allDivisors=AllDivisors(factors)
    return allDivisors.divisors()

def isAmicable(number):
    other=sum(getAllDivisors(number)[:-1])
    if (0==other):
        return False
    otherSum=sum(getAllDivisors(other)[:-1])
    return number==otherSum

amicables=set()
for i in range(1, 10000):
    if isAmicable(i):
        opposite=sum(getAllDivisors(i)[:-1])
        if i!=opposite:
            amicables.add(tuple(sorted([i, opposite])))

result=0
for amicable in amicables:
    result+=sum(amicable)
print result