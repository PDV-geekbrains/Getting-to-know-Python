# Caption.
print('Заполнение массива элементами арифметической прогрессии (An = A1 + (n - 1) * D).\n')

# Data input.
A = int(input('Введите первый элеиент массива (A): '))
N = int(input('Введите размер массива (N): '))
D = int(input('Введите коуффициент (D): '))

# Rezult output.
print([A + (i - 1) * D for i in range(1, N + 1)])