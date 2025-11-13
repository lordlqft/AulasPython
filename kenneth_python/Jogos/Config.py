import pygame

pygame.init()

LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Animação do Isaac")

FPS = 60
ESCALA = 2.0

# Paredes e Portas
parede_espessura = 40
porta_tamanho = 120
porta_left = (LARGURA - porta_tamanho) // 2
porta_right = porta_left + porta_tamanho
porta_top = (ALTURA - porta_tamanho) // 2
porta_bottom = porta_top + porta_tamanho
