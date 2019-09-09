import pytest
from payout import Payout

@pytest.fixture
def payout():
    return Payout()

def test_loss(payout):
    bet = 5
    word = 'QQ'
    rack = 'QQASDFG'
    assert payout.amount(word, rack, bet) == -bet

def test_even_money(payout):
    bet = 5
    rack = 'QIASDFG'
    word = 'QI'
    assert payout.amount(word, rack, bet) == bet

def test_double_point_multipler(payout):
    bet = 5
    rack = 'QIASUZG'
    word = 'QUIZ'
    assert payout.amount(word, rack, bet) == bet * 2

def test_five_letter_bonus_over_min(payout):
    bet = 5
    rack = 'WHILEEE'
    word = 'WHILE'
    assert payout.amount(word, rack, bet) == bet * 2

def test_five_letter_bonus_under_min(payout):
    bet = 5
    rack = 'GONERWE'
    word = 'GONER'
    assert payout.amount(word, rack, bet) == -bet

def test_six_letter_bonus_over_min(payout):
    bet = 5
    rack = 'PYTHONY'
    word = 'PYTHON'
    assert payout.amount(word, rack, bet) == bet * 3

def test_seven_letter_bonus_over_min(payout):
    bet = 5
    rack = 'PYTHONS'
    word = 'PYTHONS'
    assert payout.amount(word, rack, bet) == bet * 5
