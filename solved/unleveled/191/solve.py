#!/usr/bin/env python
# -*- coding: utf-8 -*-

def n(i):
    return _n(i, 0, 0, 0, '')

d = {}

def _n(i, c, a, l, s):
    cached_result = d.get((c, a, l))
    if cached_result is not None:
        return cached_result
    if i == c:
        return 1
    nc = c + 1
    result = _n(i, nc, 0, l, s + 'O')
    if l == 0:
        result += _n(i, nc, 0, l + 1, s + 'L')
    if a < 2:
        result += _n(i, nc, a + 1, l, s + 'A')
    d[(c, a, l)] = result
    return result 

print n(30)
