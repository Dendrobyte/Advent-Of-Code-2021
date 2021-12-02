inputFile = open("inputs/Day_1_input.txt", "r+")
inputData = inputFile.read().split("\n")
inputFile.close()

lastNum = int(inputData[0])
increases = 0
for num in inputData[1::]:
    if num == '':
        continue
    if int(num) > lastNum:
        increases += 1
    lastNum = int(num)

print("Total increases:", increases)
