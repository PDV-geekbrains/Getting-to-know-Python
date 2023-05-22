# Caption.
print("Сумма цифр 3-значного числа.\n")

# Data input.
inNum = int(input("Введите 3-значное число: "))

n = inNum
sum = 0
while n > 0:
    sum += n % 10
    n //= 10

# Rezult output.
print(f"{inNum} -> {sum} ({inNum//100} + {inNum//10%10} + {inNum%10})")