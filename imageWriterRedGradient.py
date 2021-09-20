# a class which will generate an image and write that image to a file.
import random

class CreateImage():
    def __init__(self, fileLocation, h=640, w=480):
        self.fileLoc = fileLocation
        self.height = h
        self.width = w

    def save(self):
        print("\nImage Save Starting...")
        # here we will save using a basic image format called 'PPM'. It requires very little data.
        f = open(self.fileLoc, "w")
        # for PPM file format the file starts with the magic no. 'P3' to show it's filetype.
        f.write("P3\n")
        # width and height is stated next as part of the PPM format.
        f.write(str(self.width)+ " " + str(self.height) + "\n")
        # we state the max value of colour on the third line.
        f.write("255\n")
        # we start to write the actual image data via a loop to iterate through each RGB value.
        for row in self.pixels:
            for collum in row:
                for colour in collum:
                    # writes the colour to the file and seperates with a space.
                    f.write(str(colour) + " ")
                    print("-", end ="")
                # seperates each set of colours.
                f.write(" ")
            # creates a new line for each row of pixel data.
            f.write("\n")
        print()

    def generateRandom(self):
        print("Image Generation Starting...")
        # random pixels 
        # grid of pixels
        self.pixels = []
        rTemp = 0
        for y in range(0,self.height):
            tempList = []
            rTemp = 0
            print(".",end='')
            for x in range(0,self.width):
                r = 255 - rTemp
                g = 0
                b = 0
                tempList.append([r,g,b])
                if rTemp < 255:
                    rTemp+=1
            self.pixels.append(tempList)
        # save an individual pixel
        # red, green, blue, alpha values

Image1 = CreateImage("testImage1.ppm",100,255)
Image1.generateRandom()
Image1.save()



