departure = int(input())
busses = [int(x) for x in input().split(',') if x != 'x']

def earliest_departure(t, id):
    n = id
    while n <= t:
        n += id

    return (n - t, id)

results = [earliest_departure(departure, b) for b in busses]
print(results)

best = min(results, key=lambda r : r[0])
print(best)
print(best[0] * best[1])
