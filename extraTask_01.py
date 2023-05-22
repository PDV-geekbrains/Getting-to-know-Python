# Caption
print("Произведение пар чисел списка \n")

# Data input.
inputData = input("Введите ряд целых чисел через пробел: ").split()

inputArray = []
for x in inputData:
    inputArray.append(int(x))

if len(inputArray) != 0:
    isReady = False
    i = 0
    outputArray = []
    while i <= len(inputArray) - i - 1:
        outputArray.append(inputArray[i] * inputArray[len(inputArray) - i - 1])
        i += 1
    isReady = True

# Rezult output.
print(f'{inputArray} => {outputArray}')