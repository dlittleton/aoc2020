import collections
import sys

Rule = collections.namedtuple('Rule', ['lo', 'hi'])

notes = map(str.strip, sys.stdin)
rules = collections.defaultdict(list)

def matches_any_rules(v):
    for k in rules:
        for r in rules[k]:
            if r.lo <= v <= r.hi:
                return True

    return False

for line in notes:
    if not line:
        break
    name, definition = line.split(': ')
    ranges = definition.split(' or ')
    for r in ranges:
        lo, hi = map(int, r.split('-'))
        rules[name].append(Rule(lo, hi))

_ = next(notes) # your ticket:
my_ticket = [int(v) for v in next(notes).split(',')]

_ = next(notes) # blank line:
_ = next(notes) # nearby tickets:

unmatched = []
for line in notes:
    values = [int(v) for v in line.split(',')]
    for v in values:
        if not matches_any_rules(v):
            unmatched.append(v)
        

print(unmatched)
print(sum(unmatched))

