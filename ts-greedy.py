from helpers import *    

# The idea is to take each city as a starting point and calculate the minimum path from there
# Then, compare between the generated paths to see which path was the shortest

def getNearestCity(coordinates, startingCity):
    minimumDistance = 999999999999999
    nearestCity = (0, 0)

    for nextCity in coordinates:
        if nextCity != startingCity:
            currentDistance = getEuclideanDistance(startingCity, nextCity)

            if currentDistance < minimumDistance:
                minimumDistance = currentDistance

            nearestCity = nextCity

    return nearestCity

def getPathFromStartingCity(coordinates, startingCity):
    path = [startingCity]

    nextCity = startingCity
    notVisitedCities = list(set(coordinates) - set(path))

    # while not all cities have been visited
    while len(notVisitedCities) > 0:
        nearestCity = getNearestCity(notVisitedCities, nextCity)
        
        nextCity = nearestCity
        path.append(nearestCity)

        notVisitedCities = list(set(coordinates) - set(path))

    return path

def findShortestSalesmanPathWithGreedy(coordinates):
    minimumPath = []
    minimumPathDistance = 999999999999999

    # calculate path from every city as a starting point
    for city in coordinates:
        currentPath = getPathFromStartingCity(coordinates, city)
        pathDistance = getTotalPathDistance(currentPath)
        
        print(f"Current tested path: {currentPath} | Distance: {pathDistance}")

        if pathDistance < minimumPathDistance:
            minimumPathDistance = pathDistance
            minimumPath = currentPath

    return minimumPath

def main():
    #generateRandomExampleFile()

    coordinates = readFileCoordinates()
    n = len(coordinates)

    print("Number of coordinates: ", n)
    print("Coordinates: ", coordinates)

    shortestPath = findShortestSalesmanPathWithGreedy(coordinates)

    print(f"ShortestPath: {shortestPath} | Distance: {getTotalPathDistance(shortestPath)} ")

if __name__ == '__main__':
    main()
