from copy import deepcopy
import curses
from random import randint
import time
import sys

class Board:
    def __init__(self, odds, gens, type):
        # Set the size of the simulation to the size of the terminal
        self.window = curses.initscr()
        self.rows, self.col = self.window.getmaxyx()
        self.grid = [[0 for i in range(self.col)] for j in range(self.rows)]
        if type == 1:
            self._initiate_random_board(odds)
        elif type == 2:
            self._initiate_glider()
        else:
            sentence = "Note: because of the wraparound nature of the board, the glider will eventually destroy itself       \n"
            for char in sentence:
                time.sleep(0.05)
                sys.stdout.write(char)
                sys.stdout.flush()
            self._initiate_glider_gun()
        # Run the simulation for time generations
        for i in range(gens):
            self.draw_board()
            self.update_board_normal()
        curses.endwin()

    def set(self, i, j):
        self.grid[i][j] = 1

    def create_column(self, i, j, size):
        for k in range(size):
            self.grid[i + k][j] = 1

    def create_square(self, i, j):
        self.grid[i][j] = 1
        self.grid[i][j + 1] = 1
        self.grid[i + 1][j] = 1
        self.grid[i + 1][j + 1] = 1

    # Create's a totally random board based on the inputted odds
    def _initiate_random_board(self, odds):
        for i in range(self.rows):
            for j in range(self.col):
                random_int = randint(0, odds)
                if (random_int == 1):
                    self.grid[i][j] = 1

    # Create enough gliders to fit the terminal
    def _initiate_glider(self):

        def create_glider(i, j):
            self.grid[i][j + 1] = 1
            self.grid[i + 1][j + 2] = 1
            self.grid[i + 2][j + 2] = 1
            self.grid[i + 2][j + 1] = 1
            self.grid[i + 2][j] = 1
        for i in range(int(self.col/6)):
            for j in range(int(self.rows/5)):
                create_glider(j * 5, i * 6)

    def _initiate_glider_gun(self):

        def create_gun_one(i, j):
            self.set(i, j + 2)
            self.set(i, j + 3)
            self.set(i + 1, j + 1)
            self.set(i + 1, j + 5)
            self.create_column(i + 2, j, 3)
            self.set(i + 3, j + 4)
            self.create_column(i + 2, j + 6, 3)
            self.set(i + 3, j + 7)
            self.set(i + 5, j + 1)
            self.set(i + 5, j + 5)
            self.set(i + 6, j + 2)
            self.set(i + 6, j + 3)

        def create_gun_two(i, j):
            self.create_column(i + 2, j, 3)
            self.create_column(i + 2, j + 1, 3)
            self.set(i + 1, j + 2)
            self.set(i + 5, j + 2)
            self.create_column(i, j + 4, 2)
            self.create_column(i + 5, j + 4, 2)

        create_gun_one(2, 10)
        create_gun_two(0, 20)
        self.create_square(4, 0)
        self.create_square(2, 34)



    # Adds up how many of a tile's naighbors are alive
    def check_neighbors(self, r, c):
        count = 0;
        if (self.grid[(r - 1) % self.rows][c] == 1):
            count+= 1
        if (self.grid[(r + 1) % self.rows][c] == 1):
            count+= 1
        if (self.grid[r][(c - 1) % self.col] == 1):
            count+= 1
        if (self.grid[r][(c + 1) % self.col] == 1):
            count+= 1
        if (self.grid[(r - 1) % self.rows][(c - 1) % self.col] == 1):
            count+= 1
        if (self.grid[(r + 1) % self.rows][(c + 1) % self.col] == 1):
            count+= 1
        if (self.grid[(r - 1) % self.rows][(c + 1) % self.col] == 1):
            count+= 1
        if (self.grid[(r + 1) % self.rows][(c - 1) % self.col] == 1):
            count+= 1
        return count

    #  Updates the board based on the rules of the game
    def update_board_normal(self):
        # Create a copy of the board state so the changes made don't
        # impact other tiles in the same update
        temp = deepcopy(self.grid)
        for i in range(self.rows):
            for j in range(self.col):
                total = self.check_neighbors(i, j)
                if total < 2:
                    temp[i][j] = 0
                if total == 3:
                    temp[i][j] = 1
                if total > 3:
                    temp[i][j] = 0
        self.grid = temp

    # Use curses to draw the board state in a new terminal
    def draw_board(self):
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        for i in range(self.rows - 1):
            for j in range(self.col):
                if (self.grid[i][j] == 1):
                    self.window.attron(curses.color_pair(1))
                    self.window.addstr(i,j,' ')
                    self.window.attroff(curses.color_pair(1))
                else:
                    self.window.addstr(i,j,' ')
        self.window.refresh()
        time.sleep(.01)
