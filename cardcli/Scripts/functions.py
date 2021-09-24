import variables as var
import colors

import curses

def draw_rect(r, c, rs, cs, color):
    for i in range(r, r + rs):
        for j in range(c, c + cs):
            var.window.addstr(i, j, ' ')

    for i in range(r, r + rs):
        var.window.addstr(i, c, '|', curses.color_pair(color))
        var.window.addstr(i, c + cs - 1, '|', curses.color_pair(color))

    for i in range(c, c + cs):
        var.window.addstr(r, i, '-', curses.color_pair(color))
        var.window.addstr(r + rs - 1, i, '-', curses.color_pair(color))

    var.window.addstr(r, c, '#', curses.color_pair(color))
    var.window.addstr(r, c + cs - 1, '#', curses.color_pair(color))
    var.window.addstr(r + rs - 1, c, '#', curses.color_pair(color))
    var.window.addstr(r + rs - 1, c + cs - 1, '#', curses.color_pair(color))

def adventure_init():
    var.Player.cards = [10001, 10002, 10003, 10004, 10005]
    var.Player.deck_1 = [[10001, 0, 2], [10002, 0, 2], [10003, 0, 2], [10004, 0, 2], [10005, 0, 2]]

def battle_start():
    var.Game.state = 'start'
    pass
