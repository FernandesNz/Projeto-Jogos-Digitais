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
fonte = pygame.font.Font("assets/fonts/font.ttf", 37)
fonte_players = pygame.font.Font("assets/fonts/font.ttf", 27)
back = pygame.image.load("assets/images/back.png")


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/fonts/font.ttf", size)


with open('players.json') as f:
    jogadores = json.load(f)

# Ordenação dos jogadores pela pontuação
jogadores.sort(key=lambda x: x['score'], reverse=True)

rakingTxt = fonte.render("Ranking", True, (255,255,255))


def rankingMvp():

    cor = (255, 255, 255)
    pos_y = 100
    for i, jogador in enumerate(jogadores[:20]):
        texto = f"{i+1}º {jogador['nome']} - Score: {jogador['score']} "
        superficie_texto = fonte_players.render(texto, True, cor)
        screen.blit(superficie_texto, (300, pos_y))
        pos_y += 30

def retorna():

    RANK_MOUSE_POS = pygame.mouse.get_pos()

    BACK_BUTTON = Button(back, pos=(60, 80), 
        text_input="", font=get_font(60), base_color="#d7fcd4", hovering_color="red")

    for button in [BACK_BUTTON]:
        button.changeColor(RANK_MOUSE_POS)
        button.update(screen)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(RANK_MOUSE_POS):
                    import main


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    
    
    screen.blit(BG, (0,0))
    rankingMvp()
    screen.blit(rakingTxt, (480, 40))
    retorna()

    pygame.display.update()