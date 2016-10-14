#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple, defaultdict

T = namedtuple("T", ["digit", "twosum", "count"])

table = []
table.append([T(i, i, 1) for i in range(10)])

for step in range(19):
    d = defaultdict(int)
    for digit in range(10):
        for t in table[-1]:
            if (t.twosum + digit) < 10:
               d[(digit, t.digit+digit)] += t.count
    newt = []
    for (digit, twosum), count in d.iteritems():
         newt.append(T(digit, twosum, count))
    table.append(newt)
print sum([t.count for t in table[-1] if t.digit != 0])
