#!/usr/bin/env python
# -*- coding: utf-8 -*-

sizeX=20
sizeY=20

class Grid:
    def __init__(self, rawGrid):
        self.__grid=map(lambda x: x.split(" "), rawGrid.split("\n"))
    def getElement(self, x, y):
        return self.__grid[y][x]
    def productXX(self, x, y):
        product=1
        if not (x+4<=20):
            raise Exception("Out of reach in XX ")
        for i in range(x, x+4):
            product*=int(self.getElement(i, y))
        return product

input=open("input.txt").read().rstrip("\n")
grid=Grid(input)
print grid.productXX(16, 0)
