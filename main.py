#Matheus Fernandes - 42139694
#teste 1

import random
import pygame
from random import randint

pygame.init()
win_height = 600
win_width = 800
win_mode = (win_width, win_height)
win = pygame.display.set_mode(win_mode)
pygame.display.set_caption("SOS Flood")

# posição do obstaculo
x = 250
y = 0

# Tamanho do obstaculo
height = 30
width = 200

#velocidade do obstaculo
velY = 6

# posição do Heroi
posicaoHeroi = [350, 550]

#velocidade do heroi
velocidadeHeroi = [4, 4]





pygame.draw.rect(win, (255, 255, 255), (10, 10, 50, 50))
running = True
while running:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    y += velY

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]: posicaoHeroi[0] -= velocidadeHeroi[0]
    if pressed[pygame.K_RIGHT]: posicaoHeroi[0] += velocidadeHeroi[0]
    
    
    

    if(y >= win_height):
        posicao = randint(0, 1)
        y = 0
        if(posicao == 0):
            x = 250
        if(posicao == 1):
            x = 350
    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 255, 255), (x, y, width, height))
    pygame.draw.rect(win, (150, 255, 0), (0, 0, 250, 600))
    pygame.draw.rect(win, (150, 255, 0), (550, 0, 250, 600))
    pygame.draw.circle(win, (255,255,255), posicaoHeroi, 20)
    pygame.display.update()
 