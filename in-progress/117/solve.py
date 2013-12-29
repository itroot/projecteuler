#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from OwnMemoize import Memoize

upperLimit = 50

def rgb_n_tiles(callee, number, i, n):
    r = i + n
    if not r > number:
        return callee(callee, number - r)
    else:
        return 0

def rgb_tiles(callee, number):
    result = 1
    if number<2:
        return result
    for i in range(0, number):
        result += sum(map(lambda e: rgb_n_tiles(callee, number, i, e), range(2,5)))
    return result

m = Memoize()
print m.run(rgb_tiles, upperLimit)
