import variables as var

import title
import menu
import adventuremap
import extralevelselect

import sys
import pygame

pygame.init()
clock = pygame.time.Clock()

var.screen = pygame.display.set_mode((1024, 640))
pygame.display.set_caption('Dessert Defense')

def main():
    while 1:
        clock.tick(40)
        display()
        input_handle()

def input_handle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                temp = pygame.mouse.get_pos()
                
                var.Inputs.Mouse.lx = temp[0]
                var.Inputs.Mouse.ly = temp[1]

                if var.Game.scene == 'title':
                    title.mouse_linput_handle()

                elif var.Game.scene == 'menu':
                    menu.mouse_linput_handle()

def display():
    var.screen.fill((255, 255, 255))

    if var.Game.scene == 'title':
        title.display()

    elif var.Game.scene == 'menu':
        menu.display()

    pygame.display.flip()

main()