from solver import Solver

class Payout:
    def __init__(self, solver = Solver()):
        self.solver = solver

    def amount(self, word, rack, bet=5):
        minimum = 10
        multipliers = { 2: 1, 3: 1, 4: 1, 5: 2, 6: 3, 7: 5 }

        valid_words = self.solver.solve(rack)
        hand_points = self.solver.score_word(word)
        print(f'Valid Words: {valid_words}')
        print(f'Words: {word}')
        if hand_points >= minimum and word in valid_words:
            return bet * (hand_points // minimum) * multipliers[len(word)]
        else:
            return -bet

