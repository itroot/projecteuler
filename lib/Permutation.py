#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def nth_permutation(digits, number):
    length=len(digits)
    factorial=math.factorial(length)
    prevFactorial=math.factorial(length-1)
    if (number<0 or number>=factorial):
        raise Exception("Incorrect parameters, digits: %s, number: %d" % (str(digits), number))
    if (0==number):
        return digits
    divide_result=number//(prevFactorial)
    reminder=number%(prevFactorial)
    newDigits=list(digits)
    newDigits[0], newDigits[divide_result]=newDigits[divide_result], newDigits[0]
    return [newDigits[0]]+nth_permutation(sorted(newDigits[1:]), reminder)
