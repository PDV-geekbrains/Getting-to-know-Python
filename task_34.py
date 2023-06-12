# Caption.
print('Поиск ритма.\n')

# Data input.
poem = input('Введите стихотворение: ').strip()

vowelList = 'аеёиоуыэюя'
def CountVowels(subString):
    sum = 0
    for l in subString:
        if l in vowelList:
            sum += 1
    return sum
def IsAllItemsEqual(list):
    result = True
    for item in list:
        if item != list[0]:
            result = False
    return result

y = list(map(lambda p: CountVowels(p), poem.split(' ')))

# Result output.
if IsAllItemsEqual(y): print('Парам пам-пам')
else: print('Пам парам')
