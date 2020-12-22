import collections
import sys

def load_cards(lines):
    next(lines) # skip player
    for l in lines:
        if not l:
            break
        yield int(l)


def score(cards):
    return sum(i * c for i, c in enumerate(reversed(cards), 1))

lines = map(str.rstrip, sys.stdin)
p1 = collections.deque(load_cards(lines))
p2 = collections.deque(load_cards(lines))

while p1 and p2:
    a = p1.popleft()
    b = p2.popleft()
    if a > b:
        p1.append(a)
        p1.append(b)
    else:
        p2.append(b)
        p2.append(a)

print(p1)
print(p2)

print(score(p1) if p1 else score(p2))
