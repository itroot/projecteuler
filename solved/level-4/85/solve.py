#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

approximation=2*10**6

def rectangleNumber(width, height):
    result=0
    for x in range(1, width+1):
        for y in range(1, height+1):
            result+=(width-x+1)*(height-y+1)
    return result

x=1
y=1
allNumbers=[]
while True:
    if (rectangleNumber(x, y)<approximation):
        x+=1
    else:
        allNumbers.append(((x, y), rectangleNumber(x, y)))
        allNumbers.append(((x-1, y), rectangleNumber(x-1, y)))
        #print x, y
        if x==1:
            break
        y+=1
        x=1

resultTuple=min(allNumbers, key=lambda e: math.fabs(e[1]-approximation))
print resultTuple[0][0]*resultTuple[0][1]