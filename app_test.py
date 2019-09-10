import pytest
import app
import json

@pytest.fixture
def app():
    app = server.create_app()
    app.debug = True
    return app.test_client()

def test_solve(app):
    res = app.post('/solve', data=json.dumps(dict(selection='JAB', rack='ABHIJKL', coins=100)), content_type='application/json')
    wordlist = json.loads(res.data)['wordlist']
    winner = json.loads(res.data)['winner']
    coins = json.loads(res.data)['coins']
    assert winner == True
    assert coins == 105
    assert wordlist[0] == 'HIJAB-19'
    assert len(wordlist) == 48
    assert res.status_code == 200
