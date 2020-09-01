import glob
from os.path import splitext
from PIL import Image, ImageDraw
import imageTrimmer as it

rotationAngles = [90, 180, 270]
for concretFile in glob.glob('/media/mk/3C243342451A70C5/Grant_rak/Zdjecia_krakow/OTAGOWANE/train/*/*.png', recursive=True):
    print(concretFile)
    img = Image.open(concretFile)
    path, ext = splitext(concretFile)
    print(path)
    print(ext)
    for rotationOneAngle in rotationAngles:
        newname = path + 'r' + str(rotationOneAngle) + ext
        img.rotate(rotationOneAngle, expand=True).save( newname, 'PNG')