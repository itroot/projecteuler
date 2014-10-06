#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from sss import is_special
from itertools import combinations


data = []
with open("sets.txt") as f:
    for line in f:
        data.append(map(int, line.rstrip("\n").split(",")))
print sum(map(sum, filter(is_special, data)))
