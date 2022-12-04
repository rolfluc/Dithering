import csv

#future work:
#instead of simply listing every color, allow ranges of colors

def ExtractColors(imName):
    colors = list()
    colorPixel = (0,0,0)
    with open(imName) as colorFile:
        csvReader = csv.reader(colorFile)
        for row in csvReader:
            red = int(row[0])
            green = int(row[1])
            blue = int(row[2])
            colorPixel = (red,green,blue)
            colors.append(colorPixel)
    return colors