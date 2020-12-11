import sys

def count_arrangements(values):
    paths = [0] * len(values)
    paths[-1] = 1
    i = len(values) - 1
    while i >= 0:

        for j in range(i + 1, len(values)):
            if values[j] - values[i] > 3:
                break
            paths[i] += paths[j]

        i -= 1

    return paths[0]


values = [int(l) for l in sys.stdin]
values.append(0)
values.sort()
values.append(values[-1] + 3)
print(count_arrangements(values))