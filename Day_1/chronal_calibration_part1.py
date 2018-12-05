def readFile(fileName):
    inputs = []
    with open("inputs.txt","r") as f:
        for line in f:
            inputs.append(line)

    return inputs

def getFrequency(inputs):
    resultFreq = 0
    for freq in inputs:
        resultFreq += int(freq)

    return resultFreq

def findRepeatingFreq(inputs):
    currFreq = 0
    currIdx = 0
    savedFreqs = [currFreq]
    while True:        
        currFreq += int(inputs[currIdx])
        if currIdx == len(inputs)-1:
            currIdx = 0
        else:
            currIdx += 1

        if currFreq in savedFreqs:
            return  currFreq    
        else: 
            savedFreqs.append(currFreq)
        
    return savedFreqs
    
def main():
    inputs = readFile("inputs.txt")
    #inputs = ["+3", "+3", "4", "-2", "-4"]
    #inputs = ["+1", "-1"]
    #inputs = ["7", "7", "-2", "-7", "-4"]
    #inputs = ["-6", "3", "8", "5", "-6"]
    print(findRepeatingFreq(inputs))
    
if __name__ == "__main__":
    main()