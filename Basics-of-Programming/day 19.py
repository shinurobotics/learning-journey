ParticipantNumber = 2
ParticipantData = []
registeredParticipants = 0
OutputFile = open("ParticipantData.txt","w")

while (registeredParticipants < ParticipantNumber):
    tempPartData = [] #name,age,origin
    name = input("Please type your name:\n")
    tempPartData.append(name)
    age = int(input("Please type your age:\n"))
    tempPartData.append(age)
    country = input("Please type your origin country:\n")
    tempPartData.append(country)
    ParticipantData.append(tempPartData)
    registeredParticipants += 1
print(ParticipantData)

for participants in ParticipantData:
    for data in participants:
        OutputFile.write(str(data))
        OutputFile.write(" ")
    OutputFile.write("\n")
OutputFile.close()

InputFile = open("ParticipantData.txt","r")
InputList = []
for line in InputFile:
    tempParticipant = line.strip("\n").split()
    print(tempParticipant)
    InputList.append(tempParticipant)
    print(InputList)
     #"Ronaldo 41 Portugal \n".strip() -> "Ronaldo 41 Portugal"
     #"Ronaldo 41 Portugal".split() -> ["Ronaldo","41","Portugal"]

Age = {}
for part in InputList:
    tempAge = int(part[1])
    if tempAge in Age:
            Age[tempAge] += 1
    else:
        Age[tempAge] = 1
print(Age)

Oldest = 0
Youngest = 100
mostOccuringage = 0
counter = 0
for tempAge in Age:
    if tempAge > Oldest:
        Oldest = tempAge
    if tempAge < Youngest:
        Youngest = tempAge
    if Age[tempAge] >= counter:
        counter = Age[tempAge]
        mostOccuringage = tempAge
print(Oldest)
print(Youngest)
print("The most occuring age is:",mostOccuringage,"with",counter,"participants")

Country = {}
for part in InputList:
    tempCountry = part[-1]
    if tempCountry in Country:
            Country[tempCountry] += 1
    else:
        Country[tempCountry] = 1
print("Countries that attended:",Country)

InputFile.close()
