import pygame
import sys

# Iniciamos pygame
pygame.init()

# Configuramos la pantalla
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Power Racing")

# Cargamos las imágenes que necesitamos
bg = pygame.image.load("./Main/bg.jpg")
bgScore = pygame.image.load("./Main/Score_normal.png")
bgHelp = pygame.image.load("./Main/help.png")
bgUser = pygame.image.load("./Main/usuario.png")
boton = pygame.image.load("./boton/play.png").convert()
boton.set_colorkey((0, 0, 0))
botonOn = pygame.image.load("./boton/play_on.png").convert()
botonOn.set_colorkey((0, 0, 0))

# Clase para crear botones
class Button():
    def __init__(self, image, pos, textInput, font, baseColor, hoveringColor):
        self.image = image
        self.xPos = pos[0]
        self.yPos = pos[1]
        self.font = font
        self.baseColor, self.hoveringColor = baseColor, hoveringColor
        self.textInput = textInput
        self.text = self.font.render(self.textInput, True, self.baseColor)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.xPos, self.yPos))
        self.textRect = self.text.get_rect(center=(self.xPos, self.yPos))
        self.hovering = False

    def update(self, screen):
        if self.hovering:
            screen.blit(botonOn, self.rect)  # Cambia la imagen al pasar el mouse
        else:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.textRect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.textInput, True, self.hoveringColor)
            self.hovering = True
        else:
            self.text = self.font.render(self.textInput, True, self.baseColor)
            self.hovering = False

    def changeImage(self, newImage):
        self.image = newImage
        self.rect = self.image.get_rect(center=(self.xPos, self.yPos))
# Función necesaria para crear texto
def getFont(size):
    return pygame.font.Font(None, size)
# Ventana de juego
def play():
    while True:
        playMousePos = pygame.mouse.get_pos()

        pass

        pygame.display.update()
# Ventana de Score
def score():
    while True:
        screen.blit(bgScore, (0, 0))
        scoreMousePos = pygame.mouse.get_pos()
        backButton = Button(boton, pos=(140, 458), 
                            textInput="BACK", font=getFont(40), baseColor="White", hoveringColor="#163371")
        clearButton = Button(boton, pos=(340, 458), 
                            textInput="CLEAR", font=getFont(40), baseColor="White", hoveringColor="#163371")
        for button in [backButton, clearButton]:
            button.changeColor(scoreMousePos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.checkForInput(scoreMousePos):
                    mainMenu()
                if clearButton.checkForInput(scoreMousePos):
                    # Código para borrar el archivo de texto
                    pass

        pygame.display.update()
#Ventana de ayuda
def help():
    while True:
        helpMousePos = pygame.mouse.get_pos()
        screen.blit(bgHelp, (0, 0))
        backButton = Button(boton, pos=(399, 457), 
                            textInput="BACK", font=getFont(40), baseColor="White", hoveringColor="#163371")
        backButton.changeColor(helpMousePos)
        backButton.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.checkForInput(helpMousePos):
                    mainMenu()
        pygame.display.update()
# Ventana de usuario
def user():

    fuente = getFont(40)
    texto = ""
    while True:
        helpMousePos = pygame.mouse.get_pos()
        screen.blit(bgUser, (0, 0))
        okButton = Button(boton, pos=(398, 390), 
                            textInput="OK", font=getFont(40), baseColor="White", hoveringColor="#163371")
        okButton.changeColor(helpMousePos)
        okButton.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if okButton.checkForInput(helpMousePos):
                    print("Texto ingresado:", texto)
                    texto = ""  
                    mainMenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]
                elif event.key == pygame.K_RETURN:
                    print("Texto ingresado:", texto)
                    texto = ""
                    mainMenu()
                else:
                    texto += event.unicode

        texto_superficie = fuente.render(texto, True, "white")
        texto_rect = texto_superficie.get_rect()
        texto_rect.center = (400, 250)     
        screen.blit(texto_superficie, texto_rect)   
        pygame.display.update()

#Ventana seleción de personaje
def Selection_character():
    pass
# Ventana de menu principal
def mainMenu():
    while True:
        screen.blit(bg, (0, 0))

        menuMousePos = pygame.mouse.get_pos()

        playButton = Button(boton, pos=(192, 178), 
                            textInput="PLAY", font=getFont(40), baseColor="#d7fcd4", hoveringColor="#163371")
        scoreButton = Button(boton, pos=(192, 251), 
                            textInput="SCORE", font=getFont(40), baseColor="#d7fcd4", hoveringColor="#163371")
        helpButton = Button(boton, pos=(192, 322), 
                            textInput="HELP", font=getFont(40), baseColor="#d7fcd4", hoveringColor="#163371")
        exitButton = Button(boton, pos=(192, 393), 
                            textInput="EXIT", font=getFont(40), baseColor="#d7fcd4", hoveringColor="#163371")

        for button in [playButton, scoreButton, helpButton, exitButton]:
            button.changeColor(menuMousePos)
            button.update(screen)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.checkForInput(menuMousePos):
                    user()
                if scoreButton.checkForInput(menuMousePos):
                    score()
                if helpButton.checkForInput(menuMousePos):
                    help()
                if exitButton.checkForInput(menuMousePos):
                    pygame.quit()
                    sys.exit()                
        pygame.display.update()
# Iniciamos el juego
mainMenu()
