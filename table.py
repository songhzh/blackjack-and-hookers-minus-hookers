from dealer import Dealer
from player import Player
from enum import Enum, auto
from hand import PlayerActions

class PlayerResult(Enum):
    WIN = auto()
    WIN_NATURAL = auto()
    PUSH = auto()
    LOSE = auto()

class Table:
    def __init__(self, players):
        if len(players) == 0:
            raise Exception('players cannot be empty')
        self.players = players
        self.dealer = Dealer()

    def play(self):
        self.play_init()
        print('Dealer\n', self.dealer.hand)
        if not self.dealer.hand.blackjack:
            self.play_players()
            self.play_dealer()
        self.play_resolve()

    def play_init(self):
        self.dealer.init()
        for p in self.players:
            p.init()
            self.dealer.deal(p.hand)
            self.dealer.deal(p.hand)
            print(p.name, '\n', p.hand)
        self.dealer.deal_self()
        self.dealer.deal_self()

    def play_players(self):
        for p in self.players:
            h = p.hand
            while h is not None:
               self.play_hand(p, h)
               h = h.next

    def play_hand(self, player, hand):
        while hand.playing:
            action = hand.act()
            if action == PlayerActions.HIT:
                self.dealer.deal(hand)
            if action == PlayerActions.STAND:
                break
            if action == PlayerActions.SPLIT:
                new_hand = hand.split()
                self.dealer.deal(hand)
                self.dealer.deal(new_hand)
            if action == PlayerActions.DOUBLE:
                player.double()
                self.dealer.deal(hand)
                break
            if action == PlayerActions.SURRENDER:
                hand.surrender()
                break

    def play_dealer(self):
        while self.dealer.hand.value < 16:
            self.dealer.deal_self()

    def play_resolve(self):
        print('Dealer', self.dealer.hand, self.dealer.hand.value)
        for p in self.players:
            h = p.hand
            while h is not None:
                result = self.resolve_hand(h)
                print(p.name, h, h.value, result)
                h = h.next

    def resolve_hand(self, h):
        if h.bust or h.surrendered:
            return PlayerResult.LOSE
        if h.blackjack:
            if self.dealer.hand.blackjack:
                return PlayerResult.PUSH
            elif h.natural:
                return PlayerResult.WIN_NATURAL
            else:
                return PlayerResult.WIN
        if self.dealer.hand.bust:
            return PlayerResult.WIN
        if self.dealer.hand.blackjack:
            return PlayerResult.LOSE
        return PlayerResult.WIN if h.value > self.dealer.hand.value else PlayerResult.LOSE