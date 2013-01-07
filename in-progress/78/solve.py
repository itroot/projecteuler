#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://en.wikipedia.org/wiki/Partition_(number_theory)#Generating_function
"""

def pentagonal(n):
    return n*(3*n-1)/2

cache=[1]

def p(n):
    result=0
    if n<0:
        pass
    elif n==0:
        result=1
    else:
        k=0
        while True:
            value=k/2+1
            sign=(-1)**(k)
            shift=pentagonal(sign*value)
            rshift=n-shift
            if rshift<0:
                break
            else:
                result+=(-1)**(k/2)*cache[rshift]
            k+=1
    return result

for i in range(1, 1000000):
    #print i
    number=p(i)
    delimiter=10**6
    cache.append(number)
    if number%delimiter==0:
        print i
        break

