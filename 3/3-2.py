import sys

lines = [l.rstrip() for l in sys.stdin.readlines()]
ylen = len(lines)
xlen = len(lines[1])

def count_trees(x, y):
    trees = 0
    xpos = x
    ypos = y

    while ypos < ylen:
        if lines[ypos][xpos % xlen] == '#':
            trees += 1
        xpos += x
        ypos += y

    return trees


slopes = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2)
]

p = 1
for s in slopes:
    p *= count_trees(*s)
print(p)
