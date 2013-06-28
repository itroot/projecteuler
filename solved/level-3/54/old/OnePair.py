# -*- coding: utf-8 -*-

from Combination import *

class OnePair(Combination):
    def __init__(self):
        Combination.__init__(self)
    def classify(self, cards):
        pairIndexes=findPairIndexInCards(cards)
        if pairIndexes:
            otherCards=[]
            for (i, card) in enumerate(cards):
                if not i in pairIndexes:
                    otherCards.append(card)
            return ["OnePair", cards[pairIndexes[0]].rank()]+sorted(map(lambda e: e.rank(), otherCards), reverse=True)
        else:
            return (None, None)
