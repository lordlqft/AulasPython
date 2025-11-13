import pygame
from Config import *
from GetImages import load_isaac_images
from Walls import criar_paredes, desenhar_paredes
from Movement import mover_jogador, teleporte
from Animation import animar_isaac

# ISAAC
isaac_images = load_isaac_images()
pos_x, pos_y = LARGURA // 2, ALTURA // 2
velocidade = 4
direcao = "down"
ultima_direcao = "down"
frame = 0
relogio = pygame.time.Clock()

rodando = True
while rodando:

    TELA.fill((40, 40, 40))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

# MOVIMENTO
    teclas = pygame.key.get_pressed()
    movendo = False
    mov_x = 0
    mov_y = 0

    if teclas[pygame.K_w]:
        mov_y = -velocidade
        direcao = "up"
        movendo = True
    if teclas[pygame.K_s]:
        mov_y = velocidade
        direcao = "down"
        movendo = True
    if teclas[pygame.K_a]:
        mov_x = -velocidade
        direcao = "left"
        movendo = True
    if teclas[pygame.K_d]:
        mov_x = velocidade
        direcao = "right"
        movendo = True

    if mov_x != 0 and mov_y != 0:
        mov_x *= 0.7071
        mov_y *= 0.7071

    base_img = isaac_images["down"][2]
    sw, sh = base_img.get_size()
    sw = int(sw * ESCALA)
    sh = int(sh * ESCALA)

    walls = criar_paredes()

    pos_x, pos_y = mover_jogador(pos_x, pos_y, mov_x, mov_y, sw, sh, walls)
    pos_x, pos_y = teleporte(pos_x, pos_y, sw, sh)

    if movendo:
        ultima_direcao = direcao
    else:
        direcao = "down"

    imagem, frame = animar_isaac(isaac_images, direcao, ultima_direcao, movendo, frame)

    desenhar_paredes(TELA, walls)

    iw, ih = imagem.get_size()
    imagem = pygame.transform.scale(imagem, (int(iw * ESCALA), int(ih * ESCALA)))
    TELA.blit(imagem, (int(pos_x), int(pos_y)))

    pygame.display.flip()
    relogio.tick(FPS)

pygame.quit()
