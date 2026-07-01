# Syntax like grammar in English

#Print statement
print("Hello, World!")

#Variables
name = "Visnu"
age = 19
print(name)
print(age)

#User input
name = input("Enter your name: ")
print("Hello,", name)

#If statement
age = 18
if age >= 18:
    print("Adult")

#If-else statement
number = 5
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#For loop
for i in range(5):
    print(i)

#Function
def greet():
    print("Welcome!")
print(greet())

#List
fruits = ["Apple", "Banana", "Orange"]
for fruit in fruits:
    print(fruit)
    
#Dictionary 
student = {"Name": "Visnu", "Age": 19}
print(student["Name"])

#Import Module
import random
print(random.randint(1, 10))

#Try-Except
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
