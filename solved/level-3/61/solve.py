#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from SequenceNumber import *

sequences=[
    TriangleNumber(),
    SquareNumber(),
    PentagonalNumber(),
    HexagonalNumber(),
    HeptagonalNumber(),
    OctagonalNumber(),
]

def get4DigitNumbersList():
    result=[]
    for sequence in sequences:
        numbers=[]
        while True:
            number=sequence.generate()
            digitsInNumber=len(str(number))
            if (digitsInNumber>4):
                break
            if 4==digitsInNumber:
                numbers.append(number)
            sequence.advance()
        result.append(numbers)
    return result

sequenceNumberCollectionList=get4DigitNumbersList()

def findCycle(sequenceNumberCollectionList, cycleFound=[]):
    length=len(sequenceNumberCollectionList)
    if (0==length) and (str(cycleFound[-1])[-2:]==str(cycleFound[0])[0:2]):
        print sum(cycleFound)
        return True
    for (i, sequenceNumberCollection) in enumerate(sequenceNumberCollectionList):
        for number in sequenceNumberCollection:
            if 0==len(cycleFound) or str(cycleFound[-1])[-2:]==str(number)[0:2]:
                if findCycle(sequenceNumberCollectionList[0:i]+sequenceNumberCollectionList[i+1:], cycleFound+[number]):
                    return True

findCycle(sequenceNumberCollectionList)
