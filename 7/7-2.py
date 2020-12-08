import collections
import sys

bags = collections.defaultdict(dict)

def parse_child_bags(value):
    bags = value.split(',')
    for b in bags:
        color = b.strip(' .\n')
        if color != 'no other bags':
            c = color.split(' ')
            yield int(c[0]), ' '.join(c[1:-1])


def count_bags(c):
    total = 0
    if bags[c]:        
        for child in bags[c]:
            count = bags[c][child]
            total += count * (count_bags(child) + 1)

    print('Total for {0}: {1}'.format(c, total))
    return total


for line in sys.stdin:
    outer, inner = line.split('bags contain')
    outer = outer.strip()
    children = parse_child_bags(inner)
    for i, c in children:
        bags[outer][c] = i

print(bags)
n = count_bags('shiny gold')
print(n)