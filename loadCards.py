import random
import string

import pygame.image

colors = ['C', 'D', 'H', 'S']
figures = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
cards = []
ranCardsPlayer = []
ranCardsComputer = []
class Card:
    def __init__(self, color, figure, image):
        self.color = color
        self.figure = figure
        self.image = image
        self.state = "Deck"


def loadCards():
    for color in range(len(colors)):
        for figure in range(len(figures)):
            cards.append(Card(colors[color], figures[figure], pygame.image.load("PNG/" + figures[figure] + colors[color] + ".png")))

def randomCards(forWho):
    for i in (1, 2, 3, 4, 5):
        a = random.randint(0, 51)
        while cards[a].state != "Deck":
            a = random.randint(0, 51)
        ranCardsPlayer.append(cards[a]) if forWho == "Player" else ranCardsComputer.append(cards[a])
        cards[a].state = forWho

