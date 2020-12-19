import collections
import sys
import re

Rule = collections.namedtuple('Rule', ['leaf', 'first', 'second'])
rulebook = {}

def do_11():
    x = expand('42')
    y = expand('31')

    # Repeat pattern 10 times. Arbitrarily chosen to cover input range
    expression = '('
    expression += '|'.join(x*i + y*i for i in range(1, 10)) 
    expression += ')'
    return expression


def do_8():
    x = expand('42')
    expression = '('
    expression += '|'.join(x*i for i in range(1, 10))
    expression += ')'
    return expression

def expand(key):
    if key == '11':
        return do_11()
    elif key == '8':
        return do_8()

    rule = rulebook[key]

    if rule.leaf:
        return rule.leaf
    
    expression = ''
    if rule.second:
        expression += '('

    for r in rule.first:
        expression += expand(r)

    if rule.second:
        expression += '|'

        for r in rule.second:
            expression += expand(r)

        expression += ')'
    
    return expression
            
 
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

r = expand('0')
complete = re.compile('^' + r + '$')

matching = [l for l in lines if complete.match(l)]
for m in matching:
    print(m)
print(len(matching))