#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from OwnMemoize import Memoize

upperLimit = 50

def solve(callee, length):
    #print length
    result = 1
    for start in range(length-3+1):
        for end in range(start+3, length+1):
            #print length, start, end
            result += callee(callee, length - end - 1)
    return result

m = Memoize()
print m.run(solve, upperLimit)
