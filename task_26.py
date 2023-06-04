# Caption.
print('Возведение числа А в целую степень B с помощью рекурсии\n')

# Data input.
a = int(input('Введите число А: '))
b = int(input('Введите число В: '))

def pow(a, b):
    if b == 0:
        return 1
    return pow(a, b - 1) * a

# Rezult output.
print(pow(a, b))