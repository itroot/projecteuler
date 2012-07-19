#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Fibonacci:
    def __init__(self):
        self.__cache=[0, 1]
    def __PopulateCacheUntil(self, position):
        length=len(self.__cache)
        for i in range(length, position+1):
            self.__cache.append(self.__cache[i-1]+self.__cache[i-2])
    def GetNumberAtPosition(self, position):
        if (position>=len(self.__cache)):   
            self.__PopulateCacheUntil(position)
        return self.__cache[position]

MAX_FIBONACCI=4000000
fibonacci=Fibonacci()
position=0
result=0

while True:
    fibonacciNumber=fibonacci.GetNumberAtPosition(position)
    if (fibonacciNumber>MAX_FIBONACCI):
        break
    if (0==fibonacciNumber%2):
        result+=fibonacciNumber
    position+=1

print result
