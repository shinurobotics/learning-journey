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

OutputFile = open("ParticipantData.txt","r")
Wholefile = OutputFile.read()
print(Wholefile)
