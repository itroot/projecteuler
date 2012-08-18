#!/usr/bin/env python
# -*- coding: utf-8 -*-

codeWordLength=3
encodedAsciiText=open("cipher1.txt").read().rstrip("\r\n").split(",")
#print encodedAsciiText

letter2RateList=[{} for i in range(0, codeWordLength)]
for (i, letter) in enumerate(encodedAsciiText):
    letter2RateIndex=i%codeWordLength
    letter2rate=letter2RateList[letter2RateIndex]
    if not letter in letter2rate:
        letter2rate[letter]=0
    letter2rate[letter]+=1

for letter2rate in letter2RateList:
    rates=sorted(letter2rate.iteritems(), key=lambda e: e[1])
    print rates
    print

