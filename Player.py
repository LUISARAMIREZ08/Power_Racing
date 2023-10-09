import pygame 
import sys
import random
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
        if self.rect.x < 550:
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

class enemy_car(pygame.sprite.Sprite):
    def __init__(self, bad,lane):
        super().__init__()
        self.bad = bad
        self.lane = lane

        if self.bad == 1:
            self.image = enemy_modern_blue
        elif self.bad == 2:
            self.image = enemy_super_cyan
        elif self.bad == 3:
            self.image = enemy_kar_pink
        elif self.bad == 4:
            self.image = enemy_modern_green
        else:
            self.image = enemy_modern_pink

        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (Settings.car_width, Settings.car_height))
        self.rect.x = self.lane
        self.rect.y = Settings.enemy_pos_y

        self.mask = pygame.mask.from_surface(self.image)
    
    def move(self):
        if self.rect.x < 650:
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


aux = False
collision_count = 0

def crash(value):
    global aux,collision_count

    if value == True and aux == False:
        aux = True
        collision_count += 1
    
    if value == False and aux == True:
        aux = False

    if collision_count >= Settings.num_vidas:
        print("GAME OVER")
        sys.exit()

#LOGICA DEL JUEGO
def main_juego():
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            player.process_event_car(event) 
        player.move_car(event)  

        #Crea los enemigos
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
