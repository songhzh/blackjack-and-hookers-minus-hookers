import random
from card import Card
from hand import Hand

num_decks = 4

class Dealer:
    def __init__(self):
        self.shoe = None
        self.hand = None

    def add_deck(self):
        for r in range(1, 14):
            for s in range(1, 5):
                self.shoe.append(Card(r, s))
    
    def init(self):
        self.shoe = []
        self.hand = Hand()
        for _ in range(num_decks):
            self.add_deck()
        random.shuffle(self.shoe)

    def deal(self, hand):
        card = self.shoe.pop()
        hand.add(card)

    def deal_self(self):
        self.deal(self.hand)