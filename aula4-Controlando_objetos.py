import pygame
from pygame.locals import *
from sys import exit

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
white = (255, 255, 255)

# Posição
x = largura_tela // 2
y = 0

# Frames
clock = pygame.time.Clock()
fps = 60

# Loop para fazer o jogo funcionar
while True:
    # Preenche a tela
    tela.fill((0, 0, 0))

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
    pygame.draw.rect(tela, red, (x, y, 40, 50))

    # Ativar o fps
    clock.tick(fps)

    
    # Atualiza a tela
    pygame.display.update()