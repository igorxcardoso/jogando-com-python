import pygame

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Triangulando")

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
