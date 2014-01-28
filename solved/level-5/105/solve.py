#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import combinations
from collections import defaultdict

def all_sets(l):
    result = []
    for i in range(len(l)):
        result.extend(map(list, combinations(l, i+1)))
    return result

data = []


with open("sets.txt") as f:
    for line in f:
        data.append(map(int, line.rstrip("\n").split(",")))

def is_special(datum):
    sets = all_sets(datum)
    sums = set()
    len2sum = defaultdict(list)
    for subset in sets:
        s = sum(subset)
        if s in sums:
            return False
        else:
            sums.add(s)
        len2sum[len(subset)].append(s)
    length = 0
    for i in range(len(datum)):
        if length >= min(len2sum[i+1]):
            return False
        else:
            length = max(len2sum[i+1])
    return True

print sum(map(sum, filter(is_special, data)))
