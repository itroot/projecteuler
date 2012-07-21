#!/usr/bin/env python
# -*- coding: utf-8 -*-

sizeX=20
sizeY=20

patternXX=[(0, 0), (1, 0), (2, 0), (3, 0)]
patternYY=[(0, 0), (0, 1), (0, 2), (0, 3)]
patternXY=[(0, 0), (1, 1), (2, 2), (3, 3)]
patternYX=[(0, 0), (1, -1), (2, -2), (3, -3)]
patterns=[patternXX, patternYY, patternXY, patternYX]

class Grid:
    def __init__(self, rawGrid):
        self.__grid=map(lambda x: x.split(" "), rawGrid.split("\n"))
    def getElement(self, x, y):
        return self.__grid[y][x]
    def productByPattern(self, x, y, pattern):
        product=1
        for point in pattern:
            (xShift, yShift)=point
            newX=x+xShift
            newY=y+yShift
            if not (0<=newX<=sizeX and 0<=newY<=sizeY):
                raise Exception("Out of reach in XX ")
            product*=int(self.getElement(newX, newY))
        return product

input=open("input.txt").read().rstrip("\n")
grid=Grid(input)
product=0
for x in range(0, sizeX):
    for y in range(0, sizeY):
        for pattern in patterns:
            try:
                current=grid.productByPattern(x, y, pattern)
                product=max(product, current)
            except:
                pass
print product
