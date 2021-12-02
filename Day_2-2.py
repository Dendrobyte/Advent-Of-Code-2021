inputFile = open("inputs/Day_2_input.txt")
inputData = inputFile.read().split("\n")
inputFile.close()
inputData = inputData[0:-1]  # Trim off ending new line

horizontal = 0
depth = 0
aim = 0
for line in inputData:
    data = line.split(" ")
    if data[0] == "forward":
        horizontal += int(data[1])
        depth += aim*int(data[1])
    elif data[0] == "down":
        aim += int(data[1])
    elif data[0] == "up":
        aim -= int(data[1])

print("Final horizontal pos:", horizontal)
print("Final depth pos: ", depth)
print("Multiplied:", horizontal*depth)
