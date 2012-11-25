#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from Factorize import *

def eulerTotient(number):
    factorization=factorize(number)
    uniquePrimeList=list(set(factorization))
    return reduce(lambda a, b: a*(b-1), uniquePrimeList, 1)

print eulerTotient(87109)
