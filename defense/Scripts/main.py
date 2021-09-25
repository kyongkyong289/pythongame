import variables as var

import sys
import pygame

pygame.init()

var.screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Dessert Defense')

def main():
    while 1:
        input_handle()

def input_handle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

main()