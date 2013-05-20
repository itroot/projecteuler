#!/usr/bin/env python
# -*- coding: utf-8 -*-

upperLimit=50
coordinateRange=range(0, upperLimit+1)

def scalar(v1, v2):
    return v1[0]*v2[0]+v1[1]*v2[1]

def isRight(x1, y1, x2, y2):
    point0=(x2-x1, y2-y1)
    point1=(x1, y1)
    point2=(x2, y2)
    return 0==scalar(point0, point1) or 0==scalar(point1, point2) or 0==scalar(point0, point2)

result=0
for x1 in coordinateRange:
    for y1 in coordinateRange:
        for x2 in coordinateRange:
            for y2 in coordinateRange:
                if (x1==0 and y1==0) or (x2==0 and y2==0) or (x1==x2 and y1==y2):
                    continue
                if (isRight(x1, y1, x2, y2)):
                    result+=1
print result/2
