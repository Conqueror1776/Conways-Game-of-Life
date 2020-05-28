from cell import Cell
from random import randint
import curses
import time

class Board:
    def __init__(self, rows, columns):
        self.window = curses.initscr()
        self.rows, self.col = self.window.getmaxyx()
        self.grid = [[Cell() for i in range(self.col)] for j in range(self.rows)]

        self._initiate_random_board(1)

    def _initiate_random_board(self, odds):
        for i in self.grid:
            for j in i:
                random_int = randint(0, odds)
                if (random_int == 1):
                    j.set_alive()

    def draw_board(self):
        #curses.curs_set(0)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        self.window.attron(curses.color_pair(1))
        for i in range(self.rows - 1):
            for j in range(self.col):
                self.window.addstr(i,j," ")
                time.sleep(.01)
                self.window.refresh()
        self.window.attroff(curses.color_pair(1))
        curses.endwin()


thing = Board(10,10)
thing.draw_board()
