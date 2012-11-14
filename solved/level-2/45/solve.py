#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from SequenceNumber import *

solutionKnown=40755
sequences=[TriangleNumber(), PentagonalNumber(), HexagonalNumber()]

while True:
    if (1==len(set(map(lambda e: e.generate(), sequences)))):
        result=sequences[0].generate()
        if result>solutionKnown:
            print result
            break
    (position, number)=min(enumerate(sequences), key=lambda e: e[1].generate())
    sequences[position].advance()
