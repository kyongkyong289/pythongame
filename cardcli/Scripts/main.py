import curses
import sys
import traceback
import platform

import colors
import variables as var
import debug

import title
import menu
import field
import battle

var.screen = curses.initscr() 

def init():
    curses_settings()
    debug.debug()

def main():
    input_handle()
    display()

def display():
    var.window.erase()

    if var.Game.scene == 'title':
        title.display()

    elif var.Game.scene == 'menu':
        menu.display()

    elif var.Game.scene == 'field':
        field.display()

    elif var.Game.scene == 'battle':
        battle.display()

    var.window.refresh()

def input_handle():
    key = var.window.getch()
    
    if key == 27:
        sys.exit()

    elif var.Game.scene == 'title':
        title.input_handle(key)

    elif var.Game.scene == 'menu':
        menu.input_handle(key)

    elif var.Game.scene == 'field':
        field.input_handle(key)

    elif var.Game.scene == 'battle':
        battle.input_handle(key)

def curses_settings():
    var.window = curses.newwin(30, 96, 0, 0)

    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    var.window.keypad(True)

    curses.start_color()
    curses.use_default_colors()

    var.window.timeout(25)

    color_init()

def color_init():
    for i in range(1, 17):
        curses.init_pair(i, i - 1, -1)

    if platform.system() == 'Windows':
        colors.fg_black = 1
        colors.fg_red = 5
        colors.fg_yellow = 7
        colors.fg_green = 3
        colors.fg_cyan = 4
        colors.fg_blue = 2
        colors.fg_magenta = 6
        colors.fg_white = 8
        colors.fg_lblack = 9
        colors.fg_lred = 13
        colors.fg_lyellow = 15
        colors.fg_lgreen = 11
        colors.fg_lcyan = 12
        colors.fg_lblue = 10
        colors.fg_lmagenta = 14
        colors.fg_lwhite = 16

    else:
        colors.fg_black = 1
        colors.fg_red = 2
        colors.fg_yellow = 4
        colors.fg_green = 3
        colors.fg_cyan = 7
        colors.fg_blue = 5
        colors.fg_magenta = 6
        colors.fg_white = 8
        colors.fg_lblack = 9
        colors.fg_lred = 10
        colors.fg_lyellow = 12
        colors.fg_lgreen = 11
        colors.fg_lcyan = 15
        colors.fg_lblue = 13
        colors.fg_lmagenta = 14
        colors.fg_lwhite = 16

try:
    init()
    
    while 1:
        main()

except:
    curses.endwin()
    print(var.Game.state)
    traceback.print_exc()
    sys.exit()
