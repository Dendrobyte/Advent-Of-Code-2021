# The 'ol input gettaroo
inputFile = open("inputs/Day_5_input.txt")
inputData = inputFile.read().split("\n")
inputFile.close()

# Let's parse the data first into two lists of tuples, such that indices will match each "side" of the arrow
x1y1 = []
x2y2 = []
for line in inputData:
    nums = line.split(" -> ")
    x1y1Coords = (int(nums[0].split(",")[0]), (int(nums[0].split(",")[1])))
    x2y2Coords = (int(nums[1].split(",")[0]), (int(nums[1].split(",")[1])))
    x1y1.append(x1y1Coords)
    x2y2.append(x2y2Coords)

# Let's find the max num real quick and build a corresponding matrix
maxNum = -1
for val in x1y1:
    potMax = max(val[0], val[1])
    if potMax > maxNum:
        maxNum = potMax
for val in x2y2:
    potMax = max(val[0], val[1])
    if potMax > maxNum:
        maxNum = potMax

# Python list tricks get messy with memory and reference, so we gotta do this the long way
ventMap = []
for i in range(maxNum+1):
    newRow = []
    for j in range(maxNum+1):
        newRow.append(".")
    ventMap.append(newRow)

# Annnnd now we set the positions of the numebrs with the coordinates above (we can assume the lists are the same length)
for item in enumerate(x1y1):
    coordInd = item[0]
    x1 = x1y1[coordInd][0]
    x2 = x2y2[coordInd][0]
    y1 = x1y1[coordInd][1]
    y2 = x2y2[coordInd][1]
    # x1 = x2 -- Vertical line
    if x1 == x2:
        for pos in range(min(y1, y2), max(y1, y2)+1):
            # TODO I could (well, should) functionize this her (everywhere we add a 1 or increment by 1), but alas it's a note for now
            if ventMap[x1][pos] == ".":
                ventMap[x1][pos] = 1
            else:
                ventMap[x1][pos] += 1

    # y1 = y2 -- Horizontal line
    if y1 == y2:
        for row in range(min(x1, x2), max(x1, x2)+1):
            if ventMap[row][y1] == ".":
                ventMap[row][y1] = 1
            else:
                ventMap[row][y1] += 1
    # Account for diagonals
    else:
        # If the change in value is the same, we have a diagonal
        if abs(x1-x2) == abs(y1-y2):
            # print("Diagonal line found at ({},{}) and ({},{}).".format(x1, y1, x2, y2))
            # We want to always start at the higher coordinate based on Y, then go down left or right depending on X (keep in mind that higher means lower index)
            # NOTE I know the comparisons can be done in one big block by multiplying the travelDist by +1 or -1. I'll leave naive solution here for now :)
            endTravelDistance = abs(x1-x2)
            travelDist = 0
            if x1 > x2:
                # Go left
                if y2 > y1:
                    # Go up
                    while travelDist < endTravelDistance+1:
                        if ventMap[x1-travelDist][y1+travelDist] == ".":
                            ventMap[x1-travelDist][y1+travelDist] = 1
                        else:
                            ventMap[x1-travelDist][y1+travelDist] += 1

                        travelDist+=1
                elif y1 > y2:
                    # Go down
                    while travelDist < endTravelDistance+1:
                        if ventMap[x1-travelDist][y1-travelDist] == ".":
                            ventMap[x1-travelDist][y1-travelDist] = 1
                        else:
                            ventMap[x1-travelDist][y1-travelDist] += 1

                        travelDist+=1
            elif x1 < x2: # Dis is a lotta code, sorry gods
                # Go left
                if y2 > y1:
                    # Go up
                    while travelDist < endTravelDistance+1:
                        if ventMap[x1+travelDist][y1+travelDist] == ".":
                            ventMap[x1+travelDist][y1+travelDist] = 1
                        else:
                            ventMap[x1+travelDist][y1+travelDist] += 1

                        travelDist+=1
                elif y1 > y2:
                    # Go down
                    while travelDist < endTravelDistance+1:
                        if ventMap[x1+travelDist][y1-travelDist] == ".":
                            ventMap[x1+travelDist][y1-travelDist] = 1
                        else:
                            ventMap[x1+travelDist][y1-travelDist] += 1

                        travelDist+=1

# Flippy flip (transpose)
ventMap = [[ventMap[j][i]
            for j in range(len(ventMap))] for i in range(len(ventMap[0]))]
pointsOfOverlap = 0
for row in ventMap:
    for col in row:
        if col != ".":
            if col >= 2:
                pointsOfOverlap += 1


def printVentMap():  # For debugging and presentation
    for line in ventMap:
        for item in line:
            print(format(str(item), '<2s'), end="")
        print()


# printVentMap()


print("Number of points where vents overlap:", pointsOfOverlap)
