from hand import Hand

class Player:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.hand = None

    def init(self, bet):
        self.hand = Hand(bet)

    def win(self, bet):
        self.cash += bet

    def win_natural(self, bet):
        self.cash += bet * 1.5

    def push(self):
        pass

    def lose(self, bet):
        self.cash -= bet

    @property
    def total_bet(self):
        total_bet = 0
        h = self.hand
        while h is not None:
            total_bet += h.bet
            h = h.next
        return total_bet

    def can_double(self, bet):
        return self.cash - self.total_bet - bet >= 0
        