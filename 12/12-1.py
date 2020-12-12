import sys

def heading_to_direction(h):
    directions = ['E', 'N', 'W', 'S']
    return directions[h]


def calculate_rotation(direction, amount):
    value = amount / 90
    if direction == 'R':
        value *= -1

    return value
    

x, y, h = 0, 0 ,0

for l in sys.stdin:
    c = l[0]
    value = int(l[1:])
    
    if c == 'F':
        c = heading_to_direction(h)

    if c == 'L' or c == 'R':
        h += calculate_rotation(c, value)
        h = int(h % 4)
    elif c == 'E':
        x += value
    elif c == 'N':
        y += value
    elif c == 'W':
        x -= value
    elif c == 'S':
        y -= value


print(x, y)
print(abs(x) + abs(y))