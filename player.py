from hand import Hand

class Player:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.hand = None
        self.bet = None

    def init(self):
        self.hand = Hand()

    def double(self):
        pass

    def win(self):
        pass

    def win_natural(self):
        pass

    def push(self):
        pass

    def lose(self):
        pass