from itertools import combinations
from solver import Solver
from math import floor

if __name__ == '__main__':
    solver = Solver()
    combos = list(combinations(self.letter_list(52), 7)) # 99_884_400
    # joined = [''.join(combo) for combo in combos]

    deck = [''.join(combo) for combo in combos]

    print(deck)
    f = open('combos.json','w')
    f.write(deck)
    f.close()
