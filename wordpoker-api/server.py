from flask import Flask, jsonify, request
from flask_cors import CORS # allow communication with react app
from solver import Solver
import sys

def create_app(config=None):
    app = Flask(__name__)
    CORS(app)

    @app.route('/solve', methods=['POST'])
    def solve():
        solver = Solver()
        rack = request.json['rack']
        wordlist = solver.solve(rack)
        wordlist.sort(key=len)
        wordlist.reverse()
        return jsonify({'wordlist': wordlist})

    return app

if __name__ == '__main__':
    app = create_app()
    app.debug = True
    app.run()
