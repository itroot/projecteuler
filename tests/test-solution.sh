#!/usr/bin/env bash

SOLUTION=${1}

cd $(dirname ${SOLUTION})
[[ "$(./solve.py)" == "$(cat answer.txt)" ]] && { echo "Success: ${SOLUTION}"; } || { echo "Fail in {$SOLUTION}"; exit 1; }
cd - 2>&1 >/dev/null
