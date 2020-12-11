import sys

class Seats:

    def __init__(self, rows):
        self.seats = rows
        self.nrows = len(self.seats)
        self.ncols = len(self.seats[0])


    def count_neighbors(self, r, c):
        neighbors = 0
        rows = [r - 1, r, r + 1]
        cols = [c - 1, c, c + 1]

        for i in rows:
            for j in cols:
                if i == r and j == c:
                    continue
                if 0 <= i < self.nrows and 0 <= j < self.ncols and self.seats[i][j] == '#':
                    neighbors += 1

        return neighbors


    def print(self):
        for row in self.seats:
            print(row)


    @property
    def occupied(self):
        n = 0
        for r in self.seats:
            for c in r:
                if c == '#':
                    n += 1

        return n


    def step(self):

        updates = []
        for r, row in enumerate(self.seats):
            for c, seat in enumerate(row):
                if seat == '.':
                    continue
                
                neighbors = self.count_neighbors(r, c)
                if seat == 'L' and neighbors == 0:
                    updates.append((r, c, '#'))
                elif seat == '#' and neighbors >= 4:
                    updates.append((r, c, 'L'))

        for r, c, seat in updates:
            self.seats[r][c] = seat

        return len(updates)

        
seats = Seats([list(l.strip()) for l in sys.stdin])

updates = 1
while updates > 0:
    updates = seats.step()

print(seats.occupied)