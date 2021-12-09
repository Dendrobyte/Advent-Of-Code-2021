# The 'ol input gettaroo
inputFile = open("inputs/Day_7_input.txt")
inputData = [int(x) for x in inputFile.read().split(",")]
inputFile.close()

import statistics
medianOfInput = statistics.median(inputData)
print("Place to move to is:", int(medianOfInput))

totalFuel = 0
for crab in inputData:
    totalFuel += abs(crab-medianOfInput)

print("Total fuel used:", int(totalFuel))