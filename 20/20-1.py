import collections
import sys

def get_value(pixels):
    b = ''.join(pixels).replace('#', '1').replace('.', '0')
    # Include forward and reverse to account for rotation/flipping
    return int(b, 2), int(b[::-1], 2)


class Tile:

    def __init__(self, id, pixels):
        self.id = id
        self.pixels = pixels

        self.values = [
            *get_value(self.pixels[0]),
            *get_value(p[9] for p in self.pixels),
            *get_value(self.pixels[9]),
            *get_value(p[0] for p in self.pixels)
        ]

        


tiles = {}

lines = [l for l in map(str.rstrip, sys.stdin) if l]
for i in range(0, len(lines), 11):
    id = int(lines[i][4:-1])
    pixels = [list(l) for l in lines[i+1:i+11]]
    tiles[id] = Tile(id, pixels)


c = collections.Counter()
for t in tiles:
    print(tiles[t].values)
    c.update(tiles[t].values)

singles = set(v for v in c if c[v] == 1)

edges_by_tiles = {t : sum(1 for v in tiles[t].values if v in singles) for t in tiles}

# Edges are double counted because of forward/reverse both being included
corners = [t for t in tiles if edges_by_tiles[t] == 4]
print(corners)

p = 1
for c in corners:
    p *= c
print(p)

