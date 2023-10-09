import pygame
import sys
from Load_Images.images import *
from botones import *
from Submenu import *

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

black = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

submenu = Submenu()

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #Eventos de la pantalla actual
        submenu.process_events_submenu(event)

    # Dibuja el fondo y los botones de la pantalla actual
    submenu.draw_submenu(screen)

    # Actualiza los botones de la pantalla actual
    submenu.update_submenu()

    pygame.display.flip()

pygame.quit()