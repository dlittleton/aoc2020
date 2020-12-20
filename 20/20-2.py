import sys

class Grid:

    def __init__(self, size):
        self.size = size
        self._max_index = size - 1

        self.flipped = False
        self.rotation = 0
        
        self._values = ['.'] * size * size


    def _find_index(self, x, y):
        if self.flipped:
            y = self._max_index - y

        if self.rotation == 1:
            x, y = y, self._max_index - x
        elif self.rotation == 2:
            x, y = self._max_index - x, self._max_index - y
        elif self.rotation == 3:
            x, y = self._max_index - y, x

        return (x * self.size) + y



    def __getitem__(self, pos):
        idx = self._find_index(*pos)
        return self._values[idx]


    def __setitem__(self, pos, value):
        idx = self._find_index(*pos)
        self._values[idx] = value

    def flip(self):
        self.flipped = not self.flipped

    
    def rotate(self):
        self.rotation = (self.rotation + 1) % 4


    def dump(self):
        for i in range(self.size):
            l = ''
            for j in range(self.size):
                l += self[i,j]
            print(l)
        print()


class Tile(Grid):

    def __init__(self, id):
        super().__init__(10)
        self.id = id


    def dump(self):
        print('Tile {0}'.format(self.id))
        super().dump()


tiles = {}

lines = [l for l in map(str.rstrip, sys.stdin) if l]
for i in range(0, len(lines), 11):
    id = int(lines[i][4:-1])
    t = Tile(id)
    for x, line in enumerate(lines[i+1:i+11]):
        for y, c in enumerate(line):
            t[x,y] = c
    tiles[id] = t

print(len(tiles))