#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Tail:
    def __init__(self, number, length):
        self.number=number
        self.length=length
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return "(%d, %d)" % (self.number, self.length)
  
class Sequence:
    def __init__(self):
        self.__cache={
            2: Tail(1, 0)
        }
    def __advance(self, number):
        if (0==number%2):
            return number/2
        else:
            return 3*number+1
    def cache(self):
        return self.__cache
    def populateTo(self, upperBound):
        for i in range(1, upperBound):
            if not i in self.__cache:
                self.populate(i)
    def populate(self, number):
        sequence=[]
        while True:
            sequence.append(number)
            if number in self.__cache:
                tail=self.__cache[number]
                length=tail.length+len(sequence)
                for i in range(0, len(sequence)-1):
                    length-=1
                    self.__cache[sequence[i]]=Tail(sequence[i+1], length)
                return
            else:
                number=self.__advance(number)
    def build(self, number):
        result=[]
        if not number in self.__cache:
            self.populate(number)
        result.append(number)
        while 1!=number:
            tail=self.__cache[number]
            number=tail.number
            result.append(number)
        return result


sequence=Sequence()
sequence.populateTo(1000000)
cache=sequence.cache()
longestStart=max(cache.iterkeys(), key=lambda k: cache[k].length)
print longestStart
