inputFile = open("inputs/Day_1_input.txt", "r+")
inputData = inputFile.read().split("\n")
inputFile.close()
del inputData[len(inputData)-1]

# Convert all to nums
for i in range(len(inputData)):
    inputData[i] = int(inputData[i])

firstWindow = inputData[0] + inputData[1] + inputData[2]
lastSum = firstWindow
increases = 0
try:
    for numInd in range(len(inputData[1::])):
        newSum = inputData[numInd] + inputData[numInd+1] + inputData[numInd+2]
        #print(newSum, lastSum)
        if newSum > lastSum:
            increases += 1
        lastSum = newSum
except:
    print("Index error!")
    # Turns out we don't need to calculate the last windows

print("Total increases:", increases)
