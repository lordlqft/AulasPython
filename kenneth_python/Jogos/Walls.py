import pygame
from Config import (
    LARGURA, ALTURA,
    parede_espessura,
    porta_left, porta_right,
    porta_top, porta_bottom
)

def criar_paredes():
    wall_rects = []

# Cima
    wall_rects.append(pygame.Rect(0, 0, porta_left, parede_espessura))
    wall_rects.append(pygame.Rect(porta_right, 0, LARGURA - porta_right, parede_espessura))

# Baixo
    wall_rects.append(pygame.Rect(0, ALTURA - parede_espessura, porta_left, parede_espessura))
    wall_rects.append(pygame.Rect(porta_right, ALTURA - parede_espessura, LARGURA - porta_right, parede_espessura))

# Esquerda
    wall_rects.append(pygame.Rect(0, 0, parede_espessura, porta_top))
    wall_rects.append(pygame.Rect(0, porta_bottom, parede_espessura, ALTURA - porta_bottom))

# Direita
    wall_rects.append(pygame.Rect(LARGURA - parede_espessura, 0, parede_espessura, porta_top))
    wall_rects.append(pygame.Rect(LARGURA - parede_espessura, porta_bottom, parede_espessura, ALTURA - porta_bottom))

    return wall_rects

def desenhar_paredes(tela, walls):
    for wr in walls:
        pygame.draw.rect(tela, (255, 255, 255), wr)
