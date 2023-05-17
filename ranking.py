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



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.blit(BG, (0,0))
    rankingMvp()
    screen.blit(rakingTxt, (480, 40))

    pygame.display.update()