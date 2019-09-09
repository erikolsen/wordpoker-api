from itertools import combinations
from solver import Solver
from math import floor

EMPTY_LETTERS  = {"A": 0, "C": 0, "B": 0, "E": 0, "D": 0, "G": 0,
                  "F": 0, "I": 0, "H": 0, "K": 0, "J": 0, "M": 0,
                  "L": 0, "O": 0, "N": 0, "Q": 0, "P": 0, "S": 0,
                  "R": 0, "U": 0, "T": 0, "W": 0, "V": 0, "Y": 0,
                  "X": 0, "Z": 0}

class StatMaker:
    def __init__(self, wordlist):
        self.wordlist = wordlist
        self.total_chars = sum([len(word) for word in wordlist]) # 2439263


    @property
    def char_counts(self):
        chars = EMPTY_LETTERS.copy()
        for word in self.wordlist:
            for char in word:
                chars[char] += 1
        return chars

    @property
    def char_percents(self):
        return {key: value/self.total_chars for key, value in self.char_counts.items() }

    def letters_per_deck_size(self, size):
        return { key: floor(value * size) for key, value in self.char_percents.items() }

    def letters_per_deck_size(self, size):
        return { key: floor(value * size) for key, value in self.char_percents.items() }

    def letter_list(self, size):
        return [letter for letter, number in self.letters_per_deck_size(size).items() for _ in range(number if number > 0 else 1)]

    def combinations_for_deck(self):
        solver = Solver()
        combos = list(combinations(self.letter_list(52), 7)) # 99_884_400
        joined = [''.join(combo) for combo in combos]
        unsolved = []
            # solved = solver.solve(word)
            # if len(solved) > 0:
                # whee.append(sum([solver.score_word(x) for x in solved])/ len(solved))
            # else:
                # unsolved.append(word)

        whee = [solver.score_word(word) for word in joined]
        print(f'Unsolved: {len(unsolved)}')
        average = sum(whee) / len(whee)
        return average #f'{} {}'

