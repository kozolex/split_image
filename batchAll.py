import glob
from PIL import Image, ImageDraw
import imageTrimmer as it

for concretFile in glob.glob('../Otagowane/otagowane18.06.20/*/*.png', recursive=True):
    print(concretFile)
    testImage = it.ImageTrimmer(concretFile, 256, 192)
    testImage.trimmingProcess(savePar=1, drawPar=0, fileExt= 'png')
    del testImage
    break
print ('End of procesing')