#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from EratosthenesSieve import *

sieve=EratosthenesSieve()
sieve.growToNumber(120000)
print sieve.sieve()[10000]
