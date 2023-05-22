#Caption
print("Деление шоколадной плитки.\n")

length = int(input("Введите кол-во долек по длине плитки: "))
width = int(input("Введите кол-во долек по ширине плитки: "))
piecesNumber = int(input("Введите кол-во долек которое можно отломить: "))

isFound = False
lengthTmp = length
# Отламываем рядами поперёк плитки.
while length > 0:
    if width * length == piecesNumber:
        isFound = True
    length -= 1
# Если решение не найдено, отламываем рядами вдоль плитки.
length = lengthTmp
if isFound == False:
    while width > 0:
        if width * length == piecesNumber:
            isFound = True
        width -= 1
# Вывод результата.
if isFound == True:
    print("yes")
else:
    print("no")