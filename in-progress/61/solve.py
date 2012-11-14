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

for sequence in sequences:
    result=[]
    while True:
        number=sequence.generate()
        digitsInNumber=len(str(number))
        if (digitsInNumber>4):
            break
        if 4==digitsInNumber:
            result.append(number)
        sequence.advance()
    print result
