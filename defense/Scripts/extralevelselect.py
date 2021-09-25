import pygame
import visual as vs
import variables as var
import uidata as ui
import inputfunctions as iff

def display():
    var.screen.blit(vs.font_title.render('Select Level', True, vs.Colors.black), ui.Main.title_text)