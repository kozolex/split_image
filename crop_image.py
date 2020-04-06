from PIL import Image, ImageDraw

def crop(path, input, height, width, k, page, area):
    im = Image.open(input)
    imgwidth, imgheight = im.size
    for i in range(0,imgheight,height):
        for j in range(0,imgwidth,width):
            box = (j, i, j+width, i+height)
            a = im.crop(box)
            try:
                o = a.crop(area)
                o.save(os.path.join(path,"PNG","%s" % page,"IMG-%s.png" % k))
            except:
                pass
            k +=1

img = Image.open(open('input/test.png', 'rb'))
imgWidth, imgHeight = img.size
crop_size = 100
padding = 20
if crop_size <= imgWidth and crop_size<= imgHeight:
    print('Image resolition: {0},{1}'.format(imgWidth, imgHeight))
    partsWidth = int(imgWidth / (crop_size - (2*padding)))
    partsHeight = int(imgHeight / (crop_size - (2*padding)))
    print('Parts on x and y: {0},{1}'.format(partsWidth, partsHeight))
    paddingWidth = imgWidth - crop_size*int(imgWidth / crop_size)
    paddingHeight = imgHeight - crop_size*int(imgHeight / crop_size)
    print('Rest size: {0},{1}'.format(paddingWidth, paddingHeight))

    drawing = ImageDraw.Draw(img)
    for idx in range(0,partsWidth+1):
        for idy in range(partsHeight+1):
            drawing.rectangle((((idx * crop_size) - (padding*idx), (idy * crop_size) - (padding*idy)), (crop_size, crop_size)), outline="red", width=1)
else:
    print ('Crop size is too large.' )

img.show()

