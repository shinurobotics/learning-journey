from random import random
from time import time

randVal = random() # 0.0 <= N < 1.0
#print(randVal)

#time.time() -> timevalue
#time.time() -> timevalue 2

upper = 1.0
lower = 0.0

guess = 0.5
#guess = 0.5 -> Too Low -> lower = 0.5
#guess = 0.9 -> Too High -> upper = 0.9
starttime = time()
while(True):
    if guess == randVal:
        break
    elif guess < randVal:
        lower = guess
    else:
        upper = guess
    guess = (upper+lower)/2 # (0.5+0.9)/2 -> 0.7 
endtime = time()
print(guess)
print("It took us:",endtime-starttime,"seconds")
