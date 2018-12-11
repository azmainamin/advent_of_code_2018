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
    pass


def main():
    grid = createGrid()
    #prettyPrintGrid(grid)
    powerGrid = createPowerGrid(grid)
    #prettyPrintGrid(powerGrid)
main()