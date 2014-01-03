#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from OwnMemoize import Memoize

upperLimit = 10**6

# copy-paste from 114

def solve(callee, length):
    #print length
    result = 1
    for start in range(length-50+1):
        for end in range(start+50, length+1):
            #print length, start, end
            result += callee(callee, length - end - 1)
    return result

m = Memoize()
i = 1
while m.run(solve, i) < upperLimit:
    i += 1
print i
