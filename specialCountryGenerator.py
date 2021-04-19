import time
from random import seed, random,randint

class specialCountryNode:
    def __init__ (self, nameOfCountry, data):
        self.nameOfCountry = nameOfCountry
        self.data = data

def specialCountryGenerator():
    seed(time.ctime())
    specialCountryList = []    
    
    for x in range(100000):
        
        specialCountryName = chr(randint(64, 91))
        
        for i in range(randint(0, 56)):
            specialCountryName = specialCountryName + chr(randint(97, 122))
        
        pHolder = 0.0
        while(pHolder < .394 or pHolder > .957):
            pHolder = float( int(random() * 1000) / 1000 )
                


        sC = specialCountryNode(specialCountryName, pHolder)
        specialCountryList.append(sC)

    return specialCountryList

if __name__ == "__main__":
    listOfSpecialCountries = specialCountryGenerator()
    print(len(listOfSpecialCountries))