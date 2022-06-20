###
# This is a program to run a Travelling Salesman Problem solving algorithm using brute force
# As such, it uses a very inefficient method, by calculating every permutation possible for a set of cities
# and then, iterating over each permutation and each city in the permutation to calculate the total distance
# of a given permutation, and find the smallest one.
#
# For sets up to 8 cities, it is reasonably fast to execute, taking a few seconds for execution
# For 9 and above, the time it takes to execute rises sharply, 
# with 9 elements taking many minutes to execute on a fairly modern CPU
# 
# To use, simply run this script, and it will generate a random sized sample from 1 to 100 cities and save to a file
# which it will use as source for the test (as it takes factorial time to execute, most random samples won't be able to be executed properly)
# The size of the sample can be fixed in the helpers.py file.
###
from helpers import *

# Extremely inefficient permutation algorithm
# Selects an element, removes it, calculates the permutations of the 
# remaining items recursively and concatenates each recursive result to the initial element
def permute(elements: list):
    if len(elements) < 2:
        return [elements]

    perms = []

    for element in elements:                                                        
        otherElements = [item for item in elements if item != element]              
        permutationsOfTheOtherElements = permute(otherElements)                     

        for permutation in permutationsOfTheOtherElements:                          
            perms = [*perms, [element, *permutation]]                               

    return perms

# To find the shortest path,
# calculate all permutations for the provided set, 
# and for each permutation, calculate the total euclidean distance between the sequence of points
# The requirement to calculate all permutations makes this also very inefficient
def findShortestSalesmanPathByBruteForce(cityCoordinates):
    smallestDistance = float('inf')
    smallestPath = []

    for permutation in permute(cityCoordinates):
        currentDistance = 0

        for index, city in enumerate(permutation):
            if index < len(permutation) - 1:
                nextCity = permutation[index + 1]
                currentDistance += getEuclideanDistance(city, nextCity)

        if currentDistance < smallestDistance:
            smallestDistance = currentDistance
            smallestPath = permutation

    return smallestPath

def main():
    #generateRandomExampleFile()

    cityCoordinates = readFileCoordinates()
    n = len(cityCoordinates)

    print("Number of coordinates: ", n)
    print("Coordinates: ", cityCoordinates)

    shortestPath = findShortestSalesmanPathByBruteForce(cityCoordinates)

    print(f"ShortestPath: {shortestPath} | Distance: {getTotalPathDistance(shortestPath)}")

if __name__ == '__main__':
    main()    
