from flask import Flask, jsonify, request
from flask_cors import CORS # allow communication with react app
import json
from solver import Solver
from payout import Payout
import sys

def create_app(config=None):
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def hello_world():
        return 'Word Poker!'

    @app.route('/deal')
    def deal():
        # with open('mock_deck.json', 'r') as f:
        with open('deck.json', 'r') as f:
            deck = json.load(f)
        return jsonify({'deck': deck})

    @app.route('/solve', methods=['POST'])
    def solve():
        print(f'Request: {request}')
        solver = Solver()
        payout = Payout()
        rack = request.json['rack']
        selection = request.json['selection']
        coins = int(request.json['coins'])

        wordlist = solver.solve(rack)
        wordlist.sort(key=lambda x: solver.score_word(x))
        wordlist.reverse()

        average = [solver.score_word(word) for word in wordlist][len(wordlist)//2]
        wordlist_presenter = [ f'{word}-{str(solver.score_word(word))}' for word in wordlist ]
        winner = selection in wordlist
        new_coins = coins + payout.amount(selection, rack)
        return jsonify({'wordlist': wordlist_presenter, 'average': average, 'winner': winner, 'coins': new_coins})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
