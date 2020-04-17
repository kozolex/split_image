from os import path
from PIL import Image, ImageDraw

class ImageTrimmer:
    """
    Class to split image to part with constant side size. 

    """
    def __init__(self, imagePath, sizeCrop):
        self.imagePath = imagePath
        self.sizeCrop = sizeCrop
        self.img = Image.open( open(imagePath, 'rb') )
        self.imgWidth, self.imgHeight = self.img.size
        self.imgBaseName = path.basename(imagePath)  
        self.imageName, self.imageExt = path.splitext(self.imgBaseName)

        print(f'File to analyze {self.imgBaseName}')
        print(f'File name: {self.imageName}')
        print(f'File extention: {self.imageExt}')
        print(f'Crop size: {sizeCrop}')

    def giveStepSize(self, sizeImage, sizeCrop):
        padding = int(sizeImage / sizeCrop / 4)      #auto padding
        if padding == 0: padding+=1
        parts = int(sizeImage / sizeCrop) + padding  #how many parts fit in to size Image and one more to using as a padding

        sizeOver = (sizeCrop * parts) - sizeImage    #size over the image
        sizeOverSingle = int(sizeOver / (parts-1))   #size over the image
        sizeStep = int(sizeCrop -  sizeOverSingle)

        print('sizeImage, sizeCrop, padding, parts, sizeOver, sizeOverSingle : {0}, {1}, {2}, {3}, {4}, {5}'.format(sizeImage, sizeCrop, padding, parts, sizeOver, sizeOverSingle) )
        return sizeStep, int(parts)
    
    def trimmingProcess(self, savePar=False, drawPar = False):
        if self.sizeCrop <= self.imgWidth and self.sizeCrop<= self.imgHeight:
            stepSizeW, partsWidth = self.giveStepSize(self.imgWidth, self.sizeCrop)
            stepSizeH, partsHeight = self.giveStepSize(self.imgHeight, self.sizeCrop)
            
            if drawPar == True:
                imgDraw = Image.open( open(self.imagePath, 'rb') )
                drawing = ImageDraw.Draw(imgDraw)

            for idx in range(0, partsWidth):

                for idy in range(0, partsHeight):
                    idxNow = idx * stepSizeW
                    idyNow = idy * stepSizeH
                    box = (idxNow, idyNow, idxNow + self.sizeCrop, idyNow + self.sizeCrop)

                    #Saving crop of source image to file
                    if savePar == True:
                        crop = self.img.crop(box)
                        crop.save('./output/'+str(box).replace('(', '').replace(')', '').replace(', ', '_')+'.png', 'PNG')
                        crop.save('./output/test_'+str(box).replace('(', '').replace(')', '').replace(', ', '_')+'.png', 'PNG')
                    
                    #Drawing for feedback - debaging - optional
                    if drawPar == True:
                        drawing.rectangle( box, outline=(idx%3*255,(idx+idy)%2*255,0,128), width=(idx+idy)%2+1)
                        drawing.text((idxNow,idyNow), str(idxNow)+ ' '+ str(idyNow), fill=(0,255,0,128))
        else:
            print ('Crop size is too large.' )
        
        if drawPar == True:
            imgDraw.show()



#testImage = ImageTrimmer('input/DSC01129.JPG', 604)
testImage = ImageTrimmer('input/test.png', 604)
testImage.trimmingProcess(savePar=1, drawPar=1)