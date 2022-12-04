from PIL import Image
from PIL import ImageEnhance
from PIL import ImageDraw
import sys
from scipy.spatial import distance
from math import sqrt

#local defs
from colorimporter import *
from nearestneighbor import *

usage = '''usage: python3 fs_dither.py colorfile.dat inimage.ext outimage.ext'''

if(len(sys.argv) < 4):
    print(usage)
    exit(-1)

color_name = sys.argv[1]
in_name = sys.argv[2]
out_name = sys.argv[3]

y = 0
x = 0


def GetError(oldpixel,newPixel):
    return [oldpixel[0] - newPixel[0],oldpixel[1] - newPixel[1],oldpixel[2] - newPixel[2]]

def ApplyError(pixelVal, quanterr, mult):
    applied = [quanterr[0]*mult,quanterr[1]*mult,quanterr[2]*mult]
    return tuple([int(min(pixelVal[0] + applied[0],255)),int(min(pixelVal[1] + applied[1],255)),int(min(pixelVal[2] + applied[2],255))])


def ValidateColors(image):
    for y in range(0,image.height):
        for x in range(0,image.width):
            pixel = fle.getpixel((x,y))
            if pixel not in colors:
                return False
    return True

colors = ExtractColors(color_name)


try:
    fle = Image.open(in_name)

    for y in range(0,fle.height):
        for x in range(0,fle.width):
            #https://en.wikipedia.org/wiki/Floyd%E2%80%93Steinberg_dithering
            pixel = fle.getpixel((x,y))
            newPixel = findNearest_distance3D(pixel,colors)

            fle.putpixel((x,y),newPixel)
            err = GetError(pixel, newPixel)
            
            if x < fle.width-1:
                upPix = fle.getpixel((x+1,y))
                fle.putpixel((x+1,y), ApplyError(upPix,err,(7 / 16)))

            if x > 0 and y < fle.height-1:
                upPix = fle.getpixel((x-1,y+1))
                fle.putpixel((x-1,y+1),ApplyError(upPix,err,(3 / 16)))

            if y < fle.height-1:
                upPix = fle.getpixel((x,y+1))
                fle.putpixel((x,y+1),ApplyError(upPix,err,(5 / 16)))

            if x < fle.width-1 and y < fle.height-1:
                upPix = fle.getpixel((x+1,y+1))
                fle.putpixel((x+1,y+1),ApplyError(upPix,err,(1 / 16)))
    
    correct = ValidateColors(fle)
    if correct: 
        fle.save(out_name)
    else:
        print("Color Validation Failed - Unexpected Error")
        exit(-1)

except Exception as E:
    print("File Error")

