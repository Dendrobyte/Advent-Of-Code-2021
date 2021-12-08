# The 'ol input gettaroo
inputFile = open("inputs/Day_6_input.txt")
inputData = [int(x) for x in inputFile.read().split(",")]
inputFile.close()

"""
Functions

Dictionary shifting functions for cleaner code below
"""

def downShift(dictS):
    temp = dictS[0]
    # JOTE: print( list(dictS.keys())[-8:] ) -- Go backwards if need be
    # Shift all the fish down
    for key in list(dictS.keys())[0:8]:
        dictS[key] = dictS[key+1]
    dictS[6] += temp # Add any fish that restart on to those with 6 days left
    dictS[8] = temp # Add all the fish that have multiplied
    return dictS # I don't think this does in-place...? Idk, just to be safe I guess

def totalFishLeft(dictS):
    returnSum = 0
    for val in dictS.values():
        returnSum += val
    return returnSum
"""
For part 2, recursion is going to take far too long...
Using a hint from some others on the NYU CS Discord, I'll try doing it based on number of days, not each fish in the input

We'll go ahead and store how many fish we have left with some certain day using a dictionary.
That way, we have a pretty straightforward and relatively quick solution.
"""
# Create a dictionary with fish that have some number of days remaining. Dictionary comprehension, very epic.
fishDict = {k:0 for k in range(9)}
# Add the initial fish into the dictionary
startingFish = [int(x) for x in inputData]
for fish in startingFish:
    fishDict[fish] += 1
dayLength = 256
for i in range(dayLength):
    fishDict = downShift(fishDict)
print(fishDict)
print("The resulting number of fish after", dayLength, "days is:", totalFishLeft(fishDict))

#print("Fishes after", daysLeft, "days:", len(updateList))
