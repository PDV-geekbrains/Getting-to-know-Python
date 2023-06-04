# Caption.
print('Сумма двух целых неотрицательных чисел Sum(А, В).\n')

# Data input.
a = int(input('введите число А: '))
b = int(input('Введите число В: '))

def sum(a, b):
    if a >= b:
        if b == 0:
            return a
        return sum(a, b - 1) + 1
    else:
        if a == 0:
            return b
        return sum(a - 1, b) + 1

# Result output.
print(sum(a, b))