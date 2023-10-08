import pygame
import sys
from Load_Images.imagenes import *


WIDTH = 800
HEIGHT = 500

black = (0, 0, 0)



class Button:
    def __init__(self, x, y, normal_image, hover_image):
        self.x = x
        self.y = y
        self.normal_image = normal_image
        self.hover_image = hover_image
        self.hovered = False

    def is_hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        rect = self.normal_image.get_rect().move(self.x, self.y)
        return rect.collidepoint(mouse_pos)

    def update(self):
        if self.is_hovered():
            self.image = self.hover_image
        else:
            self.image = self.normal_image

    def mouse_motion(self):
        if self.is_hovered():
            self.hovered = True
        else:
            self.hovered = False

    def mouse_click(self):
        if self.hovered:
            self.on_click()

    def process_events(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.mouse_motion()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_click()

    def on_click(self):
        if self == buttons[0]:
            print("Botón PLAY presionado")
        elif self == buttons[1]:
            print("Botón SCORE presionado")
        elif self == buttons[2]:
            print("Botón HELP presionado")
        elif self == buttons[3]:
            pygame.quit()
            sys.exit()

buttons = [
    Button(50, 130, Button_Play, Button_Play_mouse),
    Button(50, 220, Button_score, Button_score_mouse),
    Button(50, 310, Button_help, Button_help_mouse),
    Button(50, 400, Button_exit, Button_exit_mouse), 
]