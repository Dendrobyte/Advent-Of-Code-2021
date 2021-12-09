# The 'ol input gettaroo
inputFile = open("inputs/Day_7_input.txt")
inputData = [int(x) for x in inputFile.read().split(",")]
inputFile.close()

"""
Brute force

Pretty straightforward... for every single number on the horizontal access, find the total cost of all moments and then find the minimum for that.

I'll write that and try to optimize later (TM). Probably something to do with 1 + 2 + 3 + ... + n fuel for each step.
"""

# Calculate the fuel cost for a crab to get to a target position
def calcFuelForCrab(crabPos, targetPos):
    crabCost = 0
    for step in range(1, abs(crabPos-targetPos)+1):
        crabCost += step
    return crabCost

minPosVal = min(inputData) # Full input: 0
maxPosVal = max(inputData) # Full input: 1934

# Make a list to store total fuel for every crab to move to position i
fuelCostPerCoord = []

# Do this for every possible position a crab can move to
import time
start = time.time()
for pos in range(maxPosVal):
    # Find fuel cost for every crab
    print("Calculating crab movement for position ", pos, "...", sep="", end="\r")
    totalFuelCost = 0
    for crab in inputData:
        totalFuelCost += calcFuelForCrab(crab, pos)
    fuelCostPerCoord.append(totalFuelCost)
print() # Empty line to avoid the carriage return
end = time.time()

minFuelCost = min(fuelCostPerCoord)
minFuelCostIndex = fuelCostPerCoord.index(minFuelCost)
print("The lowest fuel cost is {} at position {}. Process took {} seconds".format(minFuelCost, minFuelCostIndex, end-start))
