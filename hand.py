from card import Card
from enum import Enum, auto

class PlayerActions(Enum):
    HIT = auto()
    STAND = auto()
    SPLIT = auto()
    DOUBLE = auto()
    SURRENDER = auto()

class Hand:
    def __init__(self):
        self.cards = []
        self.surrendered = False
        self.split = False
        self.next = None

    def split_init(self, card):
        self.cards = [card]
        self.split = True

    def add(self, card):
        self.cards.append(card)

    def split(self):
        a, b = self.cards
        self.init_split(a)
        self.next = Hand()
        self.next.init_split(b)
        return self.next

    def surrender(self):
        self.surrendered = True

    def get_ace_values(self, total, ace_count):
        if ace_count == 0:
            return 0
        if total + 10 + ace_count > 21:
            return ace_count
        return 10 + ace_count

    def act(self):
        action = PlayerActions.STAND
        if action == PlayerActions.SURRENDER:
            self.surrendered = True
        return action
    
    @property
    def value(self):
        non_aces = [card for card in self.cards if card.rank != 1]
        total = sum(card.value for card in non_aces)
        total += self.get_ace_values(total, len(self.cards) - len(non_aces))
        return total

    @property
    def playing(self):
        return self.value < 21

    @property
    def bust(self):
        return self.value > 21

    @property
    def blackjack(self):
        return self.value == 21

    @property
    def natural(self):
        return self.blackjack and len(self.cards) == 2

    def __str__(self):
        return ' '.join(str(card) for card in self.cards)