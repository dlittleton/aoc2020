import collections
import sys

def load(stream):
    values = set()
    i = 0
    for line in map(str.rstrip, stream):
        j = 0
        for c in line:
            if c == '#':
                values.add((i, j, 0))
            j += 1
        i += 1

    return values


def neighbors(x, y ,z):
    for i in [x-1, x, x+1]:
        for j in [y-1, y, y+1]:
            for k in [z-1, z, z+1]:
                if i != x or j != y or k != z:
                    yield i, j, k


def run(active):
    next_active = set()
    counts = collections.Counter()

    for cube in active:
        counts.update(neighbors(*cube))


    for cube in active:
        if 2 <= counts[cube] <= 3:
            next_active.add(cube)
            del counts[cube]

    next_active.update(c for c in counts if counts[c] == 3)
    return next_active

    
cubes = load(sys.stdin)
for _ in range(6):
    cubes = run(cubes)

print(len(cubes))