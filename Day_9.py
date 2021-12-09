# The 'ol input gettaroo
inputFile = open("inputs/Day_9_input.txt")
inputData = inputFile.read().split("\n")
inputFile.close()

# I'm sure there's some easier way to do this, but this strikes me as easy for now...?
someMatrix = []

for line in inputData:
    newRow = []
    for c in line:
        newRow.append(int(c))
    someMatrix.append(newRow)

# Iterate through and find risk places and add them (+ 1) to the sum
riskSum = 0
for row in range(len(someMatrix)):
    for col in range(len(someMatrix[0])):
        val = someMatrix[row][col]
        # Top row
        if row == 0:
            # Top left
            if col == 0:
                if val < someMatrix[row][col+1] and val < someMatrix[row+1][col]:
                    riskSum += val + 1
            # Top right
            elif col == len(someMatrix[row])-1:
                if val < someMatrix[row][col-1] and val < someMatrix[row+1][col]:
                    riskSum += val + 1
            # General top values
            else:
                if val < someMatrix[row][col-1] and val < someMatrix[row][col+1] and val < someMatrix[row+1][col]:
                    riskSum += val + 1
        # Bottom row
        elif row == len(someMatrix)-1:
            # Bottom left
            if col == 0:
                if val < someMatrix[row][col+1] and val < someMatrix[row-1][col]:
                    riskSum += val + 1
            # Bottom right
            elif col == len(someMatrix[row])-1:
                if val < someMatrix[row][col-1] and val < someMatrix[row-1][col]:
                    riskSum += val + 1
            # General Bottom values
            else:
                if val < someMatrix[row][col-1] and val < someMatrix[row][col+1] and val < someMatrix[row-1][col]:
                    riskSum += val + 1

        # Left-most column (corners already accounted for)
        elif col == 0:
            if val < someMatrix[row-1][col] and val < someMatrix[row+1][col] and val < someMatrix[row][col+1]:
                riskSum += val + 1
        # Right-most column (corners already accounted for)
        elif col == len(someMatrix)-1:
            if val < someMatrix[row-1][col] and val < someMatrix[row+1][col] and val < someMatrix[row][col-1]:
                riskSum += val + 1
        # Everything else
        else:
            print("Current coordinates are {},{}".format(row, col))
            if val < someMatrix[row-1][col] and val < someMatrix[row+1][col] and val < someMatrix[row][col-1] and val < someMatrix[row][col+1]:
                riskSum += val + 1

print("The final sum of risk points is:", riskSum)
