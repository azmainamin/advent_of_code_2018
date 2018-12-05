def readFile(fileName):
    inputs = []
    with open(fileName,"r") as f:
        for line in f:
            inputs.append(line)

    return inputs

def findItemsWithThreeRepeatingLetters(inputs):
    return getNumOfRepeatingLetters(inputs, 3)


def findItemsWithTwoRepeatingLetters(inputs):
    return getNumOfRepeatingLetters(inputs, 2)

def getNumOfRepeatingLetters(inputs, num):
    count = 0

    for item in inputs:
        letterCountMap = {}
        for char in item:          
            if char in letterCountMap:
                letterCountMap[char] = letterCountMap[char] + 1
            else:
                letterCountMap[char] = 1

        if hasExactlyNRepeatingLetters(letterCountMap, num):
            count += 1

    return count

def hasExactlyNRepeatingLetters(inp, N):
    for k, v in inp.items():
        if v == N:
            return True
    
    return False

def main():
   inp = readFile("input.txt")
   twoRepeatingLettersCount = findItemsWithTwoRepeatingLetters(inp)
   threeRepeatingLettersCount = findItemsWithThreeRepeatingLetters(inp)
   
   checkSum = twoRepeatingLettersCount * threeRepeatingLettersCount

   print(checkSum)


if __name__ == "__main__":
    main()