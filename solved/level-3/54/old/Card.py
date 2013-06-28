# -*- coding: utf-8 -*-

class Card:
    def __init__(self, abbreviation):
        self.__abbreviation=abbreviation
        self.__rank=letter2rank[abbreviation[0]]
        self.__suit=letter2suit[abbreviation[1]]
    def rank(self):
        return self.__rank
    def suit(self):
        return self.__suit
    def __repr__(self):
        return self.__abbreviation

