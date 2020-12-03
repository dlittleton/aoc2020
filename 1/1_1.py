import sys

values = list(map(int, sys.stdin.readlines()))
for i, x in enumerate(values):
    for y in values[i:]:
        if x + y == 2020:
            print(x*y)