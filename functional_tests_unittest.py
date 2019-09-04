import unittest
import pdb
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class HomePageTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome(options=options)

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        self.browser.get('http://localhost:3000')
        self.assertIn('Word Poker', self.browser.title)
        header = self.browser.find_element_by_tag_name('header')
        self.assertIn('Word Poker', header.text)

    def test_new_rack(self):
        self.browser.get('http://localhost:3000')
        cards = self.browser.find_elements_by_class_name('card')
        expected = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.assertEqual(len(cards), 7)
        self.assertEqual(expected, [card.text for card in cards])


if __name__ == '__main__':
    unittest.main()

