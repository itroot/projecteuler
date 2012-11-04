#!/usr/bin/env python
# -*- coding: utf-8 -*-

class HighCard(Combination):
    def __init__(self):
        Combination.__init__(self)
    def classify(self, cards):
        return tuple(["HighCard"]+sorted(map(lambda e: e.rank(), cards), reverse=True))
