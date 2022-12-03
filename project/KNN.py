
class Knn:
    ## Find the closest colered pixel coordinate to the given coordinate
    @staticmethod
    def GetClosestNeighbour(coordinate,numTable,wholeTable=False):
        #the whole search range thing does not seem efficient at the moment
        if wholeTable:
            nearbyCoords = Knn.GetNeighbouringCoordinateRange(coordinate,30)
        else:
            nearbyCoords = Knn.GetNeighbouringCoordinateRange(coordinate)
        nearestCord=[]
        dist = 40
        #TODO: optimize with a tabel using premade distances so the calculations are reduced
        for i in range(nearbyCoords[0][0],nearbyCoords[0][1]):
            for j in range(nearbyCoords[1][0],nearbyCoords[1][1]):
                if[i,j] in numTable:
                    if not nearestCord:
                        nearestCord= [i,j]
                    elif ((nearestCord[0]-coordinate[0])**2 +(nearestCord[1]-coordinate[1])**2)>((i-coordinate[0])**2 +(j-coordinate[1])**2):
                        nearestCord =[i,j]
        if nearestCord:
            dist = (nearestCord[0]-coordinate[0])**2+(nearestCord[1]-coordinate[1])**2
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
            if(max>27):
                max=27
            coordRange.append([min,max])
        return coordRange

    ## returns distance to nearest coolored coordinate 0 if they overlap
    @staticmethod
    def DistanceToNearesNeighbour(coordinate,numTable):
        if coordinate in numTable:
            return 0
        nearCord=Knn.GetClosestNeighbour(coordinate,numTable)
        if nearCord != 100:
            return nearCord
        return Knn.GetClosestNeighbour(coordinate,numTable,True)

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
    def ComparenNumberWithBoolCodrdinates(number,trainData):
        distList=[]
        for i in range(len(trainData)):
            dist=0
            for j in range(len(number)):
                dist += Knn.DistanceToNearesNeighbour(number[j],trainData[i])
            distList.append([dist,i])
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

    ## gets the precentage of incorrect guesses
    @staticmethod
    def GetErrorPercentage(testData,trainData,testLabels,trainLabels,entries=10,trainEntries=1000):
        trainBoolTable=Knn.CreatePixelBoolCoordinateTable(trainData,trainEntries)
        testBoolTable=Knn.CreatePixelBoolCoordinateTable(testData,entries)
        correctRecognitions=0
        for i in range(entries):
            distList= Knn.ComparenNumberWithBoolCodrdinates(testBoolTable[i],trainBoolTable)
            recognizedNumber= Knn.GetTheMajorityNeighbourNumber(distList,trainLabels)
            if testLabels[i]==recognizedNumber:
                correctRecognitions +=1
            else:
                print(str(testLabels[i])+" =/= "+str(recognizedNumber)+" at index:"+str(i))
        return 1-correctRecognitions/entries
