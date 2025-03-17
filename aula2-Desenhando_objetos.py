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

# Loop para fazer o jogo funcionar
while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()

    # Desenhos
    pygame.draw.rect(tela, (255, 0, 0), (200, 300, 40, 50))
    pygame.draw.circle(tela, (0, 0, 255), (300, 260), 40)
    pygame.draw.line(tela, (255, 255, 0), (390, 0), (390, 600), 5)

    pygame.display.update()