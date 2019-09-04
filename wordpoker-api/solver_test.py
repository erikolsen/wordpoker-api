from solver import Solver

def test_solve():
    solver = Solver()
    dealt = 'JREZQXW'
    expected = ['ER', 'EX', 'JEW', 'RE', 'REW', 'REX', 'REZ', 'WE', 'WEX', 'ZEX']
    whee = [(word, solver.score_word(word)) for word in expected]
    assert solver.solve(dealt) == expected
