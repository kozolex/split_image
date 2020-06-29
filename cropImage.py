from PIL import Image, ImageDraw

def crop(path, input, height, width, k, page, area):
    im = Image.open(input)          #load input image 
    imgwidth, imgheight = im.size   #grab size image
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

def giveStepSizePadding (sizeImage, sizeCrop = 200, minPadding = 0.1):
    padding = (minPadding * sizeCrop)
    sizeCropNoPadding =  int(sizeCrop - padding)
    parts = int(sizeImage / sizeCropNoPadding) + 1              #how many parts fit in to sizeImage and one more
    sizeOver = int((parts * sizeCropNoPadding) - sizeImage  )   #size over the image
    sizeStep = int(sizeCrop -  int(sizeOver/int(parts)))
    print('size, crop, cropNo, parts, over, steps, result : {0}, {1}, {2}, {3}, {4}, {5}, {6}'.format(sizeImage, sizeCrop, sizeCropNoPadding, parts, sizeOver, sizeStep, parts*sizeStep ) )
    return sizeStep, parts

def giveStepSize (sizeImage, sizeCrop = 200):
    padding = int(sizeImage / sizeCrop)          #auto padding
    parts = int(sizeImage / sizeCrop) + padding  #how many parts fit in to size Image and one more
    sizeOver = (sizeCrop * parts) - sizeImage    #size over the image
    sizeOverSingle = int(sizeOver / (parts-1))   #size over the image
    sizeStep = int(sizeCrop -  sizeOverSingle)

    print('sizeImage, sizeCrop, padding, parts: {0}, {1}, {2}, {3}'.format(sizeImage, sizeCrop, padding, parts ) )
    return sizeStep, int(parts)


img = Image.open(open('input/test.png', 'rb'))
imgWidth, imgHeight = img.size
crop_size = 604
percentPadding = 0.1

if crop_size <= imgWidth and crop_size<= imgHeight:
    stepSizeW, partsWidth = giveStepSize(imgWidth, crop_size)
    stepSizeH, partsHeight = giveStepSize(imgHeight, crop_size)

    drawing = ImageDraw.Draw(img)
    for idx in range(0, partsWidth):
        for idy in range(0, partsHeight):
            idxNow = idx * stepSizeW
            idyNow = idy * stepSizeH
            box = (idxNow, idyNow, idxNow + crop_size, idyNow + crop_size)
            crop = img.crop(box)
            crop.save('./output/test_'+str(box).replace('(', '').replace(')', '').replace(', ', '_')+'.png', 'PNG')
            drawing.rectangle( box, outline="red", width=2)
            
    
else:
    print ('Crop size is too large.' )

img.show()

