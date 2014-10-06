#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from sss import is_special
from itertools import combinations

print "".join(map(str, min(filter(is_special ,list(combinations(range(20, 46), 7))), key=lambda e: sum(e))))
