import uidata as UI
import variables as var
import colors
import curses
import functions as func

def display():
    var.window.border('|', '|', '-', '-', '#', '#', '#', '#')
    var.window.addstr(UI.Main.title_text[0], UI.Main.title_text[1], 'MENU', curses.color_pair(colors.fg_white))
    var.window.addstr(UI.Menu.new_game[0], UI.Menu.new_game[1], 'NEW GAME', curses.color_pair(colors.fg_white))
    var.window.addstr(UI.Menu.load_game[0], UI.Menu.load_game[1], 'LOAD GAME', curses.color_pair(colors.fg_white))
    var.window.addstr(UI.Menu.dungeon[0], UI.Menu.dungeon[1], 'DUNGEON', curses.color_pair(colors.fg_white))

    var.window.addstr(UI.Menu.cursor[var.Cursor.menu][0], UI.Menu.cursor[var.Cursor.menu][1], '>', curses.color_pair(colors.fg_white))

def input_handle(key):
    if key == 96 + 5:
        if var.Cursor.menu == 0:
            func.adventure_init()
            var.Game.scene = 'field'

    elif key == 96 + 23 and var.Cursor.menu > 0:
        var.Cursor.menu -= 1

    elif key == 96 + 19 and var.Cursor.menu < 2:
        var.Cursor.menu += 1

