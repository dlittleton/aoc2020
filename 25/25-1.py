card = int(input())
door = int(input())

card_loops = 0
door_loops = 0

value = 1
subject = 7
mod = 20201227

i = 0
while card_loops == 0 or door_loops == 0:
    i += 1
    value = (value * subject) % mod
    if value == card:
        card_loops = i

    if value == door:
        door_loops = i

print(card_loops)
print(door_loops)

value = 1
for _ in range(card_loops):
    value = (value * door) % mod
print(value)

value =  1
for _ in range(door_loops):
    value = (value * card) % mod

print(value)
