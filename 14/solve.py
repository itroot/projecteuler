#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Sequence:
    def __init__(self):
        self.__cache={2:1}
    def __advance(self, number):
        if (0==number%2):
            return number/2
        else:
            return 3*number+1
    def build(self, number):
        result=[]
        while 1!=number:
#        if number in sequence:
#            result.append(sequence[number])
#            return result
#        else:
            result.append(number)
            number=self.__advance(number)
        result.append(1)
#    sequence[number]=result
        return result


sequence=Sequence()
for i in range(1, 10):
    s=sequence.build(i)
    print len(s), s
