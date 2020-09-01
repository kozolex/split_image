import glob
from os.path import splitext
from PIL import Image, ImageDraw
import imageTrimmer as it

rotationAngles = [90, 180, 270]
for concretFile in glob.glob('/media/mk/3C243342451A70C5/Grant_rak/Zdjecia_krakow/OTAGOWANE/val/*/*.png', recursive=True):
    print(concretFile)
    img = Image.open(concretFile)
    path, ext = splitext(concretFile)
    print(path)
    print(ext)
    newname = path + 'augLR' + ext
    img.transpose(Image.FLIP_LEFT_RIGHT).save( newname, 'PNG')
    newname = path + 'augTB' + ext
    img.transpose(Image.FLIP_TOP_BOTTOM).save( newname, 'PNG')
        