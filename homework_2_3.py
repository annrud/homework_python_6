print('Программа принимает на вход число n, создаёт словарь '
      'из n чисел последовательности (1 + (1/n))^n и '
      'выводит на экран их сумму')
while True:
    number = input('Введите число n: ')
    if number.isdigit():
        break
    print('Неверно введено число!')

dct = {k: round((1+(1/k))**k, 2) for k in range(1, int(number)+1)}
print(dct)

print(f'Сумма значений = {round(sum(dct.values()), 2)}')



