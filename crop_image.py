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

img = Image.open(open('./input/test.png', 'rb'))
imgWidth, imgHeight = img.size
crop_size = 200
if crop_size <= imgWidth and crop_size<= imgHeight:
    print(imgWidth, imgHeight)
    partsWidth = int(imgWidth / crop_size)
    partsHeight = int(imgHeight / crop_size)
    print(partsWidth, partsHeight)
    paddingWidth = imgWidth - crop_size*int(imgWidth / crop_size)
    paddingHeight = imgHeight - crop_size*int(imgHeight / crop_size)
    print(paddingWidth, paddingHeight)

    drawing = ImageDraw.Draw(img)
    x, y = 10, 10
    x1, y1 = x + crop_size
    top_left = (50, 50)
    bottom_right = (100, 100)

    outline_width = 10
    outline_color = "black"
else:
    print ('Crop size is too large.' )

#img.show()

