animals = ["dog","cat","monkey"]
file = open("favanimals","w")
for pets in animals:
    file.write(pets + "\n")
file.close()

file = open("favanimals","r")
shop = file.read()
print(shop)
file.close

file = open("favanimals","r")
Firstline = file.readline()
print(Firstline, end = "")
Secondline = file.readline()
print(Secondline, end = "")
for line in file:
    print(line)
file.close()

lastanimal = "fish"
file = open("favanimals","a")
file.write(lastanimal)
file.close()

file = open("favanimals","r")
for line in file:
    print(line,end = "")
file.close()
