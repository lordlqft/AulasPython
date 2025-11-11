import pygame
import random

pygame.init()
TELA = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Coletar Moedas")
relogio = pygame.time.Clock()

# Cores
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)

# Jogador
jogador = pygame.Rect(375, 500, 50, 50)

# Lista de moedas
moedas = []

# Controle de tempo
ultimo_spawn = 0
intervalo_spawn = 1000  # 1 segundo (1000 ms)

# Contador de moedas coletadas
moedas_coletadas = 0

# Fonte para exibir o texto
fonte = pygame.font.Font(None, 36)

rodando = True
while rodando:
    tempo_atual = pygame.time.get_ticks()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimento do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]: jogador.x -= 5
    if teclas[pygame.K_RIGHT]: jogador.x += 5
    if teclas[pygame.K_UP]: jogador.y -= 5
    if teclas[pygame.K_DOWN]: jogador.y += 5

    # Gerar nova moeda a cada 1 segundo
    if tempo_atual - ultimo_spawn > intervalo_spawn:
        x = random.randint(0, 800 - 30)
        y = random.randint(0, 600 - 30)
        moedas.append(pygame.Rect(x, y, 30, 30))
        ultimo_spawn = tempo_atual

    # Checar colisão com moedas
    for moeda in moedas[:]:
        if jogador.colliderect(moeda):
            moedas.remove(moeda)
            moedas_coletadas += 1

    # Desenho
    TELA.fill(BRANCO)
    pygame.draw.rect(TELA, AZUL, jogador)
    for moeda in moedas:
        pygame.draw.rect(TELA, AMARELO, moeda)

    # Renderizar texto de pontuação
    texto = fonte.render(f"Moedas coletadas: {moedas_coletadas}", True, PRETO)
    TELA.blit(texto, (10, 10))

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
