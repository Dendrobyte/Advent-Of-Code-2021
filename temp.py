# The 'ol input gettaroo
inputFile = open("inputs/Day_6_input.txt")
inputData = [int(x) for x in inputFile.read().split(",")]
inputFile.close()

"""
For part 2, recursion is going to take far too long...
Using a hint from some others on the NYU CS Discord, I'll try doing it based on number of days, not each fish in the input

I'll just go through the list and if I find something that's 0, replace with 6 and add an 8.
Not that straightforward, but you'll see. Then we return the length of the list
"""
# Iterate through initList, add to updateList, then set init to update and reset update
initList = inputData.copy()
updateList = initList.copy()
daysLeft = 80
for i in range(daysLeft):
    print("Running for day", i, "...") # Just to make sure we don't stall, but it sure does slow down.
    for fishInd, fishVal in enumerate(initList):
        if fishVal == 0:
            updateList[fishInd] = 6
            updateList.append(8)
        else:
            updateList[fishInd] = fishVal-1
    # Update the lists (avoids concurrent modification)
    initList = updateList.copy()


print("Fishes after", daysLeft, "days:", len(updateList))
