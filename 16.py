"""Implement an algorithm that takes a adjacency list and produces a 
topological sort of the vertices. 

INPUT: 

1 2 
1 3 
1 4 
3 5 
2 5 
4 5 

Returns: 
1 2 3 4 5

https://www.careercup.com/question?id=5178686040965120
"""

def topologicalSort(adjacencyList):
    # Hash set to check if current node has already been added
    nodeSet = set()
    sortedList = []

    # Assumes the first element is the current node
    # Assumes elements past the first are adjacent nodes (directed)
    for l in adjacencyList:
        # Adds current node if not in set
        if l[0] not in nodeSet:
            nodeSet.add(l[0])
            sortedList.append(l[0])

        # Check adjacent nodes
        for i in xrange(1, len(l)):
            if l[i] not in nodeSet:
                nodeSet.add(l[i])
                sortedList.append(l[i])

    return sortedList



adjacencyList = [[1, 2], [1, 3], [1, 4], [3, 5], [2, 5], [4, 5]]

print topologicalSort(adjacencyList) 