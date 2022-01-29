import pygame
from Constants import *
from Cards import *
from Board import Board

a = True
board = Board()
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

start = True
turn = "Player"
def pickCard():
    get = 1
    cardWidth = CARD_WIDTH / (len(ranCardsPlayer)/3)
    cardHeight = CARD_HEIGHT / (len(ranCardsPlayer)/3)
    pos = pygame.mouse.get_pos()
    x, y = pos

    for card in cards:
        if card.pos_x < x < card.pos_x + cardWidth and card.pos_y < y < card.pos_y + cardHeight and card.state == "Player":
            if not boardCards or boardCards[len(boardCards)-1].figure == 'Q' or card.color == boardCards[len(boardCards)-1].color or card.figure == boardCards[len(boardCards)-1].figure or (card.figure == 'Q' and boardCards[len(boardCards)-1].figure not in ('2', '3', '4')):
                card.pos_x = 0
                card.pos_y = 0
                card.state = "Deck"
                for playerCard in ranCardsPlayer:
                    if playerCard.pos_x > x:
                        playerCard.pos_x -= CARD_WIDTH / 2
                ranCardsPlayer.remove(card)
                boardCards.append(card)
                get = 0
            break
    if get:
        a = random.randint(0, 51)
        while cards[a].state != "Deck":
            a = random.randint(0, 51)
        ranCardsPlayer.append(cards[a])
        cards[a].state = "Player"

def chooseCardToPick():
    get = 1
    for card in ranCardsComputer:
        if ((boardCards[len(boardCards)-1].figure == 'Q' or #dama na wierzchu
                card.color == boardCards[len(boardCards)-1].color or #ten sam kolor
                card.figure == boardCards[len(boardCards)-1].figure or #ta sama figura
                card.figure == 'Q') and
                (boardCards[len(boardCards)-1].figure not in ('2', '3', '4') and (boardCards[len(boardCards)-1].figure != 'K' and boardCards[len(boardCards)-1].color not in ('H', 'S'))) #poloz dame ale nie na waleczną
        ):
            card.pos_x = 0
            card.pos_y = 0
            card.state = "Deck"
            ranCardsComputer.remove(card)
            boardCards.append(card)
            get = 0
            break

    if get:
        a = random.randint(0, 51)
        while cards[a].state != "Deck":
            a = random.randint(0, 51)
        ranCardsComputer.append(cards[a])
        cards[a].state = "Computer"

while a:
    if turn == "Computer":
        start = False
        chooseCardToPick()
        turn = "Player"

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
            if turn == "Player":
                pickCard()
                turn = "Computer"

    board.draw(SCREEN)
    pygame.display.update()

