import glob
from PIL import Image, ImageDraw
import imageTrimmer as it

IN_DIR = '/media/mk/3C243342451A70C5/Grant_rak/Zdjecia_krakow/OTAGOWANE/val/*/*.'
IN_DIR = '/media/mk/3C243342451A70C5/Grant_rak/modele/mel_seg_grant/dataset/01_aug/*.'

for concretFile in glob.glob(IN_DIR+ 'png', recursive=True):
    print(concretFile)
    testImage = it.ImageTrimmer(concretFile, 256, 192)
    testImage.trimmingProcess(savePar=1, drawPar=0, fileExt= 'png')
    del testImage
print ('End of procesing')