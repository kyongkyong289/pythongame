import curses

import variables as var
import uidata as UI
import colors
import functions as func

def display():
    var.window.border('|', '|', '-', '-', '#', '#', '#', '#')

    # Field
    func.draw_rect(UI.Battle.player_hero[0], UI.Battle.player_hero[1], UI.Battle.player_hero[2], UI.Battle.player_hero[3], colors.fg_white)
    func.draw_rect(UI.Battle.enemy_hero[0], UI.Battle.enemy_hero[1], UI.Battle.enemy_hero[2], UI.Battle.enemy_hero[3], colors.fg_white)
    
    for i in range(6):
        func.draw_rect(UI.Battle.player_units[i][0], UI.Battle.player_units[i][1], UI.Battle.cell_size[0], UI.Battle.cell_size[1], colors.fg_white) 
        func.draw_rect(UI.Battle.enemy_units[i][0], UI.Battle.enemy_units[i][1], UI.Battle.cell_size[0], UI.Battle.cell_size[1], colors.fg_white)

def input_handle(key):
    pass
