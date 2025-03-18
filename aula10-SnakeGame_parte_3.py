import pygame
from pygame.locals import *
from sys import exit
from random import randint

# Inicia o pygame
pygame.init()

# Definir a largura e altura da tela
largura_tela = 640
altura_tela = 480
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Define o título da janela
pygame.display.set_caption('Jogo da Cobrinha')

# Cores
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)

# Posição inicial da cobra
x_cobra = largura_tela // 2
y_cobra = altura_tela // 2

# Controle de movimento
velocidade = 20
x_controle = velocidade
y_controle = 0

# Posição inicial da maçã
def gerar_posicao_maca():
    return randint(0, (largura_tela // 20) - 1) * 20, randint(0, (altura_tela // 20) - 1) * 20

x_maca, y_maca = gerar_posicao_maca()

# Fonte
fonte = pygame.font.SysFont('arial', 40, True, True)
pontos = 0

# Frames
clock = pygame.time.Clock()
fps = 10

# Sons
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
try:
    pygame.mixer.music.load('./músicas/SUPER_MARIO_BROS_MÚSICAS.mp3')
    pygame.mixer.music.play(-1)
    barulho_colisao = pygame.mixer.Sound('./músicas/ringtone_mario.mp3')
except:
    print("Erro ao carregar arquivos de música.")
    barulho_colisao = None

# Corpo da cobra
lista_cobra = []
comprimento_inicial = 5
morreu = False

# Função para aumentar a cobra
def aumenta_cobra(lista_cobra):
    for x, y in lista_cobra:
        pygame.draw.rect(tela, green, (x, y, 20, 20))

# Função para reiniciar o jogo
def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, x_maca, y_maca, morreu, lista_cobra, x_controle, y_controle
    pontos = 0
    comprimento_inicial = 5
    x_cobra = largura_tela // 2
    y_cobra = altura_tela // 2
    x_maca, y_maca = gerar_posicao_maca()
    morreu = False
    lista_cobra = []
    x_controle = velocidade
    y_controle = 0

# Loop principal do jogo
while True:
    tela.fill(white)
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, black)

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()

        if evento.type == KEYDOWN:
            if evento.key == K_a and x_controle == 0:
                x_controle = -velocidade
                y_controle = 0
            if evento.key == K_d and x_controle == 0:
                x_controle = velocidade
                y_controle = 0
            if evento.key == K_w and y_controle == 0:
                y_controle = -velocidade
                x_controle = 0
            if evento.key == K_s and y_controle == 0:
                y_controle = velocidade
                x_controle = 0

    x_cobra += x_controle
    y_cobra += y_controle

    # Teletransporte da borda
    if x_cobra >= largura_tela:
        x_cobra = 0
    elif x_cobra < 0:
        x_cobra = largura_tela - 20
    if y_cobra >= altura_tela:
        y_cobra = 0
    elif y_cobra < 0:
        y_cobra = altura_tela - 20

    # Desenho da cobra e da maçã
    cobra = pygame.draw.rect(tela, green, (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, red, (x_maca, y_maca, 20, 20))

    # Verifica colisão com a maçã
    if cobra.colliderect(maca):
        x_maca, y_maca = gerar_posicao_maca()
        while [x_maca, y_maca] in lista_cobra:
            x_maca, y_maca = gerar_posicao_maca()
        pontos += 1
        if barulho_colisao:
            barulho_colisao.play()
        comprimento_inicial += 1

    # Atualiza a lista do corpo
    lista_cabeca = [x_cobra, y_cobra]
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game over! Pressione R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, black)
        ret_texto = texto_formatado.get_rect()
        morreu = True
        while morreu:
            tela.fill(white)
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    exit()
                if evento.type == KEYDOWN and evento.key == K_r:
                    reiniciar_jogo()
            ret_texto.center = (largura_tela // 2, altura_tela // 2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    # Atualiza a tela
    tela.blit(texto_formatado, (450, 40))
    pygame.display.update()
    clock.tick(fps)