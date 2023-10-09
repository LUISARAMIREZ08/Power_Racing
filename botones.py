import pygame
import sys
from Load_Images.images import *

class Button:
    def __init__(self, x, y, normal_image, hover_image):
        self.x = x
        self.y = y
        self.normal_image = normal_image
        self.hover_image = hover_image
        self.image = self.normal_image
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

    def process_events(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.mouse_motion()

#Lista que contiene las instancias de los botones del menu principal
buttons_main = [
    Button(50, 130, Button_Play, Button_Play_mouse),
    Button(50, 220, Button_score, Button_score_mouse),
    Button(50, 310, Button_help, Button_help_mouse),
    Button(50, 400, Button_exit, Button_exit_mouse), 
]
#Lista que contiene las instancias de los botones del submenu user
buttons_sub_menu_user = [
    Button(305,372, Button_user_ok, Button_user_ok_mouse),
]
#Lista que contiene las instancias de los botones del submenu score
buttons_sub_menu_score = [
    Button(47,440, Button_score_back, Button_score_back_mouse),
    Button(248,440, Button_score_clear, Button_score_clear_mouse),
]
#Lista que contiene las instancias de los botones del submenu help
buttons_sub_menu_help = [
    Button(306,438, Button_help_back, Button_help_back_mouse),
]