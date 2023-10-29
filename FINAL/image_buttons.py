import pygame 
from button import Button

def list_buttons_principal():
    button_play = Button(50, 130,258,62, pygame.image.load("Buttons/Frame 3.png"), pygame.image.load("Buttons/Frame 4.png"),None)
    button_score = Button(50, 220,258,62,pygame.image.load("Buttons/Frame 1.png"), pygame.image.load("Buttons/Frame 2.png"),None)
    button_help = Button(50, 310,258,62, pygame.image.load("Buttons/Frame 5.png"), pygame.image.load("Buttons/Frame 6.png"),None)
    button_exit = Button(50, 400,258,62, pygame.image.load("Buttons/Frame 7.png"), pygame.image.load("Buttons/Frame 8.png"),None)

    buttons_list = [button_play,button_score,button_help,button_exit]

    return buttons_list

def buttons_user():
    button_menu_user = Button(305,372,180,40, pygame.image.load("Buttons/Frame 9.png"),pygame.image.load("Buttons/Frame 11.png"),None)

def buttons_score():
    button_menu_score = Button(47,440,180,40, pygame.image.load("Buttons/Frame 12.png"),pygame.image.load("Buttons/Frame 13.png"),None)
    button_clear_score = Button(248,440,180,40, pygame.image.load("Buttons/Frame 16.png"),pygame.image.load("Buttons/Frame 17.png"),None)
    
def background(screen, buttons):
    Main = pygame.image.load("./Main/power racing.png")
    screen.blit(Main, (0, 0))
    for button in buttons:
        screen.blit(button.image, (button.x, button.y))
    return screen