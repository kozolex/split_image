import glob
from PIL import Image, ImageDraw
import imageTrimmer as it

rotationAngles = [90, 180, 270]
for concretFile in glob.glob('/media/mk/3C243342451A70C5/Grant_rak/Zdjecia_krakow/OTAGOWANE/otagowane18.06.20/*/*.tif', recursive=True):
    print(concretFile)
    img = Image.open(concretFile)
    for rotationOneAngle in rotationAngles:
        img.rotate(rotationOneAngle, expand=True).save(concretFile + 'r' + str(rotationOneAngle), 'TIFF')