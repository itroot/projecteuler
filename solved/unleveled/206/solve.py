#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

data = "1_2_3_4_5_6_7_8_9_0"

def rpl(i):
    return int(data.replace("_", str(i)))

minp = rpl(0)
maxp = rpl(9)

for i in xrange(int(math.sqrt(minp)) - 1, int(math.sqrt(maxp)) + 2):
    if i % 30 != 0:
        continue
    sq = str(i ** 2)
    if len(data) == len(sq):
        allok = True
        for o, n in zip(data, sq):
            if o == "_":
                continue
            if o != n:
                allok = False
                break
        if allok:
            print i
            break

