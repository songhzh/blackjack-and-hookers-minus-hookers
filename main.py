from table import Table
from player import Player
from clear import *

start = 100
bet = 10

if __name__ == "__main__":
    clear()
    print('Please enter your name')
    name = input(' >')
    player = Player(name, start)
    players = [player]
    table = Table(players)
    while table.check_players(bet):
        clear()
        table.play(bet)
    print('The house wins!')