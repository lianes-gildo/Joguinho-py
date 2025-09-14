import pygame
import random

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

jogador = pygame.Rect(180, 500, 40, 40)
velocidade = 5
obstaculos = []

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
