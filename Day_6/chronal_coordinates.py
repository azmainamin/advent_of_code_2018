
def readFile():
    inps = []

    with open("input.txt", "r") as file:
        for line in file:
            x, y = line.strip("\n").split(",")
            x, y = int(x), int(y)
            inps.append((x,y))

    return inps

def prettyPrintGrid(grid):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in grid]))

def placePoints(inps):

    grid = [[ -1 for j in range(360)] for i in range(360)]
    for i in range(len(inps)):
        x, y = inps[i]
        grid[y][x] = i

    return grid

def manhattanDistance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    manhattanDistance = abs(x1- x2) + abs(y1 -y2)
    return manhattanDistance

def getMinManHatDistanceForEachPoint(grid, inps):

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            point = (i,j) #swap?
            minDist = 1000
            for c in range(len(inps)):
                manDist = manhattanDistance(point, inps[c])
                if manDist == minDist:
                    grid[i][j] = "#"
                if manDist < minDist:
                    minDist = manDist                   
                    grid[i][j] = c

    return grid

def createEdgePoints():
    edgePoints = set()
    for i in range(360):
        edgePoints.add((0, i))
        edgePoints.add((i, 0))
        edgePoints.add((360, i))
        edgePoints.add((i,360))

    return edgePoints

def notInfinite(edgePoints, distGrid, inps):
    notInfinite = set()
    for row in range(len(distGrid)):
        for col in range(len(distGrid[row])):
            p = (row, col)
            if p not in edgePoints:
                index = distGrid[row][col]
                notInfinite.add(index)

    return notInfinite

def calculateArea(distGrid, notInfinitePoints):
    pointToArea = {}
    for i in range(len(distGrid)):
        for j in range(len(distGrid[i])):
            if distGrid[i][j] in notInfinitePoints:
                if distGrid[i][j] in pointToArea:
                    pointToArea[distGrid[i][j]] += 1
                else:
                   pointToArea[distGrid[i][j]] = 1

    #print(notInfinitePoints)
    print(pointToArea)
    maxArea = max(pointToArea, key=lambda x: pointToArea[x])

    print(pointToArea[maxArea])
def main():
    inps = readFile()
    grid = placePoints(inps)
    distGrid = getMinManHatDistanceForEachPoint(grid, inps)
    edgePoints = createEdgePoints()
    notInfinitePoints = notInfinite(edgePoints, distGrid, inps)
    calculateArea(distGrid, notInfinitePoints)
    #prettyPrintGrid(grid)
    #prettyPrintGrid(distGrid)
    #print(notInfinitePoints)


if __name__ == "__main__":
    main()