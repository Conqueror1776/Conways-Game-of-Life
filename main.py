from board import Board

def run_game():
    print("Select an option for running the program:\n")
    type = int(input("1.   Random Board\n2.   Gliders\n3.   Glider Gun\n"))
    odds = 10
    if type == 1:
        odds = int(input("How sparce are the squares?\n"))
    time = int(input("How long should the simulation last? (generations)\n"))
    test = Board(odds, time, type)

run_game()
