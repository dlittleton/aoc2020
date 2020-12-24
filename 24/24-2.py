import collections
import re
import sys

directions = re.compile(r'e|se|sw|w|nw|ne')
points = collections.defaultdict(bool)

def neigbors(x, y):
    yield x + 2, y
    yield x + 1, y - 1
    yield x - 1, y - 1
    yield x - 2, y
    yield x - 1, y + 1
    yield x + 1, y + 1


def cycle(black):
    counts = collections.Counter()

    for b in black:
        counts.update(neigbors(*b))

    new = set()
    for p in counts:
        is_black = p in black
        if is_black and counts[p] <= 2:
            new.add(p)
        elif not is_black and counts[p] == 2:
            new.add(p)

    return new


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


black = set(p for p in points if points[p])

for _ in range(100):
    black = cycle(black)

print(len(black))