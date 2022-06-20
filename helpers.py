# Helper file to unclutter main algorithm files and share behavior

from math import sqrt
import random
import numpy as np

# Generates a random example file in the expected format, 
# describing a series of 2D coordinates for the cities, separated by semicolons:
# NUMBEROFENTRIES;X1;Y1;X2;Y2.....Xn;Yn
def generateRandomExampleFile():
    sampleSize = random.randint(1, 10);
    # sampleSize = 9

    x = np.random.randint(0, 1001, sampleSize)
    y = np.random.randint(0, 1001, sampleSize)

    with open('example-file.txt', 'w') as exampleFile:
        exampleFile.write(str(sampleSize))

        for i in range(sampleSize):
            exampleFile.write(';')
            exampleFile.write(str(x[i]))
            exampleFile.write(';')
            exampleFile.write(str(y[i]))

# Read the file coordinates from the example file
# and returns it as a list of tuples representing each coordinate
def readFileCoordinates():
    with open('example-file.txt', 'r') as exampleFile:
        fileAsText = exampleFile.read()

    tokens = fileAsText.split(';')

    n = int(tokens[0])
    numberOfCoordinates = n * 2

    data = []

    for i in range(1, numberOfCoordinates, 2):
        coordinate = (int(tokens[i]), int(tokens[i+1]))
        data.append(coordinate)

    return data

# Just a helper function to more easily calculate the 
# straight line distance between two 2D coordinates
def getEuclideanDistance(a, b):
    return sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

def getTotalPathDistance(path):
    pathDistance = 0
    
    for i in range(len(path) - 1):
        pathDistance += getEuclideanDistance(path[i], path[i + 1])

    return pathDistance

