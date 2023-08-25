import random
import pygame
from pygame.locals import * #Funções e constantes
from sys import exit #função para fechar janela
from random import randint #Sorteia valores de posições y x


pygame.init() #Iniciando a biblioteca


#musica de fundo
pygame.mixer.music.set_volume(0.100)
musicaDeFundo = pygame.mixer.music.load('sons/AS MAIS TOCADAS BOLSONARO 2022 - BOLSONARO PRESIDENTE 2022 - MÚSICA DO BOLSONARO 2022(MP3_160K).mp3')
pygame.mixer.music.play(-1)

#Barulho da colisão

#sonColisao1 = pygame.mixer.Sound('sons/B_vagabundo.wav')
sonColisao2 = pygame.mixer.Sound('sons/B_vagabundo.wav')

#Imagens
fundo = pygame.image.load('img/Planalto.jpeg')
bolsonaro = pygame.image.load('img/id-jair-cabeca.png')
rolex = pygame.image.load('img/Rolex-PNG-Photo.png')

#Queda
gravidade = 0.09
velocidade_vertical = 0

#Tamanho da tela
largura = 640
altura = 480

#Para locomoção
x = largura/2 #meio da tela
y = altura/2 #meio da tela

#Recebendo função randint
x_bolsonaro = randint(40, 600)
y_bolsonaro = randint(50, 430)

x_Rolex = randint(40, 600)
y_Rolex = randint(50, 430)

#Texto
fonte = pygame.font.SysFont('Times New Roman',40,True,True) #Fonte, tamanho, negrito, arial
pontos = 0

tela = pygame.display.set_mode((largura, altura), pygame.FULLSCREEN)

pygame.display.set_caption('Jogo') #Nomeando janela

relogio = pygame.time.Clock() #frames objeto


#loop que irá rodar o game
while True:
    relogio.tick(50) #Controlar frames por segundo
    #tela.fill((0,0,0)) #tela que fica quando o bloco passa
    mensagem = f'Jóias: {pontos}'
    textoFormatado = fonte.render(mensagem, False, (255,255,255)) # Mensagem, pixelado, cor
    tela.blit(fundo,(0,0))
    tela.blit(textoFormatado, (440,20)) # texto e posição
    tela.blit(bolsonaro, (x_bolsonaro,y_bolsonaro))
    tela.blit(rolex, (x_Rolex,y_Rolex))

    # Atualizar a velocidade vertical
    velocidade_vertical += gravidade

    # Atualizar a posição vertical do Rolex
    y_Rolex += velocidade_vertical

    # Verificar se o Rolex atingiu o chão
    if y_Rolex > altura:
        y_Rolex = 0  # Reposiciona o Rolex no topo da tela
        x_Rolex = randint(0, 600)  # Reposiciona o Rolex horizontalmente
        velocidade_vertical = 0  # Reseta a velocidade vertical

    #evento de sair do jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

        #Controlar objeto com botões
        '''
        if evento.type == KEYDOWN:
            if evento.key == K_a:
                x = x - 20
            elif evento.key == K_d:
                x = x + 20
            elif evento.key == K_w:
                y = y - 20
            elif evento.key == K_s:
                y = y + 20 '''

    #Com tecla prescionada
    if pygame.key.get_pressed()[K_a]:
        x_bolsonaro = x_bolsonaro - 15
    elif pygame.key.get_pressed()[K_d]:
        x_bolsonaro = x_bolsonaro + 15
    elif pygame.key.get_pressed()[K_w]:
        y_bolsonaro = y_bolsonaro - 15
    elif pygame.key.get_pressed()[K_s]:
        y_bolsonaro = y_bolsonaro + 15

    # Definir os tamanhos desejados
    novo_largura_bolsonaro = 70
    novo_altura_bolsonaro = 70

    novo_largura_rolex = 60
    novo_altura_rolex = 60

    # Redimensionar as imagens
    bolsonaro = pygame.transform.scale(bolsonaro, (novo_largura_bolsonaro, novo_altura_bolsonaro))
    rolex = pygame.transform.scale(rolex, (novo_largura_rolex, novo_altura_rolex))

    #Objetos
    #primeiro parametro é a cor e depois x, y, largPixels, alturaPixels
    #ret_verde = pygame.draw.rect(tela, (0,255,0),(x , y,25,25))
    #ret_vermelho = pygame.draw.rect(tela, (255,0,0),(x_vermelho,y_vermelho,25,25))
    bolsonaro_rect = bolsonaro.get_rect(topleft=(x_bolsonaro, y_bolsonaro))
    tela.blit(bolsonaro, (x_bolsonaro, y_bolsonaro))

    # Objeto Rolex
    rolex_rect = rolex.get_rect(topleft=(x_Rolex, y_Rolex))
    tela.blit(rolex, (x_Rolex, y_Rolex))

    #Condição de colizão
    if bolsonaro_rect.colliderect(rolex_rect):
        y_Rolex = 0  # Reposiciona o Rolex no topo da tela
        x_Rolex = randint(0, 600)  # Reposiciona o Rolex horizontalmente
        pontos = pontos + 1
        print("Roubou")
        sonColisao2.play()

    #movimentação automarica

    '''if y >= altura:
        y = 0
        y = y+1'''

    #circulo que no final coloca o raio dele
    #pygame.draw.circle(tela, (255,0,0),(340,100), 35)#circulo que no final coloca o raio dele
    #linha que se passa a posição inicial com a final e depois a expessura
    #pygame.draw.line(tela, (0,255,0), (390,0),(390,600),5)


    pygame.display.update() #O jogo ficará sempre atualizando sem parar a janela
