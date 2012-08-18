#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

tripletSum=1000

def is_square(number):
    sqrtNumber=int(math.sqrt(number))
    return sqrtNumber*sqrtNumber==number

def verifyFirstTwoNumbers(first, second):
     sumOfSquares=first**2+second**2
     if is_square(sumOfSquares):
        return True

for first in range (1,1000):
    for second in range(first, 1000):
        if verifyFirstTwoNumbers(first, second):
            third=int(math.sqrt(first**2+second**2))
            sum=(first+second+third)
            if 1000==sum:
                print first*second*third


