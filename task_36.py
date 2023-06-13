# Caption.
print('Использование функции, принимающей другую функцию.\n')

# Data input.
rows = int(input('Введите число строк: '))
columns = int(input('Введите число столбцов: '))

def print_operation_table(operation, num_rows = 6, num_columns = 6):
    arr=[]
    for i in range(1, num_rows + 1):
        arr.append([])
        for j in range(1, num_columns + 1):
            arr[i - 1].append(operation(i, j))
    return arr

arr=print_operation_table(lambda i, j: i * j, rows, columns)

# Rezult output.
for row in arr:
    for item in row:
        print(str(item), end='\t')
    print()
