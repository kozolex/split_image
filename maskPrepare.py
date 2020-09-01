#use this file if your masks are 16bits but value 1 is a mask and rest is a background
import glob
from PIL import Image, ImageDraw

#print(glob.glob('../Otagowane/otagowane18.06.20/czw_kwi_9_11_40_58_2020a/*.png'))

for concretFile in glob.glob('/media/mk/3C243342451A70C5/Grant_rak/Zdjecia_krakow/OTAGOWANE/val/*/*.png', recursive=True):
    print(concretFile)
    img16 = Image.open(concretFile)
    img8 = img16.convert('L')
    threshold = 1  
    img8 = img8.point(lambda p: p > threshold and 255)
    #img8.show()
    img8.save(concretFile)