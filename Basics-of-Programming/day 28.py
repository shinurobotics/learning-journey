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
    def __init__(self,hand = [],money = 100):
        self.hand = hand
        self.score = 0 #"3 4" -> " 3 4 10"
                       # 7 -> 7 + 10
        self.score = self.setScore()
        print(self.score)
        self.money = money
    
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
            
Player1 = Player(["3","7","5"])               
print(Player1)
                
