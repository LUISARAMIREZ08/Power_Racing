import pygame
from Load_Images.images import *
from botones import *

class Submenu:
    def __init__(self):
        self.current_screen = True
        self.current_background = Main  # Imagen de fondo actual
        self.current_buttons = buttons_main #Boton actual

    def process_events_submenu(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.current_screen == True:
                if self.current_buttons[0].is_hovered():
                    self.switch_to_user_screen()
                elif self.current_buttons[1].is_hovered():
                    self.switch_to_store_screen()
                elif self.current_buttons[2].is_hovered():
                    self.switch_to_help_screen()
                elif self.current_buttons[3].is_hovered():
                    pygame.quit()
                    sys.exit()
    #Usuario
    def switch_to_user_screen(self):
        self.current_screen = False
        self.current_background = image_user
        self.current_buttons = buttons_sub_menu_user
    #Score
    def switch_to_store_screen(self):
        self.current_screen = False  
        self.current_background = image_score  
        self.current_buttons = buttons_sub_menu_score 
    #Help
    def switch_to_help_screen(self):
        self.current_screen = False
        self.current_background = image_help
        self.current_buttons = buttons_sub_menu_help

    #Funcion que hace que los botones se actualicen
    def update_submenu(self):
        for button in self.current_buttons:
            button.update()
    #Funcion que dibuja los botones y el fondo
    def draw_submenu(self, screen):
        screen.blit(self.current_background, (0, 0))
        for button in self.current_buttons:
            screen.blit(button.image, (button.x, button.y))
