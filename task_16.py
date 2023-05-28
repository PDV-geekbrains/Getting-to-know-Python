import random

# Caption.
print("Количество вхождений числа K в массив A[1..N].\n")

# Data input.
N = int(input("Введите число элементов в массиве (N): "))
K = int(input('Введите число для поиска (K): '))

n = 0
arr = []
for i in range(N):
    arr.append(random.randint(1, N))
for i in range(0, len(arr)):
    if K == arr[i]:
        n += 1

# Rezult output.
print(*arr)
print(f'-> {n}')