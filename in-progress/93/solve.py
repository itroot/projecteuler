#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
import fractions

operationMap = {
"+" : lambda a, b: a+b,
"-" : lambda a, b: a-b,
"*" : lambda a, b: a*b,
"/" : lambda a, b: fractions.Fraction(a, b), # FIXME
}

operationList=list(operationMap.iterkeys())
#print operationList
# /4+3+12 - infix notations

# http://en.wikipedia.org/wiki/Binary_tree#Combinatorics
infixPatterns=["ooonnnn", "onononn"] # oonnonn

def calculateInfix(notation):
    stack=[]
    #print notation
    while len(notation)!=0:
        atom=notation.pop()
        if isinstance(atom, int):
            stack.append(fractions.Fraction(atom))
        else:
            try:
                stack.append(operationMap[atom](stack.pop(), stack.pop()))
            except ZeroDivisionError:
                return None
    if (len(stack)!=1):
        raise Exception("Invalid notation")
    return stack[0]

def applyOperation(numberList, operationOrder):
    result=[]
    for pattern in infixPatterns:
        numbers=list(numberList)
        ops=list(operationOrder)
        notation=map(lambda e: {"n": numbers, "o": ops}[e].pop(), pattern)
        infix=calculateInfix(list(notation))
        #print numberList, operationOrder, notation, "->", infix
        if not infix is None:
            result.append(infix)
    return result

def consecutiveIndex(numberList):
    index=0
    while len(numberList)>index and numberList[index]==index+1:
        index+=1
    return index

output=[]
for combination in itertools.combinations(range(1, 10), 4):
    result=[]
    for permutation in itertools.permutations(combination):
        for operationOrder in itertools.combinations_with_replacement(operationList, 3):
            for operationPermutation in itertools.permutations(operationOrder):
                result.extend(applyOperation(list(permutation), list(operationPermutation)))
    sortedResultList=sorted(list(set(map(lambda f: f.numerator, filter(lambda f: f>0 and f.denominator==1, result)))))
    consecutive=consecutiveIndex(sortedResultList)
    print sortedResultList, consecutive
    output.append((combination, consecutive))
print "".join(sorted(max(output, lambda e: e[1])))
