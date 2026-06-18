from random import randint
#randint(a,b) -> a <= N <= b
randVal = randint(0,100)
Number_of_turns = 1

while(True):
    guess = int(input("Please enter your guess: "))
    if guess == randVal:
        break
    elif guess < randVal:
        print("Higher than than the number you guessed")
        Number_of_turns += 1
    else:
        print("Lesser than than the number you guessed")
        Number_of_turns += 1

if Number_of_turns == 1:
    print("You took",Number_of_turns,"turn","to guess it correctly")
    print("Luck was on your side")
else:
    print("You took",Number_of_turns,"turns","to guess it correctly")
