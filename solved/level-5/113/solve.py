#!/usr/bin/env python
# -*- coding: utf-8 -*-

def memoize(f):
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)

@memoize
def increasing_count(start_digit, length, limit):
    if 0 == length:
        return 1
    result = 0
    for i in range(start_digit, limit):
        result += increasing_count(i, length - 1, limit)
    return result

def below(i):
    result = 0
    for i in range(1, i+1):
        result += increasing_count(1, i, 10) + increasing_count(1, i, 11) - 1 - 9
    return result

print below(100)