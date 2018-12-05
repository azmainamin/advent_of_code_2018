from inventory_management_system import readFile

def findCorrectIds(inputs):
    for i in range(len(inputs) - 1):   
        id1 = inputs[i]
        for j in range(i + 1, len(inputs)):
            id2 = inputs[j]
            if isDifferenceOne(id1, id2):
                return (id1, id2)

    return "No correct Id found."

def isDifferenceOne(id1, id2):
    diff = 0
    for i in range(len(id1)):
        if diff > 1:
            return False        
        if id1[i] != id2[i]:
            diff += 1
    if diff == 1:
        return True
def getCommonChars(id1, id2):
    commonChars = [id1[i] for i in range(len(id1)) if id1[i] == id2[i]]

    return "".join(commonChars)
        
def main():
    inputs = readFile("input.txt")
    id1, id2 = findCorrectIds(inputs)

    print(getCommonChars(id1, id2))

if __name__ == "__main__":
    main()