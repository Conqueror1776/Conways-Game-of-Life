import time
import curses


def pbar(window):
    curses.curs_set()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    for i in range(10):
        window.attron(curses.color_pair(1))
        window.addstr(10,i," ")
        window.attroff(curses.color_pair(1))
        window.refresh()
        time.sleep(0.5)

curses.wrapper(pbar)
