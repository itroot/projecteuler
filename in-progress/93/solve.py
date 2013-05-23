#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

operationMap = {
"+" : lambda a, b: a+b,
"-" : lambda a, b: a-b,
"*" : lambda a, b: a*b,
"/" : lambda a, b: a/float(b), # FIXME
}

operationList=list(operationMap.iterkeys())
#print operationList
# /4+3+12 - infix notations

def applyOperation(numberList, operationOrder):
    textResult=""
    print numberList, operationOrder
    while len(numberList)!=1:
        a=numberList.pop()
        b=numberList.pop()
        op=operationMap[operationOrder.pop()]
        numberList.append(op(a, b))
    print numberList[0]
    return numberList[0]
# FIXME need *+23-1, use stack for this
for combination in itertools.combinations(range(1, 10), 4):
    combination=[1, 2, 3, 4]
    result=[]
    for permutation in itertools.permutations(combination):
        for operationOrder in itertools.combinations(operationList, 3):
            result.append(applyOperation(list(permutation), list(operationOrder)))
    print sorted(result)
    break
