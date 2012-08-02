#!/usr/bin/env python
# -*- coding: utf-8 -*-

def isPalindromic(itemList):
    length=len(itemList)
    for i in range(0, length//2):
        if (itemList[i]!=itemList[length-i-1]):
            return False
    return True


upperLimit=10**6
doublePalindromic=[]
for i in range(1, upperLimit):
    strI=str(i)
    binI=bin(i)[2:]
    #print binI
    if (isPalindromic(strI)) and isPalindromic(binI):
        #print i
        doublePalindromic.append(i)

print sum(doublePalindromic)
