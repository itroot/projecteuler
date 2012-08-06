#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class EratosthenesSieve:
    def __init__(self):
        self.__sieve=[2]
        self.__upperBound=self.__sieve[-1]
    def sieve(self):
        return self.__sieve
    def __isFactoringWithSieve(self, number):
        numberSqrtPlusOne=int(math.ceil(math.sqrt(number)))+1
        for prime in self.__sieve:
            if (prime>numberSqrtPlusOne):
                return False
            if (0==number%prime):
                return True
        return False
    def growToNumber(self, number):
        current=self.__upperBound
        while (current<=number):
            if (not self.__isFactoringWithSieve(current)):
                self.__sieve.append(current)
            current+=1
        self.__upperBound=number

