from flask import Flask, jsonify, request
from flask_cors import CORS # allow communication with react app
from solver import Solver
import sys

def create_app(config=None):
    app = Flask(__name__)
    CORS(app)

    @app.route('/solve', methods=['POST'])
    def solve():
        print(f'Request: {request}')
        solver = Solver()
        rack = request.json['rack']
        selection = request.json['selection']
        coins = int(request.json['coins'])

        wordlist = solver.solve(rack)
        wordlist.sort(key=lambda x: solver.score_word(x))
        wordlist.reverse()
        # average = sum([solver.score_word(word) for word in wordlist]) / len(wordlist)
        average = [solver.score_word(word) for word in wordlist][len(wordlist)//2]
        whee = [ f'{word}-{str(solver.score_word(word))}' for word in wordlist ]
        winner = selection in wordlist
        new_coins = coins + 5 if winner else coins - 5
        return jsonify({'wordlist': whee, 'average': average, 'winner': winner, 'coins': new_coins})

    return app

if __name__ == '__main__':
    app = create_app()
    app.debug = True
    app.run()
