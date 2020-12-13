_ = input()
schedule = input().strip().split(',')
bus_gaps = []

gap = 0
for s in schedule:
    if s != 'x':
        bus_gaps.append((int(s), gap))
    gap += 1

def find_first_match(bus, start, step):
    while (start + bus[1]) % bus[0] != 0:
        start += step
    
    return start


def get_period(bus, start, step):
    a = find_first_match(bus, start, step)
    b = find_first_match(bus, a + step, step)

    return (a, b - a)

start = 0
step = bus_gaps[0][0]
for b in bus_gaps[1:]:
    start, step = get_period(b, start, step)
    print(start, step)


print(start)