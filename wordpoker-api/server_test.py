import pytest
import server
import json

@pytest.fixture
def app():
    app = server.create_app()
    app.debug = True
    return app.test_client()

def test_solve(app):
    res = app.post('/solve', data=json.dumps(dict(chosen='JAB', rack='ABHIJKL')), content_type='application/json')
    wordlist = json.loads(res.data)['wordlist']
    assert wordlist[0] == 'KIBLAH'
    assert len(wordlist) == 48
    assert res.status_code == 200
