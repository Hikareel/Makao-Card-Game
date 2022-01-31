from random import random
from Cards import *


class Game:
    def __init__(self):
        self.start = True
        self.turn = "Player"
        self.askFigure = None
        self.colorChange = None
        self.fight = 0
        self.que = 0
        self.turnsLeft = 0
        self.playerWaits = 0
        self.computerWaits = 0

    def putCardOnTable(self, card, who):
        if who == "Player":
            ranCardsPlayer.remove(card)
        elif who == "Computer":
            ranCardsComputer.remove(card)
        card.pos_x = 0
        card.pos_y = 0
        card.state = "Deck"
        boardCards.append(card)


    def changeColor(self, who):
        b = 1
        if who == "Computer":
            a = random.randint(0, 3)
            self.colorChange = colors[a]
        elif who == "Player":
            while b:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:
                            self.colorChange = 'S'
                            b = 0
                        if event.key == pygame.K_c:
                            self.colorChange = 'C'
                            b = 0
                        if event.key == pygame.K_d:
                            self.colorChange = 'D'
                            b = 0
                        if event.key == pygame.K_h:
                            self.colorChange = 'H'
                            b = 0
        self.turnsLeft = 2
        print(who, " zmienia kolor na: ", self.colorChange)


    def figureAsk(self, who):
        b = 1
        if who == "Computer":
            a = random.randint(3, 8)
            self.askFigure = figures[a]
        elif who == "Player":
            while b:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_5:
                            self.askFigure = '5'
                            b = 0
                        if event.key == pygame.K_6:
                            self.askFigure = '6'
                            b = 0
                        if event.key == pygame.K_7:
                            self.askFigure = '7'
                            b = 0
                        if event.key == pygame.K_8:
                            self.askFigure = '8'
                            b = 0
                        if event.key == pygame.K_9:
                            self.askFigure = '9'
                            b = 0
                        if event.key == pygame.K_0:
                            self.askFigure = '10'
                            b = 0
        self.turnsLeft = 2
        print(who, " rząda: ", self.askFigure)


    def pickCard(self):
        get = 1
        ex = 0
        cardWidth = CARD_WIDTH / (len(ranCardsPlayer) / 3)
        cardHeight = CARD_HEIGHT / (len(ranCardsPlayer) / 3)
        pos = pygame.mouse.get_pos()
        x, y = pos

        for card in ranCardsPlayer:
            if card.pos_x < x < card.pos_x + cardWidth and card.pos_y < y < card.pos_y + cardHeight:
                if self.colorChange is None:  # Jesli nie ma na rządaniu koloru
                    if self.askFigure is None:
                        # Jesli karta na stole nie jest waleczna
                        if not boardCards or (self.fight == 0 and self.que == 0):
                            if card.figure == 'Q':
                                #self.putCardOnTable(card, "Player")
                                ex = 1
                            if not boardCards or boardCards[len(boardCards) - 1].figure == 'Q':
                                #self.putCardOnTable(card, "Player")
                                if card.figure == 'A':
                                    self.changeColor("Player")
                                elif card.figure == 'J':
                                    self.figureAsk("Player")
                                ex = 1
                            if not boardCards or (card.figure == boardCards[len(boardCards) - 1].figure or card.color == boardCards[len(boardCards) - 1].color):
                                #self.putCardOnTable(card, "Player")
                                if card.figure == 'A':
                                    self.changeColor("Player")
                                elif card.figure == 'J':
                                    self.figureAsk("Player")
                                ex = 1
                            if not boardCards or ((card.figure in ['2', '3'] or (card.figure == 'K' and card.color in ['H', 'S'])) and (card.figure == boardCards[len(boardCards) - 1].figure or card.color == boardCards[len(boardCards) - 1].color)):
                                #self.putCardOnTable(card, "Player")
                                if card.figure == '2':
                                    self.fight += 2
                                elif card.figure == '3':
                                    self.fight += 3
                                elif card.figure == 'K':
                                    self.fight += 5
                                ex = 1
                            if not boardCards or (card.figure == '4' and (card.figure == boardCards[len(boardCards) - 1].figure or card.color == boardCards[len(boardCards) - 1].color)):
                                #self.putCardOnTable(card, "Player")
                                self.que += 1
                                ex = 1
                        # Jesli na stole jest waleczna
                        else:
                            if not boardCards or (card.figure == boardCards[len(boardCards) - 1].figure or card.color == boardCards[len(boardCards) - 1].color):
                                if (card.figure in ['2', '3'] or (card.figure == 'K' and card.color in ['H', 'S'])) and self.fight != 0:
                                    #self.putCardOnTable(card, "Player")
                                    if card.figure == '2':
                                        self.fight += 2
                                    elif card.figure == '3':
                                        self.fight += 3
                                    elif card.figure == 'K':
                                        self.fight += 5
                                    ex = 1
                                elif card.figure == '4' and self.que != 0:
                                    #self.putCardOnTable(card, "Player")
                                    self.que += 1
                                    ex = 1

                    elif card.figure == self.askFigure or card.figure == 'J' or card.figure == 'Q':
                        #self.putCardOnTable(card, "Player")
                        self.turnsLeft -= 1
                        if self.turnsLeft == 0:
                            self.askFigure = None
                            print("Koniec rządania")
                        if card.figure == 'J':
                            self.figureAsk("Player")
                        ex = 1

                elif card.color == self.colorChange or card.figure == 'A' or card.figure == 'Q':
                    #self.putCardOnTable(card, "Player")
                    self.turnsLeft -= 1
                    if self.turnsLeft == 0:
                        self.colorChange = None
                        print("Koniec rządania")
                    if card.figure == 'A':
                        self.changeColor("Player")
                    ex = 1

                if ex == 1:
                    get = 0
                    ranCardsPlayer.remove(card)
                    card.pos_x = 0
                    card.pos_y = 0
                    card.state = "Deck"
                    boardCards.append(card)
                    if self.computerWaits <= 1:
                        self.computerWaits = 0
                        self.turn = "Computer"
                    else:
                        self.computerWaits -= 1
                        print("Komputer stoi jeszcze ", self.computerWaits, " kolejek")
                    break
        if get:
            if 5 < x < 125 and 5 < y < 65:
                if self.que > 0:
                    #self.takeCard("Player")
                    a = random.randint(0, 51)
                    while cards[a].state != "Deck":
                        a = random.randint(0, 51)
                    ranCardsPlayer.append(cards[a])
                    cards[a].state = "Player"
                    self.playerWaits = self.que
                    self.que = 0
                elif self.fight > 0:
                    while self.fight > 0:
                        #self.takeCard("Player")
                        a = random.randint(0, 51)
                        while cards[a].state != "Deck":
                            a = random.randint(0, 51)
                        ranCardsPlayer.append(cards[a])
                        cards[a].state = "Player"
                        self.fight -= 1
                else:
                    #self.takeCard("Player")
                    a = random.randint(0, 51)
                    while cards[a].state != "Deck":
                        a = random.randint(0, 51)
                    ranCardsPlayer.append(cards[a])
                    cards[a].state = "Player"
                self.turn = "Computer"


    def chooseCardToPick(self):
        get = 1
        ex = 0

        for card in ranCardsComputer:
            if self.colorChange is None:  # Jesli nie ma na rządaniu koloru
                if self.askFigure is None:
                    # Jesli karta na stole nie jest waleczna
                    if self.fight == 0 and self.que == 0:
                        if card.figure == 'Q':
                            #self.putCardOnTable(card, "Computer")
                            ex = 1
                        if not boardCards or boardCards[len(boardCards) - 1].figure == 'Q':
                            #self.putCardOnTable(card, "Computer")
                            if card.figure == 'A':
                                self.changeColor("Computer")
                            elif card.figure == 'J':
                                self.figureAsk("Computer")
                            ex = 1
                        if not boardCards or (card.figure == boardCards[len(boardCards) - 1].figure or card.color == boardCards[len(boardCards) - 1].color):
                            #self.putCardOnTable(card, "Computer")
                            if card.figure == 'A':
                                self.changeColor("Computer")
                            elif card.figure == 'J':
                                self.figureAsk("Computer")
                            ex = 1
                        if not boardCards or ((card.figure in ['2', '3'] or (card.figure == 'K' and card.color in ['H', 'S'])) and (card.figure == boardCards[len(boardCards) - 1].figure or card.color == boardCards[len(boardCards) - 1].color)):
                            #self.putCardOnTable(card, "Computer")
                            if card.figure == '2':
                                self.fight += 2
                            elif card.figure == '3':
                                self.fight += 3
                            elif card.figure == 'K':
                                self.fight += 5
                            ex = 1
                        if not boardCards or (card.figure == '4' and (card.figure == boardCards[len(boardCards) - 1].figure or card.color == boardCards[len(boardCards) - 1].color)):
                            #self.putCardOnTable(card, "Computer")
                            self.que += 1
                            ex = 1
                    # Jesli na stole jest waleczna
                    else:
                        if not boardCards or (card.figure == boardCards[len(boardCards) - 1].figure or card.color == boardCards[len(boardCards) - 1].color):
                            if (card.figure in ['2', '3'] or (card.figure == 'K' and card.color in ['H', 'S'])) and self.fight != 0:
                                #self.putCardOnTable(card, "Computer")
                                if card.figure == '2':
                                    self.fight += 2
                                elif card.figure == '3':
                                    self.fight += 3
                                elif card.figure == 'K':
                                    self.fight += 5
                                ex = 1
                            elif card.figure == '4' and self.que != 0:
                                #self.putCardOnTable(card, "Computer")
                                self.que += 1
                                ex = 1

                elif card.figure == self.askFigure or card.figure == 'J' or card.figure == 'Q':
                    #self.putCardOnTable(card, "Computer")
                    self.turnsLeft -= 1
                    if self.turnsLeft == 0:
                        self.askFigure = None
                        print("Koniec rządania")
                    if card.figure == 'J':
                        self.figureAsk("Computer")
                    ex = 1

            elif card.color == self.colorChange or card.figure == 'A' or card.figure == 'Q':
                #self.putCardOnTable(card, "Computer")
                self.turnsLeft -= 1
                if self.turnsLeft == 0:
                    self.colorChange = None
                    print("Koniec rządania")
                if card.figure == 'A':
                    self.changeColor("Computer")
                ex = 1

            if ex == 1:
                get = 0
                ranCardsComputer.remove(card)
                card.pos_x = 0
                card.pos_y = 0
                card.state = "Deck"
                boardCards.append(card)
                if self.playerWaits <= 1:
                    self.playerWaits = 0
                    self.turn = "Player"
                else:
                    self.playerWaits -= 1
                    print("Gracz stoi jeszcze ", self.playerWaits, " kolejek")
                break
        if get:
            if self.que > 0:
                #self.takeCard("Computer")
                a = random.randint(0, 51)
                while cards[a].state != "Deck":
                    a = random.randint(0, 51)
                ranCardsComputer.append(cards[a])
                cards[a].state = "Computer"
                self.computerWaits = self.que
                self.que = 0
            elif self.fight > 0:
                while self.fight > 0:
                    #self.takeCard("Computer")
                    a = random.randint(0, 51)
                    while cards[a].state != "Deck":
                        a = random.randint(0, 51)
                    ranCardsComputer.append(cards[a])
                    cards[a].state = "Computer"
                    self.fight -= 1
            else:
                #self.takeCard("Computer")
                a = random.randint(0, 51)
                while cards[a].state != "Deck":
                    a = random.randint(0, 51)
                ranCardsComputer.append(cards[a])
                cards[a].state = "Computer"
            self.turn = "Player"
