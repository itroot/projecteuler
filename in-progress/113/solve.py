#!/usr/bin/env python
# -*- coding: utf-8 -*-


def inc(digit):
    return range(digit, 10)

def dec(digit):
    return range(0, digit)

def count(length, digit, getrange):
    if length == 1:
        return 1
    result = 0
    for d in getrange(digit):
        result += count(length-1, d, getrange)
    return result

