def calculatePower(x,y,serialNum):
    rackId = x + 10
    powerLevel = rackId * y + serialNum
    powerLevel = powerLevel * rackId

    powerLevelStr = str(powerLevel)

    if len(powerLevelStr) > 2:
        hundredsDigit = int(powerLevelStr[::-1][2])
    else:
        hundredsDigit = 0

    return hundredsDigit - 5

def prettyPrintGrid(grid):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in grid]))

def createGrid():
    maxX = 300 # From problem statement
    maxY = 300

    grid = [[ (j + 1, i + 1) for j in range(maxY)] for i in range(maxX)]

    return grid

def createPowerGrid(grid):
    powerGrid = [[0 for j in range(301)]for i in range(301)]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            x = grid[row][col][0]
            y = grid[row][col][1]
            powerGrid[row+1][col+1] = calculatePower(x, y, 1133)
            
    return powerGrid

def scanSquares(powerGrid):
    maxTotal = 0
    coord = (1,1)
    for i in range(1, len(powerGrid)):
        for j in range(1, len(powerGrid[i])):
            if i + 3 < len(powerGrid) and j + 3 < len(powerGrid[i]):
                total = threeByThreeSquare(powerGrid, (i,j))
                if total > maxTotal:
                    maxTotal = total
                    coord = (i,j)

    return maxTotal, coord

def threeByThreeSquare(grid, coord):
    x, y = coord[0], coord[1]
    x1, y1 = x + 3, y + 3
    total = 0

    for row in range(x,x1):
        for col in range(y, y1):
            total += grid[row][col]

    return total


def main():
    grid = createGrid()
    powerGrid = createPowerGrid(grid)
    total, coord = scanSquares(powerGrid)
    coord = (coord[1], coord[0])
    print(total, coord)

main()