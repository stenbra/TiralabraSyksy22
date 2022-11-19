from matplotlib import pyplot
import numpy as np
import struct

#TODO make this check neightbours
def CreateListOfNeighbourCoords(coordinate):
    nList = []
    

def DistanceToNearesNeighbour(coordinate,numbertable):
    if coordinate in numbertable:
        return 0
    return 10

def CreatePixelBoolCoordinateTable(data):
    boolCordTable = [[0]]*len(data)
    for i in range(len(data)):
        ##TODO turn into dictionary
        boolTable=[]
        for j in range(28):
            for k in range(28):
                if data[i][j][k] > 73:
                    boolTable.append([j,k])
        boolCordTable[i]=boolTable
    return boolCordTable

def ComparenNumberWithBoolCodrdinates(number,trainData):
    shortestDist = 1000
    numberIndex = 0
    for i in range(len(trainData)):
        dist=0
        dist = DistanceToNearesNeighbour(number,trainData[i])
        if dist < shortestDist:
            numberIndex = i
            shortestDist= dist
    return numberIndex


def main():

    #loading train
    with open('datafiles/train-images.idx3-ubyte','rb') as f:
        magic, size = struct.unpack(">II", f.read(8))
        nrows, ncols = struct.unpack(">II", f.read(8))
        trainData = np.fromfile(f, dtype=np.dtype(np.uint8).newbyteorder('>'))
        trainData = trainData.reshape((size, nrows, ncols))
        # print(data[0][0][0])
        # print(data[len(data)-1])

    with open('datafiles/train-labels.idx1-ubyte','rb') as f:
        magic, size = struct.unpack(">II", f.read(8))
        trainlData = np.fromfile(f, dtype=np.dtype(np.uint8).newbyteorder('>'))
        trainlData = trainlData.reshape((size,)) # (Optional)
        print(trainlData)

    #loading test
    with open('datafiles/t10k-images.idx3-ubyte','rb') as f:
        magic, size = struct.unpack(">II", f.read(8))
        nrows, ncols = struct.unpack(">II", f.read(8))
        data = np.fromfile(f, dtype=np.dtype(np.uint8).newbyteorder('>'))
        data = data.reshape((size, nrows, ncols))
        pyplot.imshow(data[5,:,:], cmap='gray')
        pyplot.show()
        # print(data[0][0][0])
        # print(data[len(data)-1])

    with open('datafiles/t10k-labels.idx1-ubyte','rb') as f:
        magic, size = struct.unpack(">II", f.read(8))
        lData = np.fromfile(f, dtype=np.dtype(np.uint8).newbyteorder('>'))
        lData = lData.reshape((size,)) # (Optional)
        print(lData)

    #Table generation
    trainBoolCoordtable = CreatePixelBoolCoordinateTable(trainData)
    testBoolCoordtable = CreatePixelBoolCoordinateTable(data)
    recognisedNumberIdx= ComparenNumberWithBoolCodrdinates(testBoolCoordtable[5],trainBoolCoordtable)
    print(lData[recognisedNumberIdx])

if __name__ == "__main__":
    main()