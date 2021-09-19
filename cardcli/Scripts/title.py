import uidata as UI
import variables as var
import colors
import curses

def display():
    var.window.border('|', '|', '-', '-', '#', '#', '#', '#')
    var.window.addstr(UI.Main.title_text[0], UI.Main.title_text[1], 'PYCARD', curses.color_pair(colors.fg_white))

def input_handle(key):
    if key == 96 + 5:
        var.Game.scene = 'menu'
