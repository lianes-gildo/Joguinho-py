import pygame
import random

pygame.init()

largura, altura = 400, 600
tela = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()

jogador = pygame.Rect(180, 500, 40, 40)
velocidade = 5
obstaculos = []