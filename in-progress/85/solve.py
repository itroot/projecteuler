#!/usr/bin/env python
# -*- coding: utf-8 -*-

def rectangleNumber(width, height):
    result=0
    for x in range(1, width+1):
        for y in range(1, height+1):
            addend=(width-x+1)*(height-y+1)
            if x<=height and y<=width:# and not x==y:
                addend+=(height-x+1)*(width-y+1)
            result+=addend if x==y else addend
    return result/2

print rectangleNumber(2, 1)
