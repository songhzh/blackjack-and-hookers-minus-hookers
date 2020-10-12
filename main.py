from table import Table
from player import Player

def main():
    players = [Player('a', 100), Player('b', 100)]
    table = Table(players)
    table.play()

if __name__ == "__main__":
    main()