from random import shuffle

def createDeck():
    Deck = []
    FaceValue =["A","J","K","Q"]
    for i in range(4):
        for card in range(2,11):
            Deck.append(str(card))
        for card in FaceValue:
            Deck.append(card)
        shuffle(Deck)
    return Deck
    
class Player:
    def __init__(self,hand = [],money = 100):
        self.hand = hand
        self.score = 0 #"3 4" -> " 3 4 10"
                       # 7 -> 7 + 10
        self.score = self.setScore()
        self.money = money
        self.bet = 0
    
    def __str__(self):       #print(Player)
        currentHand = " "  #self.hand = ["A","10"]
                           #"A 10"
        for card in self.hand:
            currentHand += str(card) + " "
        finalstatus = currentHand + "score: " + str(self.score)
        #"A 10 2 4 score: 17"
        return finalstatus
    
    def setScore(self):
        faceCardsDict = {"A":11,"J":10,"K":10,"Q":10,"2":2,"3":3,"4":4,
        "5":5,"6":6,"7":7,"8":8,"9":9,"10":10}
        self.score = 0
        print(self.score)
        acecounter = 0
        for card in self.hand: #"10"
            self.score += faceCardsDict[card]
            if card == "A":
                acecounter += 1
            if self.score > 21 and acecounter != 0:
                self.score -= 10
                acecounter -= 1
        return self.score
    
    def hit(self,card):
        self.hand.append(card)
        self.score = self.setScore()
            
    def play(self,newHand):
        self.hand = newHand
        self.score = self.setScore()
    
    def betMoney(self,amount):    #Money 100, bet(20)
        self.money -= amount #Money 100 -> 80
        self.bet += amount   #Bet 0 -> 20
        
    def win(self,result):
        if result == True:
            if self.score == 21 and len(self.hand) == 2:
                self.money += 2.5*self.bet
                self.money += 2*self.bet
                self.bet = 0
            else:
                self.money += 2*self.bet
        else:
            self.bet = 0

def printHouse(House):
    for card in range(len(House.hand)):
        if card == 0:
            print("X",end = " ")
        elif card == len(House.hand) - 1:
            print(House.hand[card])
        else:
            print(House.hand[card],end = " ")

cardDeck = createDeck()
Firsthand = [cardDeck.pop(),cardDeck.pop()]
Secondhand = [cardDeck.pop(),cardDeck.pop()]
Player1 = Player(Firsthand)
House = Player(Secondhand)

while(True):
    Action = input("Do you want another card?:")
    if Action.lower() == "yes":
        Player1.hit(cardDeck.pop())
        print(Player1)
        printHouse(House)
    else:
        break
printHouse(House)
