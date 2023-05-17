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

translucido = (0,0,0, 100)

title = fonteTitle.render("Escolha seu Personagem", True, (255,255,0))

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

    pygame.display.update()