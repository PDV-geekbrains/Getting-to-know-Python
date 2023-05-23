# Caption.
print('Вывод всех целых степеней двойки не превосходящих числа N.')

# Data input.
inputNumber = int(input('Введите положительное целое число N: '))

result = [1]
if inputNumber > 0:
    for i in range(1, inputNumber, 1):
        product = 1
        for j in range(1, i + 1, 1):
            product *= 2
        if product <= inputNumber:
            result.append(product)
        else:
            break
else:
    result = []

# Rezult output.
print(f'{inputNumber} -> {result}')