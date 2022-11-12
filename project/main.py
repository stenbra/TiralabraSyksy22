from matplotlib import pyplot
import LoadCSVData as csvLoader
import numpy as np
import pandas as pd

def main():
    #loading
    a=csvLoader.CSVConverter("train-images.idx3-ubyte","train-labels.idx1-ubyte","mnist_train.csv",60000)
    a.convert()
    trainData = pd.read_csv("mnist_train.csv")
    trainDataSmall = trainData.iloc[:1000]
    print(trainDataSmall.head(5))

    label = trainDataSmall["label"]
    pixelData = trainDataSmall.drop("label",axis=1)
    print(label.shape)
    print(pixelData.head(3))
    print(pixelData.shape)


    # #plotting
    pyplot.figure(figsize=(7,7))
    idx =468
    grid_data = pixelData.iloc[idx].to_numpy().reshape(28,28)
    pyplot.imshow(grid_data,interpolation="none",cmap="gray")
    pyplot.imsave("test.png",grid_data,cmap="gray")

    print(label[idx])

if __name__ == "__main__":
    main()