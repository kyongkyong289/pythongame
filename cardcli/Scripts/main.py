import curses
import variables as var
import sys
import traceback

import title

var.screen = curses.initscr() 

def init():
    curses_settings()

def main():
    input_handle()
    display()

def display():
    var.window.erase()

    if var.Game.scene == 'title':
        title.display()

    var.window.refresh()

def input_handle():
    key = var.window.getch()
    
    if key == 27:
        sys.exit()

def curses_settings():
    var.window = curses.newwin(30, 96, 0, 0)

    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    var.window.keypad(True)

    curses.start_color()
    curses.use_default_colors()

    var.window.timeout(25)

    for i in range(1, 16):
        curses.init_pair(i, i, 0)

try:
    init()
    
    while 1:
        main()

except:
    curses.endwin()
    traceback.print_exc()
    sys.exit()
