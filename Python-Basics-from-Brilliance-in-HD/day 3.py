# 1 as True Value
# 0 as False Value
# Alternative True -> not False
# Alternative False -> not True

a,b = not False,not True
print(a)
print(b)

correctPassword = "Python123"
Password = input("Please type the password: ")
isCorrectPassword = Password == correctPassword
print(isCorrectPassword)

age = int(input("What is your age?"))
canVote = age >=18
if canVote:
    print(canVote)
    print("You are to eligible to vote")
else:
    print(canVote)
    print("You are not eligible to vote")
  
-----------------------------------------------------------------------------------
