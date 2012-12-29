#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sqrtApprox(number):
    import pythonic_bisect
    class Power2:
        def __getitem__(self, number):
            return number**2
    return pythonic_bisect.bisect_right(Power2(), number, 0, number+1)-1

def isSquare(number):
    naiveSqrt=sqrtApprox(number)
    return number==naiveSqrt**2

upperLimit=100
digitNumber=100
result=0

for i in range(1, upperLimit+1):
    if not isSquare(i):
        number=i*10**(2*digitNumber)
        naiveSqrt=sqrtApprox(number)
        result+=sum(map(lambda e: int(e), list(str(naiveSqrt))[:digitNumber]))

print result
