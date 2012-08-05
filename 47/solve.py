#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from EratosthenesSieve import *
import bisect
import math

upperLimit=100000

sieve=EratosthenesSieve()
sieve.growToNumber(upperLimit)
primeList=sieve.sieve()
primesSet=set(primeList)

