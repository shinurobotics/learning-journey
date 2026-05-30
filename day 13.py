#File.close() -> close the file after using it

VacationSpots = ["London","Paris","New York","Utah","Icelands"]
VacationFile = open("VacationPlaces","w")
for Spots in VacationSpots:
    VacationFile.write(Spots + "\n")
VacationFile.close()

VacationFile = open("VacationPlaces","r")
TheWholeFile = VacationFile.read()
print(TheWholeFile)
VacationFile.close()

Firstline = VacationFile.readline()
print(Firstline)
Secondline = VacationFile.readline()
print(Secondline,end = "")
for line in VacationFile:
    print(line, end = "")
VacationFile.close()

FinalSpot = "Thailand"
VacationFile = open("VacationPlaces","a")
VacationFile.write(FinalSpot)
VacationFile.close()
VacationFile = open("VacationPlaces","r")
TheWholeFile = VacationFile.read()
print(TheWholeFile)
VacationFile.close()
