import sys

lines = [l.rstrip() for l in sys.stdin.readlines()]
trees = 0
index = 0

# skip first line
for l in lines[1:]:
    index += 3
    if l[index % len(l)] == '#':
        trees += 1

print(trees)