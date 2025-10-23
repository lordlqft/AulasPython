# Exemplo de uso do módulo pygame
import pygame
import random

pygame.init()

# --- Configurações da Tela e Cores ---
LARGURA, ALTURA = 600, 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Cobrinha")
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

# --- Configurações do Jogo ---
TAMANHO_BLOCO = 20
velocidade = 8
clock = pygame.time.Clock()
fonte = pygame.font.SysFont(None, 25)

def desenhar_cobra(lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, VERDE, [x[0], x[1], TAMANHO_BLOCO, TAMANHO_BLOCO])

def rodar_jogo():
    fim_de_jogo = False

    # Posição inicial da cobra e movimento
    x1 = LARGURA / 2
    y1 = ALTURA / 2
    x1_change = 0
    y1_change = 0

    lista_cobra = []
    comprimento_cobra = 1

    # Posição inicial da comida
    comida_x = round(random.randrange(0, LARGURA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO
    comida_y = round(random.randrange(0, ALTURA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO

    while not fim_de_jogo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim_de_jogo = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -TAMANHO_BLOCO
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = TAMANHO_BLOCO
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -TAMANHO_BLOCO
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = TAMANHO_BLOCO
                    x1_change = 0

        # Verifica colisão com as paredes
        if x1 >= LARGURA or x1 < 0 or y1 >= ALTURA or y1 < 0:
            fim_de_jogo = True

        x1 += x1_change
        y1 += y1_change
        tela.fill(PRETO)

        # Desenha a comida
        pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, TAMANHO_BLOCO, TAMANHO_BLOCO])

        # Gerencia o corpo da cobra
        cabeca_cobra = []
        cabeca_cobra.append(x1)
        cabeca_cobra.append(y1)
        lista_cobra.append(cabeca_cobra)
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        # Verifica colisão com o próprio corpo
        for x in lista_cobra[:-1]:
            if x == cabeca_cobra:
                fim_de_jogo = True

        desenhar_cobra(lista_cobra)
        pygame.display.update()

        # Verifica se comeu a comida
        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, LARGURA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO
            comida_y = round(random.randrange(0, ALTURA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO
            comprimento_cobra += 1

        clock.tick(velocidade)

    pygame.quit()

rodar_jogo()