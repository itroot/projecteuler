#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_multiply_by_5_or_3(number):
    return (0==number%3) or (0==number%5)

result=0;

for i in range(1, 1000):
    if is_multiply_by_5_or_3(i):
        result+=i

print result

    
