import collections
import sys

class Filter:

    def __init__(self, init):
        self.size = len(init)
        self.values = collections.deque(init)

    def _has_value(self, value):
        for i, v in enumerate(self.values):
            for j in range(self.size):
                if v + self.values[j] == value:
                    return True

        return False

    def check(self, value):
        result = self._has_value(value)
        self.values.popleft()
        self.values.append(value)
        return result


def find_contiguous_sum(target):
    size = len(all_values)
    for i in range(size):
        sum = 0
        j = i
        while sum < target and j < size:
            sum += all_values[j]
            j += 1
            if sum == target:
                return min(all_values[i:j]), max(all_values[i:j])
            
        

count = 25
if len(sys.argv) > 1:
    count = int(sys.argv[1])

all_values = [int(l) for l in sys.stdin]

f = Filter(all_values[0:count])


target = 0
for v in all_values[count:]:
    if not f.check(v):
        target = v
        break

lo, hi = find_contiguous_sum(target)
print(target)
print(lo, hi)
print(lo + hi)
