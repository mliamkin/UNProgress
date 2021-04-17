class Country:
    def __init__(self, nameOfCountry, leftNode, rightNode, grossDomestic, unemployedCash, vulnerableCash, moderateFood, severeFood, smallScaleAg, notSmallScaleAg, stuntingChildren, wastingChildren, overweightChildren, hivIncidence, tropicalDiseases, marriedBefore15, marriedBefore18, womensHealth, contraceptionUse, noSex, sexHealthRights, handwashingFac, levelOfWaterStress, veryLowWater, lowWater, mediumLowWater, mediumHighWater, highWater, veryHighWater, popCleanCooks, popIncrease, realGDP2018, realGDP2019, informalAg, informalNonAg, unemploymentYouth, unemploymentAdult, unemploymentTotal, researchExpends2010, researchExpends2017, resourceFlow2015, resourceFlow2018, govMetCriteria, changeInSlumPop00_14, changeInSlumPop14_18, highCapSys, lowCapSys, shareOfAccess, builtUpArea2000, builtUpArea2015, openPublicSpaces2019, foodLost, marineProtect2010, marineProtect2015, marineProtect2019, noNationalT, noProgressT, progressT, onTrackT, homicide15_18, homicide19_30, prisonOverCaps100_119, prisonOverCaps120_149, prisonOverCaps150, developAssitance14_16, developAssitance15_17):
        self.nameOfCountry = nameOfCountry
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.grossDomestic = grossDomestic
        #GOAL 1
        self.unemployedCash = unemployedCash #Social Protection Coverages for Unemployed (%) 
        self.vulnerableCash = vulnerableCash #For Vulnerable (%) 
        #GOAL 2
        self.moderateFood = moderateFood #Moderate Food Insecurity (%) 
        self.severeFood = severeFood #Severe Food Insecutiy (%) 
        self.smallScaleAg = smallScaleAg #Average Annual Income from Agriculture, for Small-Scale ($ in thousands)
        self.notSmallScaleAg = notSmallScaleAg #for Non-Small-Scale Producers ($ in thousands)
        self.stuntingChildren = stuntingChildren #Children under 5 years who are stunted (%)
        self.wastingChildren = wastingChildren #Children under 5 who are wasting (%)
        self.overweightChildren = overweightChildren #Children under 5 who are overweight (%)
        #GOAL 3
        self.hivIncidence = hivIncidence #HIV Incidence Rates (Ints)
        self.tropicalDiseases = tropicalDiseases #Proportion of People requiring interventions against tropical diseases (Ints)
        #GOAL 5
        self.marriedBefore15 = marriedBefore15 #Women married before they were 15 yrs old (%)
        self.marriedBefore18 = marriedBefore18 #Women married after 15 but before 18 yrs old (%)
        self.womensHealth = womensHealth #Percent of Women who decide their own health care
        self.contraceptionUse = contraceptionUse #percent of women who decide their contraception use
        self.noSex = noSex #percent of women who decide to say no to sex
        self.sexHealthRights = sexHealthRights #percent of women who make decisions regarding sexual and reproductive health and rights
        #GOAL 6
        self.handwashingFac = handwashingFac #Proportion of population that have a handwashing station with soap and water (%)
        self.levelOfWaterStress = levelOfWaterStress #Level of Water Stress (%)
        self.veryLowWater = veryLowWater #Very Low integrated water resource management levels (%)
        self.lowWater = lowWater #Low integrated water resource management levels (%)
        self.mediumLowWater = mediumLowWater #Medium Low integrated water resource management levels (%)
        self.mediumHighWater = mediumHighWater #Medium High integrated water resource management levels (%)
        self.highWater = highWater #High integrated water resource management levels (%)
        self.veryHighWater = veryHighWater #Very High integrated water resource management levels (%)
        #GOAL 7
        self.popCleanCooks = popCleanCooks #Annual incremental increase in population with clean cooking solutions (millions of people)
        self.popIncrease = popIncrease #Annual incremental increase in population (millions of people
        #GOAL 8
        self.realGDP2018 = realGDP2018 #Annual growth rate of real GDP per employed person (%)
        self.realGDP2019 = realGDP2019 #Same but in 2019
        self.informalAg = informalAg #Proportion of informal employment in the agricultural sector in 2016 (%)
        self.informalNonAg = informalNonAg #same but in the non-agricultural sectors
        self.unemploymentYouth = unemploymentYouth #Unemployment rate for youth, 2019 (%)
        self.unemploymentAdult = unemploymentAdult #Unemployment rate for adults, 2019
        self.unemploymentTotal = unemploymentTotal #Unemployment rate total, 2019
        #GOAL 9
        self.researchExpends2010 = researchExpends2010 #Research and development expenditures as proportion of GDP, 2010 (%)
        self.researchExpends2017 = researchExpends2017 #same but in 2017
        #GOAL 10
        self.resourceFlow2015 = resourceFlow2015 #Total resource flows for development to developing countries by region of recipient in 2015 (billions of dollars)
        self.resourceFlow2018 = resourceFlow2018 #Same as above but in 2018
        self.govMetCriteria = govMetCriteria #Percent of governments in the a region that report meeting the critera for having a set of policy measures to facilitate migration, 2019
        #GOAL 11
        self.changeInSlumPop00_14 = changeInSlumPop00_14 #Changes of urban population living in slums, 2000-2014 (%)
        self.changeInSlumPop14_18 = changeInSlumPop14_18 #Same, 2014-2018
        self.highCapSys = highCapSys #Access to high capacity public transport system 1000m, 2019 (%)
        self.lowCapSys = lowCapSys #Access to low capacity public transport system 500m, 2019 (%)
        self.shareOfAccess = shareOfAccess #Share of urban population with access to public transport, 2019 (%)
        self.builtUpArea2000 = builtUpArea2000 #Built up area per capita, 2000 (square meters per person)
        self.builtUpArea2015 = builtUpArea2015 #Same, 2015
        self.openPublicSpaces2019 = openPublicSpaces2019 #Proportion of pop within 400m walking distance to open public spaces, 2019 (%)
        #GOAL 12
        self.foodLost = foodLost #Proportion of food lost in 2016 (%)
        #GOAL 14
        self.marineProtect2010 = marineProtect2010 #Mean percent of each marine key biodiversity covered by protected areas, 2010 (%)
        self.marineProtect2015 = marineProtect2015 #Same in 2015
        self.marineProtect2019 = marineProtect2019 #Same in 2019
        #Additional data in the report detailing fish stocks in bio sustainable levels, only for Seas and Oceans not countries or landmasses
        #GOAL 15
        self.noNationalT = noNationalT #Num of countires in a region that do not have a national target with Aichi Biodiversity Target 2, 2011-2020 
        self.noProgressT = noProgressT #Same but for countries that have made no progress or are moving away from target
        self.progressT = progressT #Same but for countries that are making progress but is insufficient
        self.onTrackT = onTrackT #Same but for countries who are on target or will exceed target goal
        #GOAL 16
        self.homicide15_18 = homicide15_18 #Change in intentional homicide rates, 2015-2018 (%)
        self.homicide19_30 = homicide19_30 #Same but with projected rates, 2019-2030 (%)
        self.prisonOverCaps100_119 = prisonOverCaps100_119 #Proportion of countries where prisoners outnumber prison caps, 100-119 (%)
        self.prisonOverCaps120_149 = prisonOverCaps120_149 #Same but 120-149
        self.prisonOverCaps150 = prisonOverCaps150 #Same but 150 and over
        #GOAl 17
        self.developAssitance14_16 = developAssitance14_16 #Total developmental assitance to statistical capacity-building activities, 2014-2016 (millions of dollars)
        self.developAssitance15_17 = developAssitance15_17 #Same but, 2015-2017