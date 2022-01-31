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
askFigure = None
colorChange = None
fight = 0
que = 0
turnsLeft = 0
playerWaits = 0
computerWaits = 0


def takeCard(who):
    a = random.randint(0, 51)
    while cards[a].state != "Deck":
        a = random.randint(0, 51)
    if who == "Player":
        ranCardsPlayer.append(cards[a])
        cards[a].state = "Player"
    elif who == "Computer":
        ranCardsComputer.append(cards[a])
        cards[a].state = "Computer"


def putCardOnTable(card, who):
    card.pos_x = 0
    card.pos_y = 0
    card.state = "Deck"
    if who == "Player":
        ranCardsPlayer.remove(card)
    elif who == "Computer":
        ranCardsComputer.remove(card)
    boardCards.append(card)


def changeColor(who):
    global colorChange
    global turnsLeft
    if who == "Computer":
        a = random.randint(0, 3)
        colorChange = colors[a]
    elif who == "Player":
        while colorChange is None:
            smallfont = pygame.font.SysFont('Corbel', 16)
            text = smallfont.render('Jaki kolor chcesz położyć:\nS - spade\nC - club\nD - diamond\nH - heart', True,(255, 255, 0))
            SCREEN.blit(text, (0, 200))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        colorChange = 'S'
                    if event.key == pygame.K_c:
                        colorChange = 'C'
                    if event.key == pygame.K_d:
                        colorChange = 'D'
                    if event.key == pygame.K_h:
                        colorChange = 'H'
    turnsLeft = 2
    print(who, " zmienia kolor na: ", colorChange)


def figureAsk(who):
    global askFigure
    global turnsLeft
    if who == "Computer":
        a = random.randint(3, 8)
        askFigure = figures[a]
    elif who == "Player":
        while askFigure is None:
            smallfont = pygame.font.SysFont('Corbel', 16)
            text = smallfont.render('Jaką figurę chcesz zarządać (5-10)', True,(255, 255, 0))
            SCREEN.blit(text, (0, 200))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_5:
                        askFigure = '5'
                    if event.key == pygame.K_6:
                        askFigure = '6'
                    if event.key == pygame.K_7:
                        askFigure = '7'
                    if event.key == pygame.K_8:
                        askFigure = '8'
                    if event.key == pygame.K_9:
                        askFigure = '9'
                    if event.key == pygame.K_0:
                        askFigure = '10'
    turnsLeft = 2
    print(who, " rząda: ", askFigure)


def pickCard():
    global colorChange, turnsLeft, askFigure, turn, playerWaits, fight, que, computerWaits
    get = 1
    ex = 0
    cardWidth = CARD_WIDTH / (len(ranCardsPlayer) / 3)
    cardHeight = CARD_HEIGHT / (len(ranCardsPlayer) / 3)
    pos = pygame.mouse.get_pos()
    x, y = pos

    for card in ranCardsPlayer:
        if card.pos_x < x < card.pos_x + cardWidth and card.pos_y < y < card.pos_y + cardHeight:
            if colorChange is None:  # Jesli nie ma na rządaniu koloru
                if askFigure is None:
                    # Jesli karta na stole nie jest waleczna
                    if not boardCards or (fight == 0 and que == 0):
                        if card.figure == 'Q':
                            putCardOnTable(card, "Player")
                            ex = 1
                        elif not boardCards or boardCards[len(boardCards) - 1].figure == 'Q':
                            putCardOnTable(card, "Player")
                            if card.figure == 'A':
                                changeColor("Player")
                            elif card.figure == 'J':
                                figureAsk("Player")
                            ex = 1
                        elif not boardCards or (card.figure == boardCards[len(boardCards) - 1].figure or card.color == boardCards[len(boardCards) - 1].color):
                            putCardOnTable(card, "Player")
                            if card.figure == 'A':
                                changeColor("Player")
                            elif card.figure == 'J':
                                figureAsk("Player")
                            ex = 1
                    # Jesli na stole jest waleczna
                    else:
                        if not boardCards or (card.figure == boardCards[len(boardCards) - 1].figure or card.color == boardCards[len(boardCards) - 1].color):
                            if card.figure in ['2', '3', 'K'] and que == 0:
                                putCardOnTable(card, "Player")
                                if card.figure == '2':
                                    fight += 2
                                elif card.figure == '3':
                                    fight += 3
                                elif card.figure == 'K':
                                    fight += 5
                                ex = 1
                            elif card.figure == '4' and fight == 0:
                                putCardOnTable(card, "Player")
                                que += 1
                                ex = 1

                elif card.figure == askFigure or card.figure == 'J' or card.figure == 'Q':
                    putCardOnTable(card, "Player")
                    if turnsLeft == 0:
                        askFigure = None
                        print("Koniec rządania")
                    else:
                        turnsLeft -= 1
                    if card.figure == 'J':
                        figureAsk("Player")
                    ex = 1

            elif card.color == colorChange or card.figure == 'A' or card.figure == 'Q':
                putCardOnTable(card, "Player")
                if turnsLeft == 0:
                    colorChange = None
                    print("Koniec rządania")
                else:
                    turnsLeft -= 1
                if card.figure == 'A':
                    changeColor("Player")
                ex = 1

            if ex == 1:
                get = 0
                if computerWaits == 0:
                    turn = "Computer"
                else:
                    computerWaits -= 1
                    print("Komputer stoi jeszcze ", computerWaits, " kolejek")
                break
    if get:
        if 5 < x < 125 and 5 < y < 65:
            if que != 0:
                takeCard("Player")
                playerWaits = que
                que = 0
            if fight != 0:
                while fight != 0:
                    takeCard("Player")
                    fight -= 1
            else:
                takeCard("Player")
            turn = "Computer"


def chooseCardToPick():
    global colorChange, turnsLeft, askFigure, turn, playerWaits, fight, que, computerWaits
    get = 1
    ex = 0

    for card in ranCardsComputer:
        if colorChange is None:  # Jesli nie ma na rządaniu koloru
            if askFigure is None:
                # Jesli karta na stole nie jest waleczna
                if not boardCards or (fight == 0 and que == 0):
                    if card.figure == 'Q':
                        putCardOnTable(card, "Computer")
                        ex = 1
                    elif not boardCards or boardCards[len(boardCards) - 1].figure == 'Q':
                        putCardOnTable(card, "Computer")
                        if card.figure == 'A':
                            changeColor("Computer")
                        elif card.figure == 'J':
                            figureAsk("Computer")
                        ex = 1
                    elif not boardCards or (card.figure == boardCards[len(boardCards) - 1].figure or card.color == boardCards[len(boardCards) - 1].color):
                        putCardOnTable(card, "Computer")
                        if card.figure == 'A':
                            changeColor("Computer")
                        elif card.figure == 'J':
                            figureAsk("Computer")
                        ex = 1
                # Jesli na stole jest waleczna
                else:
                    if not boardCards or (card.figure == boardCards[len(boardCards) - 1].figure or card.color == boardCards[len(boardCards) - 1].color):
                        if card.figure in ['2', '3', 'K'] and que == 0:
                            putCardOnTable(card, "Computer")
                            if card.figure == '2':
                                fight += 2
                            elif card.figure == '3':
                                fight += 3
                            elif card.figure == 'K':
                                fight += 5
                            ex = 1
                        elif card.figure == '4' and fight == 0:
                            putCardOnTable(card, "Computer")
                            que += 1
                            ex = 1

            elif card.figure == askFigure or card.figure == 'J' or card.figure == 'Q':
                putCardOnTable(card, "Computer")
                if turnsLeft == 0:
                    askFigure = None
                    print("Koniec rządania")
                else:
                    turnsLeft -= 1
                if card.figure == 'J':
                    figureAsk("Computer")
                ex = 1

        elif card.color == colorChange or card.figure == 'A' or card.figure == 'Q':
            putCardOnTable(card, "Computer")
            if turnsLeft == 0:
                colorChange = None
                print("Koniec rządania")
            else:
                turnsLeft -= 1
            if card.figure == 'A':
                changeColor("Computer")
            ex = 1

        if ex == 1:
            get = 0
            if playerWaits == 0:
                turn = "Player"
            else:
                playerWaits -= 1
                print("Gracz stoi jeszcze ", playerWaits, " kolejek")
            break
    if get:
        if que != 0:
            takeCard("Computer")
            computerWaits = que
            que = 0
        if fight != 0:
            while fight != 0:
                takeCard("Computer")
                fight -= 1
        else:
            takeCard("Computer")
        turn = "Player"


while a:

    if turn == "Computer" and computerWaits == 0:
        chooseCardToPick()
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

    board.draw(SCREEN)
    pygame.display.update()
