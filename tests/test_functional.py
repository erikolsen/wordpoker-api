import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from mock_deck import MOCK_DECK

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_home_page(browser):
    browser.get('http://localhost:3000')
    assert 'Word Poker' == browser.title
    header = browser.find_element_by_id('app-name')
    coins = browser.find_element_by_id('coins')
    assert coins.text == '100'
    assert 'Word Poker' == header.text

def test_new_cards(browser):
    browser.get('http://localhost:3000')
    cards = browser.find_elements_by_class_name('card')
    expected = [''.join(card['letter']+card['value']) for card in MOCK_DECK[0:7]]
    assert len(cards) == 7
    assert expected == [card.text for card in cards]

def test_hold_card(browser):
    browser.get('http://localhost:3000')
    cards = browser.find_elements_by_class_name('card')
    cards[0].click()
    held = browser.find_elements_by_class_name('held')
    assert 1 == len(held)
    assert held[0].text == 'HELD'

def test_unhold_card(browser):
    browser.get('http://localhost:3000')
    cards = browser.find_elements_by_class_name('card')
    cards[0].click()
    held = browser.find_elements_by_class_name('held')
    assert 1 == len(held)
    cards[0].click()
    held = browser.find_elements_by_class_name('held')
    assert 0 == len(held)

def test_hold_and_draw(browser):
    browser.get('http://localhost:3000')
    cards = browser.find_elements_by_class_name('card')
    cards[0].click()
    draw_button = browser.find_element_by_id('draw')
    draw_button.click()
    new_cards = browser.find_elements_by_class_name('card')
    expected = ['A1', 'H3', 'I1', 'J10', 'K5', 'L2', 'M4']
    assert expected == [card.text for card in new_cards]

def test_select_word(browser):
    browser.get('http://localhost:3000')
    cards = browser.find_elements_by_class_name('card')
    cards[0].click()
    cards[1].click()
    draw_button = browser.find_element_by_id('draw')
    draw_button.click()
    cards[4].click()
    cards[0].click()
    cards[1].click()
    selection = browser.find_element_by_id('selection')
    total = browser.find_element_by_id('total')
    assert selection.text == 'JAB'
    assert total.text == '15'

def test_submit_word(browser):
    browser.get('http://localhost:3000')
    cards = browser.find_elements_by_class_name('card')
    cards[0].click()
    cards[1].click()
    draw_button = browser.find_element_by_id('draw')
    draw_button.click()
    cards[4].click()
    cards[0].click()
    cards[1].click()

    submit_button = browser.find_element_by_id('submit')
    submit_button.click()

    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'wordlist')))
    wordlist = browser.find_elements_by_class_name('wordlist')
    coins = browser.find_element_by_id('coins')
    expected = 'HIJAB-19'

    assert coins.text == '105'
    assert expected == wordlist[0].text
