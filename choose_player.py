import sys
import pygame
import json
from pygame.locals import *
from button import Button

pygame.init()
screen_width = 1180
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

BG = pygame.image.load("assets/images/Background3.png")
fonteTitle = pygame.font.Font("assets/fonts/font.ttf", 34)
bombeira = pygame.image.load("assets/images/bombeira200.png")
bombeiro = pygame.image.load("assets/images/bombeiro200.png")
teste = pygame.image.load("assets/images/teste.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/fonts/font.ttf", size)

translucido = (0,0,0, 100)

title = fonteTitle.render("Escolha seu Personagem", True, (255,255,0))


def escolher():

    RANK_MOUSE_POS = pygame.mouse.get_pos()

    BOMBEIRA_BUTTON = Button(image=None, pos=(400, 500), 
        text_input="CLOE", font=get_font(30), base_color="#d7fcd4", hovering_color="green")
    
    BOMBEIRO_BUTTON = Button(image=None, pos=(800, 500), 
        text_input="GEORGE", font=get_font(30), base_color="#d7fcd4", hovering_color="green")

    for button in [BOMBEIRA_BUTTON,BOMBEIRO_BUTTON]:
        button.changeColor(RANK_MOUSE_POS)
        button.update(screen)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BOMBEIRA_BUTTON.checkForInput(RANK_MOUSE_POS):
                    with open('player.txt', 'w') as arquivo:
                        arquivo.write('0')
                    import game
                if BOMBEIRO_BUTTON.checkForInput(RANK_MOUSE_POS):
                    with open('player.txt', 'w') as arquivo:
                        arquivo.write('1')
                    import game
            


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    retangulo = pygame.Surface((800, 600), pygame.SRCALPHA)


    screen.blit(BG, (0,0))

    retangulo.fill(translucido)
    screen.blit(retangulo,(200, 50))
    screen.blit(title, (220, 130))
    screen.blit(bombeira,(300, 250))
    screen.blit(bombeiro,(700, 250))
    escolher()

    pygame.display.update()