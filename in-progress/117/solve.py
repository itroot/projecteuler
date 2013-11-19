#!/usr/bin/env python
# -*- coding: utf-8 -*-

upperLimit = 50

memory = {}

def cnumber(n, first, size):
    key = (n, first, size)
    if (key in memory):
        return memory[key]
    result = 0
    if not first:
        result += 1
    if n<size:
        result
    for i in range(0, n-size+1):
        result += cnumber(n-i-size, False, size)
    memory[key] = result
    return result

print cnumber(upperLimit, True, 2) + cnumber(upperLimit, True, 3) + cnumber(upperLimit, True, 4)
