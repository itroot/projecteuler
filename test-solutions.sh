#!/usr/bin/env bash

for FILE in $(find -name solve.py)
do
    cd $(dirname ${FILE})
    [[ "$(./solve.py)" == "$(cat answer.txt)" ]] && { echo "Success: ${FILE}"; } || { echo "Fail in {$FILE}"; exit 1; }
    cd - 2>&1 >/dev/null
done
exit 0;
