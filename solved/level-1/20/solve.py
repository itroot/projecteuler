#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

print reduce(lambda a, b: int(a)+int(b), str(math.factorial(100)))
