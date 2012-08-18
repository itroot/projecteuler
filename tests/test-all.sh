#!/usr/bin/env bash

PROCESS_NUM=4

find ../solved -name solve.py | xargs -n1 -P${PROCESS_NUM} ./test-solution.sh
