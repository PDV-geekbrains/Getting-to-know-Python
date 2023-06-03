import random

# Caption.
print('Нахождение максимального числа ягод, которое может \n' +
      'собрать за один заход собирающий модуль.\n')

# Data input.
bushesOnGardenBedNum = int(input('Введите количество кустов на грядке: '))
bushToProcess = int(input('Введите номер куста для сбора ягод: '))

bushes = [random.randint(1, 10) for i in range(0, bushesOnGardenBedNum + 1)]
sum = 0
if bushToProcess == 1:
    bushes[0] = bushes[len(bushes) - 1]
if bushToProcess == len(bushes) - 1:
    bushes.append(bushes[1])
for i in range(bushToProcess - 1, bushToProcess + 2):
    sum += bushes[i]

# Rezult output.
print(*bushes[1 : bushesOnGardenBedNum + 1])
print(sum)
