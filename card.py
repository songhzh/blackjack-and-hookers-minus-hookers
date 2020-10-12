suit_unicodes_fill = {
    1: u'\U00002660',
    2: u'\U00002665',
    3: u'\U00002666',
    4: u'\U00002663',
    5: 'x'
}

suit_unicodes_line = {
    1: u'\U00002664',
    2: u'\U00002661',
    3: u'\U00002662',
    4: u'\U00002667',
    5: 'x'
}

card_ranks = {
    1: 'A',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'T',
    11: 'J',
    12: 'Q',
    13: 'K'
}

class Card:
    def __init__(self, rank, suit = 5):
        self.rank = rank
        self.suit = suit

    @property
    def value(self):
        if self.rank in [11, 12, 13]:
            return 10
        return self.rank

    def __str__(self):      
        return '[{}.{}]'.format(card_ranks[self.rank], suit_unicodes_fill[self.suit])

    def __repr__(self):
        return '[{}.{}]'.format(self.rank, self.suit)