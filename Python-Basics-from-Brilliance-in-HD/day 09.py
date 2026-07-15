# Creating a tuple
fruits = ("Apple", "Banana", "Orange")
print(fruits)

# Accessing tuple elements
print(fruits[0])
print(fruits[2])

# Tuple slicing
fruits = ("Apple", "Banana", "Orange", "Mango")
print(fruits[1:3])

# Membership operator
print("Banana" in fruits)

# Looping through a tuple
countries = ("Malaysia", "Singapore", "Thailand")
for country in countries:
    print(country)

# Length of a tuple
print(len(countries))

# Finding the index of an element
print(countries.index("Singapore"))

# Counting occurrences
countries = ("Malaysia", "Singapore", "Malaysia", "Thailand")
print(countries.count("Malaysia"))

# Tuple packing
student = ("Visnu", 19, "Malaysia")
print(student)

# Tuple unpacking
name, age, country = student
print(name)
print(age)
print(country)

# Convert tuple to list
studentList = list(student)
print(studentList)

# Convert list to tuple
studentList = ["Visnu", 19, "Malaysia"]
student = tuple(studentList)
print(student)

# Concatenate tuples
numbers = (1, 2, 3)
moreNumbers = (4, 5)
result = numbers + moreNumbers
print(result)

# Repeat a tuple
numbers = (1, 2)
print(numbers * 3)

# Reverse a tuple using slicing
numbers = (10, 20, 30, 40)
print(numbers[::-1])

# Loop through a tuple using index
for i in range(len(numbers)):
    print(f"Index {i}: {numbers[i]}")
