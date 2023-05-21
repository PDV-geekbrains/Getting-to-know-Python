# Task caption.
print("Счастливый билетик.\n")

ticketNumber = int(input("Введите 6-значный номер проездного билета: "))

def sum (number):
    s = 0
    while number > 0:
        s += number % 10
        number //= 10
    return s

if(sum(ticketNumber // 1000) == sum(ticketNumber % 1000)):
    print("yes")
else: 
    print("no")
