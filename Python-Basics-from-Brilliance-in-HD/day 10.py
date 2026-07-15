# Example 1: Simple Function
def greet():
    print("Hello, World!")
greet()

# Example 2: Function with One Parameter
def greet(name):
    print("Hello,", name)
greet("Visnu")

# Example 3: Function with Two Parameters
def add(a, b):
    print(a + b)
add(10, 20)

# Example 4: Function Returning a Value
def square(number):
    return number ** 2
result = square(5)
print(result)

# Example 5: Function with User Input
def welcome():
    name = input("Enter your name: ")
    print("Welcome,", name)
welcome()

# Example 6: Function to Find Maximum
def maximum(a, b):
    if a > b:
        return a
    else:
        return b
print(maximum(15, 20))

# Example 7: Function with Default Parameter
def greet(name="Guest"):
    print("Hello,", name)
greet()
greet("John")

# Example 8: Check Even or Odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(12))

# Example 9: Find Factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))

# Example 10: Count Vowels
def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count
print(count_vowels("Programming"))

# Example 11: Function Returning Multiple Values
def calculation(a, b):
    return a + b, a - b
sum_result, difference = calculation(20, 10)
print(sum_result)
print(difference)

# Example 12: Function Calling Another Function
def greet():
    print("Hello!")
def goodbye():
    print("Goodbye!")
def message():
    greet()
    goodbye()
message()

# Example 13: Calculate Area of Rectangle
def rectangle_area(length, width):
    return length * width
print(rectangle_area(8, 5))

# Example 14: Check Voting Eligibility
def can_vote(age):
    if age >= 18:
        return True
    return False
print(can_vote(20))

# Example 15: Print a Multiplication Table
def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
multiplication_table(5)

# Example 16: Recursive Function
def countdown(number):
    if number == 0:
        print("Blast Off!")
    else:
        print(number)
        countdown(number - 1)
countdown(5)
