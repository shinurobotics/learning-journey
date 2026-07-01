first = "Hello"
second = "world!"
print(first)
print(second)
print(first,second) # same as print(first + " " + second)

to = "Hi"
print(to*3)

name = "Visnu"
print(len(name))

answer = "Biology"
Subject = "maths"
print(answer.lower())
print(Subject.upper())

text = " Python "
print(text.strip())

Sentence = "I love Python"
Words = print(Sentence.split())

Job = "Rngineer"
print(Job.replace("R","E"))
Job1 = "Doctor"
print(Job1.replace("Doctor","Nurse"))

Favouritesub = "I love to study Physics"
              # 0123456789.....
print(Favouritesub.find("love"))
print("Physics" in Favouritesub) # True if exists
print("You" in Favouritesub)     # False if don't exist
print(Favouritesub[0])
print(Favouritesub[5])
print(Favouritesub[-3])

Poster = "Be stemholic gaiss"
print(Poster[0:4])
print(Poster[8:])
print(Poster[-3:-1])

Country = "Portugal"
Champion = "World Cup"
print(f"I supports {Country}.")
print(f"It won the {Champion} 2026")
