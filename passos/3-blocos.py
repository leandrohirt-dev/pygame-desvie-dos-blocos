import pygame
import random

pygame.init()
tela = pygame.display.set_mode((600, 400))
relogio = pygame.time.Clock()
jogador = pygame.Rect(270, 350, 60, 20)
blocos = []

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jogador.x -= 7
    if teclas[pygame.K_RIGHT]:
        jogador.x += 7
    jogador.clamp_ip(tela.get_rect())

    if random.random() < 0.05:
        x = random.randint(0, 570)
        blocos.append(pygame.Rect(x, -30, 30, 30))
    for bloco in blocos:
        bloco.y += 6

    tela.fill((20, 20, 35))
    pygame.draw.rect(tela, (0, 200, 255), jogador)
    for bloco in blocos:
        pygame.draw.rect(tela, (255, 80, 80), bloco)
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
