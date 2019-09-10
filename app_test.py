import pytest
import app
import json

@pytest.fixture
def client():
    test_app = app.create_app()
    test_app.debug = True
    return test_app.test_client()

def test_deal(client):
    res = client.get('/deal')
    deck = json.loads(res.data)['deck']
    assert len(deck) == 102
    assert res.status_code == 200

def test_solve(client):
    res = client.post('/solve', data=json.dumps(dict(selection='JAB', rack='ABHIJKL', coins=100)), content_type='application/json')
    wordlist = json.loads(res.data)['wordlist']
    winner = json.loads(res.data)['winner']
    coins = json.loads(res.data)['coins']
    assert winner == True
    assert coins == 105
    assert wordlist[0] == 'HIJAB-19'
    assert len(wordlist) == 48
    assert res.status_code == 200
