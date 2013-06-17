#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import combinations

squareNumberList = [x**2 for x in range(1, 10)]
#print squareNumberList
squareDigitList = map(lambda e: (e/10, e%10), squareNumberList)
print squareDigitList

cubeCombinations = list(combinations(range(0, 10), 6))

# todo extend 6+9
for cube1 in cubeCombinations:
    for cube2 in cubeCombinations:
        print cube1, cube2
