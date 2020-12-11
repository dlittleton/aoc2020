import collections
import sys

def differences(values):
    prev = 0
    for v in values:
        yield v - prev
        prev = v
    yield 3

values = sorted(map(int, sys.stdin))
count = collections.Counter(differences(values))
print(count[1], count[3])
print(count[1] * count[3])