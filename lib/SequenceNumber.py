# -*- coding: utf-8 -*-

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

class SquareNumber(SequenceNumber):
    def generate(self):
        n=self.n()
        return n**2

class PentagonalNumber(SequenceNumber):
    def generate(self):
        n=self.n()
        return n*(3*n-1)/2

class HexagonalNumber(SequenceNumber):
    def generate(self):
        n=self.n()
        return n*(2*n-1)

class HeptagonalNumber(SequenceNumber):
    def generate(self):
        n=self.n()
        return n*(5*n-3)/2

class OctagonalNumber(SequenceNumber):
    def generate(self):
        n=self.n()
        return n*(3*n-2)
