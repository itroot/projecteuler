#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from EratosthenesSieve import *

sieve=EratosthenesSieve()
sieve.growToNumber(2000000)
print sum(sieve.sieve())
