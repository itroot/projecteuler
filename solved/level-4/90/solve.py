#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import combinations

squareNumberList = [x**2 for x in range(1, 10)]
#print squareNumberList
squareDigitList = map(lambda e: (e/10, e%10), squareNumberList)
#print squareDigitList, len(squareDigitList)

"""
def splitList(l, number):
    left = []
    right = []
    if not number < 2**len(l):
        raise Exception("Number is too big")
    index = 0
    for i in range(0, len(l)):
        flag = number % 2
        number = number / 2
        if flag == 1:
            left.append(l[index])
        else:
            right.append(l[index])
        index += 1
    return (left, right)

def cleanSet(st):
    if 6 in st:
        st.remove(6)
    if 9 in st:
        st.remove(9)
"""

def expandSet(numberSet):
    if 9 in numberSet:
        numberSet.add(6)
    if 6 in numberSet:
        numberSet.add(9)
"""
for i in range(0, 2**len(squareDigitList)):
    (left, right) = splitList(squareDigitList, i)    
    oneCubeDigits = set(map(lambda e: e[0], left) + map(lambda e: e[1], right))
    secondCubeDigits = set(map(lambda e: e[1], left) + map(lambda e: e[0], right))
    cleanSet(oneCubeDigits)
    cleanSet(secondCubeDigits)
    print oneCubeDigits , secondCubeDigits
        #print oneCubeDigits, secondCubeDigits
"""
#"""
cubeCombinations = list(combinations(range(0, 10), 6))
# todo extend 6+9
result=[]
for cube1 in cubeCombinations:
    cube1set = set(cube1)
    expandSet(cube1set)
    for cube2 in cubeCombinations:
        cube2set = set(cube2)
        expandSet(cube2set)
        found = True
        for (digit1, digit2) in squareDigitList:
            if not ((digit1 in cube1set and digit2 in cube2set) or (digit1 in cube2set and digit2 in cube1set)):
                found = False
                break
        if (found):
            result.append((cube1, cube2))
result = map(lambda e: (tuple(sorted(e[0])), tuple(sorted(e[1]))), result)
result = map(lambda e: {True: e, False: (e[1], e[0])}[e[1]>e[0]], result)
result = list(set(result))
#print result
#import pprint
#pprint.pprint(result)
print len(result)
#"""
