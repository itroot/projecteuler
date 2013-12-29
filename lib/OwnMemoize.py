# -*- coding: utf-8 -*-

from functools import partial

class Memoize:
    __d={}
    def wrap(self, origin_handler, handler, parameters):
        if parameters in self.__d:
            return self.__d[parameters]
        else:
            result = origin_handler(handler, parameters)
            self.__d[parameters] = result
            return result
    def run(self, handler, parameters):
        new_handler = partial(Memoize.wrap, self, handler)
        return new_handler(new_handler, parameters)
