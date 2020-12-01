import xlwt
from xlwt import Workbook
from DraftDecks.ColorSet import ColorSet,ColorSetIdx
from DraftDecks.BoosterCard import BoosterCard
##########PRINTS HEADERS TO XCEL SPREADSHEET##################
#List depends on distribtution
def AddHeadersToXcel(Sheet, Dist_Name, List):
    if('CMC' in Dist_Name):
        #Print Row Headers
        for i in range(0,12):
            RowHeader = "%d Mana" % i
            Sheet.write(i+1,0,RowHeader)

        #Print Col Headers
        for idx in ColorSetIdx:
            ColHeader = idx.name
            Sheet.write(0, idx.value+1, ColHeader)

    elif('Type' in Dist_Name):
        #Print Row Headers
        for i in range(0,len(List)):
            RowHeader = "%s" % List[i]
            Sheet.write(i+1,0,RowHeader)

        #Print Col Headers
        for idx in ColorSetIdx:
            ColHeader = idx.name
            Sheet.write(0, idx.value+1, ColHeader)    
    elif('SubType' in Dist_Name):
        #Print Row Headers
        for i in range(0,len(List)):
            RowHeader = "%s" % List[i]
            Sheet.write(i+1,0,RowHeader)

        #Print Col Headers
        for idx in ColorSetIdx:
            ColHeader = idx.name
            Sheet.write(0, idx.value+1, ColHeader)
    elif('Power' in Dist_Name):
        #Print Row Headers
        for i in range(0,11):
            RowHeader = "%d Power" % i
            Sheet.write(i+1,0,RowHeader)

        #Print Col Headers
        for idx in ColorSetIdx:
            ColHeader = idx.name
            Sheet.write(0, idx.value+1, ColHeader)
    elif('Toughness' in Dist_Name):
        #Print Row Headers
        #Up to 17 because ZNR has 1 card with 17 toughness...
        for i in range(0,18):
            RowHeader = "%d" % i
            Sheet.write(i+1,0,RowHeader)

        #Print Col Headers
        for idx in ColorSetIdx:
            ColHeader = idx.name
            Sheet.write(0, idx.value+1, ColHeader)