#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from Factorize import *
    
number=int(open("input.txt").read())


print factorize(number)[-1]
