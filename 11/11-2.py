import sys

class Seats:

    def __init__(self, rows):
        self.seats = rows
        self.nrows = len(self.seats)
        self.ncols = len(self.seats[0])

    
    def visible_search(self, i, j, istep, jstep):
        i += istep
        j += jstep
        while 0 <= i < self.nrows and 0 <= j < self.ncols:
            if self.seats[i][j] == 'L':
                return 0
            elif self.seats[i][j] == '#':
                return 1

            i += istep
            j += jstep

        return 0


    def count_visible(self, r, c):
        
        neighbors = 0
    
        neighbors += (
            self.visible_search(r, c, -1, -1) + 
            self.visible_search(r, c, -1, 0)  + 
            self.visible_search(r, c, -1, 1) + 
            self.visible_search(r, c, 0, -1) + 
            self.visible_search(r, c, 0, 1) + 
            self.visible_search(r, c, 1, -1) +
            self.visible_search(r, c, 1, 0) + 
            self.visible_search(r, c, 1, 1))

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
                
                neighbors = self.count_visible(r, c)
                if seat == 'L' and neighbors == 0:
                    updates.append((r, c, '#'))
                elif seat == '#' and neighbors >= 5:
                    updates.append((r, c, 'L'))

        for r, c, seat in updates:
            self.seats[r][c] = seat

        return len(updates)

        
seats = Seats([list(l.strip()) for l in sys.stdin])

updates = 1
while updates > 0:
    updates = seats.step()

print(seats.occupied)