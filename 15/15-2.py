starting = map(int, input().split(','))

values = {}
i = 0
for current_number in starting:
    next_number = 0 if current_number not in values else values[current_number] - i
    values[current_number] = i
    i += 1

while i < 30000000:
    current_number = next_number
    next_number = 0 if current_number not in values else i - values[current_number]
    values[current_number] = i
    i += 1

print(current_number)