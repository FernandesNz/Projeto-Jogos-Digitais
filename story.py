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
fonte = pygame.font.Font("assets/fonts/font.ttf", 25)
fonteComecar = pygame.font.Font("assets/fonts/font.ttf", 35)


translucido = (0,0,0, 100)

title = fonte.render("Escolha seu Personagem", True, (255,255,0))
story1 = fonte.render("A cidade Porto real sofreu um grave", True, (255,255,255))
story2 = fonte.render("desastre, ela fica numa região ", True, (255,255,255))
story3 = fonte.render("litorânea e foi atingida por uma ", True, (255,255,255))
story4 = fonte.render("tempestade que ocasionou em uma ", True, (255,255,255))
story5 = fonte.render("grande enchente. Agora cabe a você ", True, (255,255,255)) 
story6 = fonte.render("ajudar as vitimas que estão em ", True, (255,255,255))
story7 = fonte.render("apuros nessa terrível enchente.", True, (255,255,255))
story8 = fonte.render("Vamos nessa?", True, (255,255,255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    STORY_MOUSE_POS = pygame.mouse.get_pos()

    retangulo = pygame.Surface((900, 650), pygame.SRCALPHA)
    
    screen.blit(BG, (0,0))
    retangulo.fill(translucido)
    screen.blit(retangulo,(150, 30))
    screen.blit(story1,(160,60))
    screen.blit(story2,(220, 120))
    screen.blit(story3,(190,180))
    screen.blit(story4,(200, 240))
    screen.blit(story5,(180,300))
    screen.blit(story6,(210, 360))
    screen.blit(story7,(210, 420))
    screen.blit(story8,(460, 480))

    OPTIONS_BACK = Button(image=None, pos=(600, 580), 
                            text_input="INICIAR", font=fonteComecar, base_color="BLACK", hovering_color="Green")

    OPTIONS_BACK.changeColor(STORY_MOUSE_POS)
    OPTIONS_BACK.update(screen)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(STORY_MOUSE_POS):
                    import choose_player


    pygame.display.update()