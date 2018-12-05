def readFile(fileName):
    inputs = []
    with open(fileName,"r") as f:
        for line in f:
            inputs.append(line)

    return inputs


def makeRectangle(left, top, dims):
  """
  @param left - int
  @param top - int
  @param dims - tuple(int,int)
  """  
  res = []
  
  for i in range(top, top + dims[1] ):
    for j in range(left, left + dims[0]):
      res.append((i,j))
  return res

def cleanInputs(inputs):
    retval = []

    for inp in inputs:
        claimId, _, useful = inp.partition("@")
        coord, delim, dims = useful.partition(":")
        left, _, top = coord.partition(",")
        dim1,_,dim2 = dims.partition("x")
        claimId = int(claimId.replace("#", ""))
        retval.append((int(left), int(top), (int(dim1), int(dim2)), claimId))
    
    return retval

    
def findOverlappingSquares(rect, store, multipleVisited):

  count = 0
  for coord in rect:
    if coord in store:
      multipleVisited.add(coord)
      count += 1
    else:
        store.add(coord)
  
  #print(count)
  return count, store, multipleVisited

def findSquaredWithinMultipleClaim(cleanedInputs):
    
    visitedCoordinates = set()
    multipleVisited = set()
    for inp in cleanedInputs:
        rect = makeRectangle(inp[0], inp[1], inp[2])
        count, visitedCoordinates, multipleVisited = findOverlappingSquares(rect, visitedCoordinates, multipleVisited)

    return multipleVisited
def findUniqueClaim(cleanedInputs, multipleVisited):
    for inp in cleanedInputs:
        rect = makeRectangle(inp[0], inp[1], inp[2])
        if len(set(rect).intersection(multipleVisited)) == 0:
            return inp[3]


def main():
    inputs = readFile("input.txt")
    cleanedInputs = cleanInputs(inputs)
    overlappingSquares = findSquaredWithinMultipleClaim(cleanedInputs)
    print(len(overlappingSquares))
    uniqueClaim = findUniqueClaim(cleanedInputs, overlappingSquares)
    print(uniqueClaim)

if __name__ == "__main__":
    main()