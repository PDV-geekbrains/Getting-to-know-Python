import random

# Caption.
print('Поиск в массиве A[1..N] часла ближайшего по величине ' +
      'к заданному числу K.\n')

# Data input.
arrayLength = int(input('Введите размер массива (N): '))
K = int(input('Введите число (K): '))

arr = [random.randint(1, arrayLength + 1) for i in range(0, arrayLength)]
nearestNum = arr[0]
for j in range(len(arr)):
    if abs(nearestNum - K) > abs(arr[j] - K):
        nearestNum = arr[j]

# Rezult output.
print(*arr)
print(f'-> {nearestNum}')