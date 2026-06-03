#Sets ={"Element1", "Element2", "Element1", "Element4"}
#print(Sets)
#if "Element1" in Sets:
#    print("Yes")

Countrylist = []
for i in range(5):
    Country = input("Please type your country: ")
    Countrylist.append(Country)
    Countryset = set(Countrylist)
print(Countrylist)
print(Countryset)
if "India" in Countryset:
    print("attended")

#Dictionary = {"Key":"Value","Key2":"Value2","Key3":"Value3"}

CountryDictionary = {}
for Country in Countrylist:
    if Country in CountryDictionary:
        CountryDictionary[Country] += 1
    else:
        CountryDictionary[Country] = 1
print(CountryDictionary)
    
#Sets remove duplicate and output will be in random order
#Lists give the ouput according to order and dosent remove any duplicate
