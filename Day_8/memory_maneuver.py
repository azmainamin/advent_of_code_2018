def readFile():
    inps = []
    with open("test.txt", "r") as file:
        lines = "".join([x for x in file]).split(" ")
        for line in lines:
            inps.append((int(line.strip("\n"))))
    return inps

def findNodeInfo(inps):
    childNodes = inps[0]
    metaData = inps[1]

    inps = inps[2:] # Exclude header info
    totalMeta = 0

    for node in range(childNodes): # If childNode is 0, we won't go inside for loop
        total, inps = findNodeInfo(inps)
        totalMeta += total
    # If we are here, we know either childNode = 0 or we looped over all childs, and we already truncated inps 
    # to exclude first 2 item (# of child and # of meta). So inps[:metaData] is just the metadatas
    totalMeta += sum(inps[:metaData]) 

    if childNodes == 0: # We know that after the next item, it will be the metas
       return totalMeta, inps[metaData:]
    else: 
        return totalMeta, inps[metaData:]
     
def main():
    inps = readFile()

    print(findNodeInfo(inps)[0])
    
if __name__ == "__main__":
    main()