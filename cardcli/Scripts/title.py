import variables as var
import curses

def display():
    var.window.border('|', '|', '-', '-', '#', '#', '#', '#')
    var.window.addstr(1, 1, 'Hello')
