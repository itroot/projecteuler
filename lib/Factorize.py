# -*- coding: utf-8 -*-

import math
from EratosthenesSieve import *

class Factorization:
    def __init__(self):
        self.__sieve=sieve=EratosthenesSieve()
        self.__cache={}
    def factorize(self, factoree):
        number=factoree
        #if 1000==number:
        #    print self.__cache
        sieve=self.__sieve
        if (number<2):
            raise Exception("Can't factorize %d" % number)
        sqrtnumber=int(math.ceil(math.sqrt(number)))
        factorization=[]
        sieve.growToNumber(sqrtnumber+1)
        sieve=sieve.sieve()
        for prime in sieve:
            while True:
                if 1==number:
                    break
                elif (0==number%prime):
                    factorization.append(prime)
                    number=number/prime
                    if (number in self.__cache):
                        #print "Hit"
                        factorization+=self.__cache[number]
                        number=1
                        break
                else:
                    break
        if (1!=number):
            factorization.append(number)
        self.__cache[factoree]=factorization
        return factorization

def factorize(number):
    f=Factorization()
    return f.factorize(number)
    
def factorization2power(factorization):
    result={}
    for factor in factorization:
        if factor in result:
            result[factor]+=1
        else:
            result[factor]=1
    return result

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
