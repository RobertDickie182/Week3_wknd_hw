import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Hearts", 1)
        self.card2 = Card("Clubs", 6)
        self.cards = [self.card1, self.card2]

    def test_card_ace(self):
        self.assertEqual(True, self.card1.value)

    def test_highest_card(self):
        self.assertEqual("Clubs", self.card2.suit)

    def test_total_calculation(self):
        result = CardGame.cards_total(self, self.cards)
        self.assertEqual("You have a total of 7", result)

