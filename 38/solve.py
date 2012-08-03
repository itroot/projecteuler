#!/usr/bin/env python
# -*- coding: utf-8 -*-

def tryToGeneratePandigital(number):
    sortedNaturalDigits=range(1, 10)
    digits=[]
    counter=1
    while True:
        digits+=str(number*counter)
        length=len(digits)
        if length>9:
            return (False, 0)
        elif length==9:
            break
        else:
            counter+=1
    digits=map(lambda e: int(e), digits)
    #print digits
    result=(sorted(digits)==sortedNaturalDigits)
    #if result:
    #    print sorted(digits), sortedNaturalDigits
    return (result, reduce(lambda a, b: 10*a+b, digits))

numbers=[]

for i in range(1, 100000):
    (result, number)=tryToGeneratePandigital(i)
    if result:
        numbers.append(number)

print max(numbers)



