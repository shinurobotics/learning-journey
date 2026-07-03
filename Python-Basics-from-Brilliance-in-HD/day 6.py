# List
pet = ["dogs", "cats", "fish", "parrot"]
pet[2] = "squirrel"
pet[-1] = "hamster"
print(pet)

letters = ["A", "E", "K", "O", "M"]
letters[1:4] = ["z","i","b"]
print(letters)

fruits = ["Mango","Banana"]
fruits.insert(0,"Apple")
fruits.insert(2,"Kiwi")
print(fruits)
fruits.pop(1) # same as fruits.remove("Mango")
print(fruits)

marks = [55,85,90,40]
for i in range(len(marks)):
    marks[i] += 5
print(marks)

# Set
colours = {"Purple", "Red"}
colours.add("Green") #append() for lists , add() for sets
print(colours)
colours.discard("Purple")
#discard doesnt show the error if the 'set.discard(item)' item not in set
#remove wioll show the error if the 'set.remove(item)' item not in set
print(colours)

numbers = {1,2,3}
numbers.update({4,5}) #add() is for one element, update() is for multiple element
print(numbers)
numbers.clear()
print(numbers)
