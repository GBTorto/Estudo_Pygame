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