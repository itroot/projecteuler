#!/usr/bin/env bash

find ../ -name solve.py | xargs -n1 -P4 ./test-solution.sh
