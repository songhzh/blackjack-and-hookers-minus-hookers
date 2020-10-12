from dealer import Dealer
from player import Player
from enum import Enum, auto
from hand import PlayerActions
from clear import *

class PlayerResult(Enum):
    WIN = auto()
    WIN_NATURAL = auto()
    PUSH = auto()
    LOSE = auto()

def print_hand(name, hand):
    print('{} ({:>2}) -{}'.format(hand, hand.value, name))

def print_dealer_hand(dealer):
    print('{} [?.?] (??) -Dealer'.format(dealer.hand.cards[0]))

class Table:
    def __init__(self, players):
        if len(players) == 0:
            raise Exception('players cannot be empty')
        self.players = players
        self.dealer = Dealer()

    def check_players(self, bet):
        valid = [p for p in self.players if p.cash >= bet]
        return len(valid) > 0

    def play(self, bet):
        self.play_init(bet)
        if self.dealer.hand.cards[0].rank in [1, 10] and self.dealer.hand.blackjack:
            print('Dealer has blackjack.')
        else:
            self.play_players()
            self.play_dealer()
        self.play_resolve()

    def play_init(self, bet):
        self.dealer.init()
        for p in self.players:
            p.init(bet)
            self.dealer.deal(p.hand)
            self.dealer.deal(p.hand)
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
            clear()
            print('Cash/Bet/Total: ${}/${}/${}'.format(player.cash - player.total_bet, player.total_bet, player.cash))
            print_dealer_hand(self.dealer)
            print_hand(player.name, hand)
            print()
            action = hand.act(player.can_double(hand.bet))
            if action == PlayerActions.HIT:
                self.dealer.deal(hand)
            if action == PlayerActions.STAND:
                break
            if action == PlayerActions.DOUBLE:
                hand.double()
                self.dealer.deal(hand)
                break
            if action == PlayerActions.SPLIT:
                new_hand = hand.split()
                self.dealer.deal(hand)
                self.dealer.deal(new_hand)
            if action == PlayerActions.SURRENDER:
                hand.surrender()
                break

    def play_dealer(self):
        while self.dealer.hand.value < 16:
            self.dealer.deal_self()

    def play_resolve(self):
        clear()
        print_hand('Dealer', self.dealer.hand)
        print()
        for p in self.players:
            h = p.hand
            while h is not None:
                result = self.resolve_hand(h)
                print_hand(p.name, h)
                if result == PlayerResult.WIN:
                    p.win(h.bet)
                    print('{} wins! +${}'.format(p.name, h.bet))
                if result == PlayerResult.WIN_NATURAL:
                    p.win_natural(h.bet)
                    print('{} has blackjack! +${}'.format(p.name, h.bet * 1.5))
                if result == PlayerResult.PUSH:
                    p.push()
                    print('{} pushes. +/-$0'.format(p.name))
                if result == PlayerResult.LOSE:
                    p.lose(h.bet)
                    print('{} loses... -${}'.format(p.name, h.bet))
                h = h.next
            print('{} has ${}'.format(p.name, p.cash))
        input('\nPress enter to continue')

    def resolve_hand(self, hand):
        if hand.bust or hand.surrendered:
            return PlayerResult.LOSE
        if hand.blackjack:
            if self.dealer.hand.blackjack:
                return PlayerResult.PUSH
            elif hand.natural:
                return PlayerResult.WIN_NATURAL
            else:
                return PlayerResult.WIN
        if self.dealer.hand.bust:
            return PlayerResult.WIN
        if self.dealer.hand.blackjack:
            return PlayerResult.LOSE
        return PlayerResult.WIN if hand.value > self.dealer.hand.value else PlayerResult.LOSE