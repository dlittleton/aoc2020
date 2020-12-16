import sys

class Rule:

    def __init__(self, name, ranges):
        self.name = name
        self.ranges = ranges

    
    @classmethod
    def parse(cls, line):
        name, definition = line.split(': ')
        ranges = []
        for r in definition.split(' or '):
            lo, hi = map(int, r.split('-'))
            ranges.append(range(lo, hi + 1)) # inclusive
        return cls(name, ranges)

    
    def match(self, value):
        return any(value in r for r in self.ranges)

notes = map(str.strip, sys.stdin)
rules = []

for line in notes:
    if not line:
        break
    rules.append(Rule.parse(line))

_ = next(notes) # your ticket:
my_ticket = [int(v) for v in next(notes).split(',')]

_ = next(notes) # blank line:
_ = next(notes) # nearby tickets:

tickets = [[int(v) for v in l.split(',')] for l in notes]
valid_tickets = [t for t in tickets if all(any(r.match(v) for r in rules) for v in t)]

possible_rules = [set(rules) for r in rules]
for i, pr in enumerate(possible_rules):
    temp = list(pr)
    for r in temp:
        if any(not r.match(t[i]) for t in valid_tickets):
            pr.remove(r)


# Reduce
while not all(len(pr) == 1 for pr in possible_rules):
    for i, pr in enumerate(possible_rules):
        if(len(pr) == 1):
            print("Found unique: {0}".format([r.name for r in pr]))
            for j, other in enumerate(possible_rules):
                if i != j:
                    other.difference_update(pr)

p = 1
for i, r in enumerate(possible_rules):
    rule = r.pop()
    if rule.name.startswith('departure'):
        p *= my_ticket[i]

print(p)