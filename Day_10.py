# The 'ol input gettaroo
inputFile = open("inputs/Day_10_input.txt")
inputData = inputFile.read().split("\n")
inputFile.close()

# Syntax error points
errPoints = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

# Need to keep in mind that incomplete lines are technically okay for now
illegalScore = 0
for line in inputData:
    # We doin' this stack style
    lineQueue = []
    for char in range(len(line)):
        if char == len(line)-1:
            break # Don't worry about incomplete lines
        lineChar = line[char]
        if lineChar == '(' or lineChar == '[' or lineChar == '{' or lineChar == '<':
            lineQueue.append(lineChar)
        else:
            # Then it's a closing pair
            lastOpen = lineQueue.pop()
            if (lastOpen == '(' and lineChar == ')') or (lastOpen == '[' and lineChar == ']') or (lastOpen == '{' and lineChar == '}') or (lastOpen == '<' and lineChar == '>'):
                continue
            else:
                illegalScore += errPoints[lineChar]
                break # on to the next line

print("The total illegal score is:", illegalScore)