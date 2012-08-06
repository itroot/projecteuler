#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from Factorize import *

upperLimit=1000000
length=3

class FactorizationMemoize:
    def __init__(self):
        self.__f=Factorization()
        self.__cache={}
    def factorize(self, number):
        numberCached=self.__cache.get(number)
        if None==numberCached:
            numberCached=self.__f.factorize(number)
            self.__cache[number]=numberCached
            return numberCached
        else:
            return numberCached
def main():
    f=FactorizationMemoize()
    for i in range(2, upperLimit):
        if i%100==0:
            print i
        numbers=range(i, i+length)
        factorizations=map(lambda e: set(f.factorize(e)), numbers)
        if not reduce(lambda a, b: a and (len(b)==length), factorizations, True):
            continue
        else:
            print i, factorizations
            break

main()
