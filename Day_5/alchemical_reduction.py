def readFile(fileName):
    res = []
    with open("input.txt", "r") as f:
        for line in f:
            res.append(line)

    return res


def getNoblePolymerLength(inp):
  i = 0
  j = i + 1

  while j < len(inp):
    if inp[i].isupper() and inp[i].lower() == inp[j] :
      inp = removeDuplicates(inp,i,j)
      i -= 1
      j -= 1
    elif inp[i].islower() and inp[i].upper() == inp[j]:
      inp = removeDuplicates(inp,i,j)
      i -= 1
      j -= 1 
    else:
      i += 1
      j += 1
  
  return len(inp) - 1 #to negate \n in the end

def removeDuplicates(inp,i, j):
  if j + 1 >= len(inp):
    return inp[:i]
  else:
    return inp[:i] + inp[j+1:]
####################### PART 2 ###############################

def removePairsOfLetters(inp, char):
  lowerCaseCharInput = inp.replace(char, "").replace(char.lower(), "") # Assuming char is always upper

  return lowerCaseCharInput

def getLengthOfShortestPolymer(inp):
  ENGLISH_LETTERS = [chr(i) for i in range(65, 91)]
  
  minLength = len(inp)
  for letter in ENGLISH_LETTERS:
    inpWithRemovedPair = removePairsOfLetters(inp, letter)
    length = getNoblePolymerLength(inpWithRemovedPair)
    if length < minLength:
      minLength = length

  return minLength


################ MAIN ########################################

def main():
    inp = readFile("input.txt")
    inpStr = inp[0]
    polymerLength = getNoblePolymerLength(inpStr)
    print(polymerLength)

    minLength = getLengthOfShortestPolymer(inpStr)
    print(minLength)



if __name__ == "__main__":
    main()
