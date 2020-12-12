import sys

def heading_to_direction(h):
    directions = ['E', 'N', 'W', 'S']
    return directions[h]


def calculate_rotation(direction, amount):
    value = amount / 90
    if direction == 'R':
        value *= -1

    return value
    
wx, wy = 10, 1
x, y = 0, 0

for l in sys.stdin:
    c = l[0]
    value = int(l[1:])
    
    if c == 'F':
        x += value * wx
        y += value * wy
    elif c == 'L' or c == 'R':
        h = calculate_rotation(c, value)
        h = int(h % 4)

        if h == 0:
            pass
        elif h == 1:
            wx, wy = -wy, wx
        elif h == 2:
            wx, wy = -wx, -wy
        else:
            wx, wy = wy, -wx

    elif c == 'E':
        wx += value
    elif c == 'N':
        wy += value
    elif c == 'W':
        wx -= value
    elif c == 'S':
        wy -= value

    print('Ship: {0}, {1}'.format(x, y))
    print('Waypoint: {0}, {1}'.format(wx, wy))


print(x, y)
print(abs(x) + abs(y))