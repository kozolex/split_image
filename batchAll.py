import glob
from PIL import Image, ImageDraw
import imageTrimmer as it

for concretFile in glob.glob('/media/mk/3C243342451A70C5/Grant_rak/Zdjecia_krakow/OTAGOWANE/otagowane18.06.20/*/*.tif', recursive=True):
    print(concretFile)
    testImage = it.ImageTrimmer(concretFile, 256, 192)
    testImage.trimmingProcess(savePar=1, drawPar=0, fileExt= 'jpg')
    del testImage
print ('End of procesing')