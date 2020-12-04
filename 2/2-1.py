import sys

valid = 0
for line in map(str.rstrip ,sys.stdin):
    rule, password = line.split(':')
    counts, symbol = rule.split(' ')
    lo, hi = counts.split('-')

    n = sum(1 for c in password if c == symbol)
    if int(lo) <= n <= int(hi):
        valid += 1

print(valid)
    