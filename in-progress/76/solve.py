#!/usr/bin/env python
# -*- coding: utf-8 -*-

inputNumber=100

def differentWaysWithMaximum(number, maximum):
    result=(0, [])
    if 0==number:
        result=(1, [[]])
    else:
        for i in reversed(range(1, maximum+1)):
            left=number-i
            if (left>=0):
                numberAndWays=differentWaysWithMaximum(left, i)
                array=result[1]+[([i]+x) for x in numberAndWays[1]]
                result=(result[0]+numberAndWays[0], array)
    #print (number, maximum, result)
    return result

def differentWays(number):
    return differentWaysWithMaximum(number, number-1)

print differentWays(10)
