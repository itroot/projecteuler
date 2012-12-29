#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sqrtApprox(number):
    import bisect
    class Power2:
        def __getitem__(self, number):
            return number**2
    return bisect.bisect_right(Power2(), number, 0, number+1)-1


print sqrtApprox(2*10**40)
