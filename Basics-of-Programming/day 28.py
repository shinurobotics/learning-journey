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

cardDeck = createDeck()
print(cardDeck)

class Player:
    def _init_(self,hand = [],money = 100):
        self.hand = hand
        self.score = 0
        self.money = money
    
    def _str_(self):       #print(Player)
        currentHand = " "  #self.hand = ["A","10"]
                           #"A 10"
        for card in self.hand:
            currentHand += str(card) + " "
        finalstatus = currentHand + "score: " + str(self.score)
        #"A 10 2 4 score: 17"
        return finalstatus
    
    def setScore():
        faceCardsDict = {"A":11,"J":10,"K":10}
        for card in self.hand: #"10"
        if int(card) in range(2,11):
            self.score += int(card)
        elif card in faceCardsDict: #"A"
            self.score += faceCardsDict[]
