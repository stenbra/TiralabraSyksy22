from matplotlib import pyplot

class plotter:
    def __init__(self):
        self.testnumbers =[]
        self.wrongGuesses =[]
    def AddClosNeighbour(self,numbers):
        closeNeighbours =[]
        for i in range(len(numbers)):
            closeNeighbours.append([numbers[0],numbers[1]])
        return closeNeighbours
    def AddTestNumber(self,number,lable,closeNeighbours):
        self.testnumbers.append([number,lable,closeNeighbours])

    def SetWrongGuesses(self,guessdata):
        self.wrongGuesses=[]
        for i in range(len(guessdata)):
            self.wrongGuesses.append([guessdata[i][0],guessdata[i][1],guessdata[i][2]])
    def PlotTestNumber(self):
        if len(self.testnumbers)<1:
            return
        if len(self.testnumbers)==1:
            fig, axs = pyplot.subplots(2,len(self.testnumbers[0][2])+1)
        else:
            fig, axs = pyplot.subplots(len(self.testnumbers),len(self.testnumbers[0][2])+1)
        for i in range(len(self.testnumbers)):
            axs[i,0].imshow(self.testnumbers[i][0])
            axs[i,0].set_title("Tested Number: "+str(self.testnumbers[i][1]))
            for j in range(len(self.testnumbers[i][2])):
                axs[i,j+1].imshow(self.testnumbers[i][2][j][0])
                axs[i,j+1].set_title("Train Number: "+str(self.testnumbers[i][2][j][1]))
        
        pyplot.show()
    
    def PlotWrongGuesses(self):
        if len(self.wrongGuesses)<1:
            return
        fig, axs = pyplot.subplots(2,len(self.wrongGuesses))
        for i in range(len(self.wrongGuesses)):
            axs[0,i].imshow(self.wrongGuesses[i][0])
            axs[0,i].set_title("Test number "+str(self.wrongGuesses[i][1])+"=/= Guess "+str(self.wrongGuesses[i][2]))       
        pyplot.show()