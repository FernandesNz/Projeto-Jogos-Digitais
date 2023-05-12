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
font = pygame.font.SysFont("assets/fonts/font.ttf", 50)
cVida = pygame.image.load("assets/images/coracao.png")
cVazio = pygame.image.load("assets/images/coracao_cinza.png")
fonte = pygame.font.Font("assets/fonts/font.ttf", 30)


# posição do obstaculo
posicaoObstaculo = [385, 0]

# Tamanho do obstaculo
height = 30
width = 200

#velocidade do obstaculo
velY = 7

# posição do Heroi
posicaoHeroi = [580, 600]

#velocidade do heroi
velocidadeHeroi = [5, 5]


# cor dos corações
c1 = cVida
c2 = cVida
c3 = cVazio

#vida 
life = 3

clock = pygame.time.Clock()

CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000)
temporizador = 0

vitimasSalvas = 0
score = 0


running = True
while running:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == CLOCKTICK:
                temporizador = temporizador +1



    posicaoObstaculo[1] += velY


    #aumento de velocidade de acordo com o tempo
    if(temporizador >= 10):
        velY = 10
    if(temporizador >= 15):
        velY = 12
    if(temporizador >= 20):
        velY = 14


    #movimento do heroi

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]: 
        if(posicaoHeroi[0] > 355):
            posicaoHeroi[0] -= velocidadeHeroi[0]
    if pressed[pygame.K_RIGHT]: 
        if(posicaoHeroi[0] < 720):
            posicaoHeroi[0] += velocidadeHeroi[0]
    
    
    
    # posição em que o obstaculo restornara
    if(posicaoObstaculo[1] >= win_height):
        posicao = randint(0, 1)
        posicaoObstaculo[1] = 0
        if(posicao == 0):
            posicaoObstaculo[0] = 385
        if(posicao == 1):
            posicaoObstaculo[0] = 615


    
    score = temporizador + vitimasSalvas
    



    timer1 = fonte.render("Timer: " + str(temporizador), True, (255, 0, 255))
    scoreTxt = fonte.render("Score " + str(score), True, (255,255,255))
    vitimasTxt = fonte.render("Salvos" + str(vitimasSalvas), True, (255,255,255))

    win.fill((0,0,0))
    win.blit(bg, (0, 0))
    win.blit(vt1, (posicaoHeroi))
    win.blit(tronco, (posicaoObstaculo))
    #win.blit(timer1, (10, 80))
    win.blit(scoreTxt, (10, 620))
    win.blit(vitimasTxt, (10, 670))
    win.blit(c1,(900, 20))
    win.blit(c2,(980, 20))
    win.blit(c3,(1060, 20))
    clock.tick(60)

    pygame.display.update()
 