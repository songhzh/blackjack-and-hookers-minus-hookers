from card import Card

class Hand:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def _get_ace_values(self, total, ace_count):
        if ace_count == 0:
            return 0
        if total + 10 + ace_count > 21:
            return ace_count
        return 10 + ace_count
    
    @property
    def value(self):
        aces = [card for card in self.cards if card.rank == 1]
        pips = [card for card in self.cards if card.rank in [2, 3, 4, 5, 6, 7, 8, 9, 10]]
        faces = [card for card in self.cards if card.rank in [11, 12, 13]]
        total = sum(card.rank for card in pips) + 10 * len(faces)
        total += self._get_ace_values(total, len(aces))
        return total

    def __str__(self):
        return ' '.join(str(card) for card in self.cards)