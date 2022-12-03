from matplotlib import pyplot
from KNN import Knn
import numpy as np
from dataloader import Dataloader

def main():
    #loading train data
    trainData = Dataloader.GetImageData('datafiles/train-images.idx3-ubyte')
    trainLData = Dataloader.GetLabelData('datafiles/train-labels.idx1-ubyte')

    #loading test data
    testData = Dataloader.GetImageData('datafiles/t10k-images.idx3-ubyte')
    testLData = Dataloader.GetLabelData('datafiles/t10k-labels.idx1-ubyte')

    #Table generation
    trainBoolCoordtable = Knn.CreatePixelBoolCoordinateTable(trainData,100)
    #testBoolCoordtable = CreatePixelBoolCoordinateTable(testData)
    testNumber=Knn.CreatePixelBoolCoordinateNumber(testData[2])
    # getting a sorted list of all data points based on the distance between the colored pixels of the images
    distList= Knn.ComparenNumberWithBoolCodrdinates(testNumber,trainBoolCoordtable)
    
    

    recognizedNumber= Knn.GetTheMajorityNeighbourNumber(distList,trainLData,5)

    #the number we think it is
    print("The number that the algorith recognized "+ str(recognizedNumber))
    #the numer it is
    print("The digit tested was a "+str(testLData[2]))
    pyplot.imshow(testData[2])
    pyplot.show()
    ##commented out since it takes a while to check accuracy
    #accuracy check
    print(Knn.GetErrorPercentage(testData,trainData,testLData,trainLData,10,1000))

if __name__ == "__main__":
    main()