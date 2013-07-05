# -*- coding: utf-8 -*-

"""
http://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples
"""

pairMN=(2, 1)

def nextLevel(pairMN):
    (m, n)=pairMN
    return ((2*m-n, m), (2*m+n, m), (m+2*n, n))

def MN2ABC(pairMN):
    (m, n)=pairMN
    return (m**2-n**2, 2*m*n, m**2+n**2)

def traverse(pairMN, condition):
    if (condition(pairMN)):
        threePairMN=nextLevel(pairMN)
        for pairMN in threePairMN:
            traverse(pairMN, condition)
