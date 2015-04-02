#!/usr/bin/env python

# (a1 + an), a2 + a_n-1 ...

#?? LEAK

upperLimit = 10**5

counter = 0
ss = set(["1", "3", "5", "7", "9"])

for i in range(1, upperLimit):
    if i%10 == 0:
        continue
    s = i + int("".join(reversed(str(i))))
    if set(list(str(s))) <= ss:
        counter += 1

print counter
