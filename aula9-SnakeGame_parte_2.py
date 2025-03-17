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
pygame.display.set_caption('Jogo')

# Cores
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)

# Posição retangulo vermelho
x_cobra = largura_tela // 2
y_cobra = 0

# Controle
velocidade = 10
x_controle = velocidade
y_controle = 0

# Posição retangulo azul
x_maca = randint(0, largura_tela - 40)
y_maca = randint(0, altura_tela - 50)

# Fonte
fonte = pygame.font.SysFont('aral', 40, True, True)
pontos = 0

# Frames
clock = pygame.time.Clock()
fps = 60

# Músicas de fundo
pygame.mixer.music.set_volume(0.7)
musica_fundo = pygame.mixer.music.load('./músicas/SUPER_MARIO_BROS_MÚSICAS.mp3')
pygame.mixer.music.play(-1)

# Barulho de colisão
barulho_colisao = pygame.mixer.Sound('./músicas/ringtone_mario.mp3')

# Corpo da cobra
lista_cobra = []
comprimento_inicial = 5

# Função para fazer o corpo crescer
def aumenta_cobra(lista_cobra):
    for x, y in lista_cobra:
        pygame.draw.rect(tela, green, (x, y, 20, 20))

# Loop para fazer o jogo funcionar
while True:
    # Preenche a tela
    tela.fill(white)
    
    # Mensagem
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, black)

    # Finalização do jogo
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()

        # Clicando
        if evento.type == KEYDOWN:
            if evento.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0

            if evento.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0

            if evento.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0

            if evento.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra += x_controle
    y_cobra += y_controle

    # Desenhos
    cobra = pygame.draw.rect(tela, green, (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, red, (x_maca, y_maca, 20, 20))

    if cobra.colliderect(maca):
        x_maca = randint(0, largura_tela - 20)
        y_maca = randint(0, altura_tela - 20)
        pontos += 1
        barulho_colisao.play()
        comprimento_inicial += 1

    # Lista do corpo
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    # Ativar o fps
    clock.tick(fps)

    
    # Atualiza a tela
    tela.blit(texto_formatado, (450, 40))
    pygame.display.update()

    # Para ver as fontes disponíveis do pygame é o código
    # pygame.font.get_fonts()