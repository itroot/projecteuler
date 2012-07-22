#!/usr/bin/env python
# -*- coding: utf-8 -*-

def advanceSequence(number):
    if (0==number%2):
        return number/2
    else:
        return 3*number+1

#sequence={}

def buildSequence(number):
    result=[]
    while 1!=number:
#        if number in sequence:
#            result.append(sequence[number])
#            return result
#        else:
        result.append(number)
        number=advanceSequence(number)
    result.append(1)
#    sequence[number]=result
    return result

for i in range(1, 1000):
    sequence=buildSequence(i)
    print len(sequence), sequence
