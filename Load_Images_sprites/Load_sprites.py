import pygame
import sys

#JUGADOR PRINCIPAL
Player_image = pygame.image.load("sprites/modern_red.png").convert_alpha()
Player_rect = Player_image.get_rect()

#ENEMIGOS
enemy_modern_blue = pygame.image.load("sprites/modern_blue.png").convert_alpha()
enemy_super_cyan = pygame.image.load("sprites/super_cyan.png").convert_alpha()
enemy_kar_pink = pygame.image.load("sprites/kar_pink.png").convert_alpha()
enemy_modern_green = pygame.image.load("sprites/modern_green.png").convert_alpha()
enemy_modern_pink = pygame.image.load("sprites/modern_pink.png").convert_alpha()