import sys
args = sys.argv[1:]
number = 0
for i in args:
    number += int(i)
print(number)