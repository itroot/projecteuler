#!/usr/bin/env python
# -*- coding: utf-8 -*-

inputNumber=100

def differentWaysWithMaximum(number, maximum):
    result=(0, [])
    if 1==maximum:
        result=(1, [[1 for i in range(0, maximum)]])
    else:
        for i in range(1, maximum+1):
            newNumber=number-i
            if (newNumber>0):
                numberAndWays=differentWaysWithMaximum(newNumber, i)
                array=result[1]+[([newNumber]+x) for x in numberAndWays[1]]
                result=(result[0]+numberAndWays[0], array)
    #print (number, maximum, result)
    return result

def differentWays(number):
    return differentWaysWithMaximum(number, number)

print differentWays(5)
