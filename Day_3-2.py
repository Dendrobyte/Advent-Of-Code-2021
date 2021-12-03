# Define a function to count each digit of a given list (since it needs to update)
import Day_3 as day3


def bitCounter(listOfBinStrs):
    # Counter of bits for each position from part 1
    bitCount = {}
    for i in range(bitLength):
        bitCount['pos-'+str(i)] = [0, 0]

    # Fill dictionary
    for binString in listOfBinStrs:
        for pos, digit in enumerate(binString):
            if digit == "0":
                bitCount['pos-'+str(pos)][0] += 1
            elif digit == "1":
                bitCount['pos-'+str(pos)][1] += 1

    return bitCount


# The 'ol input gettaroo
inputFile = open("inputs/Day_3_input.txt")
inputData = inputFile.read().split("\n")
inputFile.close()
inputData = inputData[0:-1]
bitLength = len(inputData[0])

'''Oxygen Generator Rating'''
print("-------------------------------------")
# I'm going to do this rather trivially and not get obsessed with optimization
oxyGenRat = ""
prevNums = inputData.copy()
continueNums = []

for i in range(bitLength):
    bitCount = bitCounter(prevNums)
    keyStr = 'pos-'+str(i)
    # Depending on which count is higher, loop through the nums and add them properly
    if bitCount[keyStr][0] > bitCount[keyStr][1]:
        for binStr in prevNums:
            if binStr[i] == "0":
                continueNums.append(binStr)
    else:
        for binStr in prevNums:
            if binStr[i] == "1":
                continueNums.append(binStr)
    prevNums = continueNums.copy()
    continueNums = []
    # Quick check to see if we're done
    if len(prevNums) == 1:
        oxyGenRat = prevNums[0]
        break

'''CO2 Scrubber Rating'''
# I'm going to do this rather trivially and not get obsessed with optimization
co2ScrubRat = ""
prevNums = inputData.copy()
continueNums = []
for i in range(bitLength):
    bitCount = bitCounter(prevNums)
    keyStr = 'pos-'+str(i)
    # Depending on which count is higher, loop through the nums and add them properly
    if bitCount[keyStr][1] < bitCount[keyStr][0]:
        for binStr in prevNums:
            if binStr[i] == "1":
                continueNums.append(binStr)
    else:
        for binStr in prevNums:
            if binStr[i] == "0":
                continueNums.append(binStr)
    prevNums = continueNums.copy()
    continueNums = []
    # Quick check to see if we're done
    if len(prevNums) == 1:
        co2ScrubRat = prevNums[0]
        break
print("-------------------------------------")
print("Oxygen rating binary:", oxyGenRat)
oxyGenRatConvert = day3.convertBinSeqToDecimal(oxyGenRat)
print("Oxygen rating converted:", oxyGenRatConvert)
print("CO2 rating binary:", co2ScrubRat)
co2ScrubRatConvert = day3.convertBinSeqToDecimal(co2ScrubRat)
print("CO2 rating converted:", co2ScrubRatConvert)
print("Multiplied Result:", oxyGenRatConvert*co2ScrubRatConvert)
