#File = open("Filename","x")
# x can be r  for read
#          w  for write
#          a  for append
#          r+ for read + append
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

VacationFile = open("VacationPlaces","r")
Firstline = VacationFile.readline()
print(Firstline, end = "")
Secondline = VacationFile.readline()
print(Secondline,end = "")
for line in VacationFile:
    print(line, end = "")
VacationFile.close()

FinalSpot = "Thailand\n"
VacationFile = open("VacationPlaces","a")
VacationFile.write(FinalSpot)
VacationFile.close()
VacationFile = open("VacationPlaces","r")
for line in VacationFile:
    print(line,end = "")
    
VacationFile.close()

with open("VacationPlaces","r") as VacationFile:
    for line in VacationFile:
        print(line)
#automatically it closed
