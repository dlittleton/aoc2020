class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


    def cycle(self):
        a = self.next
        b = a.next
        c = b.next

        self.next = c.next
        target = self.value - 1
        if target < lo:
            target = hi

        while target in (a.value, b.value, c.value):
            target -= 1
            if target < lo:
                target = hi

        replacement = all_nodes[target]
        c.next = replacement.next
        replacement.next = a

        return self.next


values = [int(c) for c in input()]
lo = min(values)
hi = max(values)

all_nodes = {}
last = None

for v in values:
    n = Node(v)
    all_nodes[v] = n
    if last is not None:
        last.next = n        
    last = n

for i in range(hi + 1, 1000000 + 1):
    n = Node(i)
    all_nodes[i] = n
    last.next = n
    last = n
hi = 1000000

node = all_nodes[values[0]]
last.next = node

for _ in range(10000000):
    node = node.cycle()

node = all_nodes[1]
a = node.next
b = a.next

print(a.value)
print(b.value)

print(a.value * b.value)