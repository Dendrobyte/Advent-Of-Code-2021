# The 'ol input gettaroo
inputFile = open("inputs/Day_6_input.txt")
inputData = [int(x) for x in inputFile.read().split(",")]
inputFile.close()

"""
Functions

Since we can do this with an O(n) pass, we want to make a recursive solution.
We'll calculate all num of fish spawned from one fish at a time with a certain age.
"""
totalFish = 0 # Global list to store the ages
def numOfFishSpawned(currFishAge, daysLeft):
    # NOTE The LAST day is day ONE (1), and not zero
    global totalFish
    daysLeft -= 1
    currFishAge -= 1
    # If the fish has more days before the next cycle before the days end, we can add it's age - days left to the list
    if daysLeft == 1:
        totalFish += 1
    elif currFishAge == 0:
        # Restart this fish
        numOfFishSpawned(7, daysLeft)
        # New fish
        numOfFishSpawned(9, daysLeft)
    else:
        numOfFishSpawned(currFishAge, daysLeft) # Keep going with the same fish
    # print(totalFish)

print(inputData)
resultFish = 0

# Calculate the num of fish spawned by each fish
daysLeft = 81
for fishAgeInList in inputData:
    print("Running function for fish with", fishAgeInList, "days left...")
    numOfFishSpawned(fishAgeInList, daysLeft)

print("Fishes after", daysLeft, "days:", totalFish)
