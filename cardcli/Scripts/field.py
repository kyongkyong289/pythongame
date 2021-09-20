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

    var.window.addstr(UI.Main.title_text[0], UI.Main.title_text[1], 'Location : ' + var.Field.location)

    for i in range(len(field.field[var.Field.location])):
        for j in range(len(field.field[var.Field.location][0])):
            r = UI.Field.cell_interval[0] * i - var.Camera.position[0]
            c = UI.Field.cell_interval[1] * j - var.Camera.position[1]

            if r > 0 and r < 26 and c > 0 and c < 90:
                draw_terrain(r, c, field.field[var.Field.location][i][j])
    
    for i in range(len(field.objects[var.Field.location])):
        r = UI.Field.cell_interval[0] * field.objects[var.Field.location][i][0] - var.Camera.position[0]
        c = UI.Field.cell_interval[1] * field.objects[var.Field.location][i][1] - var.Camera.position[1]

        if r > 0 and r < 26 and c > 0 and c < 90:
            draw_objects(r, c, field.objects[var.Field.location][i][2])

    draw_player(UI.Field.cell_interval[0] * var.Field.player_position[0] - var.Camera.position[0], UI.Field.cell_interval[1] * var.Field.player_position[1] - var.Camera.position[1])
    
def draw_terrain(r, c, terrain): 
    func.draw_rect(r, c, UI.Field.cell_size[0], UI.Field.cell_size[1], colors.fg_white)
        
    for i in range(3):
        for j in range(4):
            if platform.system() == 'Windows':
                var.window.addstr(r + i + 1, c + j + 1, td.character[terrain][i][j], curses.color_pair(td.color_code['windows'][td.color[terrain][i][j]]))

            else:
                var.window.addstr(r + i + 1, c + j + 1, td.character[terrain][i][j], curses.color_pair(td.color_code['other'][td.color[terrain][i][j]]))

def draw_objects(r, c, ID):
    for i in range(3):
        for j in range(4):
            if platform.system() == 'Windows':
                var.window.addstr(r + i + 1, c + j + 1, td.objects[ID][i][j], curses.color_pair(td.color_code['windows'][td.objects_color[ID][i][j]]))

            else:
                var.window.addstr(r + i + 1, c + j + 1, td.objects[ID][i][j], curses.color_pair(td.color_code['other'][td.objects_color[ID][i][j]]))


def draw_player(r, c):
    var.window.addstr(r + 1, c + 2, '||')
    var.window.addstr(r + 3, c + 2, '--')

def input_handle(key):
    if key == 96 + 23 and field.walls[var.Field.location][var.Field.player_position[0] - 1][var.Field.player_position[1]] == 0:
        var.Field.player_position[0] -= 1
        var.Camera.position[0] -= UI.Field.cell_interval[0]

    elif key == 96 + 19 and field.walls[var.Field.location][var.Field.player_position[0] + 1][var.Field.player_position[1]] == 0:
        var.Field.player_position[0] += 1
        var.Camera.position[0] += UI.Field.cell_interval[0]

    elif key == 96 + 1 and field.walls[var.Field.location][var.Field.player_position[0]][var.Field.player_position[1] - 1] == 0:
        var.Field.player_position[1] -= 1
        var.Camera.position[1] -= UI.Field.cell_interval[1]

    elif key == 96 + 4 and field.walls[var.Field.location][var.Field.player_position[0]][var.Field.player_position[1] + 1] == 0:
        var.Field.player_position[1] += 1
        var.Camera.position[1] += UI.Field.cell_interval[1]

    elif key == 96 + 5:
        for i in range(len(field.connection[var.Field.location])):
            if var.Field.player_position[0] == field.connection[var.Field.location][i][0][0] and var.Field.player_position[1] == field.connection[var.Field.location][i][0][1]:
                var.Field.player_position = [field.connection[var.Field.location][i][2][0], field.connection[var.Field.location][i][2][1]]
                var.Camera.position = [field.connection[var.Field.location][i][3][0], field.connection[var.Field.location][i][3][1]]
                var.Field.location = field.connection[var.Field.location][i][1]
