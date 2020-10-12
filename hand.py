from card import Card
from enum import Enum, auto

class PlayerActions(Enum):
    HIT = 1
    STAND = 2
    DOUBLE = 3
    SPLIT = 4
    SURRENDER = 0

def get_input(valid_inputs):
    while True:
        try:
            value = int(input(' > '))
            if value in valid_inputs:
                return value
        except KeyboardInterrupt:
            exit(0)
        except:
            pass

class Hand:
    def __init__(self, bet=None):
        self.cards = []
        self.surrendered = False
        self.is_split = False
        self.next = None
        self.first_action = True
        self.bet = bet

    def init_split(self, card):
        self.cards = [card]
        self.is_split = True
        self.first_action = True

    def add(self, card):
        self.cards.append(card)

    def double(self):
        self.bet *= 2

    def split(self):
        a, b, *_ = self.cards
        self.init_split(a)
        self.next = Hand(self.bet)
        self.next.init_split(b)
        return self.next

    def surrender(self):
        self.surrendered = True
        self.bet *= 0.5

    def get_ace_values(self, total, ace_count):
        if ace_count == 0:
            return 0
        if total + 10 + ace_count > 21:
            return ace_count
        return 10 + ace_count

    def act(self, can_double):
        valid_inputs = [1, 2]
        print(' 1. Hit')
        print(' 2. Stand')
        if can_double:
            print(' 3. Double down')
            valid_inputs.append(3)
        else:
            print(' x. Double down')
        a, b, *_ = self.cards
        can_split = a.value == b.value and a.value != 1
        if self.first_action:
            if can_split:
                print(' 4. Split')
                valid_inputs.append(4)
            else:
                print(' x. Split')
            print(' 0. Surrender')
            valid_inputs.append(0)
        else:
            print(' x. Split')
            print(' x. Surrender')
        self.first_action = False
        value = get_input(valid_inputs)
        return  PlayerActions(value)
    
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
        return self.blackjack and len(self.cards) == 2 and not self.is_split

    def __str__(self):
        return ' '.join(str(card) for card in self.cards)