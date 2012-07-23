#!/usr/bin/env python
# -*- coding: utf-8 -*-

input=open("input.txt").read()

number=list("".join(input.split("\n")))

def calculateProductAt(number, position):
    product=1;
    for i in range(0,5):
        product*=int(number[position+i])
    return product

result=0

for i in range(0, len(number)-5):
    product=calculateProductAt(number, i)
    result=max(product, result)
    
print result
