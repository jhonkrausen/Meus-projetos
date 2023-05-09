import pygame
from pygame.locals import *
from random import randint

pygame.init()

LARGURA = 640
ALTURA = 480
TAMANHO = 10 

tela = pygame.display.set_mode((LARGURA, ALTURA))
titulo = pygame.display.set_caption("SNAKE")
fps = pygame.time.Clock()

Snake = []
corpoSnake = []
snakePosX = randint(0,LARGURA)
snakePosY = randint(0,ALTURA)
snakeVel = 10
snakeDir = "BAIXO"
comprimentoSnake = 5
snake = pygame.draw.rect(tela, (0,0,255), (snakePosX, snakePosY, TAMANHO, TAMANHO))

comidaPosX = randint(0, LARGURA) / TAMANHO
comidaPosY = randint(0, ALTURA) / TAMANHO
comida = pygame.draw.rect(tela, (255,0,0), (comidaPosX, comidaPosY, TAMANHO, TAMANHO))
def geraComida():
    global comidaPosX, comidaPosY
    comidaPosX = randint(0, LARGURA) 
    comidaPosY = randint(0, ALTURA)  

def aumentaSnake():
    Snake = []
    Snake.append(snakePosX)
    Snake.append(snakePosY)
    corpoSnake.append(Snake)
    for XY in corpoSnake:
        pygame.draw.rect(tela, (0,0,255), (XY[0], XY[1], TAMANHO, TAMANHO))
    if comprimentoSnake < len(corpoSnake):
        del corpoSnake[0]
   
def movimentaSnake():
    global snakePosX, snakePosY, snakeDir
    match snakeDir:
        case "CIMA":
            snakePosY = snakePosY - snakeVel
        case "BAIXO":
            snakePosY = snakePosY + snakeVel
        case "ESQUERDA":
            snakePosX = snakePosX - snakeVel
        case "DIREITA":
            snakePosX = snakePosX + snakeVel  

    if snakePosY < 0:
        snakePosY = ALTURA
    if snakePosY > ALTURA:
        snakePosY = 0

    if snakePosX < 0:
        snakePosX = LARGURA
    if snakePosX > LARGURA:
        snakePosX = 0

def eventos():
    global snakeDir
    for events in pygame.event.get():
        if events.type == QUIT:
            pygame.quit()
        if events.type == KEYDOWN:
            if events.key == K_w:
                if snakeDir != "BAIXO":
                    snakeDir = "CIMA"
            if events.key == K_s:
                if snakeDir != "CIMA":
                    snakeDir = "BAIXO"
            if events.key == K_a:
                if snakeDir != "DIREITA":
                    snakeDir = "ESQUERDA"
            if events.key == K_d:
                if snakeDir != "ESQUERDA":
                    snakeDir = "DIREITA"

def colisoes():
    global comidaPosX, comidaPosY, comprimentoSnake, snakeVel
    if  snake.colliderect(comida):
        geraComida()
        comprimentoSnake = comprimentoSnake + 1
       

def gameLoop():
    global fps, tela, comida, snake
    while True:
        fps.tick(30)
        tela.fill((0,0,0))

        comida = pygame.draw.rect(tela, (255,0,0), (comidaPosX, comidaPosY, TAMANHO, TAMANHO))
        snake = pygame.draw.rect(tela, (0,0,255), (snakePosX, snakePosY, TAMANHO, TAMANHO))

        eventos()
        colisoes()
        aumentaSnake()
        movimentaSnake()

        pygame.display.update()

gameLoop() 