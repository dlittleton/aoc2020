import sys


def position(line):
    rows = line[0:7].replace('F', '0').replace('B', '1')
    cols = line[7:10].replace('L', '0').replace('R', '1')

    r = int(rows, 2)
    c = int(cols, 2)

    return r * 8 + c


highest = max(position(l) for l in sys.stdin)
print(highest)