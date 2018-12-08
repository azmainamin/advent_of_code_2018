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

    with open("input.txt", "r") as file:
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
            #graph[node].sort()
        else:
            graph[node] = list(dep)

    nodeWithNoDep = findNodeWithNoDep(allNodes, graph)

    return allNodes, graph, nodeWithNoDep


def findNodeWithNoDep(allNodes, nodes):
    return allNodes - set(nodes.keys())

def findKeysThatHasValue(value, graph):
    def hasValue(value, valueList):
        if value in valueList:
            return True
        return False

    nodes = list(filter(lambda node: hasValue(value, graph[node]) == True, graph))
    #print(keys)
    return nodes

def traverse(graph, stack, result = []):
    """
    graph - Node: [Dependent Nodes]
    stack - Nodes in a sorted order 
    """ 
    
    # Remove node with no incoming edges from the list. Is len() 0, meaning all conditions met? If yes, add to a stack/list
    if len(graph) == 0:
        result.append(stack.pop(0))
        return result

    noDependencyNode = stack.pop(0)
    result.append(noDependencyNode)
    nodesWithIncomingEdgesFromNode = findKeysThatHasValue(noDependencyNode, graph)

    for node in nodesWithIncomingEdgesFromNode:
        graph[node].remove(noDependencyNode) # Remove C from list
        if len(graph[node]) == 0:
            graph.pop(node)
            stack.append(node)
            stack.sort()
    
    sortedStack = sorted(stack)

    return traverse(graph, stack, result)

def main():
    inps = readFile()
    allNodes, graph, nodeWithNoDep = createDependencyGraph(inps)
    # Need to meet sorting requirements 
    # when there are more than one initial node with no incoming edges
    stack = sorted(list(nodeWithNoDep))   
    result = traverse(graph,stack)

    print("".join(result))

if __name__ == "__main__":
    main()