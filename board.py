from cell import Cell
from random import randint
import curses
import time

class Board:
    def __init__(self, odds, time):
        self.window = curses.initscr()
        self.rows, self.col = self.window.getmaxyx()
        self.grid = [[0 for i in range(self.col)] for j in range(self.rows)]
        self._initiate_glider_gun()
        for i in range(time):
            self.draw_board()
            self.update_board_normal()
        curses.endwin()

    def _initiate_random_board(self, odds):
        for i in range(self.rows):
            for j in range(self.col):
                random_int = randint(0, odds)
                if (random_int == 1):
                    self.grid[i][j] = 1

    def _initiate_glider_gun(self):
        self.grid[2][4] = 1
        self.grid[3][5] = 1
        self.grid[4][5] = 1
        self.grid[4][4] = 1
        self.grid[4][3] = 1

    def check_neighbors(self, r, c):
        count = 0;
        if (self.grid[(r - 1)%self.rows][c] == 1):
            count+= 1
        if (self.grid[(r + 1)%self.rows][c] == 1):
            count+= 1
        if (self.grid[r][(c - 1)%self.col] == 1):
            count+= 1
        if (self.grid[r][(c + 1)%self.col] == 1):
            count+= 1

        if (self.grid[(r - 1)%self.rows][(c - 1)%self.col] == 1):
            count+= 1
        if (self.grid[(r + 1)%self.rows][(c + 1)%self.col] == 1):
            count+= 1
        if (self.grid[(r - 1)%self.rows][(c + 1)%self.col] == 1):
            count+= 1
        if (self.grid[(r + 1)%self.rows][(c - 1)%self.col] == 1):
            count+= 1
        return count

    def update_board_normal(self):
        temp = self.grid
        for i in range(self.rows):
            for j in range(self.col):
                total = self.check_neighbors(i, j)
                if (total < 2):
                    temp[i][j] = 0
                if (total == 3):
                    temp[i][j] = 1
                if (total > 3):
                    temp[i][j] = 0
        self.grid = temp

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
        time.sleep(4)
