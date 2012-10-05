#!/usr/bin/env python
# -*- coding: utf-8 -*-

upperLimit=10000;

hash2numberList={}


for number in range(0, upperLimit):
    hash="".join(sorted(str(number**3)))
    if not hash in hash2numberList:
        hash2numberList[hash]=[]
    numberList=hash2numberList[hash]
    numberList.append(number)
    if (len(numberList)==5):
        print min(numberList)**3
        break
#print hash2numberList
