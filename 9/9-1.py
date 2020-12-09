import collections
import sys

class Filter:

    def __init__(self, size):
        self.size = size
        self.values = collections.deque()

    def load(self, stream):
        for _ in range(self.size):
            self.values.append(int(stream.readline()))

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
        

count = 25
if len(sys.argv) > 1:
    count = int(sys.argv[1])
f = Filter(count)
f.load(sys.stdin)

for v in map(int, sys.stdin):
    if not f.check(v):
        print(v)
