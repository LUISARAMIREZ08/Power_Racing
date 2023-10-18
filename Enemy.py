import pygame 
import sys
import random
import pygame.mask

from pygame.sprite import *
from player_settings import *
from crash import *
from Player import *

class enemy_car(pygame.sprite.Sprite):
    def __init__(self, bad,lane):
        super().__init__()
        self.bad = bad
        self.lane = lane

        if self.bad == 1:
            self.image = pygame.image.load("sprites/modern_blue.png").convert_alpha()
        elif self.bad == 2:
            self.image = pygame.image.load("sprites/super_cyan.png").convert_alpha()    
        elif self.bad == 3:
            self.image = pygame.image.load("sprites/kar_pink.png").convert_alpha()
        elif self.bad == 4:
            self.image = pygame.image.load("sprites/modern_green.png").convert_alpha()
        else:
            self.image = pygame.image.load("sprites/modern_pink.png").convert_alpha()

        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (Settings.car_width, Settings.car_height))
        self.rect.x = self.lane
        self.rect.y = Settings.enemy_pos_y

        self.mask = pygame.mask.from_surface(self.image)
    
    def move(self):
        if self.rect.x < 600:
            self.rect.y += Settings.car_speed
        else:
            self.kill()

    def enemy_random():
        global enemy_timer
        enemy_timer += 1
        if enemy_timer >= Settings.time_enemy: 
            enemy_timer = 0
            lane = random.choice([Settings.carril_1, Settings.carril_2, Settings.carril_3, Settings.carril_4])
            enemy = enemy_car(random.randint(1, 5), lane)  # Crea un enemigo aleatorio
            all_sprites.add(enemy)
            enemy_sprites.add(enemy)

    def collision(self):
        car_collision_list = pygame.sprite.spritecollide(player,enemy_sprites,False,pygame.sprite.collide_mask)
        if car_collision_list:
            crash(True)
        else:
            crash(False)

