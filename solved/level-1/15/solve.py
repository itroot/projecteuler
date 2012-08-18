#!/usr/bin/env python
# -*- coding: utf-8 -*-

sizeX=20
sizeY=20

class GridRoutes:
    def __init__(self):
        self.__cache={}
    def number(self, x, y):
        if (1==x and 1==y):
            return 2
        elif (1==x):
            return y+1
        elif (1==y):
            return x+1
        else:
            dimension=tuple(sorted([x, y]))
            if dimension in self.__cache:
                return self.__cache[dimension]
            number=self.number(x-1, y)+self.number(x, y-1)
            self.__cache[dimension]=number
            return number

gridRoutes=GridRoutes()
print gridRoutes.number(sizeX, sizeY)
