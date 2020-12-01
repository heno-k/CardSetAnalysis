from DraftDecks.ColorSet import ColorSet,ColorSetIdx
from DraftDecks.BoosterCard import BoosterCard
import json
import os.path
from os import path
from CreateDraftSetJson import *
from AddHeadersToXcel import *
import xlwt
from xlwt import Workbook

#######################INITIALIZE VARIABLES##############################
SetCode =  "KLR"
FileType = ".json"
FilePath = "C:\\Users\\Henok\\source\\repos\\\CardSetAnalysis\\DraftDecks\\JSON\\" 
File = FilePath + SetCode + FileType
SetNames = {
    "ZNR": "Zendikar Rising",
    "KLR": "Kaladesh Remastered"
    }

##################RETRIEVE JSON FILE OF CARDS IN SET#######################
if(not path.exists(File)):
    CreateDraftSetJson(SetCode, File)

###############GATHERING CARDS FOR ANALYSIS OF SET########################
print("Gathering Data for the Set: %s" % SetNames[SetCode])
 
with open(File) as data_file:
    SetJson = json.load(data_file)

CardSet = []
for idx in ColorSetIdx:
    CardSet.append(ColorSet())

for cardJson in SetJson:
    # Sometimes a few fields are not specified in the Json pulled using Scryfall api
    # So populate with array with initalized values if not available. Otherwise use values
    # from Json if it is available
    BuggyField = ['mana_cost', 'oracle_text','power', 'toughness']
    #Fixed Field index corresponds to the field that may be potentially missing with respects to the order of BuggyField
    FixedField = [0] * 4

    for i in range(0, len(BuggyField)):
        if(BuggyField[i] in cardJson):
            FixedField[i] = cardJson[BuggyField[i]]
            #Edge cases for variable power/toughness... will treat as 0 since it is conditional
            if((i == 2 or i ==3 ) and FixedField[i] == '*'):
                FixedField[i] = '0'
            #If a power/toughness has a + in it, then treat it as the value preceding the +
            if((i == 2 or i ==3 ) and '+' in FixedField[i]):
                split = list(FixedField[i])
                FixedField[i] = split[0]



    #C reate booster card object
    card = BoosterCard(cardJson['name'], FixedField[0], cardJson['cmc'], cardJson['type_line'], FixedField[1], 
                        int(FixedField[2]), int(FixedField[3]), cardJson['collector_number'],cardJson['color_identity'],
                        cardJson['rarity'],cardJson['layout'])

    # Not including multi color cards or dual faced cards in statistics... easy to analyze since there aren't many of them
    ColorIdentityMap = {
    'U': ColorSetIdx.BLUE.value,
    'B': ColorSetIdx.BLACK.value,
    'G': ColorSetIdx.GREEN.value,
    'R': ColorSetIdx.RED.value,
    'W': ColorSetIdx.WHITE.value,
    }

    #Add neutral cards
    if(len(card.ColorIdentity) == 0):
        idx = ColorSetIdx.NEUTRAL.value
        CardSet[idx].AddCard(card)
    #Add mono-color cards
    elif(len(card.ColorIdentity) == 1):
        idx = ColorIdentityMap[card.ColorIdentity[0]]
        CardSet[idx].AddCard(card)
    #Add multi-color cards
    else:
        idx = ColorSetIdx.MULTI.value
        CardSet[idx].AddCard(card)


# Create an excel spreadsheet to save data to
wb = Workbook()

CMC_Sheet = wb.add_sheet('CMC')
Types_Sheet = wb.add_sheet('Types')
SubTypes_Sheet = wb.add_sheet('SubTypes')
Power_Sheet = wb.add_sheet('Power')
Toughness_Sheet = wb.add_sheet('Toughness')



########################ANALYZING SET#########################
#Print the distribution of CMC
print("Distribution of Converted Mana Cost")
AddHeadersToXcel(CMC_Sheet, 'CMC', [])
for idx in ColorSetIdx:
    print("%s Set CMC " % idx.name)
    CMC_Dist = CardSet[idx.value].PrintCMCDistribution()
    print(CMC_Dist)
    for i in range(0,len(CMC_Dist)):
            CMC_Sheet.write(i+1,idx.value+1,CMC_Dist[i])

#Print the distribution of Types
ListOfTypes = ["Lands","Creature","Enchantment","Artifact","Instant","Sorcery","Planeswalker"]
AddHeadersToXcel(Types_Sheet, 'Types', ListOfTypes)
print("\n\nTypes: %s" % ListOfTypes)
for idx in ColorSetIdx:
    print("%s Set Types " % idx.name)
    Types_Dist = CardSet[idx.value].DistributionOfTypes()
    print(Types_Dist)
    for i in range(0,len(Types_Dist)):
        Types_Sheet.write(i+1,idx.value+1,Types_Dist[i])


# Print the distribution of subtypes for each color
ListOfSubTypes = ["Warrior", "Wizard", "Cleric", "Rogue"]
AddHeadersToXcel(SubTypes_Sheet, 'SubTypes', ListOfSubTypes)
print("\n\nTypes: %s" % ListOfSubTypes)
for idx in ColorSetIdx:
    print("%s Set SubTypes " % idx.name)
    SubTypes_Dist = CardSet[idx.value].DistributionOfSubTypes(ListOfSubTypes)
    print(SubTypes_Dist)
    for i in range(0,len(SubTypes_Dist)):
        SubTypes_Sheet.write(i+1,idx.value+1,SubTypes_Dist[i])

# Print the distribution of Power for each color
print("\n\nDistribution of Power")
AddHeadersToXcel(Power_Sheet, 'Power', [])
for idx in ColorSetIdx:
    print("%s Set Power " % idx.name)
    Power_Dist = CardSet[idx.value].DistributionOfCreaturePower()
    print(Power_Dist)
    for i in range(0,len(Power_Dist)):
        Power_Sheet.write(i+1,idx.value+1,Power_Dist[i])

# Print the distribution of Toughness for each color
print("\n\nDistribution of Toughness")
AddHeadersToXcel(Toughness_Sheet, 'Toughness', [])
for idx in ColorSetIdx:
    print("%s Set Toughness " % idx.name)
    Toughness_Dist = CardSet[idx.value].DistributionOfCreatureToughness()
    print(Toughness_Dist)
    for i in range(0,len(Toughness_Dist)):
        Toughness_Sheet.write(i+1,idx.value+1,Toughness_Dist[i])

print("\n\nFinished Analysis of Distributions")
XcelFileType = ".xls"
FilePath = "C:\\Users\\Henok\\source\\repos\\\CardSetAnalysis\\Analysis\\"
XcelFile = FilePath + SetCode + XcelFileType
wb.save(XcelFile)





