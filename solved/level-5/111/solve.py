#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import combinations

primes = []

limit = 10**5

with open("../lib/data/primes-100000000.list") as f:
    for line in f:
        number = int(line)
        if number > limit:
            break
        primes.append(number)

digits = map(str, range(0, 10))

candidates_1 = []

def is_prime_5(number):
    if number < 2:
        return False
    for prime in primes:
        if prime >= number:
            break
        if 0 == number % prime:
            return False
    return True


digit_number = 10
#digit_number = 4

for digit in digits:
    for i in range(digit_number):
        for new_digit in digits:
            result = [digit] * digit_number
            result[i] = new_digit
            number = int("".join(result))
            if digit_number == len(str(number)) and is_prime_5(number):
                candidates_1.append(number)

#print candidates_1

candidates_2 = []

missed = ["2", "8", "0"]
#missed = ["0"]
templates = []
for i in range(digit_number):
    for j in range(i+1, digit_number):
        for digit in missed:
            data = [digit] * digit_number
            data[i] = "%s"
            data[j] = "%s"
            templates.append("".join(data))

for template in templates:
    for digit1 in digits:
        for digit2 in digits:
            number = int(template % (digit1, digit2))
            if digit_number == len(str(number)) and is_prime_5(number):
                candidates_2.append(number)
#print candidates_1
#print candidates_2

result_list = list(set(candidates_1 + candidates_2))
print sum(result_list)

