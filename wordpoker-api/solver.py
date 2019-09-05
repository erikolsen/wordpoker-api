from word_list import WordList
from bisect import bisect_left
from itertools import combinations
scores = {"A": 1, "C": 4, "B": 4, "E": 1, "D": 2, "G": 3,
         "F": 4, "I": 1, "H": 3, "K": 5, "J": 10, "M": 4,
         "L": 1, "O": 1, "N": 2, "Q": 10, "P": 4, "S": 1,
         "R": 1, "U": 2, "T": 1, "W": 4, "V": 5, "Y": 3,
         "X": 8, "Z": 10}


class Solver:
    def solve(self, string):
        anadict = WordList().all
        rack = ''.join(sorted(string))
        foundwords = []
        for i in range(2,len(rack)+1):
            for comb in combinations(rack,i):
                ana = ''.join(comb)
                j = bisect_left(anadict, ana)
                if j == len(anadict):
                    continue
                words = anadict[j].split()
                if words[0] == ana:
                    foundwords.extend(words[1:])
        return sorted(foundwords)

    def score_word(self, word):
        try:
            return sum([scores[c] for c in word])
        except:
            print(f'Found error: {word}')
