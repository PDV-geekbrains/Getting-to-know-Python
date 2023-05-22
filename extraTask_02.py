# Caption.
print("Сумма элементов списка, стоящих на нечётных позициях.\n")

# Data input.
inputData = input("Введите ряд целых чисел через пробел: ").split()

inputArray = []
for x in inputData:
    inputArray.append(int(x))

sum = 0
for x in range(1, len(inputArray), 2):
    sum += inputArray[x]

# Rezult output.
print(f'{inputArray} -> {sum}\n')