#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from IsSquare import *

upperLimit=100
digitNumber=100
result=0

for i in range(1, upperLimit+1):
    if not isSquare(i):
        number=i*10**(2*digitNumber)
        naiveSqrt=sqrtApprox(number)
        result+=sum(map(lambda e: int(e), list(str(naiveSqrt))[:digitNumber]))

print result
