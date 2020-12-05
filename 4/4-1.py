import sys

required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
values = dict()
valid = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        keys = values.keys()
        if all(r in keys for r in required):
            valid += 1
        values.clear()
        

    for pair in line.split():
        k, v = pair.split(':')
        values[k] = v


if all(r in keys for r in required):
            valid += 1

print(valid)