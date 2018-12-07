class Node:
    def __init__(self, id, dependencies = []):
        self.id = id
        self.dependencies = dependencies

    def __len__(self):
        return len(self.dependencies)

    def __str__(self):
        return self.dependencies

def readFile():
    inps = []

    with open("test.txt", "r") as file:
        for line in file:
            inps.append(line.split(" "))

    return inps

def parseInput(inps):
    """ 
    Item at idx 7 is dependent on item at idx 1 
    """
    nodes = {}
    allNodes = set()
    for item in inps:
        node = item[7]
        dep = item[1]
        allNodes.add(dep)
        allNodes.add(node)

        if node in nodes:
            nodes[node].append(dep)
        else:
            nodes[node] = list(dep)

    nodeWithNoDep = findNodeWithNoDep(allNodes, nodes)

    return allNodes, nodes, nodeWithNoDep


def findNodeWithNoDep(allNodes, nodes):
    return allNodes - set(nodes.keys())

def findKeysThatHasValue(value, nodes):
    def hasValue(value, valueList):
        if value in valueList:
            return True
        return False

    keys = list(filter(lambda key: hasValue(value, nodes[key]) == True, nodes))
    #print(keys)
    return keys

def traverse(allNodes, nodes, nodeWithNoDep):
    node = list(nodeWithNoDep).pop()
    nodesWithIncomingEdgesFromNode = findKeysThatHasValue(node, nodes)

def main():
    inps = readFile()
    allNodes, nodes, nodeWithNoDep = parseInput(inps)
    
    
    
    
    #print(allNodes)
    #print(nodes)
    #print(nodeWithNoDep)

if __name__ == "__main__":
    main()