import curses
import platform

import terraindata as td
import fielddata as field
import variables as var
import uidata as UI
import colors
import functions as func

def display():
    var.window.border('|', '|', '-', '-', '#', '#', '#', '#')

    for i in range(6):
        for j in range(6):
            draw_terrain(5 + 3 * i, 10 + 5 * j, field.field['home'][i][j])

def draw_terrain(r, c, terrain):
    func.draw_rect(r, c, 4, 6, colors.fg_white)

    for i in range(2):
        for j in range(4):
            if platform.system() == 'Windows':
                var.window.addstr(r + i + 1, c + j + 1, td.character[terrain][i][j], curses.color_pair(td.color_code['windows'][td.color[terrain][i][j]]))

            else:
                var.window.addstr(r + i + 1, c + j + 1, td.character[terrain][i][j], curses.color_pair(td.color_code['other'][td.color[terrain][i][j]]))

def input_handle(key):
    pass
