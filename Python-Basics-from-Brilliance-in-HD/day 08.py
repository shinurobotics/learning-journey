# Create a list
numbers = [10, 20, 30, 40, 50, 60]

# First 3 elements
print(numbers[:3])

# Last 3 elements
print(numbers[-3:])

# Elements from index 2 to 4
print(numbers[2:5])

# Every second element
print(numbers[::2])

# Reverse a list using slicing
phone = ["Apple", "Samsung", "Oppo", "Huawei", "Redmi"]
print(phone[::-1])

# Copy part of a list
copyphone = phone[3:5]
print(copyphone)

# Copy an entire list using slicing
marks = [35, 69, 78, 54]
copymarks = marks[:]

# Modify the copied list
copymarks[0] = 80
print("Original:", marks)
print("Edited:", copymarks)

# Replace elements using slicing
age = [19, 47, 88, 65, 78]
age[1:3] = [25, 32]
print(age)

# Delete elements using slicing
del age[-1:]
print(age)
