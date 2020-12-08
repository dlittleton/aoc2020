import collections
import sys

bags = collections.defaultdict(set)

def parse_child_bags(value):
    bags = value.split(',')
    for b in bags:
        color = b.strip(' .\n')
        if color != 'no other bags':
            c = color.split(' ')
            yield ' '.join(c[1:-1])

def count_parents(color):
    parents = set()
    colors = list(bags[color])
    while colors:
        c = colors.pop()
        parents.add(c)
        print(c, bags[c])
        colors.extend(bags[c])

    return len(parents)




for line in sys.stdin:
    outer, inner = line.split('bags contain')
    outer = outer.strip()
    children = parse_child_bags(inner)
    for c in children:
        bags[c].add(outer)

print(bags)
n = count_parents('shiny gold')
print(n)