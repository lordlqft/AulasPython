import pygame, os, math
pygame.init()

TELA = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Isaac")
FPS = pygame.time.Clock()

BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

isaac_path = os.path.join("Assets", "Isaac_Images")
poop_path = os.path.join("Assets", "Poop_Images")
goblin_path = os.path.join("Assets", "Goblin_Images")

isaac_idle_down = pygame.image.load(os.path.join(isaac_path, "IsaacIdleDown.png")).convert_alpha()
isaac_walk_down = pygame.image.load(os.path.join(isaac_path, "IsaacWalkDown.png")).convert_alpha()
isaac_walk_down2 = pygame.image.load(os.path.join(isaac_path, "IsaacWalkDown2.png")).convert_alpha()

isaac_idle_up = pygame.image.load(os.path.join(isaac_path, "IsaacIdleUp.png")).convert_alpha()
isaac_walk_up = pygame.image.load(os.path.join(isaac_path, "IsaacWalkUp.png")).convert_alpha()
isaac_walk_up2 = pygame.image.load(os.path.join(isaac_path, "IsaacWalkUp2.png")).convert_alpha()

isaac_idle_right = pygame.image.load(os.path.join(isaac_path, "IsaacIdleRight.png")).convert_alpha()
isaac_walk_right = pygame.image.load(os.path.join(isaac_path, "IsaacWalkRight.png")).convert_alpha()
isaac_walk_right2 = pygame.image.load(os.path.join(isaac_path, "IsaacWalkRight2.png")).convert_alpha()

isaac_idle_left = pygame.image.load(os.path.join(isaac_path, "IsaacIdleLeft.png")).convert_alpha()
isaac_walk_left = pygame.image.load(os.path.join(isaac_path, "IsaacWalkLeft.png")).convert_alpha()
isaac_walk_left2 = pygame.image.load(os.path.join(isaac_path, "IsaacWalkLeft2.png")).convert_alpha()

sprite_poop1 = pygame.image.load(os.path.join(poop_path, "Poop1.png")).convert_alpha()
sprite_poop2 = pygame.image.load(os.path.join(poop_path, "Poop2.png")).convert_alpha()
sprite_poop3 = pygame.image.load(os.path.join(poop_path, "Poop3.png")).convert_alpha()

goblin_walk_right = [pygame.image.load(os.path.join(goblin_path, f"GoblinWR{i}.png")).convert_alpha() for i in range(1, 11)]
goblin_walk_up = [pygame.image.load(os.path.join(goblin_path, f"GoblinWU{i}.png")).convert_alpha() for i in range(1, 11)]
goblin_head = pygame.image.load(os.path.join(goblin_path, "GoblinHead.png")).convert_alpha()

isaac = isaac_idle_down
isaac_rect = isaac.get_rect(center=(400, 300))
velocidade = 3
direcao = "down"
andando = False
frame = 0

poops = [
    {"sprite": sprite_poop1, "rect": sprite_poop1.get_rect(topleft=(200, 300)), "vel": [0, 0]},
    {"sprite": sprite_poop2, "rect": sprite_poop2.get_rect(topleft=(260, 300)), "vel": [0, 0]},
    {"sprite": sprite_poop3, "rect": sprite_poop3.get_rect(topleft=(320, 300)), "vel": [0, 0]},
]

goblin = goblin_head
goblin_rect = goblin.get_rect(center=(100, 100))
goblin_vel = 1.5
goblin_frame = 0

animacoes = {
    "down": [isaac_walk_down, isaac_idle_down, isaac_walk_down2, isaac_idle_down],
    "up": [isaac_walk_up, isaac_idle_up, isaac_walk_up2, isaac_idle_up],
    "right": [isaac_walk_right, isaac_idle_right, isaac_walk_right2, isaac_idle_right],
    "left": [isaac_walk_left, isaac_idle_left, isaac_walk_left2, isaac_idle_left],
}

def aplicar_empurrao(poop, direcao, poops):
    forca = 2
    dx, dy = 0, 0
    if direcao == "left": dx = -forca
    elif direcao == "right": dx = forca
    elif direcao == "up": dy = -forca
    elif direcao == "down": dy = forca
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

def mover_goblin(goblin_rect, isaac_rect):
    dx = isaac_rect.centerx - goblin_rect.centerx
    dy = isaac_rect.centery - goblin_rect.centery
    dist = math.hypot(dx, dy)
    if dist > 0:
        dx /= dist
        dy /= dist
        goblin_rect.x += dx * goblin_vel
        goblin_rect.y += dy * goblin_vel

rodando = True
game_over = False
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    if game_over:
        TELA.fill(VERMELHO)
        pygame.display.flip()
        continue

    teclas = pygame.key.get_pressed()
    andando = False
    pos_anterior = isaac_rect.copy()

    if teclas[pygame.K_a]:
        isaac_rect.x -= velocidade
        direcao = "left"
        andando = True
    elif teclas[pygame.K_d]:
        isaac_rect.x += velocidade
        direcao = "right"
        andando = True
    elif teclas[pygame.K_w]:
        isaac_rect.y -= velocidade
        direcao = "up"
        andando = True
    elif teclas[pygame.K_s]:
        isaac_rect.y += velocidade
        direcao = "down"
        andando = True

    for poop in poops:
        if isaac_rect.colliderect(poop["rect"]):
            aplicar_empurrao(poop, direcao, poops)
            isaac_rect = pos_anterior

    atualizar_poops(poops)
    mover_goblin(goblin_rect, isaac_rect)

    if goblin_rect.colliderect(isaac_rect):
        game_over = True

    goblin_frame += 1
    if goblin_frame >= 100:
        goblin_frame = 0
    if abs(goblin_rect.centerx - isaac_rect.centerx) > abs(goblin_rect.centery - isaac_rect.centery):
        goblin = goblin_walk_right[(goblin_frame // 10) % len(goblin_walk_right)]
    else:
        goblin = goblin_walk_up[(goblin_frame // 10) % len(goblin_walk_up)]

    if andando:
        frame += 1
        if frame >= 40: frame = 0
        fase = (frame // 10) % len(animacoes[direcao])
        isaac = animacoes[direcao][fase]
    else:
        isaac = animacoes[direcao][1]

    TELA.fill(BRANCO)
    for poop in poops:
        TELA.blit(poop["sprite"], poop["rect"])
    TELA.blit(isaac, isaac_rect)
    TELA.blit(goblin, goblin_rect)
    pygame.display.flip()
    FPS.tick(60)

pygame.quit()
