import sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Input Text")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 32)

input_text = ""

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key == K_RETURN:
                print(input_text)
                input_text = ""
            else:
                input_text += event.unicode
    
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (300, 250, 200, 50))
    
    text_surface = font.render(input_text, True, WHITE)
    screen.blit(text_surface, (310, 260))
    
    pygame.display.update()
