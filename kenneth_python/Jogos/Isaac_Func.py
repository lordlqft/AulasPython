import pygame
TELA = pygame.display.set_mode((800, 600))
def aplicar_empurrao(poop, direcao, poops):
    forca = 2
    dx, dy = 0, 0
    if direcao == "left":
        dx = -forca
    elif direcao == "right":
        dx = forca
    elif direcao == "up":
        dy = -forca
    elif direcao == "down":
        dy = forca

    poop["vel"][0] += dx
    poop["vel"][1] += dy

    for outro in poops:
        if outro is not poop and poop["rect"].colliderect(outro["rect"]):
            aplicar_empurrao(outro, direcao, poops)

def atualizar_poops(poops):
    atrito = 0.85
    for poop in poops:
        poop["rect"].x += poop["vel"][0]
        poop["rect"].y += poop["vel"][1]
        poop["rect"].clamp_ip(TELA.get_rect())

    for i, p1 in enumerate(poops):
        for j, p2 in enumerate(poops):
            if i != j and p1["rect"].colliderect(p2["rect"]):
                dx = (p1["rect"].centerx - p2["rect"].centerx) * 0.1
                dy = (p1["rect"].centery - p2["rect"].centery) * 0.1
                p1["rect"].x += dx
                p1["rect"].y += dy
                p2["rect"].x -= dx
                p2["rect"].y -= dy

    for poop in poops:
        poop["vel"][0] *= atrito
        poop["vel"][1] *= atrito

isaac_idle_down = pygame.image.load("IsaacIdleDown.png").convert_alpha()
isaac_walk_down = pygame.image.load("IsaacWalkDown.png").convert_alpha()
isaac_walk_down2 = pygame.image.load("IsaacWalkDown2.png").convert_alpha()

isaac_idle_up = pygame.image.load("IsaacIdleUp.png").convert_alpha()
isaac_walk_up = pygame.image.load("IsaacWalkUp.png").convert_alpha()
isaac_walk_up2 = pygame.image.load("IsaacWalkUp2.png").convert_alpha()

isaac_idle_right = pygame.image.load("IsaacIdleRight.png").convert_alpha()
isaac_walk_right = pygame.image.load("IsaacWalkRight.png").convert_alpha()
isaac_walk_right2 = pygame.image.load("IsaacWalkRight2.png").convert_alpha()

isaac_idle_left = pygame.image.load("IsaacIdleLeft.png").convert_alpha()
isaac_walk_left = pygame.image.load("IsaacWalkLeft.png").convert_alpha()
isaac_walk_left2 = pygame.image.load("IsaacWalkLeft2.png").convert_alpha()

sprite_poop1 = pygame.image.load("Poop1.png").convert_alpha()
sprite_poop2 = pygame.image.load("Poop2.png").convert_alpha()
sprite_poop3 = pygame.image.load("Poop3.png").convert_alpha()