import sys

bitsize = 36
memory = {}
mask = '0' * bitsize

def apply_mask(v):
    value = list(bin(int(v))[2:].rjust(bitsize, '0'))
    for i, c in enumerate(mask):
        if c != 'X':
            value[i] = c
    
    return int(''.join(value), 2)

for l in map(str.rstrip, sys.stdin):
    arg, value = l.split(' = ')
    if arg == 'mask':
        mask = value
    else:
        idx = int(arg[4:-1])
        memory[idx] = apply_mask(value)

n = sum(memory[k] for k in memory)
print(n)