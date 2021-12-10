# The 'ol input gettaroo
inputFile = open("inputs/Day_10_input.txt")
inputData = inputFile.read().split("\n")
inputFile.close()

# Find all legal lines and add them to a new list
legalLines = []
for line in inputData:
    # We doin' this stack style
    lineQueue = []
    for char in range(len(line)):
        # Continue the rest of the logic bc why not
        lineChar = line[char]
        if lineChar == '(' or lineChar == '[' or lineChar == '{' or lineChar == '<':
            lineQueue.append(lineChar)
        else:
            # Then it's a closing pair
            lastOpen = lineQueue.pop()
            if (lastOpen == '(' and lineChar == ')') or (lastOpen == '[' and lineChar == ']') or (lastOpen == '{' and lineChar == '}') or (lastOpen == '<' and lineChar == '>'):
                continue
            else:
                lineQueue = [] # Illegal line, reset
                break
    if len(lineQueue) > 0:
        # We hit the end and it's not illegal
        legalLines.append(line)

# Auto completion points
atcPoints = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

# Complete all legal lines
atcScores = []
for line in legalLines:
    # We'll be using the same stack approach
    # NOTE: I could be doing this within the code above, but I'll do it here now for simplicity
    lineQueue = []
    lineScore = 0
    for char in range(len(line)):
        lineChar = line[char]
        # They're all legal, but we want to build up the remaining stack
        if lineChar == '(' or lineChar == '[' or lineChar == '{' or lineChar == '<':
            lineQueue.append(lineChar)
        else:
            lastOpen = lineQueue.pop()
    # Go ahead and build a string out of the remaining chars in lineQueue (most recent on top)
    newEnding = ""
    while len(lineQueue) > 0:
        lastChar = lineQueue.pop()
        newEnding += pairs[lastChar]
        lineScore *= 5
        lineScore += atcPoints[pairs[lastChar]]
    atcScores.append(lineScore)
atcScores.sort()
midScore = atcScores[len(atcScores)//2]
print("The mid score is:", midScore)