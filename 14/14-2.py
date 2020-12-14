import sys

bitsize = 36
memory = {}
mask = '0' * bitsize

def get_addresses(addr):
    initial = list(bin(addr)[2:].rjust(bitsize, '0'))
    
    results = []

    for i, c in enumerate(mask):
        if c == '0':
            if results:
                for j, r in enumerate(results):
                    results[j] = r + initial[i]
            else:
                results.append(initial[i])
        elif c == '1':
            if results:
                for j, r in enumerate(results):
                    results[j] = r + '1'
            else:
                results.append('1')
        elif c == 'X':
            if results:
                new = []
                for j, r in enumerate(results):
                    new.append(r + '1')
                    results[j] = r + '0'
                results.extend(new)
            else:
                results.append('0')
                results.append('1')

    for r in results:
        yield int(''.join(r), 2)

for l in map(str.rstrip, sys.stdin):
    arg, value = l.split(' = ')
    if arg == 'mask':
        mask = value
    else:
        idx = int(arg[4:-1])
        for addr in get_addresses(idx):
            memory[addr] = int(value)

n = sum(memory[k] for k in memory)
print(n)