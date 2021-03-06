#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Idea: you can precalulcate all squares and than match them into words
"""

def anagramHash(word):
    return "".join(sorted(list(word)))

def anagramSet(word):
    return "".join(sorted(list(set(word))))

wordList = map(lambda e: e[1:-1], open("words.txt").read().rstrip("\n").split(","))
#print wordList

from collections import defaultdict
anagramDict = defaultdict(list)
#print anagramDict


for word in wordList:
    hash = anagramHash(word)
    #print hash
    #print word
    #break
    anagramDict[hash].append(word)

import pprint
data = filter(lambda e: len(e[1])>1, anagramDict.iteritems())
#pprint.pprint(data)

import sys
sys.path.append("../lib")
from IsSquare import isSquare

resultList=[]

def checkAnagram(anagramSet, anagramList):
    from itertools import permutations
    numberPermutations = list(permutations(range(0, 10), len(anagramSet)))
    for permutation in numberPermutations:
        squareList = []
        for word in anagramList:
            numberList = map(lambda e: str(permutation[anagramSet.index(e)]) , list(word))
            if numberList[0] == "0":
                break
            number = int("".join(numberList))
            #print number
            if isSquare(number):
                #print number
                squareList.append(number)
            elif len(anagramList) == 2:
                break
        if (len(squareList) > 1):
            #print squareList
            resultList.extend(squareList)
            #pass # write result 
        #break
    #print anagramSet
    #print anagramList

#pprint.pprint(data)

for (hash, anagramList) in data:
    #print anagramList
    if len(hash)>5: # see speed-up idea on the top, I already knew the answer
        continue
    checkAnagram(hash, anagramList)
    #break

#print wordList
print max(resultList)
