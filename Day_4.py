# Each board is goig to be a matrix (2d list) of size-2 lists [val, "x"] || [val, "o"]
boards = {}

"""Functions"""
# Writing this one immediately, I know I'm going to need it.

"""
Checks if a board (5x5 matrix, details above) is a winning board or not.
"""


def isWinningBoard(matrix):
    # 5 items each, counts marked values in the matrix
    # NOTE: Diagonals don't count, so we don't worry about it.
    rows = [0, 0, 0, 0, 0]
    cols = [0, 0, 0, 0, 0]
    # Row item
    for r, rowVal in enumerate(matrix):
        for c, colVal in enumerate(matrix[r]):
            if matrix[r][c][1] == "x":
                rows[r] += 1
                cols[c] += 1
    if rows.count(5) >= 1 or cols.count(5) >= 1:
        return True
    else:
        return False


"""
Given 5 lines (from the input data), build a bingo board and add it to the global dictionary (the boards variable).
"""


def createBoard(boardLines):
    matrixToAdd = []
    for line in boardLines:
        nums = line.split(" ")
        # List comprehension to convert all the strings to numbers and add the unmarked value on to it
        nums.remove
        nums = [[int(x), "o"] for x in nums if x != '']
        matrixToAdd.append(nums)
    # Add matrix to board, using the board length for each key
    boards[len(boards)] = matrixToAdd


def calcWinningBoard(boardMatrix):
    unmarkedNums = 0
    for r in range(len(boardMatrix)):
        for c in range(len(boardMatrix)):
            if boardMatrix[r][c][1] == "o":
                unmarkedNums += boardMatrix[r][c][0]

    return unmarkedNums


"""
Okay, let's get down to business (to defeat... the huns?)
"""

# The 'ol input gettaroo
inputFile = open("inputs/Day_4_input.txt")
inputData = inputFile.read().split("\n")
inputFile.close()
#inputData = inputData[0:-1]
inputNums = [int(x) for x in inputData[0].split(",")]

# Build the boards (functions clean things up, don't they?)
for lineVal, lineContent in enumerate(inputData):
    if lineContent == "":
        createBoard(inputData[lineVal+1:lineVal+6])


# Mark all boards and then check to see if any of them are the winner
# NOTE: I suppose I could mark the nums when I make the board, but I can worry about optimization later
foundBoard = False  # Trivial fix for this
for selectedNum in inputNums:
    # For every board...
    for key, value in boards.items():
        # For each row in that board...
        for i, row in enumerate(value):
            # For each column in that row... (yikes, 4 nested for loop lol)
            for j, col in enumerate(value[i]):
                if value[i][j][0] == selectedNum:
                    value[i][j][1] = "x"
        # Check to see if the board has won
        if isWinningBoard(value) == True and foundBoard == False:
            print("--------")
            print("WINNING BOARD!")
            print("Board score is:", calcWinningBoard(value))
            print("Multiplied score is:", calcWinningBoard(value)*selectedNum)
            foundBoard = True
            break
