from time import sleep

import pygame
from Constants import *
from Board import Board
from Game import Game
from Cards import ranCardsComputer,ranCardsPlayer

a = True
pygame.init()
board = Board()
game = Game()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)



while a:

    if game.turn == "Computer" and game.computerWaits == 0:
        game.chooseCardToPick()
        sleep(1)
    if not ranCardsComputer:
        print("Computer wins")
        a = False
    elif not ranCardsPlayer:
        print("Player wins")
        a = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game.turn == "Player":
                game.pickCard()

    board.draw(SCREEN)
    pygame.display.update()
