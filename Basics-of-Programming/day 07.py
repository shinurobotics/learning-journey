#range(starting,stopping,steps)
Numbers = []
for num in range(10):
    Numbers.append(num)
    print(num)
print(Numbers)

Scores = []
for test in range(85,100,5):
    Scores.append(test)
print(Scores)

Temperature =[]
for tempo in range(0,-60,-15):
    Temperature.append(tempo)
    print(Temperature)

#while (condition):
#    action
#    action 1
#    action 2

counter = 1
Sum = 0
while (counter <= 10):
    Sum += counter
    counter += 1
    print(Sum)

Letters = ["a","b","c","d","e"]
Index = 0
while (Index < len(Letters)):
    print(Index)
    print(Letters[Index])
    Index += 1

height = 5000
velocity = 50 
time = 0 
distance = 0
while (height>0):
    time += 1
    distance = time*velocity
    height -= distance
    print(height)
