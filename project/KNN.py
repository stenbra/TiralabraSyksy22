import math
from minheap import MinHeap
class Knn:
    ## Find the closest colered pixel coordinate to the given coordinate
    @staticmethod
    def GetClosestNeighbour(coordinate,numTable,precalcDist,searchRadius=2):
        dist = 40
        nearbyCoords = Knn.GetNeighbouringCoordinateRange(coordinate,searchRadius)

        for i in range(nearbyCoords[0][0],nearbyCoords[0][1]):
            for j in range(nearbyCoords[1][0],nearbyCoords[1][1]):
                if[i,j] in numTable:
                    cdist =precalcDist[coordinate[0]-i+searchRadius][coordinate[1]-j+searchRadius]
                    if cdist==1:
                        return 1
                    elif cdist<dist:
                        dist= cdist    
        return dist
    
    ## Definces which coordinates to search for around cordinate
    @staticmethod
    def GetNeighbouringCoordinateRange(coordinate,searchRadius=2):
        coordRange=[]
        for i in range(2):
            min =coordinate[i] - searchRadius
            max = coordinate[i]+searchRadius
            if(min<0):
                min=0
            if(max>28):
                max=28
            coordRange.append([min,max])
        return coordRange
    
    @staticmethod
    def PreCalulateDistanceToSurroundingNeighbours(searchRadius):
        distList = []
        for i in range(2*searchRadius+1):
            distListj=[]
            for j in range(2*searchRadius+1):
                distListj.append(math.sqrt((i-searchRadius)**2+(j-searchRadius)**2))
            distList.append(distListj)    
        return distList


    ## returns distance to nearest coolored coordinate 0 if they overlap
    @staticmethod
    def DistanceToNearesNeighbour(coordinate,numTable,precalcSR,precalcMax,searchRadius):
        if coordinate in numTable:
            return 0
        nearCord=Knn.GetClosestNeighbour(coordinate,numTable,precalcSR,searchRadius)
        if nearCord != 40:
            return nearCord
        return Knn.GetClosestNeighbour(coordinate,numTable,precalcMax,27)

    @staticmethod
    def CreatePixelBoolCoordinateTable(data,entryCap=0):
        entries=len(data)
        if entryCap!=0:
            entries = entryCap
        boolCordTable = [[0]]*entries
        for i in range(entries):
            boolCordTable[i]=Knn.CreatePixelBoolCoordinateNumber(data[i])
        return boolCordTable
    @staticmethod
    def CreatePixelBoolCoordinateNumber(data):
        boolTable=[]
        for j in range(28):
            for k in range(28):
                if data[j][k] > 73:
                    boolTable.append([j,k])
        return boolTable
        
    ## get a sorted list of numbers based on how close their pixels are to the given number
    @staticmethod
    def ComparenNumberWithBoolCodrdinates(number,trainData,searchRadius=2):
        distList=[]
        precalcDist = Knn.PreCalulateDistanceToSurroundingNeighbours(searchRadius)
        precalcDistAll = Knn.PreCalulateDistanceToSurroundingNeighbours(27)
        for i in range(len(trainData)):
            dist=0
            dist2=0
            for j in range(len(number)):
                dist += Knn.DistanceToNearesNeighbour(number[j],trainData[i],precalcDist,precalcDistAll,searchRadius)
            for j in range(len(trainData[i])):
                dist2 += Knn.DistanceToNearesNeighbour(trainData[i][j],number,precalcDist,precalcDistAll,searchRadius)
            distList.append([max(dist,dist2),i])

        #TODO Use heap
        distList = sorted(distList, key=lambda x: x[0])
        return distList

    ## checking the what the majority of the neighbours are
    @staticmethod
    def GetTheMajorityNeighbourNumber(datalist, labelData,neighbourCount=5):
        votelist =[]
        for i in range(neighbourCount):
            votelist.append(labelData[datalist[i][1]])
        #print(votelist)
        recognizedNumber=max(votelist,key=votelist.count)
        return recognizedNumber
    def GetTheMajorityNeighbourNumberData(datalist, labelData,trainData,neighbourCount=5):
        votelist =[]
        for i in range(neighbourCount):
            votelist.append([trainData[datalist[i][1]],labelData[datalist[i][1]]])
        return votelist

    ## gets the precentage of incorrect guesses
    @staticmethod
    def GetErrorPercentage(testData,trainData,testLabels,trainLabels,entries=10,trainEntries=1000,k=5):
        trainBoolTable=Knn.CreatePixelBoolCoordinateTable(trainData,trainEntries)
        testBoolTable=Knn.CreatePixelBoolCoordinateTable(testData,entries)
        correctRecognitions=0
        wrongGuesses=[]
        for i in range(entries):
            distList= Knn.ComparenNumberWithBoolCodrdinates(testBoolTable[i],trainBoolTable)
            recognizedNumber= Knn.GetTheMajorityNeighbourNumber(distList,trainLabels,k)
            if testLabels[i]==recognizedNumber:
                correctRecognitions +=1
            else:
                wrongGuesses.append([testData[i],testLabels[i],recognizedNumber])
                print(str(testLabels[i])+" =/= "+str(recognizedNumber)+" at index:"+str(i))
        return [(1-correctRecognitions/entries),wrongGuesses]
