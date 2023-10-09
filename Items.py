import pygame
import sys,random
from pygame.locals import *


#colores
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

screen_size = pygame.display.set_mode([800, 500])
clock = pygame.time.Clock()

carretera= pygame.image.load("Main/Carretera.png").convert()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()     
        self.image = pygame.image.load("sprites/modern_red.png").convert_alpha()
        self.rect = self.image.get_rect()
        # Define el tamaño deseado del carro
        new_width = 30  # Ancho deseado
        new_height = 60  # Alto deseado
        # Redimensiona la imagen al tamaño deseado
        self.image = pygame.transform.scale(self.image, (new_width, new_height))
        
        self.rect.x = 400
        self.rect.y = 400

    def move_right(self, pixels):
        if self.rect.x < 550:
            self.rect.x += pixels
    def move_left(self,pixels):
        if self.rect.x > 200:
            self.rect.x -= pixels

    
class enemy_car(pygame.sprite.Sprite):
    def __init__(self, bad, lane):
        super().__init__()
        global speed 
        self.size = (50,50)
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
            # Agregar un caso predeterminado para manejar valores inesperados de 'bad'
            self.image = pygame.image.load("sprites/modern_pink.png").convert_alpha()
            
        self.rect = self.image.get_rect()
        new_width = 30  # Ancho deseado
        new_height = 60  # Alto deseado
        # Redimensiona la imagen al tamaño deseado
        self.image = pygame.transform.scale(self.image, (new_width, new_height))
        
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = self.lane
        self.rect.y = -100

    def move(self):
        if self.rect.x < 650:
            self.rect.y += speed
        else:
            self.kill()

#LOGICA DEL JUEGO

speed = 5

def main_juego():
    game_over = False
    moving_left = False
    moving_right = False
    player = Player()

    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    all_sprites.add(player)  # Agregar al jugador al grupo de todos los sprites

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    moving_left = True
                if event.key == K_RIGHT:
                    moving_right = True

            if event.type == pygame.KEYUP:
                if event.key == K_LEFT:
                    moving_left = False
                if event.key == K_RIGHT:
                    moving_right = False

    # Actualizar la posición del jugador según las variables de estado
        if moving_left:
            player.move_left(5)  # Puedes ajustar la velocidad aquí
        if moving_right:
            player.move_right(5)  # Puedes ajustar la velocidad aquí

    # Crear enemigos aleatorios
        if random.randint(0, 100) < 5:
            lane = random.choice([200, 300, 400, 500])
            bad = random.randint(1, 5)
            enemy = enemy_car(bad, lane)
            all_sprites.add(enemy)
            enemies.add(enemy)

    # Actualizar la posición de los enemigos
        for enemy in enemies:
            enemy.move()

        screen_size.blit(carretera,[0,0])

    # Dibujar todos los sprites
        all_sprites.draw(screen_size)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main_juego()





