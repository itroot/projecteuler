#!/usr/bin/env python
# -*- coding: utf-8 -*-

class EratosthenesSieve:
    def __init__(self):
        self.__sieve=[2]
    def sieve(self):
        return self.__sieve
    def __isFactoringWithSieve(self, number):
        for prime in self.__sieve:
            if (0==number%prime):
                return True
        return False
    def growToNumber(self, number):
        current=self.__sieve[0]
        while (current<number):
            if (not self.__isFactoringWithSieve(current)):
                self.__sieve.append(current)
            current+=1
