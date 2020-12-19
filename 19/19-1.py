import collections
import sys

Rule = collections.namedtuple('Rule', ['leaf', 'first', 'second'])
rulebook = {}

def expand(key, results = None):
    if results is None:
        results = [[]]

    rule = rulebook[key]

    if rule.leaf:
        for r in results:
            r.append(rule.leaf)
    elif rule.second:
        new = [v[:] for v in results]
        for r in rule.first:
            expand(r, results)

        for r in rule.second:
            expand(r, new)

        results.extend(new)
    else:
        for r in rule.first:
            expand(r, results)

    return results
            
 
lines = map(str.rstrip, sys.stdin)
for line in lines:
    if not line:
        break
    key, r = line.split(': ')
    if r.startswith('"'):
        rulebook[key] = Rule(r[1:-1], [], [])
    elif '|' in r:
        x, y = r.split(' | ')
        rulebook[key] = Rule(None, x.split(' '), y.split(' '))
    else:
        rulebook[key] = Rule(None, r.split(' '), [])

space = set(''.join(r) for r in expand('0'))
matching = [l for l in lines if l in space]
print(len(matching))