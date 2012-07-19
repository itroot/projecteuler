#!/usr/bin/env python
# -*- coding: utf-8 -*-

class EratosthenesSieve:
    def __init__(self):
        self.__sieve=[2]
    def sieve(self):
        return self.__sieve
    def growToNumber(self, number):
        current=self.__sieve[0]
        print current
        while (current<number):
            for prime in self.__sieve:
                if (0==current%prime):
                    break
                self.__sieve.append(current)
            current+=1
                    
        


def factorize(number):
    current=2
    sieve=[2]
    factorization=[]
    
    return factorization
    
    

number=int(open("input.txt").read())
print factorize(number)
sieve=EratosthenesSieve()
sieve.growToNumber(1000)
print sieve.sieve()
