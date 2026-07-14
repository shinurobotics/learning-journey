fruits = ("Apple", "Banana", "Orange")
print(fruits)
print(fruits[0])
print(fruits[2])

fruits = ("Apple", "Banana", "Orange", "Mango")
print(fruits[1:3])
print("Banana" in fruits)

countries = ("Malaysia", "Singapore", "Thailand")
for country in countries:
    print(country)
print(len(countries))
print(countries.index("Singapore"))

countries = ("Malaysia", "Singapore", "Malaysia", "Thailand")
print(countries.count("Malaysia"))

student = ("Visnu", 19, "Malaysia")
print(student)
name, age, country = student
print(name)
print(age)
print(country)
studentList = list(student)
print(studentList)

studentList = ["Visnu", 19, "Malaysia"]
student = tuple(studentList)
print(student)

numbers = (1, 2, 3)
moreNumbers = (4, 5)
result = numbers + moreNumbers
print(result)

numbers = (1, 2)
print(numbers * 3)

numbers = (10, 20, 30, 40)
print(numbers[::-1])
for i in range(len(numbers)):
    print(f"Index {i}: {numbers[i]}")
