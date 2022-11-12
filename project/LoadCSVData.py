import pandas as pd
 

class CSVConverter:
    def __init__(self,imgF,labelF,outF,entries):
        self.img =imgF
        self.label = labelF
        self.out = outF
        self.entries = entries
    def convert(self):
        f = open(self.img, "rb")
        l = open(self.label, "rb")
        o = open(self.out, "w")

        f.read(16)
        l.read(8)
        images = []

        for i in range(self.entries):
            image = [ord(l.read(1))]
            for j in range(28*28):
                image.append(ord(f.read(1)))
            images.append(image)

        for image in images:
            o.write(",".join(str(pix) for pix in image)+"\n")

        f.close()
        o.close()
        l.close()
        csvF = pd.read_csv(self.out)
        #renaming the label columns
        csvF.rename(columns={csvF.columns[0]:'label'}, inplace=True)
        #updating the files
        csvF.to_csv(self.out, index=False)




