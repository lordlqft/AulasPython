import pygame
from Config import LARGURA, ALTURA

def mover_jogador(pos_x, pos_y, mov_x, mov_y, rect_w, rect_h, walls):

    nova_x = pos_x + mov_x
    nova_y = pos_y

    rect = pygame.Rect(int(nova_x), int(nova_y), rect_w, rect_h)

# X
    if not any(rect.colliderect(w) for w in walls):
        pos_x = nova_x

    nova_y = pos_y + mov_y
    rect = pygame.Rect(int(pos_x), int(nova_y), rect_w, rect_h)

# Y
    if not any(rect.colliderect(w) for w in walls):
        pos_y = nova_y

    return pos_x, pos_y


def teleporte(pos_x, pos_y, w, h):
    if pos_x > LARGURA:
        pos_x = -w
    elif pos_x + w < 0:
        pos_x = LARGURA

    if pos_y > ALTURA:
        pos_y = -h
    elif pos_y + h < 0:
        pos_y = ALTURA

    return pos_x, pos_y
