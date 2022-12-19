from matplotlib import pyplot
from KNN import Knn
import numpy as np
from dataloader import Dataloader
from plotter import plotter
def main():
    #loading train data
    trainData = Dataloader.GetImageData('datafiles/train-images.idx3-ubyte')
    trainLData = Dataloader.GetLabelData('datafiles/train-labels.idx1-ubyte')

    #loading test data
    testData = Dataloader.GetImageData('datafiles/t10k-images.idx3-ubyte')
    testLData = Dataloader.GetLabelData('datafiles/t10k-labels.idx1-ubyte')

    trainSize=int(input("Set train data size: "))
    searchRadius =int(input("Set search radius: "))
    k = int(input("Set K: "))
    #Table generation
    trainBoolCoordtable = Knn.CreatePixelBoolCoordinateTable(trainData,trainSize)
    #testBoolCoordtable = CreatePixelBoolCoordinateTable(testData)
    mode = int(input("1 for regular recognition. 2 for error precentage: "))
    if mode ==1:
        while True:
            inputt=input("Testdata index: ")
            if inputt =="q":
                break
            testIndex=int(inputt)
            testNumber=Knn.CreatePixelBoolCoordinateNumber(testData[testIndex])
            # getting a sorted list of all data points based on the distance between the colored pixels of the images


            print("STuff has been converted")
            distList= Knn.ComparenNumberWithBoolCodrdinates(testNumber,trainBoolCoordtable,searchRadius)
            recognizedNumber= Knn.GetTheMajorityNeighbourNumber(distList,trainLData,k)
            #the number we think it is
            print("The number that the algorith recognized "+ str(recognizedNumber))
            #the numer it is
            print("The digit tested was a "+str(testLData[testIndex]))
            print("plotting...")
            plter= plotter()
            plter.AddTestNumber(testData[testIndex],testLData[testIndex],Knn.GetTheMajorityNeighbourNumberData(distList,trainLData,trainData,k))
            
            #pyplot.show()
            plter.PlotTestNumber()
    if mode==2:
        ##commented out since it takes a while to check accuracy
        #accuracy check
        sampleSize=int(input("Set testsample size: "))
        errorData=Knn.GetErrorPercentage(testData,trainData,testLData,trainLData,sampleSize,trainSize,k)
        print(errorData[0])
        plter= plotter()
        plter.SetWrongGuesses(errorData[1])
        plter.PlotWrongGuesses()

if __name__ == "__main__":
    main()