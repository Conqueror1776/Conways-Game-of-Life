from copy import deepcopy
import curses
from random import randint
import time

class Board:
    def __init__(self, odds, time, type):
        # Set the size of the simulation to the size of the terminal
        self.window = curses.initscr()
        self.rows, self.col = self.window.getmaxyx()
        self.grid = [[0 for i in range(self.col)] for j in range(self.rows)]
        if type == 1:
            self._initiate_random_board(odds)
        elif type == 2:
            self._initiate_glider()
            ########### ADD OPTION
        # Run the simulation for time generations
        for i in range(time):
            self.draw_board()
            self.update_board_normal()
        curses.endwin()

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
        time.sleep(.1)
