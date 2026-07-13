numbers = [10,20,30,40,50,60]
print(numbers[:3])
print(numbers[-3:])
print(numbers[2:5])
print(numbers[::2])

phone = ["Apple","Samsung","Oppo","Huawei","Redmi"]
print(phone[::-1])
copyphone = phone[3:5]
print(copyphone)

marks = [35,69,78,54]
copymarks = marks[:]
copymarks[0] = 80
print("Original:",marks)
print("Edited:",copymarks)

age = [19,47,88,65,78]
age[1:3] = [25,32]
print(age)
del age[-1:]
print(age)
