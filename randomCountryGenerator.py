import time
from random import seed, random,randint

class Country:
    def __init__(self, nameOfCountry, povertyPct, hungerPct, healthPct, educationPct, genderEqualityPct, sanitationPct, cleanEnergyPct, economicGrowthPct, industrializationPct, reducedInequalityPct, sustainableCommunityPct, productionPct, climatePct, marineLifePct, lifeOnLandPct, justicePct, partnershipPct):
        self.nameOfCountry = nameOfCountry
        self.povertyPct = povertyPct        
        self.hungerPct = hungerPct
        self.healthPct = healthPct
        self.educationPct = educationPct
        self.genderEqualityPct = genderEqualityPct
        self.sanitationPct = sanitationPct
        self.cleanEnergyPct = cleanEnergyPct
        self.economicGrowthPct = economicGrowthPct
        self.industrializationPct = industrializationPct
        self.reducedInequalityPct = reducedInequalityPct
        self.sustainableCommunityPct = sustainableCommunityPct
        self.productionPct = productionPct
        self.climatePct = climatePct
        self.marineLifePct = marineLifePct
        self.lifeOnLandPct = lifeOnLandPct
        self.justicePct = justicePct
        self.partnershipPct = partnershipPct
        

def countryGenerator():
    seed(time.ctime())
    countryList = []
    #print(random())
    for x in range(100000):
        countryName = chr(randint(64, 91))
        
        for i in range(randint(0, 56)):
            countryName = countryName + chr(randint(97, 122))
            
        c1 = Country(countryName, float( int(random() * 100) / 100 ), float( int(random() * 100) / 100 ), 
        float( int(random() * 100) / 100 ), float( int(random() * 100) / 100 ), 
        float( int(random() * 100) / 100 ), float( int(random() * 100) / 100 ), 
        float( int(random() * 100) / 100 ), float( int(random() * 100) / 100 ), 
        float( int(random() * 100) / 100 ), float( int(random() * 100) / 100 ), 
        float( int(random() * 100) / 100 ), float( int(random() * 100) / 100 ), 
        float( int(random() * 100) / 100 ), float( int(random() * 100) / 100 ), 
        float( int(random() * 100) / 100 ), float( int(random() * 100) / 100 ), 
        float( int(random() * 100) / 100 ))     
    
        countryList.append(c1)
    
    return countryList
    '''
        print("Country: " + c1.nameOfCountry + "\n"
         +"Poverty Percentage: " +str(c1.povertyPct) + "%\n" 
         + "Hunger Percentage: " + str(c1.hungerPct) + "%\n" 
         + "Health Percentage: " + str(c1.healthPct) + "%\n" 
         + "Education Percentage: " + str(c1.educationPct) + "%\n" 
         + "Gender Equality Percentage: " + str(c1.genderEqualityPct) + "%\n" 
         + "Sanitation Percentage: " + str(c1.sanitationPct) + "%\n" 
         + "Clean Energy Percentage: " + str(c1.cleanEnergyPct) + "%\n"          
         + "Economic Growth Percentage: " + str(c1.economicGrowthPct) + "%\n"         
         + "Industrialization Percentage: " + str(c1.industrializationPct) + "%\n"
         + "Reduced Inequality Percentage: " + str(c1.reducedInequalityPct) + "%\n"
         + "Sustainable Community Percentage: " + str(c1.sustainableCommunityPct) + "%\n"
         + "Production Percentage: " + str(c1.productionPct) + "%\n"
         + "Climate Percentage: " + str(c1.climatePct) + "%\n"
         + "Marine Life Percentage: " + str(c1.marineLifePct) + "%\n"
         + "Life on Land Percentage: " + str(c1.lifeOnLandPct) + "%\n"
         + "Justice Percentage: " + str(c1.justicePct) + "%\n"
         + "Partnership Percentage: " + str(c1.partnershipPct) + "%\n")
     '''

if __name__ == "__main__":
    listOfCountries = countryGenerator()
    print(listOfCountries[0].nameOfCountry)