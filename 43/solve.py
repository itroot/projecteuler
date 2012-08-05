#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from Permutation import *

def isProblem43Number(number):
    primesAndOne=[1, 2, 3, 5, 7, 11, 13, 17]
    for (i, prime) in enumerate(primesAndOne):
        sliceNumber=int(str(number)[i:i+3])
        #print sliceNumber
    	if (sliceNumber%prime!=0):
            return False
    return True

#print isProblem43Number(1406357289)


lastThreeDigitsList=[]
for i in range(1, 1000):
   if i%17==0 and 3==len(set(str(i))):
       lastThreeDigitsList.append(i)

resultNumbers=[]
upperLimit=7
for lastThreeDigits in lastThreeDigitsList:
    digitsSet=set(range(0, 10))
    digits=sorted(list(digitsSet-set(map(lambda e: int(e), str(lastThreeDigits)))))
    #print digits
    for i in range(0, math.factorial(upperLimit)):
        permutation=nth_permutation(digits, i)
        number=reduce(lambda a, b: 10*a+b, permutation)*10**3+lastThreeDigits
        if (isProblem43Number(number)):
		resultNumbers.append(number)
print sum(resultNumbers)


