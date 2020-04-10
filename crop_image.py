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




img = Image.open(open('input/test.png', 'rb'))
imgWidth, imgHeight = img.size
crop_size = 600
percentPadding = 0.1
padding = int( percentPadding * crop_size )

if crop_size <= imgWidth and crop_size<= imgHeight:
    print('Image resolition W/H, crop, padding: {0},{1},{2},{3}'.format(imgWidth, imgHeight, crop_size, padding))
    #How many parts we need to generate
    partsWidth = int(imgWidth / (crop_size - padding))
    partsHeight = int(imgHeight / (crop_size - padding))
    print('Parts on x and y: {0},{1}'.format(partsWidth, partsHeight))

    paddingWidth = imgWidth - ((crop_size - padding)*partsWidth)
    paddingHeight = imgHeight - ((crop_size - padding)*partsHeight)
    print('Rest size W/H: {0},{1}'.format(paddingWidth, paddingHeight))

    stepSizeW = int( (imgWidth / (partsWidth + 1) ) + (paddingWidth/(partsWidth + 1)))
    stepSizeH = int( (imgHeight / (partsHeight + 1) ))
    print('Step size W/H: {0}, {1}'.format(stepSizeW, stepSizeH) )

    drawing = ImageDraw.Draw(img)
    for idx in range(0, partsWidth+1):
        for idy in range(0, partsHeight+1):
            idxNow = idx * stepSizeW
            idyNow = idy * stepSizeH
            box = (idxNow, idyNow, idxNow + crop_size, idyNow + crop_size)
            crop = img.crop(box)
            crop.save('./output/test_'+str(box).replace('(', '').replace(')', '').replace(', ', '_')+'.png', 'PNG')
            #drawing.rectangle( (idxNow, idyNow, idxNow + crop_size, idyNow + crop_size), outline="red", width=2)
            #print(idx * stepSizeW, idy * stepSizeH )
    
else:
    print ('Crop size is too large.' )

#img.show()

