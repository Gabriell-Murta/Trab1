from tracemalloc import start
from helpers import *

def dynamicTsp(startCity, otherCities):
    minimumPath = []
    minimumPathCost = 999999999999999999

    if len(otherCities) == 1:
        return [startCity, *otherCities]
    
    for city in otherCities:
        subCities = list(set(otherCities) - set({city}))

        path = [startCity, *dynamicTsp(city, subCities)]

        currentPathCost = getTotalPathDistance(path)

        if currentPathCost < minimumPathCost:
            minimumPath = path
            minimumPathCost = currentPathCost

    return minimumPath

def findShortestSalesmanPathByDynamicProgramming(cityCoordinates):
    minimumPath = []
    minimumPathDistance = 999999999999999999999999

    for startingCity in cityCoordinates:
        path = dynamicTsp(startingCity, list(set(cityCoordinates) - set({startingCity})))
        distance = getTotalPathDistance(path)
        
        if distance < minimumPathDistance:
            minimumPathDistance = distance
            minimumPath = path

    return minimumPath

def main():
    #generateRandomExampleFile()

    cityCoordinates = readFileCoordinates()
    n = len(cityCoordinates)

    print("Number of coordinates: ", n)
    print("Coordinates: ", cityCoordinates)

    shortestPath = findShortestSalesmanPathByDynamicProgramming(cityCoordinates)

    print(f"ShortestPath: {shortestPath} | Distance: {getTotalPathDistance(shortestPath)}")

if __name__ == '__main__':
    main()    
