#!/usr/bin/env python
# -*- coding: utf-8 -*-

power=1000

print reduce(lambda a, b: int(a)+int(b), str((2**power)))
