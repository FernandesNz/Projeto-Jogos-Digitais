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
fonte = pygame.font.Font("assets/fonts/font.ttf", 30)


background_color = (0, 0, 0) # preto
font = pygame.font.Font(None, 36)
game_over_text = fonte.render("Game Over", True, (255, 255, 255))

with open ('scoreAtual.txt', 'r') as arquivo:
    score = arquivo.read()

scoreTxt = fonte.render("Score: " + str(score), True, (255,255,255))

nickName = fonte.render("Nick Name", True, (255, 255, 255))

translucido = (0,0,0, 100)

input_text = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key == K_RETURN:
                novo_player = {
                    "nome": str(input_text),
                    "score": int(score)
                }

                with open('players.json', 'r') as arquivo:
                    players = json.load(arquivo)

                players.append(novo_player)

                with open('players.json', 'w') as arquivo:
                    json.dump(players, arquivo) 

                pygame.quit()
            else:
                input_text += event.unicode

    retangulo = pygame.Surface((500, 80), pygame.SRCALPHA)

    name = fonte.render(input_text, True, (255,255,255))

    screen.blit(BG, (0,0))
    screen.blit(game_over_text, (450, 100))
    screen.blit(scoreTxt, (450, 150))
    retangulo.fill(translucido)
    screen.blit(nickName,(480, 350))
    screen.blit(retangulo,(350, 400))
    screen.blit(name, (370, 420))

    pygame.display.update()

