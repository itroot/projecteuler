#!/usr/bin/env python
# -*- coding: utf-8 -*-

def readData(filename):
    lines=open("base_exp.txt").read().rstrip("\n").split("\n")
    return map(lambda e: tuple(map(int, e.split(","))), lines)

data=readData("base_exp.txt")
import math
logList=map(lambda (a, b): math.log(a)*b, data)
print sorted(enumerate(logList), key=lambda e: e[1])[-1][0]+1
