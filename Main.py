import pygame
import sys

pygame.init()

from botones import * 

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

black = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
imagen = pygame.image.load("./Main/power racing.png").convert()

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        for button in buttons:
            button.process_events(event)

    screen.blit(imagen, [0, 0])

    for button in buttons:
        button.update()
        screen.blit(button.image, (button.x, button.y))

    pygame.display.flip()

pygame.quit()

