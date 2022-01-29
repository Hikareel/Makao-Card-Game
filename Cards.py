import random
import string

import pygame.image
from Constants import *

colors = ['C', 'D', 'H', 'S']
figures = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
cards = []
ranCardsPlayer = []
ranCardsComputer = []
boardCards = []


class Card:
    def __init__(self, color, figure, image):
        self.color = color
        self.figure = figure
        self.image = image
        self.state = "Deck"
        self.back = pygame.image.load("PNG/purple_back.png")
        self.pos_x = 0
        self.pos_y = 0


def loadCards():
    for color in range(len(colors)):
        for figure in range(len(figures)):
            cards.append(Card(colors[color], figures[figure],
                              pygame.image.load("PNG/" + figures[figure] + colors[color] + ".png")))


def randomCards(forWho):
    if forWho == "Computer":
        taken = "Player"
    elif forWho == "Player":
        taken = "Computer"
    for i in (1, 2, 3, 4, 5):
        a = random.randint(0, 51)
        while cards[a].state != "Deck" and cards[a].state != taken:
            a = random.randint(0, 51)
        ranCardsPlayer.append(cards[a]) if forWho == "Player" else ranCardsComputer.append(cards[a])
        cards[a].state = forWho

