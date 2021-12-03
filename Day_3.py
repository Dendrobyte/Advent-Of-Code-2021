# Function to convert a sequence of digits in binary back to a decimal. Rather straightforward... I think
def convertBinSeqToDecimal(binSeq):
    resultNum = 0
    powerOfTwo = 0
    for digit in binSeq[::-1]:
        if digit == "1":
            resultNum += 2**powerOfTwo
        powerOfTwo += 1

    return resultNum


# The 'ol input gettaroo
inputFile = open("inputs/Day_3_input.txt")
inputData = inputFile.read().split("\n")
inputFile.close()
inputData = inputData[0:-1]

bitLength = len(inputData[0])

# Dictionary where each item is a list
# Index 0 will be 0 counts, index 1 will be 1 counts
bitCount = {}
for i in range(bitLength):
    bitCount['pos-'+str(i)] = [0, 0]

# Fill dictionary
for binString in inputData:
    for pos, digit in enumerate(binString):
        if digit == "0":
            bitCount['pos-'+str(pos)][0] += 1
        elif digit == "1":
            bitCount['pos-'+str(pos)][1] += 1

# Find max and min of each position
gamma = ""
epsilon = ""
for key in bitCount.keys():
    if bitCount[key][0] > bitCount[key][1]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

# Neatly show final results
print("Gamma binary:", gamma)
gammaConvert = convertBinSeqToDecimal(gamma)
print("Gamma converted:", gammaConvert)
print("Epsilon binary:", epsilon)
epsilonConvert = convertBinSeqToDecimal(epsilon)
print("Epsilon converted:", epsilonConvert)
print("Multiplied result:", epsilonConvert*gammaConvert)
