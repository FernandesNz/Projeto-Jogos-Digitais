#Matheus Fernandes Rodrigues 42139694
#Victória Alves dos Santos 32198973
import json
import pygame, sys
from pygame.locals import *
from button import Button


pygame.init()

SCREEN = pygame.display.set_mode((1180, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/images/Background3.png")
rank = pygame.image.load("assets/images/ranking.png")
direcionais = pygame.image.load("assets/images/direcionais.png")
space = pygame.image.load("assets/images/space.png")
mudo = pygame.image.load("assets/images/mudo.png")
volume = pygame.image.load("assets/images/volume.png")
fonte = pygame.font.Font("assets/fonts/font.ttf", 17)


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/fonts/font.ttf", size)

translucido = (0,0,0, 100)

titleInstrucoesTxt = fonte.render("Para jogar S.O.S flood é muito simples!", True, (255, 255, 255)) 

instrucoesTxt1 = fonte.render("O objetivo do jogo é desviar dos obstáculos e ", True, (255, 255, 255))
instrucoesTxt2 = fonte.render("salvar as vítimas dessa triste enchente. Para ", True, (255, 255, 255)) 
instrucoesTxt3 = fonte.render("desviar dos obstáculos que são: troncos e rochas," , True, (255, 255, 255))
instrucoesTxt4 = fonte.render("você deve usar as setas do teclado para o lado ", True, (255, 255, 255))
instrucoesTxt5 = fonte.render("direito e esquerdo e para salvar as vítimas basta", True, (255, 255, 255))
instrucoesTxt6 = fonte.render("pressionar a tecla espaço", True, (255, 255, 255))




with open('players.json') as f:
            jogadores = json.load(f)

jogadores.sort(key=lambda x: x['score'], reverse=True)







def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")
        SCREEN.blit(BG,(0,0))
        retangulo = pygame.Surface((900, 600), pygame.SRCALPHA)

        retangulo.fill(translucido)
        SCREEN.blit(retangulo,(150, 50))
        SCREEN.blit(direcionais,(700,500))
        SCREEN. blit(space,(350,570))
        SCREEN.blit(titleInstrucoesTxt,(250, 100))
        SCREEN.blit(instrucoesTxt1,(220, 150))
        SCREEN.blit(instrucoesTxt2,(220, 200))
        SCREEN.blit(instrucoesTxt3,(200, 250))
        SCREEN.blit(instrucoesTxt4,(200, 300))
        SCREEN.blit(instrucoesTxt5,(200, 350))
        SCREEN.blit(instrucoesTxt6,(350, 400))


        OPTIONS_BACK = Button(image=None, pos=(80, 50), 
                            text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Yellow")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()
def ranking():
    while True:
        RANK_MOUSE_POS = pygame.mouse.get_pos()

        fonteRankingTitle = pygame.font.Font("assets/fonts/font.ttf", 37)
        fonte_players = pygame.font.Font("assets/fonts/font.ttf", 27)

        
        

        rakingTxt = fonteRankingTitle.render("Ranking", True, (255,255,255))

        def rankingMvp():
            
            cor = (255, 255, 255)
            cor1 = (255, 255, 0)
            cor2 = (192, 192, 192)
            cor3 = (205, 127, 50)
            cor10 = (0, 255, 255)
            pos_y = 100
            for i, jogador in enumerate(jogadores[:20]):
                if(i == 0):
                    texto = f"{i+1}º {jogador['nome']} - Score: {jogador['score']}"
                    superficie_texto = fonte_players.render(texto, True, cor1)
                    SCREEN.blit(superficie_texto, (300, pos_y))
                    pos_y += 30
                elif(i == 1):
                    texto = f"{i+1}º {jogador['nome']} - Score: {jogador['score']}"
                    superficie_texto = fonte_players.render(texto, True, cor2)
                    SCREEN.blit(superficie_texto, (300, pos_y))
                    pos_y += 30
                elif(i == 2):
                    texto = f"{i+1}º {jogador['nome']} - Score: {jogador['score']}"
                    superficie_texto = fonte_players.render(texto, True, cor3)
                    SCREEN.blit(superficie_texto, (300, pos_y))
                    pos_y += 30
                elif(i > 2 and i < 10):
                    texto = f"{i+1}º {jogador['nome']} - Score: {jogador['score']}"
                    superficie_texto = fonte_players.render(texto, True, cor10)
                    SCREEN.blit(superficie_texto, (300, pos_y))
                    pos_y += 30
                else:
                    texto = f"{i+1}º {jogador['nome']} - Score: {jogador['score']}"
                    superficie_texto = fonte_players.render(texto, True, cor)
                    SCREEN.blit(superficie_texto, (300, pos_y))
                    pos_y += 30


        SCREEN.fill("white")
        SCREEN.blit(BG,(0,0))
        rankingMvp()
        SCREEN.blit(rakingTxt,(480,40))


        OPTIONS_BACK = Button(image=None, pos=(80, 50), 
                            text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Yellow")

        OPTIONS_BACK.changeColor(RANK_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(RANK_MOUSE_POS):
                    main_menu()
        pygame.display.update()


        
def main_menu():
    som = volume
    posSom = (20,600)
    nSom = 0
    while True:
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        if((posSom[0]+100 >= MENU_MOUSE_POS[0] and posSom[0] <= MENU_MOUSE_POS[0]) and (posSom[1] <= MENU_MOUSE_POS[1] and posSom[1] + 100 >= MENU_MOUSE_POS[1]) and event.type == MOUSEBUTTONDOWN):
            pygame.time.delay(700)
            if(nSom == 0):
                som = mudo
                nSom = 1
                pygame.mixer.music.stop()
                with open('music.txt', 'w') as arquivo:
                        arquivo.write('1')
            elif(nSom == 1):
                som = volume
                nSom = 0
                pygame.mixer.music.play()
                with open('music.txt', 'w') as arquivo:
                        arquivo.write('0')
        


        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(som,posSom)

        

        MENU_TEXT = get_font(100).render("SOS Flood", True, "#FFCD50")
        MENU_RECT = MENU_TEXT.get_rect(center=(590, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/images/jogar.png"), pos=(590, 250), 
                            text_input="Jogar", font=get_font(60), base_color="#d7fcd4", hovering_color="green")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/images/instrucoes.png"), pos=(590, 400), 
                            text_input="Instruções", font=get_font(60), base_color="#d7fcd4", hovering_color="yellow")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/images/sair.png"), pos=(590, 550), 
                            text_input="Sair", font=get_font(60), base_color="#d7fcd4", hovering_color="red")
        RANKING_BUTTON = Button(rank, pos=(1100, 650), 
                            text_input="", font=get_font(60), base_color="#d7fcd4", hovering_color="red")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, RANKING_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    import story
                if RANKING_BUTTON.checkForInput(MENU_MOUSE_POS):
                    ranking()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        

        pygame.display.update()
     
pygame.mixer.music.load("assets/songs/musicatema.mp3")
pygame.mixer.music.play()
main_menu()
