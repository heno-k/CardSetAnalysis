from enum import Enum
class ColorSet:
    def __init__(self):
        self.CardList = []
        self.NumCards = 0

    def AddCard(self, Card):
        self.CardList.append(Card)
        self.NumCards += 1


    def PrintCMCDistribution(self):
        Distribution = [0]*12
        for i in range(0,self.NumCards):
            Distribution[int(self.CardList[i].CMC)] += 1
        return Distribution  

    def PrintCardNamesInSet(self):
        for i in range(0,self.NumCards):
            print(self.CardList[i].CardName)

    def DistributionOfTypes(self):
        AllTypes = ["Land", "Creature", "Enchantment", "Artifact", "Instant", "Sorcery", "Planeswalker"]
        NumTypes = len(AllTypes)
        Distribution = [0] * NumTypes
        for i in range(0,self.NumCards):
            for j in range(0, NumTypes):
                if(AllTypes[j] in self.CardList[i].Type):
                    Distribution[j]+=1
                    continue
        return Distribution

    def DistributionOfSubTypes(self, ListOfSubTypes):
        NumSubTypes = len(ListOfSubTypes)
        Distribution = [0] * NumSubTypes
        for i in range(0,self.NumCards):
            if(len(self.CardList[i].SubType) is not 0):
                for j in range(0, NumSubTypes):
                    if(ListOfSubTypes[j] in self.CardList[i].SubType):
                        Distribution[j]+=1
                        continue
        return Distribution

    def DistributionOfCreatureToughness(self):
        #believe it or not, there is a card in ZNR that has 17 toughness lol
        Distribution = [0] * 18
        for i in range(0,self.NumCards):
            #Would prefer to treat modal_dfc cards as creatures, but no toughness or power given in Json
            if('Creature' in self.CardList[i].Type and not 'modal_dfc' in self.CardList[i].Layout):
                Distribution[self.CardList[i].Toughness] += 1
        return Distribution

    def DistributionOfCreaturePower(self):
        Distribution = [0] * 11
        for i in range(0,self.NumCards):
            #Would prefer to treat modal_dfc cards as creatures, but no toughness or power given in Json
            if('Creature' in self.CardList[i].Type and not 'modal_dfc' in self.CardList[i].Layout):
                Distribution[self.CardList[i].Power] += 1
        return Distribution

class ColorSetIdx(Enum):
    BLUE = 0
    BLACK = 1
    RED = 2
    GREEN = 3
    WHITE = 4
    NEUTRAL = 5
    MULTI = 6