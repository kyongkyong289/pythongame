import pygame
import visual as vs
import variables as var
import uidata as ui
import inputfunctions as iff

def display():
    var.screen.blit(vs.font_title.render('Menu', True, vs.Colors.black), ui.Main.title_text)

    pygame.draw.rect(var.screen, vs.Colors.black, ui.Menu.advenutre_button, 2)
    pygame.draw.rect(var.screen, vs.Colors.black, ui.Menu.extra_button, 2)

def mouse_linput_handle():
    if iff.point_inside_rect(var.Inputs.Mouse.lx, var.Inputs.Mouse.ly, ui.Menu.advenutre_button[0], ui.Menu.advenutre_button[1], ui.Menu.advenutre_button[2], ui.Menu.advenutre_button[3]):
        var.Game.scene = 'adventure_map'

    elif iff.point_inside_rect(var.Inputs.Mouse.lx, var.Inputs.Mouse.ly, ui.Menu.extra_button[0], ui.Menu.extra_button[1], ui.Menu.extra_button[2], ui.Menu.extra_button[3]):
        var.Game.scene = 'extra_level_select'
