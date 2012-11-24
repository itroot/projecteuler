#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from ContinuedFraction import *

upperLimit=10000
squares=set(i*i for i in range(0, upperLimit+1))
result=0
for i in range(0, upperLimit+1):
    if (not i in squares):
        notation=calculateSquareFractionNotation(i)
        if (1==len(notation[1])%2):
            result+=1
print result
