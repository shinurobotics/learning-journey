# Sort a list alphabetically (A to Z)
VacPlaces = ["Thailand", "Malaysia", "Turkey", "Singapore"]
VacPlaces.sort()
print(VacPlaces)

# Reverse the current order of a list
Element = ["Oxygen", "Nitrogen", "Carbon", "Sodium"]
Element.reverse()
print(Element)

# Sort a list in reverse alphabetical order (Z to A)
Jobs = ["Doctor", "Lawyer", "Police", "Teacher"]
Jobs.sort(reverse=True)
# reverse=True  -> Z to A (descending)
# reverse=False -> A to Z (ascending)
print(Jobs)

# Sort numbers in ascending order, then reverse them
Marks = [45, 98, 87, 53, 76]
Marks.sort()
print("Ascending:", Marks)
Marks.reverse()
print("Descending:", Marks)

# Find the minimum, maximum and average
age = [11, 31, 52, 98, 46]
print("Minimum:", min(age))
print("Maximum:", max(age))
averageAge = sum(age) / len(age)
print("Average:", averageAge)

# Using sorted() to create a new sorted list
scores = [78, 92, 45, 66, 89]
ascendingScores = sorted(scores)
descendingScores = sorted(scores, reverse=True)
print("Original:", scores)
print("Ascending:", ascendingScores)
print("Descending:", descendingScores)

# Sorting strings
fruits = ["Orange", "Apple", "Mango", "Banana"]
fruits.sort()
print(fruits)

# Reverse a string list
countries = ["Malaysia", "Thailand", "Singapore", "Japan"]
countries.reverse()
print(countries)

# Find highest and lowest marks
marks = [65, 80, 92, 55, 77]
highest = max(marks)
lowest = min(marks)
print("Highest:", highest)
print("Lowest:", lowest)

# Calculate the average marks
marks = [65, 80, 92, 55, 77]
average = sum(marks) / len(marks)
print("Average:", average)
