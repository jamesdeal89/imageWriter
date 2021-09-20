# a class which will generate an image and write that image to a file.
import random

class CreateImage():
    def __init__(self, fileLocation, h=640, w=480):
        self.fileLoc = fileLocation
        self.height = h
        self.width = w

    def save(self):
        # here we will save using a basic image format called 'PPM'. It requires very little data.
        f = open(self.fileLoc, "w")
        # for PPM file format the file starts with the magic no. 'P3' to show it's filetype.
        f.write("P3")
        # width and height is stated next as part of the PPM format.
        f.write(str(self.width)+ " " + str(self.height))
        # we state the max value of colour on the third line.
        f.write("255")

    def generateRandom(self):
        # random pixels 
        # grid of pixels
        self.pixels = []
        for x in range(0,self.width):
            tempList = []
            for y in range(0,self.height):
                r = random.randint(0,255)
                g = random.randint(0,255)
                b = random.randint(0,255)
                tempList.append([r,g,b])
            self.pixels.append(tempList)
        # save an individual pixel
        # red, green, blue, alpha values

Image1 = CreateImage("testimage1.bmp",640,480)
Image1.generateRandom()
Image1.save()



