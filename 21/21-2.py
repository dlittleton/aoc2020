from collections import Counter
import sys

class Foods:

    def __init__(self):
        self.counter = Counter()
        self.allergens = {}


    def parse(self, line):
        line = line.rstrip().rstrip(')')
        ingredients, allergens = line.split(' (contains ')
        return ingredients.split(' '), allergens.split(', ')


    def add(self, line):
        ingredients, allergens = self.parse(line)
        self.counter.update(ingredients)

        for a in allergens:
            if a in self.allergens:
                self.allergens[a].intersection_update(ingredients)
            else:
                self.allergens[a] = set(ingredients)


    def reduce(self):
        all_allergens = set(self.allergens.keys())
        while all_allergens:
            a = next(a for a in all_allergens if len(self.allergens[a]) == 1)
            all_allergens.remove(a)
            for other in all_allergens:
                self.allergens[other].difference_update(self.allergens[a])
        


    @ property
    def safe(self):
        all_ingredients = set(self.counter)

        for i in self.allergens.values():
            all_ingredients.difference_update(i)

        return all_ingredients

    
    @property
    def allergen_list(self):
        return ','.join(next(iter(self.allergens[a])) for a in sorted(self.allergens.keys()))

f = Foods()

for l in sys.stdin:
    f.add(l)

f.reduce()
v = sum(f.counter[i] for i in f.safe)
print(v)
print(f.allergen_list)