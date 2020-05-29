from board import Board

def run_game(self):
    odds = int(input("How sparce are the squares?\n"))
    time = int(input("How long should the simulation last?\n"))
    test = Board(odds, time)

rungame()
