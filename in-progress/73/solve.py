#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from Factorize import *

upperLimit=12000


f=Factorization()
print f.eulerTotient(upperLimit+1)
print "Before 1/2: ", (sum(f.eulerTotient(i) for i in range(2, upperLimit+1))-1)/2
