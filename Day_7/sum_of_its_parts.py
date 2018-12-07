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

def createDependencyGraph(inps):
    """ 
    Item at idx 7 is dependent on item at idx 1 
    """
    graph = {}
    allNodes = set()
    for item in inps:
        node = item[7]
        dep = item[1]
        allNodes.add(dep)
        allNodes.add(node)

        if node in graph:
            graph[node].append(dep)
        else:
            graph[node] = list(dep)

    nodeWithNoDep = findNodeWithNoDep(allNodes, graph)

    return allNodes, graph, nodeWithNoDep


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
    allNodes, nodes, nodeWithNoDep = createDependencyGraph(inps)
    
    
    
    
    #print(allNodes)
    #print(nodes)
    #print(nodeWithNoDep)

if __name__ == "__main__":
    main()