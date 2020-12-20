import sys

class Grid:

    def __init__(self, size):
        self.size = size
        self._max_index = size - 1

        self.x_flipped = False
        self.y_flipped = False
        self.rotation = 0
        
        self._values = ['.'] * size * size


    def _find_index(self, x, y):
        if self.x_flipped:
            x = self._max_index - x

        if self.y_flipped:
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

    def flip_x(self):
        self.x_flipped = not self.x_flipped


    def flip_y(self):
        self.y_flipped = not self.y_flipped

    
    def rotate(self):
        self.rotation = (self.rotation + 1) % 4


    def all_permutations(self):
        for _ in range(4):
            self.rotate()
            yield self

        self.flip_x()
        for _ in range(4):
            self.rotate()
            yield self

        self.flip_y()
        for _ in range(4):
            self.rotate()
            yield self

        self.flip_x()
        for _ in range(4):
            self.rotate()
            yield self



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

    @property
    def top(self):
        return [self[0,i] for i in range(self.size)]

    @property
    def right(self):
        return [self[i, self.size - 1] for i in range(self.size)]
    
    @property
    def bottom(self):
        return [self[self.size - 1, i] for i in range(self.size)]

    @property
    def left(self):
        return [self[i, 0] for i in range(self.size)]


class Arrangement:

    def __init__(self, tiles):
        self.size = int(len(tiles) ** 0.5)
        self.available = list(tiles)


    def _find_where(self, compare):

        for a in self.available:
            for t in a.all_permutations():
                if compare(t):
                    return t

   
    def solve(self):

        tile = self.available.pop()
        solution = {(0,0): tile}

        i = 0
        a = self._find_where(lambda t: t.left == tile.right)
        while a:
            i += 1
            solution[0,i] = tile = a
            self.available.remove(a)
            a = self._find_where(lambda t: t.left == tile.right)

        high = i

        i = 0
        tile = solution[0,0]
        a = self._find_where(lambda t: t.right == tile.left)
        while a:
            i -= 1
            solution[0,i] = tile = a
            self.available.remove(a)
            a = self._find_where(lambda t: t.right == tile.left)

        low = i

        for i in range(low, high+1):
            tile = solution[0,i]
            j = 0
            a = self._find_where(lambda t: t.bottom == tile.top)
            while a:
                j -= 1
                solution[j,i] = tile = a
                self.available.remove(a)
                a = self._find_where(lambda t: t.bottom == tile.top)

            tile = solution[0,i]
            j = 0
            a = self._find_where(lambda t: t.top == tile.bottom)
            while a:
                j += 1
                solution[j,i] = tile = a
                self.available.remove(a)
                a = self._find_where(lambda t: t.top == tile.bottom)

            
        return solution

        
tiles = {}

lines = [l for l in map(str.rstrip, sys.stdin) if l]
for i in range(0, len(lines), 11):
    id = int(lines[i][4:-1])
    t = Tile(id)
    for x, line in enumerate(lines[i+1:i+11]):
        for y, c in enumerate(line):
            t[x,y] = c
    tiles[id] = t


puzzle = Arrangement(list(tiles.values()))
s = puzzle.solve()

i_lo = min(k[0] for k in s)
i_hi = max(k[0] for k in s)
j_lo = min(k[1] for k in s)
j_hi = max(k[1] for k in s)

solution = s[i_lo,j_lo].id * s[i_lo, j_hi].id * s[i_hi, j_lo].id * s[i_hi, j_hi].id
print(solution)