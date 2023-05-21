print("Сумма цифр трёхзначного числа.\n")
inNum = int(input("Введите 3-х значное число: "))
n = inNum
sum = 0
while n > 0:
    sum += n % 10
    n //= 10
print(f"{inNum} -> {sum} ({inNum//100} + {inNum//10%10} + {inNum%10})")