#var = input("Message to the users")

#name = input("Please type your name: ")
#print(name)
#age = int(input("Please state your age: "))
#if age >= 0:
#    print(age)
#else:
#    print("invalid")
    
Scores = []
#diff
for i in range(5):
    currentscore = int(input("Please enter the score " + str(i+1) + ": "))
    Scores.append(currentscore)
    print("The score you entered:",currentscore) #same as the print("The score you entered:",str(currentscore)) - 1 
    #print("The score you entered was:\n",currentscore) vs print("The score you entered was:\n"+ str(currentscore)) ithu diff yenne antha num kizhe varum comapred with 1

print(Scores)

#diff when compared to above
for i in range(5):
    currentscore = float(input("Please enter the score " + str(i+1) + ": "))
    Scores.append(currentscore)
    if currentscore >= 60:
        print("The score you entered was:",currentscore,"nice")
    elif 0<= currentscore <60:
        print("The score you entered was:",currentscore,"more effort needed")
    else:
        print("The score you entered was:",currentscore,"invalid")

#int(input()) only accepts +ve or -ve whole number
#float(input()) accepts all the number
