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
