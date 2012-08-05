#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def isTriangleWord(word):
    value=reduce(lambda a, b: a+(ord(b)-ord("A")+1), word, 0)
    #print value
    valueDoubled=value*2
    floorSqrt=math.floor(math.sqrt(valueDoubled))
    return valueDoubled==floorSqrt*(floorSqrt+1)

words=map(lambda e: e.strip("\""), open("words.txt").read().split(","))

print len(filter(lambda e: isTriangleWord(e), words))
