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
    factors=factorize(number)
    allDivisors=AllDivisors(factors)
    return allDivisors.divisors()

print getAllDivisors(220)
