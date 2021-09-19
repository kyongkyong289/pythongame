import uidata as UI
import variables as var
import colors
import curses

def display():
    var.window.border('|', '|', '-', '-', '#', '#', '#', '#')
    var.window.addstr(UI.Main.title_text[0], UI.Main.title_text[1], 'PYCARD', curses.color_pair(colors.fg_white))
    var.window.addstr(UI.Title.new_game[0], UI.Title.new_game[1], 'NEW GAME', curses.color_pair(colors.fg_white))
    var.window.addstr(UI.Title.load_game[0], UI.Title.load_game[1], 'LOAD GAME', curses.color_pair(colors.fg_white))
