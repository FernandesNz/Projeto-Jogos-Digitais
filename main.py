#Matheus Fernandes - 42139694
#teste 1

import random
import pygame
from random import randint

pygame.init()
win_height = 720
win_width = 1180
win_mode = (win_width, win_height)
win = pygame.display.set_mode(win_mode)
pygame.display.set_caption("SOS Flood")
bg = pygame.image.load("assets/images/background.png")
vt1 = pygame.image.load("assets/images/heroi.png")
tronco = pygame.image.load("assets/images/tronco 2.png")

# posição do obstaculo
x = 385
y = 0

# Tamanho do obstaculo
height = 30
width = 200

#velocidade do obstaculo
velY = 7

# posição do Heroi
posicaoHeroi = [580, 600]

#velocidade do heroi
velocidadeHeroi = [5, 5]





running = True
while running:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    y += velY

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]: 
        if(posicaoHeroi[0] > 355):
            posicaoHeroi[0] -= velocidadeHeroi[0]
    if pressed[pygame.K_RIGHT]: 
        if(posicaoHeroi[0] < 720):
            posicaoHeroi[0] += velocidadeHeroi[0]
    
    
    

    if(y >= win_height):
        posicao = randint(0, 1)
        y = 0
        if(posicao == 0):
            x = 385
        if(posicao == 1):
            x = 615
    win.fill((0,0,0))
    win.blit(bg, (0, 0))
    win.blit(vt1, (posicaoHeroi))
    win.blit(tronco, (x,y))
    #pygame.draw.rect(win, (255, 255, 255), (x, y, width, height))
    #pygame.draw.circle(win, (255,255,255), posicaoHeroi, 20)
    pygame.display.update()
 