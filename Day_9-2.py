# The 'ol input gettaroo
inputFile = open("inputs/Day_9_input.txt")
inputData = inputFile.read().split("\n")
inputFile.close()

# Create the matrix used throughout this file
print("Building initial number matrix...")
wholeMap = []

for line in inputData:
    newRow = []
    for c in line:
        newRow.append(int(c))
    wholeMap.append(newRow)

"""
Classes

We just need a node class to make life easier. We'll first need to just init nodes to have values.
Then we'll iterate through a new matrix of nodes to instantiate actual nodes "connected" to each other.
"""
class Node:
    def __init__(self, matRow=-1, matCol=-1):
        if matRow == -1 and matCol == -1:
            self.value = 9999
            self.visited = False # Technically doesn't matter
        else:
            self.value = wholeMap[matRow][matCol]
            self.visited = False # Do I even need a visited variable?

    def initNeighbors(self, nodeMatRow, nodeMatCol):
        # Since it's python, I can't just try/except negative indices
        # NOTE: Using 9999 to avoid problems. I could also just do 11, but eh.
        if nodeMatRow-1 >= 0 and nodeMatRow-1 < len(nodeMatrix):
            self.up = nodeMatrix[nodeMatRow-1][nodeMatCol]
        else:
            self.up = Node()

        if nodeMatCol+1 >= 0 and nodeMatCol+1 < len(nodeMatrix[0]): # Pretty sure it's a square, but done for consistency
            self.right = nodeMatrix[nodeMatRow][nodeMatCol+1]
        else:
            self.right = Node()

        if nodeMatRow+1 >= 0 and nodeMatRow+1 < len(nodeMatrix):
            self.down = nodeMatrix[nodeMatRow+1][nodeMatCol]
        else:
            self.down = Node()

        if nodeMatCol-1 >= 0 and nodeMatCol-1 < len(nodeMatrix[0]):
            self.left = nodeMatrix[nodeMatRow][nodeMatCol-1]
        else:
            self.left = Node()

    def neighbors(self):
        return "UP: {} RIGHT:{} DOWN:{} LEFT:{}".format(self.up, self.right, self.down, self.left)
    # Just so I can print something readable
    def __repr__(self):
        nodeString = "N[{}]".format(self.value)
        return nodeString
        
"""
Functions

Pretty much BFS to get the size of a basin, if it's a low point. Also that function.
"""
def isNodeLowPoint(someNode):
    return someNode.value == min(someNode.value, someNode.up.value, someNode.right.value, someNode.down.value, someNode.left.value)

# Thanks to checking if it's a low point, we can assume it isn't a low point. We'll do this recursively... I guess. LOL.
def basinCounter(currNode):
    basinSize = 1
    neighborQueue = [currNode.up, currNode.right, currNode.down, currNode.left]
    currNode.visited = True
    while len(neighborQueue) > 0:
        checkedNode = neighborQueue.pop(0)
        if checkedNode.visited == True or checkedNode.value >= 9:
            continue
        elif checkedNode.value < 9:
            checkedNode.visited = True
            basinSize += 1
            neighborQueue += [checkedNode.up, checkedNode.right, checkedNode.down, checkedNode.left]
    
    return basinSize

    """
    RIP Recursive Solution /(v.v)\
    if currNode.value >= 9:
        return 0
    else:
        return 1 + basinCounter(currNode.up) + basinCounter(currNode.right) + basinCounter(currNode.down) + basinCounter(currNode.left)
    """
"""
Stuff

All of the things!
"""

# Create the node matrix
print("Building node matrix...")
nodeMatrix = []
for row in range(len(wholeMap)):
    newLine = []
    for col in range(len(wholeMap[row])):
        newNode = Node(row, col)
        newLine.append(newNode)
    nodeMatrix.append(newLine)

# Initialize all node neighbors
print("Initializing neighbors for every node...")
for nodeRow in range(len(nodeMatrix)):
    for nodeCol in range(len(nodeMatrix[nodeRow])):
        nodeMatrix[nodeRow][nodeCol].initNeighbors(nodeRow, nodeCol)

print("First node is", nodeMatrix[0][0])
print("First node neighbors are", nodeMatrix[0][0].neighbors())

# Store the basins
print("Finding all the basins...")
allBasinSizes = []
for nodeRow in range(len(nodeMatrix)):
    for nodeCol in range(len(nodeMatrix[nodeRow])):
        locNode = nodeMatrix[nodeRow][nodeCol]
        if isNodeLowPoint(locNode):
            basinSize = basinCounter(locNode)
            allBasinSizes.append(basinSize)

max1 = max(allBasinSizes)
allBasinSizes.remove(max1)
max2 = max(allBasinSizes)
allBasinSizes.remove(max2)
max3 = max(allBasinSizes)
allBasinSizes.remove(max3)
print("Max basin sizes:", max1, max2, max2)
print("Mult of maxes:", max1*max2*max3)