#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples

import numpy
import math

A=numpy.matrix(((1, -2, 2), (2, -1, 2), (2, -2, 3)))
B=numpy.matrix(((1, 2, 2), (2, 1, 2), (2, 2, 3)))
C=numpy.matrix(((-1, 2, 2), (-2, 1, 2), (-2, 2, 3)))
namedMatrixList=(("A", A), ("B", B), ("C", C))

head=numpy.matrix((3, 4, 5)).transpose()

result=[]

def traverse(head, path):
    triple=sorted(head.transpose().tolist()[0])
    if 2*(triple[0]+triple[2])>10**9:
        return
    if (math.fabs(triple[0]*2-triple[2])<2):
        #print path, triple
        result.append(triple)
    else:
        return
    for (name, matrix) in namedMatrixList:
        traverse(matrix*head, list(path)+[name])

traverse(head, [])
print sum(map(lambda (a, b, c): 2*(a+c), result))
