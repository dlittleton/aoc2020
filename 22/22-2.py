import collections
import sys

total_rounds = 0

def load_cards(lines):
    next(lines) # skip player
    for l in lines:
        if not l:
            break
        yield int(l)


def score(cards):
    return sum(i * c for i, c in enumerate(reversed(cards), 1))


def play(p1, p2):
    global total_rounds
    seen = set()
    p1 = collections.deque(p1)
    p2 = collections.deque(p2)

    while p1 and p2:

        total_rounds += 1
        state = (score(p1), score(p2))
        if state in seen:
            print('Instant win for p1', total_rounds)
            return True, p1, p2
        seen.add(state)

        a = p1.popleft()
        b = p2.popleft()
        if a <= len(p1) and b <= len(p2):
            p1_wins, _, _ = play(list(p1)[:a], list(p2)[:b])
        else:
            p1_wins = a > b
        
        
        if p1_wins:
            p1.append(a)
            p1.append(b)
        else:
            p2.append(b)
            p2.append(a)

    return bool(p1), p1, p2




lines = map(str.rstrip, sys.stdin)
player_1 = collections.deque(load_cards(lines))
player_2 = collections.deque(load_cards(lines))

print(player_1)
print(player_2)
p1_wins, player_1, player_2 = play(player_1, player_2)
print(player_1)
print(player_2)

print(score(player_1) if p1_wins else score(player_2))
