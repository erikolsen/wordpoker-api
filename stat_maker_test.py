import pytest
from stat_maker import StatMaker
from solver import Solver
from word_list import WordList
from itertools import combinations

@pytest.fixture
def stat_maker():
    word_list = WordList().words
    return StatMaker(word_list)

def test_deck_combos(stat_maker):
    print(stat_maker.combinations_for_deck())
    assert True == False

# def test_total_chars(stat_maker):
    # assert stat_maker.total_chars == 2_439_263

# def test_char_count(stat_maker):
    # expected =  {'A': 188703,
                 # 'B': 44953,
                 # 'C': 98230,
                 # 'D': 81731,
                 # 'E': 275582,
                 # 'F': 28930,
                 # 'G': 67910,
                 # 'H': 60702,
                 # 'I': 220483,
                 # 'J': 4010,
                 # 'K': 22075,
                 # 'L': 127865,
                 # 'M': 70700,
                 # 'N': 163637,
                 # 'O': 161752,
                 # 'P': 73286,
                 # 'Q': 4104,
                 # 'R': 170521,
                 # 'S': 234672,
                 # 'T': 159471,
                 # 'U': 80636,
                 # 'V': 22521,
                 # 'W': 18393,
                 # 'X': 6852,
                 # 'Y': 39772,
                 # 'Z': 11772}

    # assert stat_maker.char_counts == expected

# def test_char_percents(stat_maker):
    # expected = {'A': 0.07736066180645547,
                # 'C': 0.0402703603506469,
                # 'B': 0.018428927098061997,
                # 'E': 0.11297756740458081,
                # 'D': 0.033506432065751005,
                # 'G': 0.027840376375979137,
                # 'F': 0.011860139722530945,
                # 'I': 0.0903891872258137,
                # 'H': 0.02488538546274018,
                # 'K': 0.00904986465174112,
                # 'J': 0.0016439391734306634,
                # 'M': 0.028984164479189,
                # 'L': 0.05241952179818248,
                # 'O': 0.06631183271340564,
                # 'N': 0.06708460711288615,
                # 'Q': 0.0016824754034312824,
                # 'P': 0.030044320764099647,
                # 'S': 0.09620610815643905,
                # 'R': 0.06990677102059105,
                # 'U': 0.03305752598223316,
                # 'T': 0.0653767141960502,
                # 'W': 0.007540392323419,
                # 'V': 0.009232706764297249,
                # 'Y': 0.01630492488919809,
                # 'X': 0.0028090451911089538,
                # 'Z': 0.004826047867737099}

    # assert stat_maker.char_percents == expected

# def test_letter_list(stat_maker):
    # assert len(stat_maker.letter_list(52)) == 50


