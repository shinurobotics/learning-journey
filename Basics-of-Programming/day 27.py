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
