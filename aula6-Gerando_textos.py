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
white = (255, 255, 255)

# Posição retangulo vermelho
x = largura_tela // 2
y = 0

# Posição retangulo azul
x_azul = randint(0, largura_tela - 40)
y_azul = randint(0, altura_tela - 50)

# Fonte
fonte = pygame.font.SysFont('aral', 40, True, True)
pontos = 0


# Frames
clock = pygame.time.Clock()
fps = 60

# Loop para fazer o jogo funcionar
while True:
    # Preenche a tela
    tela.fill((0, 0, 0))
    
    # Mensagem
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, white)

    # Finalização do jogo
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()

        # Clicando
        # if evento.type == KEYDOWN:
        #     if evento.key == K_a:
        #         x -= 20
        #     if evento.key == K_d:
        #         x += 20
        #     if evento.key == K_w:
        #         x -= 20
        #     if evento.key == K_s:
        #         x += 20

    # Segurando
    if pygame.key.get_pressed()[K_a]:
        x -= 20
    if pygame.key.get_pressed()[K_d]:
        x += 20
    if pygame.key.get_pressed()[K_w]:
        y -= 20
    if pygame.key.get_pressed()[K_s]:
        y += 20

    # Desenhos
    ret_vermelho = pygame.draw.rect(tela, red, (x, y, 40, 50))
    ret_azul = pygame.draw.rect(tela, blue, (x_azul, y_azul, 40, 50))

    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(0, largura_tela - 40)
        y_azul = randint(0, altura_tela - 50)
        pontos += 1

    # Ativar o fps
    clock.tick(fps)

    
    # Atualiza a tela
    tela.blit(texto_formatado, (450, 40))
    pygame.display.update()

    # Para ver as fontes disponíveis do pygame é o código
    # pygame.font.get_fonts()