#To be able to run this script run:
# chmod 755 run.sh

for filename in hashcode/inputs/*.txt; do
  python3 hashcode/src/main.py $filename
done
