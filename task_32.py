import random

# Caption.
print('\nОпределение индексов элементов списка.\n')

# Data input.
lstLength = int(input('Введите размер списка: '))
lst = [str(random.randint(1, lstLength + 1)) for i in range(0, lstLength)]
print(lst)
minItem = input('Введите минимальное значение: ')
maxItem = input('Введите максимальное значение: ')

leftIndex = 0
rightIndex = 0
revLst = lst[::-1]
if lst.index(minItem) <= lst.index(maxItem):
    leftIndex = lst.index(minItem)
else:
    leftIndex = lst.index(maxItem)
if revLst.index(minItem) <= revLst.index(maxItem):
    rightIndex = len(lst) - 1 - revLst.index(minItem)
else:
    rightIndex = len(lst) - 1 - revLst.index(maxItem)

# # Result output.
print(f'-> {leftIndex}, {rightIndex}')