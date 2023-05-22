# Caption.
print('Определить минимальное число монеток которые нужно перевернуть, \n' \
      'чтобы они все были повернуты вверх одной и той же стороной.\n')

# Data input.
inputData = input('Введите через пробел 1 или 0.\n' \
                  '0 - вверху решка, 1 - вверху орёл: ').split()

coinHeadNumber = 0
for x in inputData:
    if x == '1':
        coinHeadNumber += 1

# Result output.
if coinHeadNumber <= len(inputData) - coinHeadNumber:
    print(f'{len(inputData)} -> {inputData}\n{coinHeadNumber}')
else:
    print(f'{len(inputData)} -> {inputData}\n{len(inputData) - coinHeadNumber}')