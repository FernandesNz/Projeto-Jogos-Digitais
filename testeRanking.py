import pygame 
import json
import sys

pygame.init()

# Leitura do arquivo JSON com os dados dos jogadores
with open('players.json') as f:
    jogadores = json.load(f)

# Ordenação dos jogadores pela pontuação
jogadores.sort(key=lambda x: x['score'], reverse=True)

# Função para desenhar os três melhores jogadores na tela
def desenhar_tres_melhores():
    fonte = pygame.font.SysFont('Arial', 24)
    cor = (255, 255, 255)
    pos_y = 100
    for i, jogador in enumerate(jogadores[:3]):
        texto = f"{i+1}º lugar: {jogador['nome']} - {jogador['score']} pontos"
        superficie_texto = fonte.render(texto, True, cor)
        tela.blit(superficie_texto, (100, pos_y))
        pos_y += 30

# Criação da tela do Pygame
tela = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Exemplo de leitura de arquivo JSON com dados de jogadores')

# Loop principal do Pygame
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpe a tela
    tela.fill((0, 0, 0))

    # Desenhe os três melhores jogadores na tela
    desenhar_tres_melhores()

    # Atualize a tela
    pygame.display.update()
