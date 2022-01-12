import pygame
from loadCards import *

a = True
pygame.init()
screen = pygame.display.set_mode((1280, 720), 0, 32)
loadCards()
randomCards("Player")
randomCards("Computer")

def showCards(forWho):
    if forWho == ranCardsPlayer:
        x = 350
        y = 600
        for i in range(len(forWho)):
            screen.blit(forWho[i].image, (x, y))
            x += 100
    if forWho == ranCardsComputer:
        x = 1200
        y = 50
        for i in range(len(forWho)):
            screen.blit(forWho[i].image, (x, y))
            y+=100


while a:
    screen.fill((36, 92, 25))
    showCards(ranCardsPlayer)
    showCards(ranCardsComputer)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False
    pygame.display.update()


