from solver import Solver
from word_list import WordList
from itertools import combinations

def test_solve():
    solver = Solver()
    wordlist = WordList().words
    dealt = 'JREZQXW'
    expected = ['ER', 'EX', 'JEW', 'RE', 'REW', 'REX', 'REZ', 'WE', 'WEX', 'ZEX']
    assert solver.solve(dealt) == expected

