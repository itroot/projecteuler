#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from SequenceNumber import *

sequences=[
    TriangleNumber(),
    SquareNumber(),
    PentagonalNumber(),
#    HexagonalNumber(),
#    HeptagonalNumber(),
#    OctagonalNumber(),
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
    print sequenceNumberCollectionList
    for sequenceNumberCollection in sequenceNumberCollectionList:
        for number in sequenceNumberCollection:
            pass

findCycle(sequenceNumberCollectionList)
