import re
import sys

value = re.compile(r"^(?P<value>\d+)$")
addition = re.compile(r"(?P<x>\d+)\s*\+\s*(?P<y>\d+)")
mparen = re.compile(r"(?P<x>\d+)\s*\*\s*(?P<y>\d+)(?=\))")
multiplication = re.compile(r"(?P<x>\d+)\s*\*\s*(?P<y>\d+)")
paren = re.compile(r"\((?P<value>\d+)\)")

def add(match):
    x = int(match['x'])
    y = int(match['y'])

    return str(x + y)


def mult(match):
    x = int(match['x'])
    y = int(match['y'])

    return str(x * y)

def evaluate(line):
    while not value.match(line):
        replacements = 1
        while replacements > 0:
            line, replacements = addition.subn(add, line)

        line, replacements = paren.subn(r'\1', line)
        if replacements != 0:
            continue
        
        line, replacements = mparen.subn(mult, line, 1)
        if replacements != 0:
            continue

        line = multiplication.sub(mult, line, 1)
    
    return int(line)

results = []
for l in map(str.rstrip, sys.stdin):
    results.append(evaluate(l))

print(sum(results))    