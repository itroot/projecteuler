#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
from collections import Counter
from fractions import Fraction
from decimal import Decimal

class Peter(object):
    count = 9
    values = range(1, 5)

class Colin(object):
    count = 6
    values = range(1, 7)

def _fill(player):
    player.c = Counter(
        sum(v)
        for v in itertools.product(player.values, repeat=player.count)
    )
    player.nv = sum(player.c.values())

def main():
    _fill(Peter)
    _fill(Colin)
    result = Fraction()
    for peter_score, peter_count in Peter.c.iteritems():
        for colin_score, colin_count in Colin.c.iteritems():
            if peter_score > colin_score:
                result += Fraction(peter_count * colin_count, Peter.nv * Colin.nv)
    print round(float(result), 7)
    

if __name__ == '__main__':
    main()
