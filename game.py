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
tronco = pygame.image.load("assets/images/tronco 2.png")
font = pygame.font.SysFont("assets/fonts/font.ttf", 50)
cVida = pygame.image.load("assets/images/coracao.png")
cVazio = pygame.image.load("assets/images/coracao_cinza.png")
fonte = pygame.font.Font("assets/fonts/font.ttf", 30)
rocha = pygame.image.load("assets/images/rocha_musgo.png")
troncom = pygame.image.load("assets/images/tronco_musgo.png")
bombeira = pygame.image.load("assets/images/bombeira.png")
bombeiro = pygame.image.load("assets/images/bombeiro.png")
lebron = pygame.image.load("assets/images/lebron.png")
jhonny = pygame.image.load("assets/images/jhonny.png")
kick = pygame.image.load("assets/images/kick.png")
lara = pygame.image.load("assets/images/lara.png")
cosmo = pygame.image.load("assets/images/cosmo.png")
ang = pygame.image.load("assets/images/ang.png")
cap = pygame.image.load("assets/images/cap.png")
ciborg = pygame.image.load("assets/images/ciborg.png")
padrao = pygame.image.load("assets/images/padrão.png")
goku = pygame.image.load("assets/images/goku.png")
wanda = pygame.image.load("assets/images/wanda.png")
groot = pygame.image.load("assets/images/groot.png")
cartman = pygame.image.load("assets/images/cartman.png")
kenny = pygame.image.load("assets/images/kenny.png")



# posição do obstaculo
posicaoObstaculo = [385, -150]

# Tamanho do obstaculo
hObstaculo = 30
wObstaculo = 200

#tamanho do Heroi
hHeroi = 100
wHeroi = 100

#velocidade do obstaculo
velY = 7

# posição do Heroi
posicaoHeroi = [580, 600]

#velocidade do heroi
velocidadeHeroi = [5, 5]

#posição da vitima
posicaoVitima = [615, -1200]

# cor dos corações
c1 = cVida
c2 = cVida
c3 = cVida

#vida 
life = 3

clock = pygame.time.Clock()

CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000)
temporizador = 0

vitimasSalvas = 0
score = 0
bonus = 0

estadoVitima = "fora"
ladoObstaculo = "esquerda"


player = bombeira

with open ('player.txt', 'r') as arquivo:
    playerEscolhido = arquivo.read()



obstaculo = tronco
vitima = padrao

running = True
while running:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == CLOCKTICK:
                temporizador = temporizador +1

    if(playerEscolhido == '0'):
        player = bombeira
    if(playerEscolhido == '1'):
        player = bombeiro


    posicaoObstaculo[1] += velY
    posicaoVitima[1] += velY
    



    #aumento de velocidade de acordo com o tempo
    if(temporizador >= 10):
        velY = 10
    if(temporizador >= 15):
        velY = 12
    if(temporizador >= 20):
        velY = 14
    if(temporizador >= 25):
        velY = 17
    if(temporizador >= 35):
        velY = 20

    #aumento de velocidade do heroi de acordo com o tempo
    if(temporizador >= 10):
        velocidadeHeroi = [6,6]
    if(temporizador >= 15):
        velocidadeHeroi = [8,8]
    if(temporizador >= 20):
        velocidadeHeroi = [10,10]
    if(temporizador >= 35):
        velocidadeHeroi = [12,12]
    if(temporizador >= 55):
        velocidadeHeroi = [15,15]
    
        


    #movimento do heroi

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]: 
        if(posicaoHeroi[0] > 355):
            posicaoHeroi[0] -= velocidadeHeroi[0]
    if pressed[pygame.K_RIGHT]: 
        if(posicaoHeroi[0] < 720):
            posicaoHeroi[0] += velocidadeHeroi[0]
    


    #determinando se a vitima esta ou não na tela
    if(posicaoVitima[1] < 0):
        estadoVitima = "fora"
    if(posicaoVitima[1] > 0):
        estadoVitima = "dentro"
    


    # posição em que o obstaculo restornara
    if(posicaoObstaculo[1] >= win_height):
        num_obstaculo = randint(0,2)

        if(num_obstaculo == 0):
            obstaculo = tronco
        if(num_obstaculo == 1):
            obstaculo = rocha
        if(num_obstaculo == 2):
            obstaculo = troncom

        posicao = randint(0, 1)
        posicaoObstaculo[1] = -50
        if(posicao == 0):
            posicaoObstaculo[0] = 385
            ladoObstaculo = "esquerda"
        if(posicao == 1):
            posicaoObstaculo[0] = 615
            ladoObstaculo = "direita"

    #retornar a vitima ao inicio
    if(posicaoVitima[1] > win_height):
        
        num_vitima = randint(0,12)

        if(num_vitima == 0):
            vitima = jhonny
        if(num_vitima == 1):
            vitima = kick
        if(num_vitima == 2):
            vitima = lebron
        if(num_vitima == 3):
            vitima = lara
        if(num_vitima == 4):
            vitima = cosmo
        if(num_vitima == 5):
            vitima = ang
        if(num_vitima == 6):
            vitima = cap
        if(num_vitima == 7):
            vitima = ciborg
        if(num_vitima == 8):
            vitima = padrao
        if(num_vitima == 9):
            vitima = goku
        if(num_vitima == 10):
            vitima = wanda
        if(num_vitima == 11):
            vitima = cartman
        if(num_vitima == 12):
            vitima = kenny
        pygame.mixer.music.load('assets/songs/erro.mp3')
        bonus -= 30
        if(ladoObstaculo == "esquerda"):
            posicaoVitima[0] = 655
        if(ladoObstaculo == "direita"):
            posicaoVitima[0] = 400
        if(posicaoObstaculo[1] >= 400):
            posicaoVitima[1] = posicaoObstaculo[1] - 1500
        if(posicaoObstaculo[1] < 400):
            posicaoVitima[1] = posicaoObstaculo[1] - 1000

    if((posicaoHeroi[0]+100 >= posicaoObstaculo[0] and posicaoHeroi[0] <= posicaoObstaculo[0] + 200) and (posicaoHeroi[1] <= posicaoObstaculo[1] + 30 and posicaoHeroi[1] + 100 >= posicaoObstaculo[1])):
        num_obstaculo = randint(0,2)

        if(num_obstaculo == 0):
            obstaculo = tronco
        if(num_obstaculo == 1):
            obstaculo = rocha
        if(num_obstaculo == 2):
            obstaculo = troncom
        
        posicao = randint(0, 1)
        posicaoObstaculo[1] = -50
        if(posicao == 0):
            posicaoObstaculo[0] = 385
            ladoObstaculo = "esquerda"
        if(posicao == 1):
            posicaoObstaculo[0] = 615
            ladoObstaculo = "direita"
        pygame.mixer.music.load('assets/songs/cococaindo.mp3')
        life -= 1
    if((posicaoHeroi[0]+100 >= posicaoVitima[0] and posicaoHeroi[0] <= posicaoVitima[0] + 100) and (posicaoHeroi[1] <= posicaoVitima[1] + 100 and posicaoHeroi[1] + 100 >= posicaoVitima[1]) and pressed[pygame.K_SPACE]):
        num_vitima = randint(0,12)

        if(num_vitima == 0):
            vitima = jhonny
        if(num_vitima == 1):
            vitima = kick
        if(num_vitima == 2):
            vitima = lebron
        if(num_vitima == 3):
            vitima = lara
        if(num_vitima == 4):
            vitima = cosmo
        if(num_vitima == 5):
            vitima = ang
        if(num_vitima == 6):
            vitima = cap
        if(num_vitima == 7):
            vitima = ciborg
        if(num_vitima == 8):
            vitima = padrao
        if(num_vitima == 9):
            vitima = goku
        if(num_vitima == 10):
            vitima = wanda
        if(num_vitima == 11):
            vitima = cartman
        if(num_vitima == 12):
            vitima = kenny
        
        if(ladoObstaculo == "esquerda"):
            posicaoVitima[0] = 655
        if(ladoObstaculo == "direita"):
            posicaoVitima[0] = 400
        if(posicaoObstaculo[1] >= 400):
            posicaoVitima[1] = posicaoObstaculo[1] - 1500
        if(posicaoObstaculo[1] < 400):
            posicaoVitima[1] = posicaoObstaculo[1] - 1000
        pygame.mixer.music.load('assets/songs/save.mp3')
        vitimasSalvas += 1
        bonus += 10


    if(life == 2):
        c3 = cVazio
    if(life == 1):
        c2 = cVazio
    if(life == 0):
        with open('scoreAtual.txt', 'w') as arquivo:
            arquivo.write(str(score))
        import gameover


    score = temporizador + bonus
        



    timer1 = fonte.render("Timer: " + str(temporizador), True, (255, 0, 255))
    scoreTxt = fonte.render("Score " + str(score), True, (255,255,255))
    vitimasTxt = fonte.render("Salvos " + str(vitimasSalvas), True, (255,255,255))



    win.fill((0,0,0))
    win.blit(bg, (0, 0))
    win.blit(player, (posicaoHeroi))
    win.blit(obstaculo, (posicaoObstaculo))
    win.blit(vitima, (posicaoVitima))
    win.blit(scoreTxt, (10, 620))
    win.blit(vitimasTxt, (10, 670))
    win.blit(c1,(900, 20))
    win.blit(c2,(980, 20))
    win.blit(c3,(1060, 20))
    clock.tick(60)

    pygame.display.update()
 