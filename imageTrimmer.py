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
        padding = int(sizeImage / sizeCrop /4)          #auto padding
        parts = int(sizeImage / sizeCrop) + padding  #how many parts fit in to size Image and one more
        sizeOver = (sizeCrop * parts) - sizeImage    #size over the image
        sizeOverSingle = int(sizeOver / (parts-1))   #size over the image
        sizeStep = int(sizeCrop -  sizeOverSingle)

        print('sizeImage, sizeCrop, padding, parts: {0}, {1}, {2}, {3}'.format(sizeImage, sizeCrop, padding, parts ) )
        return sizeStep, int(parts)
    
    def trimmingProcess(self, savePar=False, drawPar = False, showPar=False):
        if self.sizeCrop <= self.imgWidth and self.sizeCrop<= self.imgHeight:
            stepSizeW, partsWidth = self.giveStepSize(self.imgWidth, self.sizeCrop)
            stepSizeH, partsHeight = self.giveStepSize(self.imgHeight, self.sizeCrop)

            drawing = ImageDraw.Draw(self.img)
            for idx in range(0, partsWidth):
                for idy in range(0, partsHeight):
                    idxNow = idx * stepSizeW
                    idyNow = idy * stepSizeH
                    box = (idxNow, idyNow, idxNow + self.sizeCrop, idyNow + self.sizeCrop)
                    if savePar == True:
                        crop = self.img.crop(box)
                        crop.save('./output/test_'+str(box).replace('(', '').replace(')', '').replace(', ', '_')+'.png', 'PNG')
                    if drawPar == True:
                        drawing.rectangle( box, outline=(idx%3*255,(idx+idy)%2*255,0,128), width=(idx+idy)%2+1)
                        drawing.text((idxNow,idyNow), str(idxNow)+ ' '+ str(idyNow), fill=(0,255,0,128))
        else:
            print ('Crop size is too large.' )
        
        if showPar == True:
            self.img.show()



testImage = ImageTrimmer('input/DSC01129.JPG', 604)
testImage.trimmingProcess(drawPar=0, showPar=0)