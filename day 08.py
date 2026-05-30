Participants = ["Jen","Alex","Tina","Joe","Ben"]
position = 1 
for name in Participants:
    if name == "Tina":
        print("About to break")
    break
    print("About to increment")
    position += 1
print(position)

for index in range(len(Participants)):
    print(index)
    if Participants[index] == "Joe":
        print("Have Breaked")
    break
    print("Not breaked")

for number in range(10):
    if number%3 == 0:
        print(number)
        print("Divisible by 3")
        continue
    print("Not Divisible by 3")
