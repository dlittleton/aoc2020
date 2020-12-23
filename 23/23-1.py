import collections

def cycle(values):
    current = values.popleft()
    removed = [values.popleft() for _ in range(3)]
    
    target = current - 1
    while target not in values:
        target -= 1
        if target < low:
            target = hi

    index = values.index(target) + 1
    
    for i, r in enumerate(removed):
        values.insert(index + i, r)

    values.append(current)
    return values

values = collections.deque(map(int, input()))
low = min(values)
hi = max(values)

for i in range(100):
    values = cycle(values)

start = values.index(1)
result = ''.join(str(values[i % len(values)]) for i in range(start + 1, start + len(values)))
print(result)
