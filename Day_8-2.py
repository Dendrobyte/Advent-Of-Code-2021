# The 'ol input gettaroo
inputFile = open("inputs/Day_8_input.txt")
inputData = inputFile.read().split("\n")
inputFile.close()

# Split the input up
inputVals = [line[:line.index("|")-1] for line in inputData]
outputVals = [line[line.index("|")+2:] for line in inputData]

# Make a dictionary for segment sections to copy every time
segLights = {
    'top': 'z',
    'topL': 'z',
    'topR': 'z',
    'mid': 'z',
    'botL': 'z',
    'botR': 'z',
    'bot': 'z'
}

for i in range(len(inputData)):
    # Make a list such that each number has all letters as valid values
    validValues = ['abcdefg' for x in range(8)]
    # Now go through everything in the associated input value (idk why I'm calling them words)
    words = inputVals[i].split(" ")
    for word in words:
        wLen = len(word)
        # Isolate the unique ones (one by one, condense later)
        if wLen == 2: # 1
            validValues[1] = word
        elif wLen == 3: # 7
            validValues[7] = word
        elif wLen == 4: # 4
            validValues[4] = word
        elif wLen == 7: # 8 -- Kinda useless though
            validValues[8] = word

        # That which is in 7 but not 1 or 4 is the top segment
    # Isolate our unique combos
    

    print(validValues)

print(inputVals)
print(outputVals)
