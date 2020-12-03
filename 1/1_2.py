import sys

values = list(map(int, sys.stdin.readlines()))
for i, x in enumerate(values):
    for j, y in enumerate(values[i+1:], i+1):
        if x + y > 2020:
            continue
        for z in values[j+1:]:
            if x + y + z== 2020:
                print(x * y * z)