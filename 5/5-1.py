import math
import sys


def partition(lo, hi, seq):
    ''' seq is a sequence of booleans 
    
    True -- lower half
    False -- upper half
    '''
    for x in seq:
        half = math.ceil((hi - lo) / 2)
        if x:
            hi = lo + half
        else:
            lo = lo + half

    return lo


def position(line):
    rows = line[0:7]
    cols = line[7:10]

    r = partition(0, 127, (c == 'F' for c in rows))
    c = partition(0, 7, (c == 'L' for c in cols))
    return r * 8 + c


highest = max(position(l) for l in sys.stdin)
print(highest)