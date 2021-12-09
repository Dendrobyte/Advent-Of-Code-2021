# The 'ol input gettaroo
inputFile = open("inputs/Day_8_input.txt")
inputData = inputFile.read().split("\n")
inputFile.close()

outputVals = [line[line.index("| ")+2::] for line in inputData ]
numCount = 0
for outputs in outputVals:
    eachVal = outputs.split(" ")
    for val in eachVal:
        if len(val) == 2 or len(val) == 4 or len(val) == 3 or len(val) == 7:
            numCount += 1
print(numCount)