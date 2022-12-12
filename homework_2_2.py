print('Программа принимает на вход число N и выдает набор произведений чисел от 1 до N.')
while True:
    number = input('Введите число N: ')
    if number.isdigit():
        break
    print('Неверно введено число!')


def rec(n):
    if n == 1:
        return n
    else:
        return n*rec(n-1)


print([rec(i) for i in range(1, int(number)+1)])
