#!/usr/bin/env python
# -*- coding: utf-8 -*-

rangeStart=1
rangeEnd=101

def SquaresSumRange(lower, upper):
    result=0
    for i in range(lower, upper):
        result+=i*i
    return result

def SquareOfSumRange(lower, upper):
    result=0
    for i in range(lower, upper):
        result+=i
    result=result*result       
    return result

print SquareOfSumRange(rangeStart, rangeEnd)-SquaresSumRange(rangeStart, rangeEnd)
