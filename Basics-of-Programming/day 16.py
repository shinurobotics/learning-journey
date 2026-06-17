Blackshoes = {"42":2,"41":3,"40":4,"39":1,"38":0}
while(True): #True == True
    purchaseSize = input("What is your preferred size?\n")
    Blackshoes[purchaseSize] -= 1
    if Blackshoes[purchaseSize] < 0:
        break
print(Blackshoes)

while(True): 
    purchaseSize = input("What is your preferred size?\n")
    Blackshoes[purchaseSize] -= 1
    if Blackshoes[purchaseSize] >= 0:
        print("Stock available")
    else:
        print("Stock not available")
        break
    
print(Blackshoes)
    
