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

lines=open("roman.txt").read().rstrip("\n").split("\n")

print lines

print readRomanNumber("XLIX")
print readRomanNumber("XXXXVIIII")
