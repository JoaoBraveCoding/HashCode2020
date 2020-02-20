#!/bin/bash
#To be able to run this script run:
# chmod 755 run.sh

INPUTS=./hashcode/inputs/*.txt

for filename in $INPUTS; do
  echo "Going to run for file " $filename
  python3 ./hashcode/src/main.py $filename
done
