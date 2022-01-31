#Filip Stańczak WCY19IJ3SJ nr.Album 75155

import pygame
from Constants import *
from Cards import *


class Board:

    def __init__(self):
        self.playerCards = self.computerCards = 5
        self.selected_Card = None
        loadCards()
        randomCards("Player")
        randomCards("Computer")

    def draw(self, screen):
        screen.fill(BOARD_COLOR)
        showCards(ranCardsPlayer, screen)
        showCards(ranCardsComputer, screen)
        showCards(boardCards, screen)
        showButton(screen)


def showCards(forWho, SCREEN):
    if forWho == ranCardsPlayer:
        x = 0
        y = HEIGHT - 120
        for i in range(len(forWho)):
            SCREEN.blit(forWho[i].image, (x,y))
            forWho[i].pos_x = x
            forWho[i].pos_y = y
            x += CARD_WIDTH / (len(forWho)/3)
    elif forWho == ranCardsComputer:
        x = WIDTH - 80
        y = 0
        for i in range(len(forWho)):
            SCREEN.blit(forWho[i].back, (x,y))
            forWho[i].pos_x = x
            forWho[i].pos_y = y
            y += CARD_HEIGHT / (len(forWho)/3)

    elif forWho == boardCards:
        if len(boardCards) > 0:
            x = DECK_CARD_POSITION_X
            y = DECK_CARD_POSITION_Y
            SCREEN.blit(forWho[len(forWho)-1].image, (x, y))

def showButton(screen):
    pygame.draw.rect(screen,GRAY,(5,5,120,60))
    smallfont = pygame.font.SysFont('Corbel', 16)
    text = smallfont.render('TAKE', True, (255,255,0))

    screen.blit(text, (50, 30))
