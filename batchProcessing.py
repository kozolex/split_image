from os import path, walk
import imageTrimmer as it

f = []
mypath = 'input/full_body/'
for (dirpath, dirnames, filenames) in walk(mypath):
    print(filenames)
    for filename in filenames:
        print(filename)
        print(mypath + filename)
        testImage = it.ImageTrimmer(mypath + filename, 608, 608)
        testImage.trimmingProcess(savePar=1, drawPar=0)
        del testImage
print ('End of procesing')