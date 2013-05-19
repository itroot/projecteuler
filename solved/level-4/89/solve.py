#!/usr/bin/env python
# -*- coding: utf-8 -*-

romanMap={
"I" : 1,
"V" : 5,
"X" : 10,
"L" : 50,
"C" : 100,
"D" : 500,
"M" : 1000,
}

descendingSizeCombinations=["IV", "IX", "XL", "XC", "CD", "CM"]


def fromRomanDigit(digit):
    return romanMap[digit]

def readRomanNumber(number):
    digitList=list(number)
    result=0
    nthDigit=lambda i: fromRomanDigit(digitList[i])
    while len(digitList)!=0:
        if (len(digitList)>1 and nthDigit(0)<nthDigit(1)):
            result=result+nthDigit(1)-nthDigit(0)
            digitList.pop(0)
        else:
            result=result+nthDigit(0)
        digitList.pop(0)
    return result

def getRomanLimits():
    result=[]
    for combination in descendingSizeCombinations:
        lowerNumber=readRomanNumber(combination)
        upperNumber=readRomanNumber(combination[1])
        result.append((lowerNumber, upperNumber, combination))
    return result

romanLimits=getRomanLimits()
romanSortedList=sorted(romanMap.iteritems(), reverse=True, key=lambda e: e[1])

#print romanLimits
#print romanSortedList

def writeRomanNumber(number):
    result=""
    while number!=0:
        foundMatch=False
        #print number
        for limit in romanLimits:
            if number>=limit[0] and number<limit[1]:
                result+=limit[2]
                number-=limit[0]
                foundMatch=True
                break
        if foundMatch:
            continue
        for item in romanSortedList:
            if number>=item[1]:
                number-=item[1]
                result+=item[0]
                break
    return result

lines=open("roman.txt").read().rstrip("\n").split("\n")

newNumbers=map(lambda number : writeRomanNumber(readRomanNumber(number)), lines)

print len("".join(lines))-len("".join(newNumbers))
