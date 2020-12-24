import collections
import re
import sys

directions = re.compile(r'e|se|sw|w|nw|ne')
points = collections.defaultdict(bool)

def follow(line):
    x = 0
    y = 0

    for d in directions.findall(line):
        if d == 'e':
            x += 2
        elif d == 'se':
            x += 1
            y -= 1
        elif d == 'sw':
            x -= 1
            y -= 1
        elif d == 'w':
            x -= 2
        elif d == 'nw':
            x -= 1
            y += 1
        elif d == 'ne':
            x += 1
            y += 1

    return x, y

for line in map(str.rstrip, sys.stdin):
    coord = follow(line)
    points[coord] = not points[coord]


print(sum(1 for v in points.values() if v))