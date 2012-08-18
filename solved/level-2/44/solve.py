#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def nth_pentagonal(n):
    return n*(3*n-1)/2

upperLimit=100000
pentagonals=[]

for i in range(1, upperLimit+1):
    pentagonals.append(nth_pentagonal(i))
pentagonalsSet=set(pentagonals)

for a in range(1, upperLimit):
    for b in range(1, a):
	pentagonalSum=pentagonals[a]+pentagonals[b]
        pentagonalDif=pentagonals[a]-pentagonals[b]
        if pentagonalSum in pentagonalsSet and pentagonalDif in pentagonalsSet:
            print pentagonals[a]-pentagonals[b]
            sys.exit(0)
