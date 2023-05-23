# Caption.
print('Определение двух натуральных чисел \n' +
      'по их сумме и произведению.\n')

# Data input.
print('Загадайте два натуральных числа X и Y (не более 1000 каждое.)')
S = int(input('Введите сумму (X + Y): '))
P = int(input('Введите произведение (X * Y): '))

X = 0
Y = 0
isCorrect = False
for index in range(1, S + 1, 1):
    if index * (S - index) == P:
        X = index
        Y = S - X
        isCorrect = True
        break

# Rezult output.
if isCorrect:
    print(f'------\n{S} {P} -> {X} {Y}')
else:
    print('Вы ошиблись :(')
