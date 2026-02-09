import pygame
import random

def mudar_cores():
    vermelho = random.randint(0,255)
    verde = random.randint(0,255)
    azul = random.randint(0,255)
    return (vermelho,verde,azul)
#Inicializa pygame
pygame.init()

vermelho = 0
azul = 0
verde = 0

#configurações da janela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Exemplo com pygame")

#DEFININDO UM CLOCK PARA CONTROLAR FPS(frames por segundo)
clock = pygame.time.Clock()
FPS = 500
#define a posiçao x e y como no centro da tela


posicao_X_retangulo = LARGURA // 2
posicao_y_retangulo = ALTURA // 2
#DEFININDP A VELOCIDADE EM X E Y DO RETANGULO
velocidade_X_retangulo = 6
velocidade_y_retangulo = 5



rodando = True 
while rodando:
    #Inicio loop - procurando por eventos
    for evento in pygame.event.get():
        #se o evento fechar, o jogo existe
        if evento.type == pygame.QUIT:
        #Muda a variavel rodando para false (fecha o jogo)
            rodando = False

    #fim do loop de eventos
    posicao_X_retangulo += velocidade_X_retangulo
    posicao_y_retangulo += velocidade_y_retangulo

    #detecção de colisão com as bordas na tela
    if posicao_X_retangulo >= LARGURA - 50 or posicao_X_retangulo <= 0:
        velocidade_X_retangulo *= -1
        vermelho,verde,azul = mudar_cores()
    if posicao_y_retangulo >= ALTURA - 50 or posicao_y_retangulo <= 0:
        velocidade_y_retangulo *= -1
        vermelho,verde,azul = mudar_cores()


        #pinta a tela
        tela.fill((87,131,196))
        vermelho,verde,azul = mudar_cores()


    pygame.draw.rect(tela, (vermelho,verde,azul), (posicao_X_retangulo,posicao_y_retangulo,50,50))

    #aqui desenho elementos graficos
    #atualizando com fps
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
