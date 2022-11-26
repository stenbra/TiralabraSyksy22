import math

def GetClosestNeighbour(coordinate,numTable,wholeTable=False):
    if wholeTable:
        nearbyCoords = numTable
    else:
        nearbyCoords = GetNeighbouringCoordinateRange(coordinate)
    nearestCord=[]
    dist = 40
    for i in range(nearbyCoords[0][0],nearbyCoords[0][1]):
        for j in range(nearbyCoords[1][0],nearbyCoords[1][1]):
            if[i,j] in numTable:
                if not nearestCord:
                    nearestCord= [i,j]
                elif ((nearestCord[0]-coordinate[0])**2 +(nearestCord[1]-coordinate[1])**2)>((i-coordinate[0])**2 +(j-coordinate[1])**2):
                    nearestCord =[i,j]
    #print(str(coordinate) +" closest to: "+str(nearestCord))
    if nearestCord:
        dist = math.sqrt((nearestCord[0]-coordinate[0])**2+(nearestCord[1]-coordinate[1])**2)
    return dist

def GetNeighbouringCoordinateRange(coordinate):
    painThreshold=5
    cooordRange=[]
    for i in range(2):
        min =coordinate[i] - painThreshold
        max = coordinate[i]+painThreshold
        if(min<0):
            min=0
        if(max>27):
            max=27
        cooordRange.append([min,max])
    return cooordRange


def DistanceToNearesNeighbour(coordinate,numTable):
    if coordinate in numTable:
        return 0
    nearCord=GetClosestNeighbour(coordinate,numTable)
    if nearCord != 100:
        return nearCord
    # commented out since it slows the process, though and have not really found it more accurate
    #return GetClosestNeighbour(coordinate,numTable,True)

def CreatePixelBoolCoordinateTable(data,entryCap=0):
    entries=len(data)
    if entryCap!=0:
        entries = entryCap
    boolCordTable = [[0]]*entries
    for i in range(entries):
        ##TODO turn into dictionary perhaps
        boolTable=[]
        for j in range(28):
            for k in range(28):
                if data[i][j][k] > 73:
                    boolTable.append([j,k])
        boolCordTable[i]=boolTable
    return boolCordTable

def CreatePixelBoolCoordinateNumber(data):
    boolTable=[]
    for j in range(28):
        for k in range(28):
            if data[j][k] > 73:
                boolTable.append([j,k])
    return boolTable
    
## get a sorted list of numbers based on how close their pixels are to the given number
def ComparenNumberWithBoolCodrdinates(number,trainData):
    distList=[]
    for i in range(len(trainData)):
        dist=0
        for j in range(len(number)):
            dist += DistanceToNearesNeighbour(number[j],trainData[i])
        distList.append([dist,i])
    distList = sorted(distList, key=lambda x: x[0])
    return distList

## checking the what the majority of the neighbours are
def GetTheMajorityNeighbourNumber(datalist, labelData,neighbourCount=5):
    votelist =[]
    for i in range(neighbourCount):
        votelist.append(labelData[datalist[i][1]])
    #print(votelist)
    recognizedNumber=max(votelist,key=votelist.count)
    return recognizedNumber

## gets the precentage of incorrect guesses
def GetErrorPercentage(testData,trainData,testLabels,trainLabels,entries=100,trainEntries=1000):
    trainBoolTable=CreatePixelBoolCoordinateTable(trainData,trainEntries)
    testBoolTable=CreatePixelBoolCoordinateTable(testData,entries)
    correctRecognitions=0
    for i in range(len(testBoolTable)):
        distList= ComparenNumberWithBoolCodrdinates(testBoolTable[i],trainBoolTable)
        recognizedNumber= GetTheMajorityNeighbourNumber(distList,trainLabels,5)
        if testLabels[i]==recognizedNumber:
            correctRecognitions +=1
    return 1-correctRecognitions/entries
