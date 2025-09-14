import pygame
import random
import os

pygame.init()

largura, altura = 600, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Esquiva Blocos")
clock = pygame.time.Clock()
fonte = pygame.font.SysFont(None, 36)


ARQUIVO_RECORDE = "recorde.txt"

def carregar_recorde():
    if os.path.exists(ARQUIVO_RECORDE):
        with open(ARQUIVO_RECORDE, "r") as f:
            try:
                return int(f.read())
            except:
                return 0
    return 0

def salvar_recorde(novo_recorde):
    with open(ARQUIVO_RECORDE, "w") as f:
        f.write(str(novo_recorde))

recorde = carregar_recorde()

def criar_obstaculos():
    x = random.randint(0, largura - 40)
    return pygame.Rect(x, -40, 40, 40)

def desenhar_texto(texto, x, y, cor=(255, 255, 255)):
    imagem_texto = fonte.render(texto, True, cor)
    tela.blit(imagem_texto, (x, y))


def desenhar_jogador_triangulo(rect, cor=(0, 255, 0)):
    centro_x = rect.centerx
    topo = (centro_x, rect.top)
    canto_esquerdo = (rect.left, rect.bottom)
    canto_direito = (rect.right, rect.bottom)
    pygame.draw.polygon(tela, cor, [topo, canto_esquerdo, canto_direito])
    
def resetar_jogo():
    jogador = pygame.Rect(largura//2 - 20, altura - 100, 40, 40)
    obstaculos = []
    score = 0
    return jogador, obstaculos, score

jogador, obstaculos, score = resetar_jogo()
velocidade = 5
jogo_ativo = True

rodando = True
while rodando:
    tela.fill((40, 40, 40))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jogador.left > 0:
        jogador.x -= velocidade
    if teclas[pygame.K_RIGHT] and jogador.right < largura:
        jogador.x += velocidade

   
    if random.randint(1, 30) == 1:
        obstaculos.append(criar_obstaculos())

    for obstaculo in obstaculos:
        
        obstaculo.y += 5

        if obstaculo.colliderect(jogador):
            rodando = False

        pygame.draw.rect(tela, (255, 0, 0), obstaculo)
       
        
    obstaculos = [obstaculo for obstaculo in obstaculos if obstaculo.y < altura]

    
    pygame.draw.rect(tela, (0, 255, 0), jogador)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
