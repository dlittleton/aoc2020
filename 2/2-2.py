import sys

valid = 0
for line in map(str.rstrip ,sys.stdin):
    rule, password = line.split(':')
    counts, symbol = rule.split(' ')
    a, b = map(int, counts.split('-'))

    chars = (password[a], password[b])

    # password has a leading space due to above parsing, 
    # effectively making it 1 indexed already
    count = sum(1 for c in chars if c == symbol)
    if count == 1:
        valid += 1

print(valid)
    