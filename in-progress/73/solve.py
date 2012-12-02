#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from Factorize import *

upperLimit=12000


f=Factorization()
print f.eulerTotient(8)
print sum(f.eulerTotient(i) for i in range(2, 9))
