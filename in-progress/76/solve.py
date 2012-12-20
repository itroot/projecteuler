#!/usr/bin/env python
# -*- coding: utf-8 -*-

inputNumber=100

def differentWaysWithMaximum(number, maximum):
    result=None
    if 1==maximum:
        result=1
    else:
        for i in range(1, maximum+1):
            newNumber=number-i
            if (newNumber>=0):
                result+=differentWaysWithMaximum(newNumber, i)
    #print (number, maximum, result)
    return result

def differentWays(number):
    return differentWaysWithMaximum(number, number)

print differentWays(5)