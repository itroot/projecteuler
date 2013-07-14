#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from cpp import launch

launch(libraries = ["gmp", "gmpxx"])
