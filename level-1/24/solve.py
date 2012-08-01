#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from Permutation import *

upperLimit=9

digits=range(0, upperLimit+1)

# 0 012 -> 0 12
# 1 021 -> 1 21
# 2 102
# 3 120
# 4 201
# 5 210


#for i in range(0, math.factorial(upperLimit+1)):
#    print nth_permutation(digits, i)

print "".join(map(lambda e: str(e), nth_permutation(digits, 1000000-1)))
