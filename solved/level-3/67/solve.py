#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
import Triangle



input=open("input.txt").read()
print Triangle.solve_triangle(input)
