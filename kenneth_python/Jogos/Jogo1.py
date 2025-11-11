# Para usar esta biblioteca, primeiro instale-a no seu terminal:
# pip install pygame
# Para verificar se a instalação deu certo, digite: pip list
import pygame
import time
pygame.init()
TELA = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Movendo com o Teclado")

# Isaac Sprites
isaac = pygame.image.load("IsaacIdle.png").convert_alpha()

isaac_walk_right = pygame.image.load("IsaacWalkRight")
isaac_walk_right2 = pygame.image.load("IsaacWalkRight2")
isaac_idle_right = pygame.image.load("IsaacIdleRight")

isaac_walk_walk = pygame.image.load("IsaacWalkUp")
isaac_walk_walk2 = pygame.image.load("IsaacWalkUp2")
isaac_idle_up = pygame.image.load("IsaacIdleUp")

isaac_walk_left = pygame.image.load("IsaacWalkLeft")
isaac_walk_left2 = pygame.image.load("IsaacWalkLeft2")
isaac_idle_left = pygame.image.load("IsaacIdleLeft")

isaac_walk_down = pygame.image.load("IsaacWalkDown")
isaac_walk_down2 = pygame.image.load("IsaacWalkDown2")
isaac_idle_down = pygame.image.load("IsaacIdleDown")


isaac_rect = isaac.get_rect(center=(400, 500))
FPS = pygame.time.Clock()
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)

# Posição inicial e tamanho do isaac
isaac_x, isaac_y = 375, 500
isaac_largura, isaac_altura = 50, 50

velocidade = 5

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_a] and isaac_x > 0:
        isaac_rect.x -= velocidade
    if teclas[pygame.K_d] and isaac_x < 800 - isaac_largura:
        isaac_rect.x += velocidade

    if teclas[pygame.K_w] and isaac_y > 0:
        isaac_rect.y -= velocidade
    if teclas[pygame.K_s] and isaac_y < 600 - isaac_altura:
        isaac_rect.y += velocidade


    TELA.fill(BRANCO)
    TELA.blit(isaac, isaac_rect)
    pygame.display.flip()
    FPS.tick(60)
pygame.quit()