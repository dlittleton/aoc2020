import re
import sys

value = re.compile(r"^(?P<value>\d+)$")
expression = re.compile(r"(?P<x>\d+)\s*(?P<op>[+*])\s*(?P<y>\d+)")
paren = re.compile(r"\((?P<value>\d+)\)")

def calculate(match):
    x = int(match['x'])
    y = int(match['y'])

    return str( x * y if match['op'] == '*' else x + y)

def evaluate(line):
    while not value.match(line):
        line, replacements = expression.subn(calculate, line, 1)

        replacements = 1
        while replacements > 0:
            line, replacements = paren.subn(r'\1', line)
    
    return int(line)

results = []
for l in map(str.rstrip, sys.stdin):
    results.append(evaluate(l))

print(sum(results))    