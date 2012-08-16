#!/usr/bin/env python
# -*- coding: utf-8 -*-

maximumNumber=10000

result=0

def reversedNumber(number):
    return int(str("".join(reversed(list(str(number))))))

#print reversedNumber(123456)


def isLychrelNumber(number):
    maxIterations=50
    for i in range(0, maxIterations):
        number=number+reversedNumber(number)
        if number==reversedNumber(number):
            return False
    return True

for number in range(0, maximumNumber):
    if isLychrelNumber(number):
        result+=1

print result

