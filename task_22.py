import random

# Caption.
print('Вывод без повторений в порядке возрастания чисел, \n' +
      'встречающихся в двух исходных наборах.\n')

# Data input.
a = int(input('Введите размер 1-го набора чисел: '))
b = int(input('Введите размер 2-го набора чисел: '))

listA = [random.randint(0, a) for i in range(0, a)]
listB = [random.randint(0, b) for i in range(0, b)]

outList = []
for item in listA:
    if item in listB and not (item in outList) :
        outList.append(item)
outList.sort()

# Result output.
print(*listA)
print(*listB)
print(*outList)