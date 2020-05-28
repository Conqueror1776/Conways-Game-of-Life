from cell import Cell
from random import randint
import curses
import time

class Board:
    def __init__(self, odds):
        self.window = curses.initscr()
        self.rows, self.col = self.window.getmaxyx()
        self.grid = [[Cell() for i in range(self.col)] for j in range(self.rows)]

        self._initiate_random_board(odds)

    def _initiate_random_board(self, odds):
        for i in self.grid:
            for j in i:
                random_int = randint(0, odds)
                if (random_int == 1):
                    j.set_alive()

    def draw_board(self):
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        for i in range(self.rows - 1):
            for j in range(self.col):
                if (self.grid[i][j].alive):
                    self.window.attron(curses.color_pair(1))
                    self.window.addstr(i,j,' ')
                    self.window.attroff(curses.color_pair(1))
        self.window.refresh()
        time.sleep(1)
        curses.endwin()


thing = Board(5)
thing.draw_board()
