#!/usr/bin/env python
# -*- coding: utf-8 -*-

solutionKnown=40755

class SequenceNumber:
    def __init__(self):
        self.__n=0
    def advance(self):
        self.__n+=1
    def n(self):
        return self.__n

class TriangleNumber(SequenceNumber):
    def generate(self):
        n=self.n()
        return n*(n+1)/2

class PentagonalNumber(SequenceNumber):
    def generate(self):
        n=self.n()
        return n*(3*n-1)/2

class HexagonalNumber(SequenceNumber):
    def generate(self):
        n=self.n()
        return n*(2*n-1)

sequences=[TriangleNumber(), PentagonalNumber(), HexagonalNumber()]

while True:
    if (1==len(set(map(lambda e: e.generate(), sequences)))):
        result=sequences[0].generate()
        if result>solutionKnown:
            print result
            break
    (position, number)=min(enumerate(sequences), key=lambda e: e[1].generate())
    sequences[position].advance()
