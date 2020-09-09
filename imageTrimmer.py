from os import path, walk
from PIL import Image, ImageDraw

class ImageTrimmer:
    """
    Class to split image to part with constant side size. 

    """
    def __init__(self, imagePath, sizeCrop, sizeCropY):
        self.imagePath = imagePath
        self.sizeCrop = sizeCrop
        self.sizeCropY = sizeCropY
        self.img = Image.open( open(imagePath, 'rb') )
        self.imgWidth, self.imgHeight = self.img.size
        self.imgBaseName = path.basename(imagePath)  
        self.imageName, self.imageExt = path.splitext(self.imgBaseName)

        #print(f'File to analyze {self.imgBaseName}')
        #print(f'File name: {self.imageName}')
        #print(f'File extention: {self.imageExt}')
        #print(f'Crop size: {sizeCrop}')

    def giveStepSize(self, sizeImage, sizeCrop):
        padding = int(sizeImage / sizeCrop / 4)      #auto padding
        if padding == 0: padding+=1
        parts = int(sizeImage / sizeCrop) + padding  #how many parts fit in to size Image and one more to using as a padding

        sizeOver = (sizeCrop * parts) - sizeImage    #size over the image
        sizeOverSingle = int(sizeOver / (parts-1))   #size over the image
        sizeStep = int(sizeCrop -  sizeOverSingle)

        #print('sizeImage, sizeCrop, padding, parts, sizeOver, sizeOverSingle : {0}, {1}, {2}, {3}, {4}, {5}'.format(sizeImage, sizeCrop, padding, parts, sizeOver, sizeOverSingle) )
        return sizeStep, int(parts)

    def giveLocalAnnotation(self,annotationFileName, cropBox = (0, 0, 0, 0) ):
        """
        annotationFileName = path to annotation file usual .txt
        cropBox = x, y, w, h in pixels
        """
        boxCrop  = self.toRelative(cropBox)

        listAnnotations = self.readAnnotationFromFile(annotationFileName)
        
        for oneAnnotation in listAnnotations:
            oneAnnotation = list(map(float, oneAnnotation)) #may by i do it better 
            #print(boxCrop)
            #print(oneAnnotation)
            #print(self.compareShapes(oneAnnotation, boxCrop) )
        return

    def toPixels(self, cropBox):
        """
        Convert crop box position and size in original image -> relative float tuple to pixel tuple
        """
        #Calculating the relative coordinates of the image slice

        cropImgW = float(cropBox[2]) * self.imgWidth
        cropImgH = float(cropBox[3]) * self.imgHeight

        cropImgX = float(cropBox[0]) * self.imgWidth - cropImgW/2
        cropImgY = float(cropBox[1]) * self.imgHeight - cropImgH/2

        boxCrop = (int(cropImgX), int(cropImgY), int(cropImgX)+int(cropImgW),  int(cropImgY) +int(cropImgH) ) #relative version
        return boxCrop

    def toRelative(self, cropBox):
        """
        Convert crop box position and size in original image -> pixels to relative float tuple
        """
        #Calculating the relative coordinates of the image slice
        cropImgX = cropBox[0] / self.imgWidth
        cropImgY = cropBox[1] / self.imgHeight
        cropImgW = cropBox[2] / self.imgWidth
        cropImgH = cropBox[3] / self.imgHeight
        boxCrop = (cropImgX, cropImgY, cropImgW,  cropImgH ) #relative version
        return boxCrop
        

    def compareShapes(self, rect1, rect2):
        x = 1 
        y = 2
        w = 3
        h = 4
        if (rect1[x] > rect2[x] + rect2[w] or rect1[x] + rect1[w] < rect2[x] or
            rect1[y] > rect2[y] + rect2[h] or rect1[y] + rect1[h] < rect2[y]):
            print('detect')
            xCommon = max(rect1[x], rect2[x])
            wCommon = min(rect1[w], rect2[w])
            hCommon = max(rect1[h], rect2[h])
            yCommon = min(rect1[y], rect2[y])
            boxCommon = (xCommon, yCommon, wCommon, hCommon)
            return boxCommon
        else:
            return 


    def readAnnotationFromFile(self, filename):
        """
        Generate two demantions list from annotation file. 
        list structure = [line number] [id class, x, y, with, height]
        """
        with open(filename) as f:
            listAnnotations = [l.strip().split() for l in f]
            
        return listAnnotations
    
    def trimmingProcess(self, savePar=False, drawPar = False, fileExt = 'png'):
        if self.sizeCrop <= self.imgWidth and self.sizeCrop<= self.imgHeight:
            stepSizeW, partsWidth = self.giveStepSize(self.imgWidth, self.sizeCrop)
            stepSizeH, partsHeight = self.giveStepSize(self.imgHeight, self.sizeCropY)
            
            if drawPar == True:
                imgDraw = Image.open( open(self.imagePath, 'rb') )
                drawing = ImageDraw.Draw(imgDraw)
                for oneAnnotation in self.readAnnotationFromFile('input/' + self.imageName + '.txt'):
                    #print(oneAnnotation)
                    oneAnnotation = tuple(oneAnnotation[1:])
                    oneAnnotation = self.toPixels(oneAnnotation)
                    #print(oneAnnotation)
                    drawing.rectangle(oneAnnotation, outline=(255,0,0,128), width=2)
            imgID = 0

            for idx in range(0, partsWidth):
                imgID += 1

                for idy in range(0, partsHeight):
                    idxNow = idx * stepSizeW
                    idyNow = idy * stepSizeH
                    box = (idxNow, idyNow, idxNow + self.sizeCrop, idyNow + self.sizeCropY)

                    #Saving crop of source image to file
                    if savePar == True:
                        crop = self.img.crop(box)
                        if fileExt == 'jpg': fileExt2 = 'JPEG'
                        elif fileExt == 'tif': fileExt2 = 'TIFF'
                        else: fileExt2 = fileExt

                        crop.save('./output/'+ str(imgID) + self.imageName+'_'+str(box).replace('(', '').replace(')', '').replace(', ', '_')+'.'+fileExt, fileExt2.upper())
                    
                    #Drawing for feedback - debaging - optional
                    if drawPar == True:
                        drawing.rectangle( box, outline=(idx%3*255,(idx+idy)%2*255,0,128), width=(idx+idy)%2+1)
                        drawing.text((idxNow,idyNow), str(idxNow)+ ' '+ str(idyNow), fill=(0,255,0,128))
        
        else:
            print ('Crop size is too large.' )
        
        if drawPar == True:
            imgDraw.show()
        #print('Done.')


#Testing code
#testImage = ImageTrimmer('input/dsc00472.jpg', 608, 608)
#testImage.trimmingProcess(savePar=0, drawPar=1)
#testImage.giveLocalAnnotation('input/dsc00472.txt')


