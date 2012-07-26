#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from Fibonacci import *

fibonacci=Fibonacci()
counter=0
while True:
    fnumber=fibonacci.GetNumberAtPosition(counter)
    if len(str(fnumber))>=1000:
        print counter
        break
    else:
        counter+=1
    

