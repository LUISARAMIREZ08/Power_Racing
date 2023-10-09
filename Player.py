import pygame 
import sys
import pygame.mask

pygame.init()

screen_size = pygame.display.set_mode([800, 500])
clock = pygame.time.Clock()

background = pygame.image.load("Main/Carretera.png").convert()

from Load_Images_sprites.Load_sprites import *
from pygame.sprite import *
from player_settings import *


Settings = Settings()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = Player_image
        self.rect = Player_rect
        self.image = pygame.transform.scale(self.image, (Settings.car_width, Settings.car_height))
        self.rect.x = Settings.car_pos_x
        self.rect.y = Settings.car_pos_y
        self.mask = pygame.mask.from_surface(self.image)

    def move_right(self, pixels):
        if self.rect.x < 570:
            self.rect.x += pixels

    def move_left(self,pixels):
        if self.rect.x > 200:
            self.rect.x -= pixels
    
    def process_event_car(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.moving_right = True
            if event.key == pygame.K_LEFT:
                self.moving_left = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.moving_right = False
            if event.key == pygame.K_LEFT:
                self.moving_left = False

    def move_car(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.move_right(Settings.car_speed)
            if event.key == pygame.K_LEFT:
                self.move_left(Settings.car_speed)


player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
enemy_sprites = pygame.sprite.Group()
enemy_timer = 0

def main_juego():
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            player.process_event_car(event) 
        player.move_car(event)  

        #Crea los enemigos
        from Enemy import enemy_car
        enemy_car.enemy_random()

        #Mueve los enemigos
        for enemy in enemy_sprites:
            enemy.move()

        #Colisiones
        for enemy in enemy_sprites:
            enemy.collision()
        
        screen_size.blit(background, (0, 0))

        #Dibuja los sprites
        all_sprites.draw(screen_size)

        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main_juego()
