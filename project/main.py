from matplotlib import pyplot
import KNN
import numpy as np
from dataloader import Dataloader

def main():
    #loading train data
    trainData = Dataloader.GetImageData('datafiles/train-images.idx3-ubyte')
    trainLData = Dataloader.GetLabelData('datafiles/train-labels.idx1-ubyte')
    print(trainLData)

    #loading test data
    testData = Dataloader.GetImageData('datafiles/t10k-images.idx3-ubyte')
    testLData = Dataloader.GetLabelData('datafiles/t10k-labels.idx1-ubyte')
    print(testLData)
    #Table generation
    trainBoolCoordtable = KNN.CreatePixelBoolCoordinateTable(trainData,100)
    #testBoolCoordtable = CreatePixelBoolCoordinateTable(testData)
    testNumber=KNN.CreatePixelBoolCoordinateNumber(testData[56])

    # getting a sorted list of all data points based on the distance between the colored pixels of the images
    distList= KNN.ComparenNumberWithBoolCodrdinates(testNumber,trainBoolCoordtable)
    
    

    recognizedNumber= KNN.GetTheMajorityNeighbourNumber(distList,trainLData,5)

    #the number we think it is
    print(recognizedNumber)
    #the numer it is
    print(testLData[56])
    pyplot.imshow(testData[56])
    pyplot.show()
    print(KNN.GetErrorPercentage(testData,trainData,testLData,trainLData,100))

if __name__ == "__main__":
    main()